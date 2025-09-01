# ZaoHub
# 🌱 ZaoHub

**ZaoHub** is a marketplace platform designed to connect farmers in Kenya and East Africa directly to consumers, businesses, and organizations. The project provides both a **mobile app demo** and a **web app demo**, allowing farmers to list their products and consumers to easily purchase them from the comfort of their homes.

---

## 📖 Table of Contents
1. [About the Project](#-about-the-project)
2. [Features](#-features)
3. [Technology Stack](#-technology-stack)
4. [Project Structure](#-project-structure)
5. [Setup and Installation](#-setup-and-installation)
6. [Database Setup](#-database-setup)
7. [Running the Application](#-running-the-application)
8. [Deployment Guide](#-deployment-guide)
9. [Revenue Model](#-revenue-model)
10. [Sustainability (SDG 2)](#-sustainability-sdg-2)
11. [Future Roadmap](#-future-roadmap)
12. [License](#-license)

---

## 🌍 About the Project
ZaoHub bridges the gap between **farmers and markets** by providing a seamless platform for selling and buying farm produce. It eliminates middlemen, increases farmer profitability, and ensures consumers get fresh, affordable products.

The project is built as a **demo prototype** with basic functionalities:
- User authentication (farmers and consumers).
- Farmers can add and manage their products.
- Consumers can browse available products.
- Simple REST API backend with MySQL database.

---

## ✨ Features
- 🔑 **User Authentication**: Farmers and consumers can register/login.
- 👨‍🌾 **Farmer Dashboard**: Farmers can add, edit, and view products.
- 🛒 **Marketplace View**: Consumers can view products and prices.
- 🔄 **Live Updates**: Products refresh dynamically from the backend.
- 🔐 **Password Security**: Secure password hashing with `bcrypt`.
- ⚡ **REST APIs**: Lightweight APIs for integration with web/mobile.

---

## 🛠️ Technology Stack
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Database**: MySQL (via PyMySQL + SQLAlchemy)
- **Other Libraries**: Flask-Bcrypt, Flask-CORS
- **Hosting Options**: PythonAnywhere, Render, DigitalOcean, Netlify (frontend)

---

## 📂 Project Structure
```
ZaoHub/
│
├── backend.py            # Flask backend API
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html        # Frontend HTML
├── static/
│   ├── css/
│   │   └── styles.css    # Stylesheet
│   ├── js/
│   │   └── main.js       # Frontend JavaScript
│   └── img/
│       ├── logo.png      # ZaoHub logo
│       ├── favicon.ico   # Favicon
│       └── favicon.png   # Favicon (PNG fallback)
└── zaohub_demo.sql       # Database dump (optional)
```

---

## ⚙️ Setup and Installation
### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/zaohub.git
cd zaohub
```

### 2. Create and Activate Virtual Environment (Recommended)
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🗄️ Database Setup
### 1. Create MySQL Database
```sql
CREATE DATABASE zaohub_demo;
```

### 2. Update Backend Config
Inside `backend.py`, update:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/zaohub_demo'
```
Replace `username` and `password` with your MySQL credentials.

### 3. (Optional) Import Demo Data
```bash
mysql -u username -p zaohub_demo < zaohub_demo.sql
```

If no `.sql` file is imported, Flask will auto-create empty tables when you run the app.

---

## ▶️ Running the Application
### 1. Start the Backend
```bash
python backend.py
```
The backend runs at `http://127.0.0.1:5000`.

### 2. Open Frontend
Open `http://127.0.0.1:5000/` in your browser. You should see the ZaoHub demo page.

---

## ☁️ Deployment Guide
### Backend Options
- **PythonAnywhere**: Easiest for Flask + MySQL.
- **Render / Railway**: Free hosting for small projects.
- **VPS (DigitalOcean, AWS EC2)**: Full control.

### Frontend Options
- Serve directly from Flask (`templates/ + static/`).
- OR deploy separately on **Netlify / Vercel / GitHub Pages** (update API base URL).

### Deployment Checklist
1. Create MySQL database on server.
2. Import `zaohub_demo.sql` (or let Flask create tables).
3. Deploy Flask backend.
4. Host frontend (Flask or Netlify).
5. Update `API_BASE` in `main.js` with your server’s domain.

---

## 💰 Revenue Model
ZaoHub is designed for **sustainability and scalability**, aligning our success directly with farmers and buyers:
- **Transaction Fees**: 5–7% on each successful sale (charged to buyer).
- **Premium Logistics Services**: Cold chain transport, aggregation points (premium fees).
- **Data Insights**: Aggregated anonymized data sold to NGOs, researchers, and agribusinesses.

---

## 🎯 Sustainability (SDG 2)
ZaoHub contributes to **UN SDG 2: Zero Hunger** by:
- Increasing farmer incomes through fair market access.
- Reducing post-harvest losses via better logistics.
- Ensuring consumers access affordable, nutritious food.

---

## 🚀 Future Roadmap
- ✅ Demo prototype with login and product listing.
- 📱 Native mobile app (React Native / Flutter).
- 🛍️ Full e-commerce features (cart, payments, orders).
- 🛰️ Logistics integration (delivery tracking).
- 📊 AI-powered market insights for farmers.
- 🌍 Expansion beyond Kenya to wider East Africa.

---

## 📜 License
This project is for demo and educational purposes. All rights reserved © 2025 ZaoHub.
