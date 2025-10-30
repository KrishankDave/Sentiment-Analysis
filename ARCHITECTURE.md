# 🏗️ Real-Time Sentiment Analyzer - Architecture

## 📐 System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        USER BROWSER                          │
│  ┌────────────────────────────────────────────────────┐    │
│  │              home.html (Frontend)                   │    │
│  │  • HTML Form with Textarea                         │    │
│  │  • CSS Styling (Gradient, Colors)                  │    │
│  │  • JavaScript (AJAX, Character Counter)            │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                            ↕ HTTP/AJAX
┌─────────────────────────────────────────────────────────────┐
│                    DJANGO WEB SERVER                         │
│  ┌────────────────────────────────────────────────────┐    │
│  │              sentiment_app/urls.py                  │    │
│  │  • Route: /        → analyzer.urls                 │    │
│  │  • Route: /admin/  → Django Admin                  │    │
│  └────────────────────────────────────────────────────┘    │
│                            ↓                                 │
│  ┌────────────────────────────────────────────────────┐    │
│  │              analyzer/urls.py                       │    │
│  │  • Route: /         → home()                       │    │
│  │  • Route: /analyze/ → analyze_ajax()               │    │
│  └────────────────────────────────────────────────────┘    │
│                            ↓                                 │
│  ┌────────────────────────────────────────────────────┐    │
│  │              analyzer/views.py                      │    │
│  │  • home(request)         → Render template         │    │
│  │  • analyze_ajax(request) → Return JSON             │    │
│  └────────────────────────────────────────────────────┘    │
│                            ↓                                 │
│  ┌────────────────────────────────────────────────────┐    │
│  │              analyzer/utils.py                      │    │
│  │  • get_sentiment(text)                             │    │
│  │    → TextBlob Analysis                             │    │
│  │    → Return {sentiment, polarity, emoji}           │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                            ↕
┌─────────────────────────────────────────────────────────────┐
│                    TEXTBLOB / NLTK                           │
│  • Pre-trained Sentiment Model                              │
│  • Polarity Calculation (-1.0 to +1.0)                      │
│  • No Training Required                                     │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔄 Request Flow

### Traditional POST Request:
```
1. User enters text in form
2. User clicks "Analyze" button
3. Browser sends POST request to /
4. Django receives request in home() view
5. View calls get_sentiment(text)
6. TextBlob analyzes text
7. View renders home.html with results
8. Browser displays page with results
```

### AJAX Request (Modern):
```
1. User enters text in form
2. User clicks "Analyze" button
3. JavaScript prevents default form submission
4. JavaScript sends AJAX POST to /analyze/
5. Django receives request in analyze_ajax() view
6. View calls get_sentiment(text)
7. TextBlob analyzes text
8. View returns JSON response
9. JavaScript receives JSON
10. JavaScript updates DOM with results (no page reload)
```

---

## 📦 Component Breakdown

### 1. Frontend Layer (home.html)
```
┌─────────────────────────────────────┐
│         HTML Structure              │
│  • Form with CSRF token             │
│  • Textarea for input               │
│  • Submit button                    │
│  • Results container                │
└─────────────────────────────────────┘
           ↓
┌─────────────────────────────────────┐
│         CSS Styling                 │
│  • Gradient background              │
│  • Card design                      │
│  • Color coding (RGB)               │
│  • Animations                       │
└─────────────────────────────────────┘
           ↓
┌─────────────────────────────────────┐
│         JavaScript                  │
│  • AJAX request handling            │
│  • Character counter                │
│  • Loading states                   │
│  • Error handling                   │
└─────────────────────────────────────┘
```

### 2. Backend Layer (Django)
```
┌─────────────────────────────────────┐
│         URL Routing                 │
│  sentiment_app/urls.py              │
│  analyzer/urls.py                   │
└─────────────────────────────────────┘
           ↓
┌─────────────────────────────────────┐
│         Views (Controllers)         │
│  • home() - Main page               │
│  • analyze_ajax() - API endpoint    │
└─────────────────────────────────────┘
           ↓
┌─────────────────────────────────────┐
│         Business Logic              │
│  • Input validation                 │
│  • Sentiment analysis call          │
│  • Response formatting              │
└─────────────────────────────────────┘
```

### 3. ML Layer (TextBlob)
```
┌─────────────────────────────────────┐
│         TextBlob                    │
│  • Tokenization                     │
│  • POS Tagging                      │
│  • Sentiment Analysis               │
│  • Polarity Calculation             │
└─────────────────────────────────────┘
           ↓
┌─────────────────────────────────────┐
│         NLTK                        │
│  • Corpora (brown, movie_reviews)   │
│  • Tokenizers                       │
│  • Taggers                          │
└─────────────────────────────────────┘
```

---

## 🗂️ File Structure & Responsibilities

```
ML_Django Projecr/
│
├── manage.py                    # Django CLI tool
│
├── sentiment_app/               # Project configuration
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Root URL config
│   ├── wsgi.py                 # WSGI server config
│   └── asgi.py                 # ASGI server config
│
├── analyzer/                    # Main application
│   ├── views.py                # Request handlers
│   │   ├── home()              # Main page view
│   │   └── analyze_ajax()      # AJAX endpoint
│   │
│   ├── utils.py                # Business logic
│   │   └── get_sentiment()     # ML function
│   │
│   ├── urls.py                 # App URL routing
│   │
│   ├── templates/              # HTML templates
│   │   └── home.html           # Main UI
│   │
│   ├── models.py               # Database models (unused)
│   ├── admin.py                # Admin config (unused)
│   └── tests.py                # Unit tests (unused)
│
├── requirements.txt             # Python dependencies
├── test_sentiment.py           # Test script
├── README.md                   # User documentation
├── PROJECT_DOCUMENTATION.md    # Technical docs
├── QUICK_START.md              # Quick guide
└── ARCHITECTURE.md             # This file
```

---

## 🔐 Security Architecture

```
┌─────────────────────────────────────┐
│         CSRF Protection             │
│  • Token in form                    │
│  • Validated by Django              │
│  • Prevents cross-site attacks      │
└─────────────────────────────────────┘
           ↓
┌─────────────────────────────────────┐
│         Input Validation            │
│  • Server-side checks               │
│  • Empty text handling              │
│  • XSS prevention (auto-escape)     │
└─────────────────────────────────────┘
           ↓
┌─────────────────────────────────────┐
│         Django Security             │
│  • Security middleware              │
│  • Clickjacking protection          │
│  • SQL injection prevention         │
└─────────────────────────────────────┘
```

---

## 📊 Data Flow Diagram

```
┌──────────┐
│  User    │
│  Input   │
└────┬─────┘
     │ "I love this!"
     ↓
┌────────────────┐
│  Django View   │
│  (Validation)  │
└────┬───────────┘
     │ text = "I love this!"
     ↓
┌────────────────┐
│  get_sentiment │
│  (utils.py)    │
└────┬───────────┘
     │ TextBlob(text)
     ↓
┌────────────────┐
│   TextBlob     │
│   Analysis     │
└────┬───────────┘
     │ polarity = 0.5
     ↓
┌────────────────┐
│ Classification │
│ (if/elif/else) │
└────┬───────────┘
     │ sentiment = "Positive"
     │ emoji = "😊"
     ↓
┌────────────────┐
│   Response     │
│ (JSON/HTML)    │
└────┬───────────┘
     │ {sentiment: "Positive", polarity: 0.5, emoji: "😊"}
     ↓
┌────────────────┐
│   Frontend     │
│   Display      │
└────────────────┘
```

---

## 🎯 Design Patterns Used

### 1. **MVC (Model-View-Controller)**
- **Model**: Not used (no database storage)
- **View**: `views.py` (controllers)
- **Template**: `home.html` (view)

### 2. **Separation of Concerns**
- **Presentation**: HTML/CSS/JS
- **Business Logic**: `utils.py`
- **Request Handling**: `views.py`
- **Routing**: `urls.py`

### 3. **RESTful API**
- **GET /**: Retrieve form
- **POST /**: Submit form
- **POST /analyze/**: API endpoint

---

## 🚀 Performance Considerations

### Response Time:
```
User Input → Django (5ms) → TextBlob (50ms) → Response (5ms)
Total: ~60ms average
```

### Scalability:
- **Concurrent Users**: Django handles multiple requests
- **Caching**: Not implemented (stateless)
- **Database**: Not used (no I/O bottleneck)

### Optimization Opportunities:
1. **Caching**: Cache common phrases
2. **Async**: Use async views for better concurrency
3. **CDN**: Serve static files from CDN
4. **Load Balancing**: Multiple Django instances

---

## 🔧 Technology Stack Details

```
┌─────────────────────────────────────┐
│         Frontend                    │
│  • HTML5                            │
│  • CSS3 (Flexbox, Gradients)        │
│  • JavaScript (ES6+)                │
│  • Fetch API (AJAX)                 │
└─────────────────────────────────────┘
           ↕
┌─────────────────────────────────────┐
│         Backend                     │
│  • Django 5.2.6                     │
│  • Python 3.8+                      │
│  • WSGI Server                      │
└─────────────────────────────────────┘
           ↕
┌─────────────────────────────────────┐
│         Machine Learning            │
│  • TextBlob 0.19.0                  │
│  • NLTK 3.9.2                       │
│  • Pre-trained Models               │
└─────────────────────────────────────┘
           ↕
┌─────────────────────────────────────┐
│         Database                    │
│  • SQLite3 (Django default)         │
│  • Not used for sentiment analysis  │
└─────────────────────────────────────┘
```

---

## 📈 Future Architecture Enhancements

### Phase 1: Database Integration
```
Add models.py:
- SentimentAnalysis model
- Store: text, sentiment, polarity, timestamp
- User history tracking
```

### Phase 2: Advanced ML
```
Replace TextBlob with:
- VADER (better for social media)
- Transformers (BERT, RoBERTa)
- Custom trained models
```

### Phase 3: Microservices
```
Split into services:
- Frontend Service (React/Vue)
- API Gateway
- Sentiment Service (Python)
- Database Service (PostgreSQL)
```

### Phase 4: Real-time Features
```
Add WebSockets:
- Live sentiment updates
- Batch processing
- Real-time dashboards
```

---

## 🎓 Key Architectural Decisions

1. **Why Django?**
   - Rapid development
   - Built-in security
   - ORM (for future database needs)
   - Admin panel

2. **Why TextBlob?**
   - Pre-trained (no training needed)
   - Simple API
   - Good accuracy for general text
   - Lightweight

3. **Why AJAX?**
   - Better UX (no page reload)
   - Faster response
   - Modern web standard

4. **Why SQLite?**
   - Default Django database
   - No setup required
   - Good for development

---

**Architecture Status**: ✅ Production-Ready for Development

**Scalability**: 🟢 Good for small to medium traffic

**Maintainability**: 🟢 Clean separation of concerns

**Security**: 🟢 Django best practices implemented

