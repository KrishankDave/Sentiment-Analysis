# 💬 Real-Time Sentiment Analyzer

A Django-based web application that performs real-time sentiment analysis on user-provided text using TextBlob. The app provides instant feedback with sentiment classification (Positive, Negative, or Neutral) along with emoji indicators and polarity scores.

## 🌟 Features

- **Real-time Sentiment Analysis**: Instant sentiment detection using TextBlob
- **Visual Feedback**: Color-coded results with emoji indicators
  - 😊 Positive (Green)
  - 😐 Neutral (Gray)
  - 😠 Negative (Red)
- **Polarity Score**: Displays sentiment score from -1.0 (most negative) to +1.0 (most positive)
- **AJAX Support**: Seamless analysis without page reloads
- **Character Counter**: Real-time character count display
- **Responsive Design**: Clean, modern UI with gradient backgrounds
- **CSRF Protection**: Secure form submissions

## 📁 Project Structure

```
ML_Django Projecr/
├── sentiment_app/          # Django project directory
│   ├── __init__.py
│   ├── settings.py         # Project settings
│   ├── urls.py            # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
├── analyzer/               # Django app for sentiment analysis
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py           # View functions for handling requests
│   ├── utils.py           # Sentiment analysis utility functions
│   ├── urls.py            # App-specific URL routing
│   ├── templates/
│   │   └── home.html      # Main user interface
│   └── migrations/
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── db.sqlite3            # SQLite database
└── README.md             # This file
```

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone or Download the Project

```bash
cd "ML_Django Projecr"
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Django (>=5.0, <6.0)
- textblob (>=0.17.1)
- nltk (>=3.8)

### Step 3: Download TextBlob Corpora

```bash
python -m textblob.download_corpora
```

This downloads the necessary NLTK data for sentiment analysis.

### Step 4: Run Database Migrations

```bash
python manage.py migrate
```

### Step 5: Start the Development Server

```bash
python manage.py runserver
```

The application will be available at: **http://127.0.0.1:8000/**

## 🎯 Usage

1. **Open the Application**: Navigate to http://127.0.0.1:8000/ in your web browser

2. **Enter Text**: Type or paste any text into the textarea (e.g., "I love this product!", "This is terrible", "It's okay")

3. **Analyze**: Click the "🔍 Analyze Sentiment" button

4. **View Results**: The sentiment analysis will appear below with:
   - Emoji indicator
   - Sentiment label (Positive/Negative/Neutral)
   - Polarity score (-1.0 to +1.0)

## 🔧 Technical Details

### Sentiment Analysis Logic (`analyzer/utils.py`)

The `get_sentiment()` function uses TextBlob to analyze text:

```python
def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0.1:
        return {'sentiment': 'Positive', 'polarity': polarity, 'emoji': '😊'}
    elif polarity < -0.1:
        return {'sentiment': 'Negative', 'polarity': polarity, 'emoji': '😠'}
    else:
        return {'sentiment': 'Neutral', 'polarity': polarity, 'emoji': '😐'}
```

### Views (`analyzer/views.py`)

- **`home(request)`**: Handles both GET and POST requests for the main page
- **`analyze_ajax(request)`**: AJAX endpoint that returns JSON responses

### URL Routing

- `/` - Main sentiment analyzer page
- `/analyze/` - AJAX endpoint for sentiment analysis

## 🎨 Frontend Features

- **Modern Design**: Gradient backgrounds and smooth animations
- **Responsive Layout**: Works on desktop and mobile devices
- **AJAX Integration**: No page reloads during analysis
- **Character Counter**: Real-time text length display
- **Loading States**: Visual feedback during analysis
- **Error Handling**: User-friendly error messages

## 📊 Example Inputs & Expected Results

| Input Text | Expected Sentiment | Approximate Polarity |
|------------|-------------------|---------------------|
| "I love this product! It's amazing!" | Positive | +0.6 to +0.8 |
| "This is terrible and disappointing." | Negative | -0.6 to -0.8 |
| "It's okay, nothing special." | Neutral | -0.1 to +0.1 |
| "The weather is nice today!" | Positive | +0.4 to +0.6 |
| "I hate waiting in long queues." | Negative | -0.5 to -0.7 |

## 🔒 Security Features

- **CSRF Protection**: All forms include CSRF tokens
- **Input Validation**: Server-side validation of user inputs
- **Secure Headers**: Django security middleware enabled

## 🛠️ Customization

### Adjusting Sentiment Thresholds

Edit `analyzer/utils.py` to change sensitivity:

```python
# Current thresholds
if polarity > 0.1:  # Positive threshold
elif polarity < -0.1:  # Negative threshold
```

### Styling Changes

Modify the `<style>` section in `analyzer/templates/home.html` to customize:
- Colors
- Fonts
- Layout
- Animations

## 📝 API Endpoint

### POST `/analyze/`

**Request:**
```javascript
fetch('/analyze/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-CSRFToken': csrftoken
    },
    body: 'text=' + encodeURIComponent(text)
})
```

**Response:**
```json
{
    "sentiment": "Positive",
    "polarity": 0.625,
    "emoji": "😊"
}
```

## 🧪 Testing

To test the sentiment analysis function:

```python
from analyzer.utils import get_sentiment

# Test positive sentiment
result = get_sentiment("I love this!")
print(result)  # {'sentiment': 'Positive', 'polarity': 0.5, 'emoji': '😊'}

# Test negative sentiment
result = get_sentiment("This is terrible!")
print(result)  # {'sentiment': 'Negative', 'polarity': -1.0, 'emoji': '😠'}
```

## 🐛 Troubleshooting

### Issue: "No module named 'textblob'"
**Solution:** Run `pip install -r requirements.txt`

### Issue: TextBlob errors about missing corpora
**Solution:** Run `python -m textblob.download_corpora`

### Issue: Port 8000 already in use
**Solution:** Use a different port: `python manage.py runserver 8080`

### Issue: CSRF verification failed
**Solution:** Ensure cookies are enabled in your browser

## 📚 Dependencies

- **Django**: Web framework
- **TextBlob**: Natural language processing library for sentiment analysis
- **NLTK**: Natural Language Toolkit (required by TextBlob)

## 🎓 Learning Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [TextBlob Documentation](https://textblob.readthedocs.io/)
- [Sentiment Analysis Guide](https://en.wikipedia.org/wiki/Sentiment_analysis)

## 📄 License

This project is open-source and available for educational purposes.

## 👨‍💻 Author

Created as a demonstration of Django + Machine Learning integration for real-time sentiment analysis.

---

**Enjoy analyzing sentiments! 💬✨**

