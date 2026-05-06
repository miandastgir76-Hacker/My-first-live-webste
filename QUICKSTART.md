# 🚀 QUICKSTART GUIDE - Porsche Dealer Backend

## One-Command Setup (Windows)

Open PowerShell in the project folder and run:

```powershell
python -m pip install --upgrade pip; pip install -r requirements.txt; python manage.py migrate; python setup.py; python manage.py runserver
```

## Or Step-by-Step (Recommended)

### Step 1️⃣: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2️⃣: Setup Database
```bash
python manage.py migrate
```

### Step 3️⃣: Create Test Users
```bash
python setup.py
```

### Step 4️⃣: Start Server
```bash
python manage.py runserver
```

✅ Server will be running at: **http://localhost:8000**

---

## 📝 Test Login Credentials

Use these credentials to test the login system:

**Dealer Account:**
- Email: `dealer@porsche-dealer.com`
- Password: `Dealer@123`
- Dealership Code: `PS-2024`
- Verification Code: `123456` (any 6 digits)

**Alternative Dealer:**
- Email: `dealer2@porsche-dealer.com`
- Password: `Dealer@123`
- Dealership Code: `PS-2025`
- Verification Code: `123456`

**Admin Panel:**
- Username: `admin`
- Password: `Admin@123`
- URL: http://localhost:8000/admin

---

## 🌐 Opening the Frontend

1. Open `porsche_911_gt3_showcase.html` in your browser
2. Click the **LOGIN** button
3. Enter the test credentials above
4. You'll be redirected to the dashboard

---

## 🐛 Troubleshooting

### "Connection error" on login?
→ Make sure Django server is running: `python manage.py runserver`

### "Invalid credentials"?
→ Run `python setup.py` again to create test accounts

### Database error?
→ Run: `python manage.py migrate`

### Port already in use?
→ Run: `python manage.py runserver 8001` (use different port)

---

## 📁 Project Files

| File | Purpose |
|------|---------|
| `login.html` | Login page (frontend) |
| `porsche_911_gt3_showcase.html` | Main showroom page |
| `system-dashboard.html` | Dealer dashboard |
| `manage.py` | Django CLI |
| `setup.py` | Create test data |
| `config/` | Django configuration |
| `api/` | REST API code |
| `requirements.txt` | Python packages |
| `db.sqlite3` | Database (auto-created) |

---

## 🔌 API Endpoints

```
POST   /api/auth/login/        → Login with credentials
POST   /api/auth/logout/       → Logout (requires authentication)
GET    /api/auth/user/         → Get current user info
```

---

## ✨ Features

✅ Secure login system  
✅ Dealer verification  
✅ REST API with Django  
✅ CORS enabled  
✅ Beautiful animated UI  
✅ Admin dashboard  
✅ Session management  

---

## 📚 Next Steps

After successful setup:

1. **Test the login flow**
   - Go to `porsche_911_gt3_showcase.html`
   - Click LOGIN button
   - Enter test credentials

2. **Explore admin panel**
   - Go to http://localhost:8000/admin
   - Login with admin credentials
   - Manage dealer accounts

3. **Customize** (optional)
   - Modify API in `api/` folder
   - Add new features to dashboard
   - Customize authentication

---

## 🚨 Important Notes

- ⚠️ This is a development setup. For production, update:
  - `DEBUG = False` in `config/settings.py`
  - `SECRET_KEY` to a secure value
  - Database to PostgreSQL/MySQL
  - CORS settings for your domain
  - SSL/HTTPS configuration

- 🔐 For production, implement:
  - Proper 2FA verification
  - Email verification
  - Password reset system
  - Rate limiting
  - API key management

---

## 💡 Tips

- Use `python manage.py createsuperuser` to create additional admin accounts
- Check Django logs in terminal for debugging
- Use browser DevTools (F12) to inspect API calls
- See `README.md` for detailed documentation

---

Happy coding! 🎉

For detailed documentation, see **README.md**
