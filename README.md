# 🛒 SmartShelf AI

**SmartShelf AI** is an AI-based smart inventory and customer assistance system designed to simplify product management in stores and supermarkets.

The system organizes products using a simple hierarchy:

**Section → Subsection → Product**

It helps store staff monitor stock, track expiry dates, manage sales and restocking, remove expired stock, and quickly find products for customers.

## 🚀 Features

### 📂 Smart Store Organization

* Organizes products into Sections and Subsections.
* Makes large inventories easier to manage.
* Example: `Grocery → Snacks → Biscuits`

### 🔍 Product Search

Search for products and view:

* Product name
* Section
* Subsection
* Available stock
* Price
* Expiry date
* Stock status
* Expiry status

### 🛒 Customer Assistance

Customers can enter the product they need and SmartShelf AI provides:

* Product availability
* Store location
* Price
* Current stock
* Expiry information

### 📊 Inventory Dashboard

The dashboard provides an overview of:

* 📦 Total Products
* 🔢 Total Stock
* 🟡 Low Stock Products
* 🔴 Out-of-Stock Products
* ⏰ Expired Products
* 📅 Products Expiring Soon

### 📦 Restock Management

Store staff can:

* Select a product
* Enter the quantity to add
* Automatically update the inventory

### 🛍️ Sales Management

The system allows staff to record product sales.

When a sale is recorded:

* Stock quantity is reduced automatically.
* The system prevents selling more than the available quantity.
* Low-stock and out-of-stock alerts are displayed.

### ⏰ Expiry Tracking

SmartShelf AI monitors product expiry dates and categorizes them as:

| Status           | Meaning                            |
| ---------------- | ---------------------------------- |
| 🔴 Expired       | Product has already expired        |
| 🔴 Expires Today | Product expires today              |
| 🟠 Expires Soon  | Product expires within 7 days      |
| 🟡 Expiring      | Product expires within 30 days     |
| 🟢 Valid         | Product has sufficient expiry time |

### 🗑️ Expired Stock Removal

Expired stock can be removed from active inventory by selecting the expired product and entering the quantity to remove.

The product information can remain in the system instead of completely deleting the product record.

### ⚠️ Stock Alerts

The system automatically identifies:

* 🔴 Out of Stock
* 🟡 Low Stock

This helps staff know which products need attention.

---

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **Pandas**
* **Python Datetime**

### Future AI Technologies

The project can be extended using:

* **YOLO**
* **OpenCV**
* **Computer Vision**
* **Barcode/QR Detection**
* **Machine Learning**

---

## 📁 Project Structure

```text
SmartShelf-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── yolo11n.pt
```

> `yolo11n.pt` can be added when camera-based product detection is integrated.

---

## ⚙️ Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/SmartShelf-AI.git
```

### Step 2: Open the Project

```bash
cd SmartShelf-AI
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### Step 4: Install Requirements

```bash
pip install -r requirements.txt
```

### Step 5: Run the Application

```bash
streamlit run app.py
```

The application will open in your web browser.

---

## 🔄 System Workflow

```text
                 SmartShelf AI
                       │
                       ▼
                    Store
                       │
                       ▼
                   Section
                       │
                       ▼
                  Subsection
                       │
                       ▼
                    Product
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
        Stock Tracking      Expiry Tracking
             │                   │
             ▼                   ▼
       Sales / Restock      Expiry Alerts
             │                   │
             └─────────┬─────────┘
                       ▼
              Customer Assistance
```

---

## 🏪 Example Store Structure

```text
Grocery
│
├── Snacks
│   ├── Biscuits
│   ├── Chips
│   └── Chocolate
│
├── Beverages
│   ├── Juice
│   └── Water Bottle
│
└── Rice & Grains
    ├── Rice
    └── Wheat

Dairy
│
└── Milk Products
    ├── Milk
    ├── Curd
    └── Butter

Personal Care
│
├── Bath Products
│   └── Soap
│
├── Hair Care
│   └── Shampoo
│
└── Oral Care
    └── Toothpaste
```

---

## 🤖 Future Enhancements

The project can be further improved with:

* 📷 Real-time camera-based product detection
* 🤖 YOLO object detection
* 🔢 Automatic product counting
* 📦 Barcode and QR-code scanning
* 🗄️ Database integration
* 🔐 Login and authentication
* 📈 Advanced inventory analytics
* 🔔 Automatic stock notifications
* 🧠 AI-based demand prediction
* 🏪 Shelf-level product location tracking
* 🧾 Sales history and reports
* ☁️ Cloud deployment

---

## ⚠️ Current Limitations

* The current prototype stores inventory using Streamlit session state.
* Inventory changes may reset when the application session is restarted.
* Camera-based YOLO detection is planned as a future enhancement.
* Exact brand/SKU recognition requires suitable product data or a trained/reference model.

---

## 🎯 Project Objective

The objective of **SmartShelf AI** is to make inventory management faster, simpler, and more organized by combining stock management, expiry tracking, customer assistance, sales management, restocking, and intelligent alerts in one application.

---

## 💡 Why SmartShelf AI?

Traditional inventory management can require manual checking of shelves and stock records.

SmartShelf AI provides a centralized system where store staff can easily:

**Find → Track → Restock → Sell → Monitor → Remove Expired Stock**

This can reduce manual effort and make inventory information easier to access.

---

## 👩‍💻 Project Information

**Project Name:** SmartShelf AI
**Type:** AI-Based Smart Inventory and Customer Assistance System
**Application:** Streamlit Web Application
**Programming Language:** Python
**Domain:** Artificial Intelligence / Inventory Management / Computer Vision

---

## ⭐ Future Vision

SmartShelf AI aims to become a complete intelligent retail assistant that can use cameras and AI to automatically detect products, count shelf inventory, identify low-stock items, monitor expiry dates, and assist customers in finding products.
