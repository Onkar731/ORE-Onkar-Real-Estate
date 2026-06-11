# ORE - Onkar Real Estate

## Overview

ORE (Onkar Real Estate) is a Django-based real estate web application that enables users to browse property listings, submit inquiries, and contact realtors through a seamless online platform.

The system provides authentication features along with property listing management and email notification functionality for inquiries.

This project demonstrates real-world Django development including PostgreSQL integration, authentication, email handling via SMTP, and environment-based configuration management.

---

## Features

### User Authentication

* User Registration
* User Login
* User Logout

### Property Listings

* Browse Properties
* View Property Details
* Search and Filter Listings

### Inquiry System

* Submit Property Inquiries
* Email Notifications to Realtors
* Confirmation Email to Users

### System Features

* Secure Environment Configuration
* PostgreSQL Database Integration
* SMTP Email Integration
* Responsive UI Design

---

## Technology Stack

### Backend

* Python
* Django

### Database

* PostgreSQL

### Frontend

* HTML
* CSS
* Bootstrap
* JavaScript

### Tools

* Git
* GitHub

---

## Project Structure

```text
ORE/
│
├── accounts/
├── contacts/
├── listings/
├── pages/
├── realtors/
├── real_estate_project/
├── static/
├── templates/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/your-username/ORE.git
cd ORE
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create `.env` file and add required configuration (see below).

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run Server

```bash
python manage.py runserver
```

---

## Environment Variables

Create `.env` file:

```env
SECRET_KEY=your_secret_key

DEBUG=True

DB_NAME=ore_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
DEFAULT_FROM_EMAIL=your_email@gmail.com
```

---

## Email Feature Setup

This application uses SMTP for sending emails.

### When a property inquiry is made:

* Realtor receives an email notification
* User receives a confirmation email

⚠️ You must configure your own SMTP credentials in `.env`.

For Gmail:

* Enable 2-Step Verification
* Use App Password instead of normal password

---

## Database Configuration

This project uses **PostgreSQL** as the primary database.

Make sure PostgreSQL is installed and a database is created before running migrations.

OR

This project is designed to support flexible database configuration. By default, it uses PostgreSQL for production-level setup, but it can also be configured to run with SQLite for quick local testing and development.

### Default Setup (Recommended)

* PostgreSQL is recommended for full functionality and production-like behavior.

### Alternative Setup (Development)

* SQLite can be used without any additional setup for quick testing.

### Configuration

Database settings are managed through environment variables in the `.env` file. You can switch databases by updating the configuration in `settings.py` and `.env`.

#### Example: PostgreSQL (Recommended)

```env
DB_NAME=ore_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

#### Example: SQLite (Default Django)

If PostgreSQL is not configured, Django will automatically fall back to SQLite.

### Note

Ensure required database drivers are installed:

* PostgreSQL: `psycopg2` or `psycopg2-binary`


---

## Learning Outcomes

* Django Authentication System
* PostgreSQL Integration
* Environment-based configuration (.env)
* Email Automation with SMTP
* Real-world backend architecture
* CRUD operations and ORM usage

---

## Author

Developed by: Onkar Shengule

GitHub: https://github.com/your-username

---

## License
This project is developed for educational and learning purposes.