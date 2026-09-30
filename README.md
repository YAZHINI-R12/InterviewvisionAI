InterviewVision AI

InterviewVision AI is an AI-powered technical interview preparation platform that helps students practice interviews using their own study material. Users can enter a concept as text or upload study material as an image, and the AI generates interview questions, evaluates answers, provides feedback, and adapts the next question based on performance.

Features
Text-based concept input
Image-based study material analysis
AI-generated technical interview questions
Conversational interview practice
Answer evaluation and feedback
Adaptive questioning based on performance
Beginner-friendly interview practice
Gemini-powered AI responses
Streamlit web interface
Graceful handling of temporary Gemini API errors

Project Workflow
User
  ↓
Text / Image Study Material
  ↓
Gemini Vision / AI Analysis
  ↓
Concept Understanding
  ↓
Interview Question
  ↓
User Answer
  ↓
Answer Evaluation
  ↓
Feedback
  ↓
Adaptive Follow-up Question
Tech Stack
Python
Streamlit
Google Gemini API
Google GenAI Python SDK
HTML/CSS for interface styling


Project Structure
InterviewvisionAI/
│
├── app.py
├── prompts.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── .streamlit/
    └── secrets.toml.example

Security: The actual .streamlit/secrets.toml file must not be committed to GitHub because it contains your Gemini API key.

Setup Instructions
1. Clone the repository
git clone https://github.com/YAZHINI-R12/InterviewvisionAI.git

Move into the project directory:

cd InterviewvisionAI
2. Create a virtual environment
python -m venv venv
Windows
venv\Scripts\activate
macOS / Linux
source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Create your Gemini API key

Create a Gemini API key through Google AI Studio.

Do not publish the API key in your source code or GitHub repository.

5. Configure Streamlit secrets

Create the following directory if it does not already exist:

.streamlit/

Inside it, create:

secrets.toml

Add:

GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"

Replace YOUR_GEMINI_API_KEY with your actual API key.

Important

Your local structure should be:

.streamlit/
├── secrets.toml
└── secrets.toml.example

The real secrets.toml must remain local and must not be uploaded to GitHub.

The example file should contain only:

GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
6. Run the application

Start Streamlit:

streamlit run app.py

The application will open in your browser.

Streamlit Cloud Deployment
1. Push the project to GitHub

Make sure the repository contains:

app.py
prompts.py
requirements.txt
README.md
.gitignore
.streamlit/secrets.toml.example

Do not commit:

.streamlit/secrets.toml

Your .gitignore should include:

venv/
.venv/
__pycache__/
*.pyc
.streamlit/secrets.toml
2. Create a Streamlit Cloud app

Open Streamlit Community Cloud and create a new application.

Select:

Repository: YAZHINI-R12/InterviewvisionAI
Branch: main
Main file: app.py
3. Add the API key

In your Streamlit Cloud application:

Manage app
    ↓
Settings
    ↓
Secrets

Add:

GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"

Save the secret and restart/redeploy the application.

4. Verify the deployment

Open the generated Streamlit application URL and test:

Enter a technical concept.
Submit the concept.
Check whether Gemini generates an interview question.
Answer the question.
Verify that the AI evaluates the answer.
Test image-based study material if enabled.
Security

Never commit API keys to GitHub.

The following file is intentionally ignored:

.streamlit/secrets.toml

Use:

.streamlit/secrets.toml.example

as the public configuration template.

If an API key has previously been exposed or committed, revoke/rotate that key and configure the new key through Streamlit Cloud Secrets.

Error Handling

InterviewVision AI handles temporary Gemini service availability errors.

If Gemini returns a temporary 503 UNAVAILABLE response, the application displays a user-friendly message instead of exposing the full server error.

Gemini is temporarily experiencing high demand.
Please try again in a moment.
Usage
Text-based interview practice
Enter a concept
        ↓
AI analyzes the concept
        ↓
AI generates an interview question
        ↓
User answers
        ↓
AI evaluates the answer
        ↓
Feedback + next question
Image-based practice

Users can provide study material such as:

handwritten notes
textbook pages
lecture slides
diagrams
programming questions
code screenshots

The AI uses the provided material as context for the interview session.

Future Enhancements
Final interview performance report
Topic-wise performance tracking
Strong and weak concept identification
More adaptive difficulty levels
Interview session history
Multiple programming-language interview modes
Resume-based interview preparation
Coding question evaluation
Dashboard for progress tracking
Author

Yazhini R

BE Computer Science and Engineering Student

Project: InterviewVision AI
