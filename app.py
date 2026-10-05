import streamlit as st
import pandas as pd
from datetime import date, timedelta

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="SmartShelf AI",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 SmartShelf AI")
st.caption("AI-Based Smart Inventory and Customer Assistance System")


# =====================================================
# INITIAL PRODUCT DATA
# =====================================================

if "products" not in st.session_state:

    st.session_state.products = [

        # =================================================
        # GROCERY
        # =================================================

        {
            "Section": "Grocery",
            "Subsection": "Snacks",
            "Product": "Biscuits",
            "Quantity": 12,
            "Price": 30,
            "Expiry": date(2027, 3, 15)
        },

        {
            "Section": "Grocery",
            "Subsection": "Snacks",
            "Product": "Chips",
            "Quantity": 4,
            "Price": 20,
            "Expiry": date(2027, 1, 20)
        },

        {
            "Section": "Grocery",
            "Subsection": "Snacks",
            "Product": "Chocolate",
            "Quantity": 0,
            "Price": 50,
            "Expiry": date(2026, 12, 10)
        },

        {
            "Section": "Grocery",
            "Subsection": "Beverages",
            "Product": "Juice",
            "Quantity": 8,
            "Price": 80,
            "Expiry": date(2026, 11, 25)
        },

        {
            "Section": "Grocery",
            "Subsection": "Beverages",
            "Product": "Water Bottle",
            "Quantity": 15,
            "Price": 20,
            "Expiry": date(2028, 5, 10)
        },

        {
            "Section": "Grocery",
            "Subsection": "Rice & Grains",
            "Product": "Rice",
            "Quantity": 10,
            "Price": 650,
            "Expiry": date(2028, 8, 20)
        },

        {
            "Section": "Grocery",
            "Subsection": "Rice & Grains",
            "Product": "Wheat",
            "Quantity": 6,
            "Price": 500,
            "Expiry": date(2028, 6, 15)
        },


        # =================================================
        # DAIRY
        # =================================================

        {
            "Section": "Dairy",
            "Subsection": "Milk Products",
            "Product": "Milk",
            "Quantity": 20,
            "Price": 60,
            "Expiry": date(2026, 10, 10)
        },

        {
            "Section": "Dairy",
            "Subsection": "Milk Products",
            "Product": "Curd",
            "Quantity": 3,
            "Price": 40,
            "Expiry": date(2026, 10, 8)
        },

        {
            "Section": "Dairy",
            "Subsection": "Milk Products",
            "Product": "Butter",
            "Quantity": 2,
            "Price": 55,
            "Expiry": date(2026, 12, 20)
        },


        # =================================================
        # PERSONAL CARE
        # =================================================

        {
            "Section": "Personal Care",
            "Subsection": "Bath Products",
            "Product": "Soap",
            "Quantity": 7,
            "Price": 45,
            "Expiry": date(2028, 2, 10)
        },

        {
            "Section": "Personal Care",
            "Subsection": "Hair Care",
            "Product": "Shampoo",
            "Quantity": 2,
            "Price": 120,
            "Expiry": date(2027, 9, 15)
        },

        {
            "Section": "Personal Care",
            "Subsection": "Oral Care",
            "Product": "Toothpaste",
            "Quantity": 9,
            "Price": 90,
            "Expiry": date(2027, 7, 20)
        },


        # =================================================
        # HOUSEHOLD
        # =================================================

        {
            "Section": "Household",
            "Subsection": "Cleaning",
            "Product": "Floor Cleaner",
            "Quantity": 5,
            "Price": 150,
            "Expiry": date(2028, 3, 10)
        },

        {
            "Section": "Household",
            "Subsection": "Laundry",
            "Product": "Detergent",
            "Quantity": 1,
            "Price": 200,
            "Expiry": date(2028, 1, 15)
        }
    ]


# =====================================================
# STOCK STATUS
# =====================================================

def get_status(quantity):

    if quantity == 0:
        return "🔴 Out of Stock"

    elif quantity <= 3:
        return "🟡 Low Stock"

    else:
        return "🟢 Available"


# =====================================================
# EXPIRY STATUS
# =====================================================

def get_expiry_status(expiry_date):

    today = date.today()

    days_left = (expiry_date - today).days

    if days_left < 0:
        return "🔴 Expired"

    elif days_left == 0:
        return "🔴 Expires Today"

    elif days_left <= 7:
        return f"🟠 Expires in {days_left} days"

    elif days_left <= 30:
        return f"🟡 Expires in {days_left} days"

    else:
        return "🟢 Valid"


# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("📂 Store Sections")

sections = sorted(
    set(
        product["Section"]
        for product in st.session_state.products
    )
)

selected_section = st.sidebar.selectbox(
    "Select Section",
    ["All Sections"] + sections
)


# =====================================================
# PRODUCT SEARCH
# =====================================================

search = st.text_input(
    "🔍 Search Product",
    placeholder="Search for a product..."
)


# =====================================================
# CUSTOMER NEEDS
# =====================================================

st.divider()

st.subheader("🛒 Customer Needs")

st.write(
    "Enter what the customer needs. "
    "SmartShelf AI will find the product location, "
    "stock and expiry information."
)

customer_need = st.text_input(
    "🔎 What do you need?",
    placeholder="Example: biscuits, milk, soap..."
)

if st.button("🔎 Find Product"):

    if customer_need.strip():

        search_product = customer_need.strip().lower()

        found_products = []

        for product in st.session_state.products:

            if search_product in product["Product"].lower():

                found_products.append(product)

        if found_products:

            st.success(
                f"✅ Found {len(found_products)} product(s)"
            )

            for product in found_products:

                stock_status = get_status(
                    product["Quantity"]
                )

                expiry_status = get_expiry_status(
                    product["Expiry"]
                )

                st.markdown(
                    f"""
                    ### 🛍️ {product["Product"]}

                    📂 **Section:** {product["Section"]}

                    📁 **Subsection:** {product["Subsection"]}

                    📦 **Available Stock:** {product["Quantity"]}

                    💰 **Price:** ₹{product["Price"]}

                    📅 **Expiry Date:** {product["Expiry"].strftime("%d-%m-%Y")}

                    **Stock Status:** {stock_status}

                    **Expiry Status:** {expiry_status}
                    """
                )

                if product["Quantity"] > 0:

                    st.info(
                        f"📍 Location: "
                        f"{product['Section']} → "
                        f"{product['Subsection']}"
                    )

                else:

                    st.error(
                        "❌ Sorry, this product is currently "
                        "out of stock."
                    )

        else:

            st.warning(
                "🔍 Product not found in SmartShelf."
            )

    else:

        st.warning(
            "Please enter the product you need."
        )


# =====================================================
# CREATE DATAFRAME
# =====================================================

df = pd.DataFrame(
    st.session_state.products
)


# =====================================================
# FILTER SECTION
# =====================================================

if selected_section != "All Sections":

    df = df[
        df["Section"] == selected_section
    ]


# =====================================================
# FILTER SEARCH
# =====================================================

if search:

    df = df[
        df["Product"].str.contains(
            search,
            case=False,
            na=False
        )
    ]


# =====================================================
# DASHBOARD METRICS
# =====================================================

total_products = len(df)

total_quantity = (
    int(df["Quantity"].sum())
    if not df.empty
    else 0
)

low_stock = len(
    df[
        (df["Quantity"] > 0)
        & (df["Quantity"] <= 3)
    ]
)

out_of_stock = len(
    df[
        df["Quantity"] == 0
    ]
)

today = date.today()

expired_count = len(
    df[
        df["Expiry"] < today
    ]
)

expiring_soon_count = len(
    df[
        (df["Expiry"] >= today)
        & (df["Expiry"] <= today + timedelta(days=30))
    ]
)


col1, col2, col3, col4, col5, col6 = st.columns(6)

col1.metric(
    "📦 Products",
    total_products
)

col2.metric(
    "🔢 Total Stock",
    total_quantity
)

col3.metric(
    "🟡 Low Stock",
    low_stock
)

col4.metric(
    "🔴 Out of Stock",
    out_of_stock
)

col5.metric(
    "⏰ Expired",
    expired_count
)

col6.metric(
    "📅 Expiring Soon",
    expiring_soon_count
)


# =====================================================
# STORE INVENTORY
# =====================================================

st.divider()

st.subheader("🗂️ Store Inventory")


if df.empty:

    st.warning(
        "No products found."
    )

else:

    for section in df["Section"].unique():

        st.markdown(
            f"## 🏪 {section}"
        )

        section_df = df[
            df["Section"] == section
        ]

        for subsection in section_df[
            "Subsection"
        ].unique():

            with st.expander(
                f"📁 {subsection}",
                expanded=True
            ):

                sub_df = section_df[
                    section_df["Subsection"]
                    == subsection
                ]

                products = sub_df.to_dict(
                    "records"
                )

                cols = st.columns(4)

                for i, product in enumerate(
                    products
                ):

                    with cols[i % 4]:

                        quantity = product[
                            "Quantity"
                        ]

                        stock_status = get_status(
                            quantity
                        )

                        expiry_status = get_expiry_status(
                            product["Expiry"]
                        )

                        st.markdown(
                            f"""
                            ### 🛍️ {product["Product"]}

                            **Stock:** {quantity}

                            **Price:** ₹{product["Price"]}

                            **Expiry:** {product["Expiry"].strftime("%d-%m-%Y")}

                            **Stock:** {stock_status}

                            **Expiry:** {expiry_status}
                            """
                        )

                        st.progress(
                            min(
                                quantity / 20,
                                1.0
                            )
                        )


# =====================================================
# ADD NEW PRODUCT
# =====================================================

st.divider()

st.subheader("➕ Add New Product")

with st.expander(
    "Add a New Product"
):

    col1, col2 = st.columns(2)

    with col1:

        new_section = st.text_input(
            "Section",
            placeholder="Example: Grocery"
        )

        new_subsection = st.text_input(
            "Subsection",
            placeholder="Example: Snacks"
        )

        new_product = st.text_input(
            "Product Name",
            placeholder="Example: Cookies"
        )

    with col2:

        new_quantity = st.number_input(
            "Initial Quantity",
            min_value=0,
            value=1
        )

        new_price = st.number_input(
            "Price ₹",
            min_value=0,
            value=10
        )

        new_expiry = st.date_input(
            "Expiry Date",
            min_value=date.today()
        )


    if st.button(
        "➕ Add Product"
    ):

        if (
            new_section
            and new_subsection
            and new_product
        ):

            existing = any(
                p["Product"].lower()
                == new_product.lower()
                for p in
                st.session_state.products
            )

            if existing:

                st.error(
                    "❌ This product already exists."
                )

            else:

                st.session_state.products.append(
                    {
                        "Section": new_section,
                        "Subsection": new_subsection,
                        "Product": new_product,
                        "Quantity": new_quantity,
                        "Price": new_price,
                        "Expiry": new_expiry
                    }
                )

                st.success(
                    f"✅ {new_product} added successfully!"
                )

                st.rerun()

        else:

            st.error(
                "Please enter Section, Subsection "
                "and Product."
            )


# =====================================================
# RESTOCK PRODUCT
# =====================================================

st.divider()

st.subheader("📦 Restock Product")

product_names = sorted(
    set(
        product["Product"]
        for product in
        st.session_state.products
    )
)

if product_names:

    selected_product = st.selectbox(
        "Select Product to Restock",
        product_names
    )

    restock_quantity = st.number_input(
        "Enter quantity to add",
        min_value=1,
        value=1
    )

    if st.button(
        "➕ Restock Product"
    ):

        for product in (
            st.session_state.products
        ):

            if (
                product["Product"]
                == selected_product
            ):

                old_quantity = product[
                    "Quantity"
                ]

                product[
                    "Quantity"
                ] += restock_quantity

                new_quantity = product[
                    "Quantity"
                ]

                st.success(
                    f"✅ {selected_product} restocked! "
                    f"Stock: {old_quantity} → {new_quantity}"
                )

                break

        st.rerun()


# =====================================================
# RECORD PRODUCT SALE
# =====================================================

st.divider()

st.subheader("🛒 Record Product Sale")

if product_names:

    sold_product = st.selectbox(
        "Select Product Sold",
        product_names,
        key="sold_product"
    )

    sold_quantity = st.number_input(
        "Enter quantity sold",
        min_value=1,
        value=1,
        key="sold_quantity"
    )

    if st.button(
        "🛒 Record Sale"
    ):

        for product in (
            st.session_state.products
        ):

            if (
                product["Product"]
                == sold_product
            ):

                current_quantity = product[
                    "Quantity"
                ]

                if sold_quantity > current_quantity:

                    st.error(
                        f"❌ Cannot sell {sold_quantity}. "
                        f"Only {current_quantity} available."
                    )

                else:

                    product[
                        "Quantity"
                    ] -= sold_quantity

                    remaining = product[
                        "Quantity"
                    ]

                    if remaining == 0:

                        st.error(
                            f"🔴 {sold_product} "
                            f"is now OUT OF STOCK!"
                        )

                    elif remaining <= 3:

                        st.warning(
                            f"🟡 {sold_product} is LOW STOCK. "
                            f"Only {remaining} remaining."
                        )

                    else:

                        st.success(
                            f"✅ Sale recorded. "
                            f"{remaining} remaining."
                        )

                break

        st.rerun()


# =====================================================
# REMOVE EXPIRED PRODUCTS
# =====================================================

st.divider()

st.subheader("🗑️ Remove Expired Products")

today = date.today()

expired_products_for_removal = [
    product
    for product in st.session_state.products
    if product["Expiry"] < today and product["Quantity"] > 0
]

if expired_products_for_removal:

    expired_names = [
        product["Product"]
        for product in expired_products_for_removal
    ]

    selected_expired = st.selectbox(
        "Select Expired Product",
        expired_names,
        key="selected_expired_product"
    )

    selected_expired_product = next(
        product
        for product in st.session_state.products
        if product["Product"] == selected_expired
    )

    st.info(
        f"📦 Available expired stock: "
        f"{selected_expired_product['Quantity']}"
    )

    expired_quantity = st.number_input(
        "Quantity to remove",
        min_value=1,
        max_value=selected_expired_product["Quantity"],
        value=1,
        key="expired_quantity"
    )

    if st.button("🗑️ Remove Expired Stock"):

        selected_expired_product["Quantity"] -= expired_quantity

        st.session_state.expiry_removal_message = (
            f"✅ Removed {expired_quantity} expired "
            f"{selected_expired} from active inventory. "
            f"Remaining stock: {selected_expired_product['Quantity']}"
        )

        st.rerun()

else:

    st.success(
        "✅ No expired stock available for removal."
    )

if "expiry_removal_message" in st.session_state:

    st.success(st.session_state.expiry_removal_message)

    del st.session_state.expiry_removal_message


# =====================================================
# INVENTORY TRACKING
# =====================================================

st.divider()

st.subheader("📊 Inventory Tracking")

if not df.empty:

    display_df = df.copy()

    display_df["Stock Status"] = (
        display_df["Quantity"]
        .apply(get_status)
    )

    display_df["Expiry Status"] = (
        display_df["Expiry"]
        .apply(get_expiry_status)
    )

    display_df["Expiry"] = display_df[
        "Expiry"
    ].apply(
        lambda x: x.strftime("%d-%m-%Y")
    )

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )


# =====================================================
# RESTOCK ALERTS
# =====================================================

st.divider()

st.subheader("⚠️ Stock Alerts")

alerts = df[
    df["Quantity"] <= 3
]

if alerts.empty:

    st.success(
        "✅ All products have sufficient stock."
    )

else:

    for _, product in alerts.iterrows():

        if product["Quantity"] == 0:

            st.error(
                f"🔴 {product['Product']} "
                f"→ OUT OF STOCK"
            )

        else:

            st.warning(
                f"🟡 {product['Product']} "
                f"→ Only {product['Quantity']} remaining"
            )


# =====================================================
# EXPIRY ALERTS
# =====================================================

st.divider()

st.subheader("⏰ Expiry Alerts")

today = date.today()

expired_products = []
expiring_products = []

for product in st.session_state.products:

    days_left = (
        product["Expiry"] - today
    ).days

    if days_left < 0:

        expired_products.append(product)

    elif days_left <= 30:

        expiring_products.append(
            (product, days_left)
        )


# -------------------------
# EXPIRED PRODUCTS
# -------------------------

if expired_products:

    st.error(
        "🔴 EXPIRED PRODUCTS"
    )

    for product in expired_products:

        st.error(
            f"❌ {product['Product']} "
            f"expired on "
            f"{product['Expiry'].strftime('%d-%m-%Y')}"
        )

else:

    st.success(
        "✅ No expired products."
    )


# -------------------------
# EXPIRING PRODUCTS
# -------------------------

if expiring_products:

    st.warning(
        "🟠 PRODUCTS EXPIRING WITHIN 30 DAYS"
    )

    for product, days_left in expiring_products:

        if days_left == 0:

            message = (
                f"⚠️ {product['Product']} "
                f"expires TODAY!"
            )

        else:

            message = (
                f"⚠️ {product['Product']} "
                f"expires in {days_left} days "
                f"({product['Expiry'].strftime('%d-%m-%Y')})"
            )

        st.warning(message)

else:

    st.success(
        "✅ No products are expiring within 30 days."
    )


# =====================================================
# FOOTER
# =====================================================

st.divider()

st.caption(
    "SmartShelf AI | Smart Inventory + Expiry Tracking + Customer Assistance"
)