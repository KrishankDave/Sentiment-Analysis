# 🚀 Quick Reference Guide - Sentiment Analyzer v2.0

## 📌 Quick Access

### URLs
- **Home Page:** http://127.0.0.1:8000/
- **Login:** http://127.0.0.1:8000/login/
- **Register:** http://127.0.0.1:8000/register/
- **Admin Panel:** http://127.0.0.1:8000/admin/

### Admin Credentials
```
Username: admin
Password: admin123
```

---

## ⚡ Quick Commands

### Start Server
```bash
python manage.py runserver
```

### Run Tests
```bash
python test_auth.py
```

### Create Superuser
```bash
python manage.py createsuperuser
```

### Make Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Django Shell
```bash
python manage.py shell
```

---

## 🎯 User Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    NEW USER JOURNEY                          │
└─────────────────────────────────────────────────────────────┘

1. Visit http://127.0.0.1:8000/
   ↓
2. Redirected to /login/ (not authenticated)
   ↓
3. Click "Sign up here"
   ↓
4. Fill registration form
   ├─ Username
   ├─ Password
   └─ Confirm Password
   ↓
5. Submit → Redirected to /login/
   ↓
6. Enter credentials
   ↓
7. Submit → Redirected to home page
   ↓
8. See welcome message: "Welcome, [username] 👋"
   ↓
9. Enter text for sentiment analysis
   ↓
10. Click "Analyze Sentiment"
    ↓
11. View results (Positive/Negative/Neutral)
    ↓
12. Activity automatically saved to database
    ↓
13. Click "Logout" when done
```

---

## 📊 Database Schema

```
┌─────────────────────────────────────────────────────────────┐
│                    UserActivity Model                        │
├─────────────────────────────────────────────────────────────┤
│ Field              │ Type              │ Description         │
├────────────────────┼───────────────────┼─────────────────────┤
│ id                 │ AutoField         │ Primary key         │
│ user               │ ForeignKey(User)  │ User who analyzed   │
│ text_input         │ TextField         │ Input text          │
│ sentiment_result   │ CharField(20)     │ Positive/Neg/Neu    │
│ timestamp          │ DateTimeField     │ When analyzed       │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔐 Authentication Features

### ✅ Implemented
- User registration
- User login/logout
- Session management
- Password hashing (PBKDF2)
- CSRF protection
- Login-required protection
- Welcome message with username
- Logout button

### 🔒 Security
- `@login_required` decorator on views
- CSRF tokens on all forms
- Secure session cookies
- Password validation rules
- XSS protection (auto-escaping)

---

## 📁 Project Structure

```
ML_Django Projecr/
│
├── analyzer/                      # Main app
│   ├── migrations/
│   │   └── 0001_initial.py       # UserActivity migration
│   ├── templates/
│   │   ├── home.html             # Main page (updated)
│   │   ├── login.html            # Login page (new)
│   │   └── register.html         # Register page (new)
│   ├── admin.py                  # Admin config (updated)
│   ├── models.py                 # UserActivity model (updated)
│   ├── urls.py                   # App URLs (updated)
│   ├── utils.py                  # Sentiment analysis
│   └── views.py                  # Views (updated)
│
├── sentiment_app/                 # Project config
│   ├── settings.py               # Settings (updated)
│   └── urls.py                   # Root URLs
│
├── test_auth.py                  # Test script (new)
├── AUTHENTICATION_GUIDE.md       # Full guide (new)
├── IMPLEMENTATION_SUMMARY.md     # Summary (new)
├── QUICK_REFERENCE.md            # This file (new)
├── manage.py                     # Django CLI
└── db.sqlite3                    # Database
```

---

## 🎨 Page Layouts

### Login Page (`/login/`)
```
┌─────────────────────────────────────┐
│     🔑 Welcome Back                 │
│     Log in to analyze sentiments    │
│                                     │
│  ┌───────────────────────────────┐ │
│  │ Username: [____________]      │ │
│  │ Password: [____________]      │ │
│  │                               │ │
│  │      [🚀 Log In]              │ │
│  └───────────────────────────────┘ │
│                                     │
│  Don't have an account? Sign up     │
└─────────────────────────────────────┘
```

### Register Page (`/register/`)
```
┌─────────────────────────────────────┐
│     🔐 Create Account               │
│     Join the Sentiment Analyzer     │
│                                     │
│  ┌───────────────────────────────┐ │
│  │ Username: [____________]      │ │
│  │ Password: [____________]      │ │
│  │ Confirm:  [____________]      │ │
│  │                               │ │
│  │      [✨ Create Account]      │ │
│  └───────────────────────────────┘ │
│                                     │
│  Already have an account? Log in    │
└─────────────────────────────────────┘
```

### Home Page (Authenticated)
```
┌─────────────────────────────────────┐
│  Welcome, username 👋  [🚪 Logout] │
├─────────────────────────────────────┤
│     💬 Real-Time Sentiment Analyzer │
│     Analyze sentiment instantly     │
│                                     │
│  ┌───────────────────────────────┐ │
│  │ [Text input area...]          │ │
│  │                               │ │
│  └───────────────────────────────┘ │
│                                     │
│      [🔍 Analyze Sentiment]        │
│                                     │
│  ┌───────────────────────────────┐ │
│  │      😊 Positive               │ │
│  │      Polarity: 0.75            │ │
│  └───────────────────────────────┘ │
└─────────────────────────────────────┘
```

---

## 🛠️ Admin Panel Features

### Access
```
URL: http://127.0.0.1:8000/admin/
Username: admin
Password: admin123
```

### UserActivity Admin
```
┌─────────────────────────────────────────────────────────────┐
│  User Activities                                             │
├─────────────────────────────────────────────────────────────┤
│  Filters:                                                    │
│  ☐ Positive  ☐ Negative  ☐ Neutral                         │
│  ☐ User: testuser  ☐ User: admin                           │
│  ☐ Date: Today  ☐ This week  ☐ This month                  │
│                                                              │
│  Search: [_________________] 🔍                             │
├─────────────────────────────────────────────────────────────┤
│  Username  │ Text Input (Preview)      │ Result  │ Time    │
├────────────┼───────────────────────────┼─────────┼─────────┤
│  testuser  │ I love this product! I... │ Positive│ 17:05   │
│  testuser  │ This is terrible and a... │ Negative│ 17:05   │
│  testuser  │ It's okay, nothing spe... │ Neutral │ 17:05   │
└─────────────────────────────────────────────────────────────┘
```

---

## 🧪 Testing Checklist

### Manual Testing
```
Registration:
☐ Access /register/
☐ Enter username and password
☐ Submit form
☐ Verify redirect to login
☐ Check success message

Login:
☐ Access /login/
☐ Enter credentials
☐ Submit form
☐ Verify redirect to home
☐ Check welcome message

Sentiment Analysis:
☐ Enter text
☐ Click analyze
☐ Verify result displays
☐ Check emoji matches sentiment
☐ Verify polarity score

Activity Tracking:
☐ Login to admin panel
☐ Navigate to User Activities
☐ Verify activities are logged
☐ Check all fields are correct

Logout:
☐ Click logout button
☐ Verify redirect to login
☐ Try accessing home (should redirect)
```

### Automated Testing
```bash
python test_auth.py
```

Expected output:
```
✅ Home page redirects to login
✅ Register page accessible
✅ User registered successfully
✅ User logged in successfully
✅ Home page accessible after login
✅ Username displayed on page
✅ Logout button present
✅ Sentiment analysis works
✅ User logged out successfully
✅ Home page protected after logout
```

---

## 💡 Common Tasks

### View All Activities
```python
python manage.py shell

from analyzer.models import UserActivity
activities = UserActivity.objects.all()
for a in activities:
    print(f"{a.user.username}: {a.sentiment_result}")
```

### Count Activities by Sentiment
```python
from analyzer.models import UserActivity
positive = UserActivity.objects.filter(sentiment_result='Positive').count()
negative = UserActivity.objects.filter(sentiment_result='Negative').count()
neutral = UserActivity.objects.filter(sentiment_result='Neutral').count()
print(f"Positive: {positive}, Negative: {negative}, Neutral: {neutral}")
```

### View User's Activities
```python
from analyzer.models import UserActivity
user_activities = UserActivity.objects.filter(user__username='testuser')
for a in user_activities:
    print(f"{a.timestamp}: {a.get_short_text()} -> {a.sentiment_result}")
```

### Delete All Activities
```python
from analyzer.models import UserActivity
UserActivity.objects.all().delete()
```

---

## 🐛 Troubleshooting

### Problem: Can't access home page
**Solution:** You need to login first. Visit /login/

### Problem: Registration fails
**Solution:** Check password requirements:
- At least 8 characters
- Not too similar to username
- Not entirely numeric
- Not a common password

### Problem: Activities not showing in admin
**Solution:** 
1. Make sure you're logged in as admin
2. Check that activities were created (run shell query)
3. Refresh the admin page

### Problem: CSRF token error
**Solution:**
1. Clear browser cookies
2. Make sure CSRF middleware is enabled
3. Check that {% csrf_token %} is in forms

### Problem: Server won't start
**Solution:**
1. Run migrations: `python manage.py migrate`
2. Check for port conflicts
3. Verify Python and Django versions

---

## 📚 Documentation Files

1. **AUTHENTICATION_GUIDE.md** - Complete authentication guide
2. **IMPLEMENTATION_SUMMARY.md** - Implementation details
3. **QUICK_REFERENCE.md** - This file
4. **README.md** - Original project documentation
5. **PROJECT_DOCUMENTATION.md** - Technical documentation

---

## 🎓 Key Code Snippets

### Protect a View
```python
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def my_view(request):
    # Your code here
    pass
```

### Log Activity
```python
from analyzer.models import UserActivity

UserActivity.objects.create(
    user=request.user,
    text_input=text,
    sentiment_result=result['sentiment']
)
```

### Get Current User
```python
# In views
username = request.user.username
is_authenticated = request.user.is_authenticated

# In templates
{{ user.username }}
{{ user.is_authenticated }}
```

---

## 🎉 Success Indicators

✅ Server starts without errors  
✅ Can register new users  
✅ Can login with credentials  
✅ Home page shows welcome message  
✅ Sentiment analysis works  
✅ Activities logged in database  
✅ Admin panel shows activities  
✅ Logout works correctly  
✅ Home page protected after logout  

---

## 📞 Quick Help

**Need help?**
1. Check this guide
2. Read AUTHENTICATION_GUIDE.md
3. Run test script: `python test_auth.py`
4. Check server logs in terminal
5. Use Django shell to inspect database

**Common Commands:**
```bash
# Start server
python manage.py runserver

# Run tests
python test_auth.py

# Django shell
python manage.py shell

# Create superuser
python manage.py createsuperuser

# Make migrations
python manage.py makemigrations
python manage.py migrate
```

---

**Version:** 2.0 with Authentication & Activity Tracking  
**Last Updated:** October 30, 2025  
**Status:** ✅ Fully Functional

