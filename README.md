# Quiz App - Database Management System Project

A Python-based quiz application with a MySQL backend, featuring user authentication, multiple quiz categories, and an interactive GUI built with Tkinter.

## 🚀 Features

- User authentication (Sign Up/Login)
- Multiple quiz categories (Computer, Automobiles, Business, General Knowledge, Nature)
- Interactive GUI with responsive design
- Score tracking
- User profile management

## 🛠️ Prerequisites

- Python 3.8+
- MySQL Server
- pip (Python package manager)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/jeswin2112/S5-DBMS-PROJECT.git
   cd S5-DBMS-PROJECT
   ```

2. **Set up a virtual environment (recommended)**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**
   - Make sure MySQL server is running
   - Update the database credentials in `db_connect.py` if needed
   - Run the `database.sql` script to set up the database schema

## 🎮 How to Run

1. Start the application:
   ```bash
   python main.py
   ```

2. Use the following test credentials to log in:
   - Username: AJAY
   - Email: AJAY@GMAIL.COM
   - Password: SJC

## 📂 Project Structure

- `main.py` - Entry point of the application
- `welcome_page.py` - Main dashboard after login
- `category_select.py` - Quiz category selection
- `admin.py` - Admin dashboard
- `db_connect.py` - Database connection handler
- `database.sql` - Database schema and initial data
- `assets/` - Contains images and icons

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Python and Tkinter
- MySQL for database management