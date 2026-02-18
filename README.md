# 🧑‍💻 Tarun Kumar Genji — Django Portfolio

A full-featured portfolio website built with Django.

---

## ⚡ How to Run This Project (Every Time)

Open terminal inside the `genji` folder and run:

```powershell
.venv\Scripts\python.exe manage.py runserver
```

Then open: **http://127.0.0.1:8000/**

---

## 🛠️ First Time Setup (Only Once)

```powershell
# 1. Install all dependencies
.venv\Scripts\python.exe -m pip install -r requirements.txt

# 2. Run database migrations
.venv\Scripts\python.exe manage.py migrate

# 3. Populate database with your profile, skills & projects
.venv\Scripts\python.exe populate_db.py

# 4. Create admin login (choose your own username & password)
.venv\Scripts\python.exe manage.py createsuperuser
```

---

## 🔗 All Links

| Page         | URL                                      |
|--------------|------------------------------------------|
| 🏠 Home       | http://127.0.0.1:8000/                  |
| 📁 Projects   | http://127.0.0.1:8000/projects/         |
| 📬 Contact    | http://127.0.0.1:8000/contact/          |
| 🔐 Login      | http://127.0.0.1:8000/accounts/login/   |
| ⚙️ Admin      | http://127.0.0.1:8000/admin/            |
| 🔌 API        | http://127.0.0.1:8000/api/projects/     |

---

## 📦 Features

- ✅ Modern dark glassmorphism UI
- ✅ Projects showcase with slug-based detail pages
- ✅ Contact form → sends real email to your Gmail
- ✅ WhatsApp floating button
- ✅ Admin panel (CRUD for projects, skills, messages)
- ✅ Login / Logout authentication
- ✅ REST API for projects
- ✅ Docker ready
- ✅ GitHub Actions CI

---

## 🔑 Admin Credentials

- **URL:** http://127.0.0.1:8000/admin/
- **Username:** admin
- **Password:** admin123 *(change this after first login!)*

---

## 🐳 Run with Docker

```bash
docker-compose up --build
```

---

## 🔌 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /api/projects/` | List all projects |
| `GET /api/projects/<slug>/` | Get single project detail |

---

## 📧 Email Setup

Gmail SMTP is configured in `portfolio/settings.py`.
To change email settings, update:
```python
EMAIL_HOST_USER     = 'your@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password'
```

> Get App Password from: https://myaccount.google.com/apppasswords
