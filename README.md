A futuristic and responsive Quiz Application built using *Python Django.

This platform allows users to register, log in, attempt quizzes, track their performance, and explore different technical categories like Python, Java, DBMS, and DSA.

The project features a modern interface, animated dashboard, leaderboard system, timer-based quizzes, analytics, and dynamic quiz generation.

---


👨‍🎓 User Features
 * User Registration & Login Authentication
 * Multiple Categories
 * Timer-based Quiz System
 * Instant Result Calculation
 * Performance Analytics
 * Quiz History Tracking
 * Dark Futuristic Theme
   

🛠️ Admin Features
  * Manage Users
  * Manage Quizzes
  * Manage Questions
  * Track Quiz Attempts
  * Dashboard Analytics


 🧠 Quiz Categories
   * Python
   * Java
   * DBMS
   * DSA
   

 🎨 Technologies Used
  # Backend
  * Python
  * Django
  * SQLite

  # Frontend
  *CSS
  *HTML
  *JavaScript


📂 Project Structure

bash
quiz_project/
│
├── core/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   ├── management/
│   └── random_ai.py
│
├── static/
│
├── templates/
│
├── db.sqlite3
│
├── manage.py
│
└── requirements.txt


⚙️Installation Guide

Step 1 — Clone Repository

  bash
  git clone https://github.com/Akanksha-212/modern-ai-quiz-app.git


Step 2 — Open Project

  bash
  cd modern-ai-quiz-app


Step 3 — Create Virtual Environment

  bash
  python -m venv venv


Step 4 — Activate Virtual Environment

 #Windows

  bash
  venv\Scripts\activate


 #Mac/Linux

  bash
  source venv/bin/activate


Step 5 — Install Requirements

  bash
  pip install -r requirements.txt


Step 6 — Run Migrations

  bash
  python manage.py makemigrations


  bash
  python manage.py migrate


Step 7 — Load Quiz Categories

  bash
  python manage.py load_ai_quiz Python


  bash
  python manage.py load_ai_quiz Java


  bash
  python manage.py load_ai_quiz DBMS


  bash
  python manage.py load_ai_quiz DSA


Step 8 — Start Server
  bash
  python manage.py runserver


🌐Open in Browser
  bash
  http://127.0.0.1:8000/


📸 Main Pages
 * Home Page
 * Login Page
 * Register Page
 * Quiz List Page
 * Quiz Attempt Page
 * Result Page
 * My Attempts Dashboard
   


📊 Future Improvements
 * Real AI Question Generation 
 * Multiplayer Quiz Battle
 * Certificates & Achievements
 * Password Reset
 * AI Difficulty Prediction


🔥 Highlights
 * Fully Responsive
 * Clean Code Structure
 * Beginner Friendly
 * AI-Themed Design
 * Dark Dashboard Interface
