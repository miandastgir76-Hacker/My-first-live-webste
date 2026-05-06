# Porsche Dealer - Car Dealership Website with Login Backend

A high-end animated car dealership website with a Django REST API backend for secure dealer authentication and dashboard management.

## Project Structure

```
.
├── login.html                          # Login page
├── porsche_911_gt3_showcase.html       # Main showcase page
├── system-dashboard.html               # Dealer dashboard
├── manage.py                           # Django management script
├── setup.py                            # Database setup script
├── requirements.txt                    # Python dependencies
├── config/                             # Django configuration
│   ├── settings.py                     # Django settings
│   ├── urls.py                         # URL routing
│   ├── wsgi.py                         # WSGI application
│   └── __init__.py
└── api/                                # Django REST API app
    ├── models.py                       # Database models
    ├── views.py                        # API views
    ├── serializers.py                  # DRF serializers
    ├── admin.py                        # Django admin
    ├── apps.py                         # App configuration
    └── migrations/                     # Database migrations
```

## Installation & Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Migrations

```bash
python manage.py migrate
```

### 3. Create Test Data

```bash
python setup.py
```

This will create:
- Admin user: `admin` / `Admin@123`
- Test dealer 1: `dealer@porsche-dealer.com` / `Dealer@123`
- Test dealer 2: `dealer2@porsche-dealer.com` / `Dealer@123`

### 4. Start Django Development Server

```bash
python manage.py runserver
```

The API will be available at: `http://localhost:8000`

## API Endpoints

### Authentication Endpoints

#### POST `/api/auth/login/`
Login with dealer credentials.

**Request:**
```json
{
    "email": "dealer@porsche-dealer.com",
    "password": "Dealer@123",
    "dealership_code": "PS-2024",
    "verification_code": "123456"
}
```

**Response:**
```json
{
    "success": true,
    "message": "Login successful",
    "user": {
        "id": 1,
        "username": "dealer1",
        "email": "dealer@porsche-dealer.com",
        "first_name": "John",
        "last_name": "Smith",
        "dealer_profile": {
            "id": 1,
            "dealership_code": "PS-2024",
            "dealership_name": "Premium Porsche Dealer NYC",
            "email": "dealer@porsche-dealer.com",
            "phone": "",
            "is_active": true
        }
    }
}
```

#### POST `/api/auth/logout/`
Logout the current user.

**Response:**
```json
{
    "success": true,
    "message": "Logout successful"
}
```

#### GET `/api/auth/user/`
Get current authenticated user details.

**Response:**
```json
{
    "success": true,
    "user": {
        "id": 1,
        "username": "dealer1",
        "email": "dealer@porsche-dealer.com",
        "first_name": "John",
        "last_name": "Smith",
        "dealer_profile": {
            "id": 1,
            "dealership_code": "PS-2024",
            "dealership_name": "Premium Porsche Dealer NYC",
            "email": "dealer@porsche-dealer.com",
            "phone": "",
            "is_active": true
        }
    }
}
```

## Test Login Credentials

### Dealer Account 1
- **Email:** `dealer@porsche-dealer.com`
- **Password:** `Dealer@123`
- **Dealership Code:** `PS-2024`
- **Verification Code:** Any 6 digits (e.g., `123456`)

### Dealer Account 2
- **Email:** `dealer2@porsche-dealer.com`
- **Password:** `Dealer@123`
- **Dealership Code:** `PS-2025`
- **Verification Code:** Any 6 digits (e.g., `123456`)

### Admin Panel
- **Username:** `admin`
- **Password:** `Admin@123`
- **URL:** `http://localhost:8000/admin`

## Database Models

### DealerProfile
Extends Django's User model with dealer-specific information.

**Fields:**
- `user` - OneToOne link to Django User
- `dealership_code` - Unique dealership identifier
- `dealership_name` - Name of the dealership
- `email` - Dealership email
- `phone` - Dealership phone number
- `is_active` - Account status
- `created_at` - Creation timestamp
- `updated_at` - Last update timestamp

## Features

✅ Secure login system with dealership verification
✅ RESTful API with Django REST Framework
✅ CORS enabled for frontend communication
✅ Session-based authentication
✅ Dealer profile management
✅ Admin dashboard for managing dealers
✅ Error handling and validation
✅ Beautiful animated UI

## Frontend Integration

The frontend (`login.html`) communicates with the Django backend using fetch API:

1. User submits login form
2. Frontend sends POST request to `/api/auth/login/`
3. Backend validates credentials
4. On success, user data is stored in localStorage
5. User is redirected to dashboard

## CORS Configuration

CORS is enabled for local development. Update `CORS_ALLOWED_ORIGINS` in `config/settings.py` for production use.

## Security Notes

For production deployment:

1. Set `DEBUG = False` in settings.py
2. Change `SECRET_KEY` to a secure random value
3. Update `ALLOWED_HOSTS` to your domain
4. Use environment variables for sensitive data
5. Implement proper 2FA verification
6. Use HTTPS only
7. Set secure cookie flags
8. Implement rate limiting

## Troubleshooting

### "Connection error" on login
- Ensure Django server is running: `python manage.py runserver`
- Check that server is accessible at `http://localhost:8000`
- Verify CORS settings allow your frontend URL

### "Invalid credentials" error
- Check test data was created: `python setup.py`
- Verify dealership code matches (e.g., PS-2024)
- Ensure verification code is 6 digits

### Database errors
- Run migrations: `python manage.py migrate`
- Reset database: `python manage.py migrate zero api`, then `python manage.py migrate`

## Running the Application

### Terminal 1 - Django Backend
```bash
python manage.py runserver
```

### Terminal 2 - Frontend (optional, can use live server extension)
Open `porsche_911_gt3_showcase.html` in your browser or use VS Code Live Server extension.

## Next Steps

- [ ] Implement email-based 2FA
- [ ] Add vehicle inventory management API
- [ ] Create test drive booking system
- [ ] Add payment gateway integration
- [ ] Implement user role-based access control
- [ ] Add activity logging
- [ ] Create comprehensive admin dashboard

---

For more information, check individual files or contact the development team.
