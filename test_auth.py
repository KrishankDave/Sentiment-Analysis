"""
Test script for authentication and sentiment analysis functionality
"""
import requests
from bs4 import BeautifulSoup

BASE_URL = "http://127.0.0.1:8000"

def test_authentication_flow():
    """Test the complete authentication and sentiment analysis flow"""
    
    print("=" * 60)
    print("TESTING AUTHENTICATION & SENTIMENT ANALYSIS")
    print("=" * 60)
    
    # Create a session to maintain cookies
    session = requests.Session()
    
    # Test 1: Access home page (should redirect to login)
    print("\n1. Testing home page access (should redirect to login)...")
    response = session.get(f"{BASE_URL}/")
    print(f"   Status Code: {response.status_code}")
    print(f"   Final URL: {response.url}")
    if "login" in response.url.lower() or "login" in response.text.lower():
        print("   ✅ Correctly redirected to login page")
    else:
        print("   ❌ Did not redirect to login")
    
    # Test 2: Access register page
    print("\n2. Testing register page...")
    response = session.get(f"{BASE_URL}/register/")
    print(f"   Status Code: {response.status_code}")
    if response.status_code == 200:
        print("   ✅ Register page accessible")
    else:
        print(f"   ❌ Register page returned {response.status_code}")
    
    # Test 3: Register a new user
    print("\n3. Testing user registration...")
    response = session.get(f"{BASE_URL}/register/")
    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
    
    register_data = {
        'username': 'testuser',
        'password1': 'TestPass123!',
        'password2': 'TestPass123!',
        'csrfmiddlewaretoken': csrf_token
    }
    
    response = session.post(f"{BASE_URL}/register/", data=register_data)
    print(f"   Status Code: {response.status_code}")
    if "login" in response.url.lower() or response.status_code == 302:
        print("   ✅ User registered successfully")
    else:
        print("   ⚠️  Registration may have issues (check manually)")
    
    # Test 4: Login with the new user
    print("\n4. Testing user login...")
    response = session.get(f"{BASE_URL}/login/")
    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
    
    login_data = {
        'username': 'testuser',
        'password': 'TestPass123!',
        'csrfmiddlewaretoken': csrf_token
    }
    
    response = session.post(f"{BASE_URL}/login/", data=login_data)
    print(f"   Status Code: {response.status_code}")
    print(f"   Final URL: {response.url}")
    if response.status_code == 200 or "home" in response.url:
        print("   ✅ User logged in successfully")
    else:
        print("   ⚠️  Login may have issues")
    
    # Test 5: Access home page after login
    print("\n5. Testing home page access after login...")
    response = session.get(f"{BASE_URL}/")
    print(f"   Status Code: {response.status_code}")
    if response.status_code == 200:
        print("   ✅ Home page accessible after login")
        if "testuser" in response.text:
            print("   ✅ Username displayed on page")
        if "Logout" in response.text or "logout" in response.text:
            print("   ✅ Logout button present")
    else:
        print(f"   ❌ Home page returned {response.status_code}")
    
    # Test 6: Perform sentiment analysis
    print("\n6. Testing sentiment analysis...")
    response = session.get(f"{BASE_URL}/")
    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
    
    test_texts = [
        ("I love this product! It's amazing!", "Positive"),
        ("This is terrible and awful.", "Negative"),
        ("It's okay, nothing special.", "Neutral")
    ]
    
    for text, expected in test_texts:
        sentiment_data = {
            'text': text,
            'csrfmiddlewaretoken': csrf_token
        }
        
        response = session.post(f"{BASE_URL}/analyze/", data=sentiment_data)
        print(f"\n   Text: '{text[:40]}...'")
        print(f"   Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"   Result: {result['sentiment']} ({result['polarity']})")
            if result['sentiment'] == expected:
                print(f"   ✅ Correct sentiment: {expected}")
            else:
                print(f"   ⚠️  Expected {expected}, got {result['sentiment']}")
        else:
            print(f"   ❌ Analysis failed with status {response.status_code}")
    
    # Test 7: Test logout
    print("\n7. Testing logout...")
    response = session.get(f"{BASE_URL}/logout/")
    print(f"   Status Code: {response.status_code}")
    if "login" in response.url.lower() or response.status_code == 302:
        print("   ✅ User logged out successfully")
    else:
        print("   ⚠️  Logout may have issues")
    
    # Test 8: Verify home page is protected after logout
    print("\n8. Testing home page protection after logout...")
    response = session.get(f"{BASE_URL}/")
    print(f"   Status Code: {response.status_code}")
    print(f"   Final URL: {response.url}")
    if "login" in response.url.lower():
        print("   ✅ Home page correctly protected after logout")
    else:
        print("   ❌ Home page not protected")
    
    print("\n" + "=" * 60)
    print("TESTING COMPLETE")
    print("=" * 60)
    print("\n📝 NEXT STEPS:")
    print("1. Open http://127.0.0.1:8000/ in your browser")
    print("2. Register a new account")
    print("3. Login and test sentiment analysis")
    print("4. Login to admin panel at http://127.0.0.1:8000/admin/")
    print("   Username: admin")
    print("   Password: admin123")
    print("5. Check 'User Activities' in admin to see logged activities")
    print("=" * 60)

if __name__ == "__main__":
    try:
        test_authentication_flow()
    except requests.exceptions.ConnectionError:
        print("❌ ERROR: Could not connect to server.")
        print("   Make sure the Django server is running:")
        print("   python manage.py runserver")
    except Exception as e:
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()

