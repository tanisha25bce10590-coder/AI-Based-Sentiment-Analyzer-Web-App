 AI Sentiment Analyzer

An AI-powered web application that analyzes user emotions from textual input using Machine Learning and Natural Language Processing techniques.

 Key Highlights
 Machine Learning-based sentiment classification
 Confidence score using probability distribution
 Intelligent response generation
 Interactive web interface using Flask
 Lightweight and efficient implementation

 Tech Stack
Backend: Python, Flask
Machine Learning: Scikit-learn (Naive Bayes)
Data Processing: Pandas, TF-IDF
Frontend: HTML, CSS

 Project Structure
AI-Sentiment-App/
│── app.py
│── train.py
│── model.pkl
│── vectorizer.pkl
│── requirements.txt
│
│── templates/
│     └── index.html
│
│── static/
│     └── style.css

 Installation & Setup
1. Clone Repository
git clone <your-repo-link>
cd AI-Sentiment-App
2. Install Dependencies
pip install -r requirements.txt
3. Train Model
python train.py
4. Run Application
python app.py
5. Access Web App
http://127.0.0.1:5000/

 Working Principle
User inputs text
Text is transformed using TF-IDF vectorization
Model predicts sentiment using Naive Bayes
System returns:
Sentiment label
Confidence score
AI-generated response

 Example Output
Emotion: Positive  
Confidence: 78%  
 You seem happy and positive! Keep shining!
 Future Enhancements
Emotion classification (happy, sad, angry)
Multi-user compatibility analysis 
Deployment on cloud (Heroku / AWS)
UI enhancements and animations

 screenshot of my project result:

<img width="767" height="277" alt="AI_project1" src="https://github.com/user-attachments/assets/1ab1723a-464e-4a48-870e-61beac0c0831" />
<img width="622" height="391" alt="AI_project2" src="https://github.com/user-attachments/assets/753611bc-a232-45d1-aef9-5f1f05d7ac83" />

 Author

College Project -  AI Sentiment Analyzer Made with  using Python and knowledge of aiml

Made by - Tanisha Dangwal 
B.Tech CSE | AI & ML Enthusiast
