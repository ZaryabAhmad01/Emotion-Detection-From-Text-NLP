
# 🎭 Emotion Detection from Text using NLP

## 📊 Project Overview
This project implements a **machine learning model** to detect emotions from text using Natural Language Processing (NLP) techniques. The model classifies text into 6 emotion categories with **99.88% accuracy** using Logistic Regression and TF-IDF vectorization.

## 🎯 Emotion Categories
The model detects 6 primary emotions with the following mapping:

| Label | Emotion | Emoji | Description |
|-------|---------|--------|-------------|
| 0 | Sadness | 😢 | Feelings of sorrow, grief, or disappointment |
| 1 | Joy | 😄 | Feelings of happiness, pleasure, or delight |
| 2 | Love | ❤️ | Feelings of deep affection, care, or attachment |
| 3 | Anger | 😠 | Feelings of annoyance, displeasure, or hostility |
| 4 | Fear | 😨 | Feelings of anxiety, dread, or apprehension |
| 5 | Surprise | 😲 | Feelings of astonishment or unexpectedness |

## 📈 Performance & Results
- **Accuracy Score**: 99.88%
- **Model**: Logistic Regression
- **Vectorization**: TF-IDF with 5000 features
- **Dataset Size**: [410000] text samples
- **Train-Test Split**: 80-20 split with random state 42

## 🏗️ Technical Architecture

### Data Preprocessing Pipeline
```python
# TF-IDF Vectorization Configuration
tfidf = TfidfVectorizer(
    max_features=5000,    # Keep top 5000 words
    min_df=2,             # Ignore rare words (appear in <2 documents)
    max_df=0.8,           # Ignore very common words (appear in >80% documents)
    ngram_range=(1,2),    # Consider unigrams and bigrams
    stop_words="english"  # Remove English stop words
)
```

### Model Training
```python
# Logistic Regression Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Performance
training_accuracy = model.score(X_train, y_train) * 100
test_accuracy = model.score(X_test, y_test) * 100
```

## 🚀 Installation & Usage

### Prerequisites
```bash
pip install pandas scikit-learn numpy matplotlib seaborn jupyter
```

### Quick Start
```python
# 1. Clone the repository
git clone https://github.com/ZaryabAhmad01/Emotion-Detection-From-Text-NLP.git
cd Emotion-Detection-From-Text-NLP

# 2. Run the Jupyter notebook
jupyter notebook emotion_analysis.ipynb
```

### Make Predictions
```python
# Example usage for emotion prediction
new_tweets = [
    "This heavy feeling in my chest won't go away",  # Sadness
    "I feel so alive and happy right now",           # Joy
    "This makes me so mad I could scream",           # Anger
    "I'm afraid I'm not good enough for this",       # Fear
    "I love you more than anything",                 # Love
    "Wow! I can't believe this happened!"            # Surprise
]

for tweet in new_tweets:
    tweet_tfidf = tf.transform([tweet])
    prediction = model.predict(tweet_tfidf)[0]
    
    emotion_map = {0: "Sadness", 1: "Joy", 2: "Love", 
                   3: "Anger", 4: "Fear", 5: "Surprise"}
    
    print(f"Text: '{tweet}'")
    print(f"Predicted Emotion: {emotion_map[prediction]}")
    print("---")
```

## 💼 Business Applications

### 🏢 Customer Service
- **Sentiment Analysis**: Automatically categorize customer feedback by emotional tone
- **Priority Routing**: Route angry customers to experienced agents
- **Quality Monitoring**: Monitor agent performance based on customer emotions

### 📱 Social Media & Marketing
- **Brand Monitoring**: Track public emotional response to campaigns
- **Content Strategy**: Optimize content based on emotional engagement
- **Crisis Management**: Detect negative sentiment early

### 🏥 Mental Health
- **Therapy Apps**: Monitor patient emotional patterns over time
- **Support Systems**: Detect distress signals in user messages
- **Research**: Analyze emotional trends in population data

### 🎮 User Experience
- **Chatbots**: Adapt responses based on user emotion
- **Gaming**: Dynamic storylines based on player emotions
- **Recommendation Systems**: Suggest content based on emotional state

## 📊 Model Evaluation

### Training Metrics
```
Model: Logistic Regression
Training Accuracy: 99.88%
Test Accuracy: 99.88%
```

### Feature Importance
The model uses TF-IDF features that capture:
- **Word importance** in context
- **N-gram patterns** (single words and word pairs)
- **Emotion-specific vocabulary** for each category

## 🛠️ Technologies Used

### Core Libraries
- **Python 3.1+**
- **Pandas**: Data manipulation and analysis
- **Scikit-learn**: Machine learning algorithms and NLP tools
- **NumPy**: Numerical computations

### NLP & ML Components
- **TF-IDF Vectorizer**: Text to numerical features conversion
- **Logistic Regression**: Classification algorithm
- **Train-Test Split**: Model validation strategy
- **Accuracy Score**: Performance metric

## 📁 Project Structure
```
Emotion-Detection-From-Text-NLP/
│
├── emotion_analysis.ipynb          # Main Jupyter notebook
├── emotions.csv                    # Dataset file
├── README.md                       # Project documentation
```

## 🔮 Future Enhancements

### Immediate Improvements
- [ ] Add cross-validation for more robust evaluation
- [ ] Implement confidence scores for predictions
- [ ] Create confusion matrix visualization
- [ ] Add feature importance analysis

### Advanced Features
- [ ] Deep Learning models (LSTM, BERT, Transformers)
- [ ] Real-time emotion detection API
- [ ] Multi-language support
- [ ] Emotion intensity detection
- [ ] Mixed emotions classification

### Deployment Options
- [ ] Web interface with Streamlit/FastAPI
- [ ] REST API for integration
- [ ] Mobile application
- [ ] Browser extension

## 🎯 Key Features
- ✅ **High Accuracy**: 99.88% classification accuracy
- ✅ **Fast Inference**: Real-time emotion detection
- ✅ **Interpretable**: Logistic Regression provides clear decision boundaries
- ✅ **Scalable**: Handles large volumes of text data
- ✅ **Customizable**: Easy to extend with new emotion categories

## 👨‍💻 Author
**Zaryab Ahmad**
- BSIT Student passionate about AI, Machine Learning & Natural Language Processing
- GitHub: [ZaryabAhmad01](https://github.com/ZaryabAhmad01)
- Email: zaryabahmad983@gmail.com
  

## 🙏 Acknowledgments
- Dataset source: [Provide dataset source if available]
- Scikit-learn documentation and community
- NLP research community

---

## 📞 Contact
For questions, suggestions, or collaborations:
- GitHub: [ZaryabAhmad01](https://github.com/ZaryabAhmad01)
- Email: zaryabahmad983@gmail.com

**⭐ If this project helped you or you found it interesting, please give it a star on GitHub!**
