 SmartShelf AI

SmartShelf AI is a Streamlit-based smart inventory and customer assistance system designed to make store inventory management easier.

The application organizes products using:

Section → Subsection → Product

It helps monitor stock levels, track expiry dates, manage restocking and sales, remove expired stock, and quickly find products for customer needs.

✨ Features

📂 Store Organization

Organizes products into Sections and Subsections.

Example: Grocery → Snacks → Biscuits.

Sidebar section filtering.

🔍 Product Search

Search products by name and view:

Section and Subsection

Available quantity

Price

Expiry date

Stock status

Expiry status

🛒 Customer Needs

Enter a product name to find its:

Availability

Store location

Price

Stock status

Expiry information

📊 Inventory Dashboard

Displays:

Total products

Total stock quantity

Low-stock products

Out-of-stock products

Expired products

Products expiring within 30 days

📦 Restock Management

Select a product and add stock quantity. The inventory is updated automatically.

🛒 Sales Management

Record products sold. The quantity is deducted from inventory and the application prevents selling more items than are available.

⏰ Expiry Tracking

Products are classified as:

🔴 Expired

🔴 Expires Today

🟠 Expires within 7 days

🟡 Expires within 30 days

🟢 Valid

🗑️ Remove Expired Stock

Expired stock can be removed by selecting the expired product and entering the quantity to remove. The product record is retained rather than deleting the product completely.

⚠️ Stock Alerts

The system identifies:

🔴 Out of Stock

🟡 Low Stock

🛠️ Technologies Used

Python

Streamlit – web application interface

Pandas – inventory data handling

Python datetime – expiry-date calculations

📁 Project Structure

SmartShelf-AI/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── yolo11n.pt

yolo11n.pt is optional and can be used later for YOLO-based product detection.

🚀 How to Run

1. Create a virtual environment

python -m venv venv

Activate it on Windows PowerShell:

venv\Scripts\activate

2. Install dependencies

pip install -r requirements.txt

3. Run the application

streamlit run app.py

The SmartShelf AI application will open in your browser.

🔄 Application Flow

Store
  ↓
Section
  ↓
Subsection
  ↓
Product
  ↓
Stock & Expiry Tracking
  ↓
Customer Assistance
  ↓
Alerts / Restock / Sale / Expired Stock Removal

📦 Sample Inventory Categories

Grocery

Snacks

Beverages

Rice & Grains

Dairy

Milk Products

Personal Care

Bath Products

Hair Care

Oral Care

Household

Cleaning

Laundry

🤖 Future Enhancements

📷 Camera-based product detection

🤖 YOLO-based product recognition

🔢 Automatic product counting

📦 Barcode/QR code scanning

🗄️ Database storage

🔐 User login and authentication

📈 Inventory analytics

🔔 Automatic notifications

🧠 AI-based demand prediction

🏪 Shelf-level product location tracking

🧾 Sales history and inventory reports

⚠️ Current Limitations

Product data is currently stored in Streamlit session state.

Inventory changes may reset when the application session is restarted.

Camera/YOLO detection is not yet integrated into the current inventory code.

Exact brand/SKU recognition requires suitable product data or a trained/reference model.

🎯 Project Objective

The main objective of SmartShelf AI is to simplify inventory management by providing a structured system for tracking products, stock levels, expiry dates, customer needs, sales, restocking, and inventory alerts.

👩‍💻 Project Information

Project: SmartShelf AI
Type: AI-Based Smart Inventory and Customer Assistance System
Platform: Streamlit Web Application
Language: Python
