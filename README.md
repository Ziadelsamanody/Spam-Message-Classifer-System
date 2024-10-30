# Email Spam Classifier

![Spam Classification](https://img.shields.io/badge/Task-Spam%20Classification-blue)
![Python](https://img.shields.io/badge/Python-3.7%2B-brightgreen)
![Framework](https://img.shields.io/badge/Framework-Flask-orange)
![Model](https://img.shields.io/badge/Model-MultinomialNB-yellow)

A machine learning-based email spam classifier that helps identify unwanted spam emails from legitimate ones. The project uses MultinomialNB (Multinomial Naive Bayes) algorithm and is deployed as both a Flask web application and a static GitHub Pages site.

## 📊 Model Details

- **Algorithm**: Multinomial Naive Bayes
- **Features**: Text vectorization using Count Vectorizer
- **Performance Metrics**:
  - Accuracy: 98
  - Precision: 98
  - Recall: 93
  - F1 Score: 95

## 🚀 Live Demo

- Adding soon

## 📓 Notebooks & Development

### Kaggle Notebooks
- [Model Development & Training](https://www.kaggle.com/code/ziadelsamanody/spam-or-ham-bayes-classifer-training)
- [Data Preprocessing & EDA](https://www.kaggle.com/code/ziadelsamanody/spam-or-ham-bayes-classifier-preprocesses)
- [Model Evaluation](https://www.kaggle.com/code/ziadelsamanody/spam-or-ham-bayes-classifer-testing-evaluate)

## 🛠️ Installation & Setup

### Local Flask Application
```bash
# Clone the repository
git clone https://github.com/your-username/spam-classifier.git
cd spam-classifier

# Create and activate virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt

# Run the Flask application
python app.py
```

### Static Version (GitHub Pages)
The static version is already deployed and requires no installation. Simply visit the GitHub Pages URL to use the classifier.

## 📁 Project Structure
```
spam-classifier/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── model/
│   ├── vectorizer.pkl    # Trained CountVectorizer
│   └── model.pkl         # Trained MultinomialNB model
├── templates/            # Flask HTML templates
│   ├── index.html
│   └── result.html
├── docs/                # Static version for GitHub Pages
│   ├── index.html
│   └── model_data.json
└── README.md
```

## 🔧 Usage

### Flask Version
1. Start the Flask server
2. Navigate to `http://localhost:5000`
3. Enter the email text in the provided text area
4. Click "Check for Spam" to get the prediction

### Static Version
1. Visit the GitHub Pages URL
2. Enter the email text
3. Get instant classification results

## 🤝 Contributing
Contributions are welcome! Here's how you can help:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 🔍 Future Improvements
- [ ] Add support for multiple languages
- [ ] Implement advanced text preprocessing
- [ ] Add model retraining capability
- [ ] Improve UI/UX design
- [ ] Add API documentation
- [ ] Implement user feedback collection

## Ziad Elsamanody 
