# 🚀 Quick Start Guide - Real-Time Sentiment Analyzer

## ⚡ 3-Step Setup

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
python -m textblob.download_corpora
```

### Step 2: Setup Database
```bash
python manage.py migrate
```

### Step 3: Run Server
```bash
python manage.py runserver
```

**Open in browser:** http://127.0.0.1:8000/

---

## 🎯 Quick Test

### Test the Sentiment Analysis:
```bash
python test_sentiment.py
```

### Example Usage:

1. **Positive Text:**
   - Input: "I love this product! It's amazing!"
   - Output: 😊 Positive (Polarity: ~0.6)

2. **Negative Text:**
   - Input: "This is terrible and disappointing."
   - Output: 😠 Negative (Polarity: ~-0.7)

3. **Neutral Text:**
   - Input: "It's okay, nothing special."
   - Output: 😐 Neutral (Polarity: ~0.0)

---

## 📁 Project Files Overview

```
Key Files:
├── analyzer/utils.py          → Sentiment analysis logic
├── analyzer/views.py          → Request handlers
├── analyzer/templates/home.html → User interface
├── analyzer/urls.py           → App routing
├── sentiment_app/settings.py  → Django configuration
├── requirements.txt           → Dependencies
└── test_sentiment.py          → Test script
```

---

## 🔧 Common Commands

```bash
# Start server
python manage.py runserver

# Start on different port
python manage.py runserver 8080

# Run tests
python test_sentiment.py

# Create superuser (for admin)
python manage.py createsuperuser

# Access admin panel
# http://127.0.0.1:8000/admin/
```

---

## 🐛 Troubleshooting

**Problem:** Module not found
```bash
Solution: pip install -r requirements.txt
```

**Problem:** TextBlob corpora missing
```bash
Solution: python -m textblob.download_corpora
```

**Problem:** Port already in use
```bash
Solution: python manage.py runserver 8080
```

---

## 📱 Features at a Glance

✅ Real-time sentiment analysis  
✅ AJAX (no page reload)  
✅ Color-coded results  
✅ Emoji indicators  
✅ Polarity scores  
✅ Character counter  
✅ Responsive design  
✅ CSRF protection  

---

## 🎨 User Interface

**Input:**
- Large textarea for text entry
- Character counter
- Analyze button

**Output:**
- Emoji (😊/😐/😠)
- Sentiment label (Positive/Neutral/Negative)
- Polarity score (-1.0 to +1.0)
- Color-coded background

---

## 📊 How Sentiment is Determined

```
Polarity Score Range:
-1.0 ←────────── 0 ──────────→ +1.0
(Most Negative)  (Neutral)  (Most Positive)

Classification:
• Polarity > 0.1  → Positive 😊
• Polarity < -0.1 → Negative 😠
• Otherwise       → Neutral 😐
```

---

## 🔗 URLs

- **Home Page:** http://127.0.0.1:8000/
- **AJAX Endpoint:** http://127.0.0.1:8000/analyze/
- **Admin Panel:** http://127.0.0.1:8000/admin/

---

## 💡 Tips

1. **Try different texts** to see how sentiment changes
2. **Use emojis** in your input - they affect sentiment!
3. **Mix positive and negative** words to see neutral results
4. **Check the polarity score** for fine-grained analysis
5. **Use AJAX** for seamless experience (no page reload)

---

## 📚 Technology Stack

- **Backend:** Django 5.2.6
- **ML Library:** TextBlob 0.19.0
- **NLP Engine:** NLTK 3.9.2
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Database:** SQLite3

---

## ✨ Example Texts to Try

```
Positive:
• "I absolutely love this! Best day ever!"
• "Fantastic experience, highly recommend!"
• "Amazing quality and great service!"

Negative:
• "Worst product ever, total waste of money."
• "Terrible experience, very disappointed."
• "Horrible quality, do not buy!"

Neutral:
• "It's okay, nothing special."
• "The product works as expected."
• "Average quality, decent price."
```

---

## 🎯 Project Goals Achieved

✅ Django backend  
✅ Pre-trained ML model (TextBlob)  
✅ No datasets/CSV files  
✅ Real-time analysis  
✅ User-friendly interface  
✅ CSRF protection  
✅ AJAX functionality  
✅ Emoji indicators  
✅ Polarity scores  
✅ Responsive design  

---

## 📞 Support

For issues or questions:
1. Check README.md for detailed documentation
2. Review PROJECT_DOCUMENTATION.md for code explanations
3. Run test_sentiment.py to verify setup

---

**Ready to analyze sentiments! 💬✨**

**Server Status:** 🟢 Running at http://127.0.0.1:8000/

