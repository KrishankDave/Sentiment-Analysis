# 🔐 Authentication & Activity Tracking Guide

## Overview

This document describes the authentication system and activity tracking features added to the Real-Time Sentiment Analyzer project.

---

## 🎯 Features Implemented

### 1. User Authentication System
- ✅ User registration with Django's built-in `UserCreationForm`
- ✅ User login/logout functionality
- ✅ Login-protected sentiment analysis page
- ✅ Session management with cookies
- ✅ CSRF protection on all forms
- ✅ Welcome message with username display
- ✅ Logout button on main page

### 2. Activity Tracking System
- ✅ `UserActivity` model to track all sentiment analyses
- ✅ Automatic logging of user inputs and results
- ✅ Timestamp tracking for each activity
- ✅ Database storage with SQLite

### 3. Django Admin Panel
- ✅ Custom admin interface for `UserActivity`
- ✅ Display username, text preview, sentiment, and timestamp
- ✅ Filters by username, sentiment type, and date
- ✅ Search functionality
- ✅ Read-only access (no editing/adding)
- ✅ Pagination (25 items per page)

---

## 📂 Files Modified/Created

### Modified Files:
1. **`analyzer/models.py`** - Added `UserActivity` model
2. **`analyzer/views.py`** - Added authentication views and login protection
3. **`analyzer/admin.py`** - Configured admin panel for activity tracking
4. **`analyzer/urls.py`** - Added authentication URLs
5. **`analyzer/templates/home.html`** - Added welcome message and logout button
6. **`sentiment_app/settings.py`** - Added authentication settings

### New Files:
1. **`analyzer/templates/register.html`** - User registration page
2. **`analyzer/templates/login.html`** - User login page
3. **`test_auth.py`** - Automated testing script
4. **`AUTHENTICATION_GUIDE.md`** - This documentation file

---

## 🗄️ Database Schema

### UserActivity Model

```python
class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_input = models.TextField()
    sentiment_result = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
```

**Fields:**
- `user` - Foreign key to Django's built-in User model
- `text_input` - The text submitted for sentiment analysis
- `sentiment_result` - The result: "Positive", "Negative", or "Neutral"
- `timestamp` - Automatically set when record is created

---

## 🔄 User Flow

### New User Registration Flow:
```
1. Visit http://127.0.0.1:8000/
2. Redirected to /login/ (not authenticated)
3. Click "Sign up here" link
4. Fill registration form (username, password, confirm password)
5. Submit form
6. Redirected to /login/ with success message
7. Enter credentials and login
8. Redirected to home page (sentiment analyzer)
```

### Existing User Login Flow:
```
1. Visit http://127.0.0.1:8000/
2. Redirected to /login/ (not authenticated)
3. Enter username and password
4. Submit form
5. Redirected to home page with welcome message
6. Username displayed in header
7. Logout button available
```

### Sentiment Analysis Flow (Authenticated):
```
1. User enters text in textarea
2. Clicks "Analyze Sentiment" button
3. System analyzes sentiment using TextBlob
4. Result displayed on screen
5. Activity automatically saved to database:
   - User ID
   - Text input
   - Sentiment result
   - Timestamp
6. Admin can view all activities in admin panel
```

### Logout Flow:
```
1. Click "Logout" button
2. Session cleared
3. Redirected to /login/ with logout message
4. Home page now protected (requires login)
```

---

## 🎨 UI Components

### Login Page (`/login/`)
- Clean gradient background (purple/blue)
- White card with form
- Username and password fields
- "Log In" button
- Link to registration page
- Success/error messages display

### Register Page (`/register/`)
- Similar design to login page
- Username field
- Password field
- Confirm password field
- Password requirements displayed
- "Create Account" button
- Link to login page
- Validation error messages

### Home Page (Authenticated)
- **User Header** (new):
  - Welcome message: "Welcome, [username] 👋"
  - Logout button (red, top-right)
- Original sentiment analyzer interface
- All existing functionality preserved

---

## 🔐 Security Features

### 1. Login Protection
- `@login_required` decorator on `home()` view
- `@login_required` decorator on `analyze_ajax()` view
- Automatic redirect to login page for unauthenticated users

### 2. CSRF Protection
- CSRF tokens on all forms
- Django's built-in CSRF middleware
- Protection against cross-site request forgery

### 3. Password Security
- Django's built-in password hashing (PBKDF2)
- Password validation rules:
  - Minimum 8 characters
  - Cannot be too similar to username
  - Cannot be entirely numeric
  - Cannot be a common password

### 4. Session Management
- Secure session cookies
- Session expiration
- Logout clears session data

---

## 🛠️ Admin Panel Configuration

### Access Admin Panel:
```
URL: http://127.0.0.1:8000/admin/
Username: admin
Password: admin123
```

### UserActivity Admin Features:

**List Display:**
- Username
- Text Input (first 50 characters)
- Sentiment Result
- Timestamp

**Filters:**
- Sentiment Result (Positive/Negative/Neutral)
- Username
- Date (hierarchy)

**Search:**
- Search by username
- Search by text input
- Search by sentiment result

**Permissions:**
- View only (no add/edit)
- Activities created automatically
- Admin can only view and delete

**Ordering:**
- Most recent activities first

---

## 🧪 Testing

### Automated Testing Script

Run the test script to verify all functionality:

```bash
python test_auth.py
```

**Tests Performed:**
1. ✅ Home page redirects to login (unauthenticated)
2. ✅ Register page accessible
3. ✅ User registration works
4. ✅ User login works
5. ✅ Home page accessible after login
6. ✅ Username displayed on page
7. ✅ Logout button present
8. ✅ Sentiment analysis works (3 test cases)
9. ✅ Logout works
10. ✅ Home page protected after logout

### Manual Testing Checklist

**Registration:**
- [ ] Can access /register/
- [ ] Form validates password requirements
- [ ] Duplicate username shows error
- [ ] Password mismatch shows error
- [ ] Successful registration redirects to login

**Login:**
- [ ] Can access /login/
- [ ] Invalid credentials show error
- [ ] Valid credentials redirect to home
- [ ] Welcome message displays username

**Sentiment Analysis:**
- [ ] Can analyze text after login
- [ ] Results display correctly
- [ ] Activity saved to database
- [ ] AJAX analysis works

**Logout:**
- [ ] Logout button works
- [ ] Redirects to login page
- [ ] Home page requires login again

**Admin Panel:**
- [ ] Can login to /admin/
- [ ] UserActivity model visible
- [ ] Activities display correctly
- [ ] Filters work
- [ ] Search works
- [ ] Cannot add/edit activities

---

## 📊 Database Queries

### View All Activities:
```python
python manage.py shell

from analyzer.models import UserActivity
activities = UserActivity.objects.all()
for activity in activities:
    print(f"{activity.user.username}: {activity.sentiment_result}")
```

### View Activities by User:
```python
from analyzer.models import UserActivity
user_activities = UserActivity.objects.filter(user__username='testuser')
print(f"Total: {user_activities.count()}")
```

### View Activities by Sentiment:
```python
from analyzer.models import UserActivity
positive = UserActivity.objects.filter(sentiment_result='Positive').count()
negative = UserActivity.objects.filter(sentiment_result='Negative').count()
neutral = UserActivity.objects.filter(sentiment_result='Neutral').count()
print(f"Positive: {positive}, Negative: {negative}, Neutral: {neutral}")
```

### View Recent Activities:
```python
from analyzer.models import UserActivity
recent = UserActivity.objects.order_by('-timestamp')[:10]
for activity in recent:
    print(f"{activity.timestamp}: {activity.user.username} - {activity.sentiment_result}")
```

---

## 🚀 Quick Start Guide

### 1. Start the Server:
```bash
python manage.py runserver
```

### 2. Create a User Account:
- Open http://127.0.0.1:8000/
- Click "Sign up here"
- Enter username and password
- Click "Create Account"

### 3. Login:
- Enter your credentials
- Click "Log In"

### 4. Analyze Sentiment:
- Enter text in the textarea
- Click "Analyze Sentiment"
- View results

### 5. Check Admin Panel:
- Go to http://127.0.0.1:8000/admin/
- Login with admin credentials
- Click "User Activities"
- View all logged activities

---

## 🎓 Code Examples

### Accessing Current User in Views:
```python
@login_required
def my_view(request):
    username = request.user.username
    is_authenticated = request.user.is_authenticated
    # ... your code
```

### Creating Activity Records:
```python
from analyzer.models import UserActivity

UserActivity.objects.create(
    user=request.user,
    text_input="Sample text",
    sentiment_result="Positive"
)
```

### Querying Activities in Templates:
```python
# In views.py
activities = UserActivity.objects.filter(user=request.user)
context = {'activities': activities}

# In template
{% for activity in activities %}
    {{ activity.text_input }} - {{ activity.sentiment_result }}
{% endfor %}
```

---

## 🔧 Configuration Settings

### Authentication Settings (settings.py):
```python
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'
```

### URL Configuration (analyzer/urls.py):
```python
urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('analyze/', views.analyze_ajax, name='analyze_ajax'),
]
```

---

## 📈 Future Enhancements

### Potential Features:
1. **User Profile Page** - View personal activity history
2. **Password Reset** - Email-based password recovery
3. **Social Authentication** - Login with Google/GitHub
4. **Activity Dashboard** - Charts and statistics
5. **Export Activities** - Download as CSV/PDF
6. **Activity Filters** - Filter by date range, sentiment
7. **Batch Analysis** - Analyze multiple texts at once
8. **API Endpoints** - RESTful API for external access
9. **User Roles** - Different permissions for users
10. **Activity Sharing** - Share analysis results

---

## 🐛 Troubleshooting

### Issue: Cannot access home page
**Solution:** Make sure you're logged in. Visit /login/ first.

### Issue: Registration fails
**Solution:** Check password requirements (8+ characters, not too common).

### Issue: Activities not showing in admin
**Solution:** Make sure you're logged in as superuser (admin/admin123).

### Issue: CSRF token error
**Solution:** Clear browser cookies and try again.

### Issue: Server not starting
**Solution:** Run migrations first: `python manage.py migrate`

---

## 📞 Support

For issues or questions:
1. Check this documentation
2. Run the test script: `python test_auth.py`
3. Check server logs in terminal
4. Verify database with Django shell

---

**Last Updated:** October 30, 2025  
**Version:** 2.0 (with Authentication & Activity Tracking)

