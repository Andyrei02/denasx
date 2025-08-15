# 🎸 Denis Cenusa — Music Portfolio
> [https://denasx-production.up.railway.app/](https://denasx-production.up.railway.app/)

A minimalistic, mobile-friendly Django web app that showcases the music of Denis Cenusa — a passionate guitar creator crafting soulful riffs and bold melodies.
The site presents his works, previews, and links to streaming platforms, along with an easy-to-use admin panel for updating visuals and content.

## ✨ Features
- 🎶 Music Portfolio — display album covers, GIF previews, and personal intro.
- 📱 Responsive Design — optimized for mobile, tablet, and desktop.
- ⚡ Django Admin Panel — upload new covers, change GIF animations, and update links in seconds.
- 📂 Persistent Media Storage — works with Railway volumes or other storage backends.
- 🎯 Social Links — direct visitors to Spotify & Instagram.

## 📦 Tech Stack
- Backend: Django 5.x
- Frontend: HTML, CSS (flexbox + responsive breakpoints)
- Database: SQLite (dev) / PostgreSQL (prod)
- Hosting: Railway
- Static & Media: Django staticfiles + Railway volumes

## 🚀 Installation
Clone repository
```sh
git clone https://github.com/Andyrei02/denasx.git
cd denasx
```
Create virtual environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```
Install dependencies
```sh
pip install -r requirements.txt
```
Apply migrations
```sh
python manage.py migrate
```
Create superuser
```sh
python manage.py createsuperuser
```
Run local server
```sh
python manage.py runserver
```

## ⚙️ Environment Variables
Create a .env file in the project root:
```ini
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
CSRF_TRUSTED_ORIGINS=https://127.0.0.1
```

## 🖋️ Admin Panel Usage
1. Login at /admin
2. Edit Header Content to update:
    - GIF for animation preview
    - Intro comment
    - Cover image & linked video
3. Save — changes appear instantly.

## 🌐 Deployment on Railway
```sh
# Install Railway CLI
npm install -g @railway/cli

# Login & link project
railway login
railway link

# Deploy
railway up
```

## License

MIT
