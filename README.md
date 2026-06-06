# END-TO-END-DATA-SCIENCE-PROJECT

"COMPANY": CODTECH IT SOLUTIONS

"NAME": MAYERA HABEEB

"INTERN ID": CITS262

"DOMAIN": DATA SCIENCE

"DURATION": 4 WEEKS

"MENTOR": NEELA SANTHOSH

#"TASK-DESCRIPTION"

This task involved building a complete end-to-end data science project, from data collection and preprocessing all the way through to model deployment as a live web application. The result is a fully functional spam detection web app where a user can type any message and instantly receive a prediction of whether it is spam or not spam.

Tools and Libraries Used

The project used Python as the core language. Scikit-learn was used for text vectorization (TF-IDF) and training the Naive Bayes classification model. Flask was used to build and serve the web application. Pandas was used for data loading and exploration. Pickle was used to save and load the trained model and vectorizer. HTML and CSS were used to build the front-end webpage.

Platform

The project was developed on a Windows machine. The model training script (train_model.py) was run via Command Prompt. The Flask app (app.py) was also run via Command Prompt and accessed through a web browser at http://127.0.0.1:5000.

Dataset

The SMS Spam Collection dataset was used, containing 5,572 real SMS messages labeled as either "ham" (not spam) or "spam". The dataset was downloaded directly via Python's urllib module.

Process

The data was loaded and split into training and test sets. The text messages were converted into numerical features using TF-IDF (Term Frequency-Inverse Document Frequency) vectorization, which captures how important each word is across the dataset. A Multinomial Naive Bayes classifier was trained on these features, achieving a test accuracy of 97.85%. The trained model and vectorizer were saved using Pickle. The Flask app loads these saved files and uses them to make real-time predictions whenever a user submits a message through the webpage.

Application and Real-World Relevance

Spam detection is used by every major email provider and messaging platform in the world. This project demonstrates the full data science lifecycle — from raw data to a deployed, user-facing product — which is exactly how machine learning models are shipped in industry.

#OUTPUT

<img width="1896" height="847" alt="Image" src="https://github.com/user-attachments/assets/afc6f979-21ee-48fa-8738-0a5030084e8e" />
