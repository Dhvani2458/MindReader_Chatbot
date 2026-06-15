# 🧠 Mindreader Chatbot

A web-based interactive chatbot built using **Python Flask**, **HTML**, **CSS**, and **JavaScript** that simulates a mind-reading conversation through a decision tree while performing basic lie detection.

---

## 📌 Project Overview

The Mindreader Chatbot is an intelligent conversational application that asks users a series of questions and navigates through a predefined decision tree based on their responses. The chatbot analyzes user inputs, detects simple contradictions, and generates personalized conclusions.

The project demonstrates concepts of:

* Decision Trees
* Rule-Based Artificial Intelligence
* Memory Management
* Basic Lie Detection
* Flask Web Development
* Frontend-Backend Communication

---

## ✨ Features

### 🎭 User Setup

* Collects:

  * Role (Student/Faculty)
  * Name
  * Gender

### 🧠 Mind Reading Engine

* Uses a decision tree structure.
* Traverses different conversation paths based on user responses.
* Produces unique personality outcomes.

### 🔍 Lie Detection

* Remembers previous user statements.
* Detects simple contradictions.
* Generates warning messages when conflicting responses are found.

### 💬 Interactive Chat Interface

* Modern chatbot-style interface.
* Real-time conversation.
* Enter key support.
* Dynamic message rendering.

### 👋 Personalized Goodbye Messages

* Different farewell messages based on:

  * User role
  * Gender

---

## 🏗️ Technology Stack

### Backend

* Python
* Flask

### Frontend

* HTML5
* CSS3
* JavaScript

### Data Structures & Algorithms

* Decision Tree
* Tree Traversal
* Memory-Based Pattern Matching

---

## 📂 Project Structure

mindreader/

├── app.py

├── mindreader.py

├── requirements.txt

│

├── templates/

│ └── index.html

│

└── static/

├── style.css

└── script.js

---

## ⚙️ How It Works

### Step 1: User Registration

The chatbot collects:

* Name
* Role
* Gender

### Step 2: Conversation Begins

The chatbot starts with:

"Are you feeling honest today?"

### Step 3: Decision Tree Traversal

Based on user responses:

* Yes → Left subtree
* No → Right subtree

The chatbot continues asking questions until a leaf node is reached.

### Step 4: Mind Reading Result

A personality conclusion is displayed such as:

* "You're loyal and noble. I can respect that! 😇"
* "You’re a mastermind. 😈"
* "You see truth as a fixed concept. 🧠"

### Step 5: Lie Detection

The chatbot stores previous answers and checks for contradictions.

Example:

Input 1:
"I never lie"

Input 2:
"I lied"

Output:
"Wait, didn’t you just say you never lie? 🤔"

---

## 🌟 Key Concepts Implemented

### Decision Tree

A tree-based structure where each node represents a question and each branch represents a possible answer.

### Tree Traversal

The chatbot traverses the tree according to user responses until a conclusion node is reached.

### Memory-Based Reasoning

The chatbot remembers previous statements and performs contradiction checks.

### Session Management

Flask sessions are used to:

* Store user information
* Preserve conversation state
* Maintain chatbot memory

---

## 🚀 Installation

### Clone Repository

git clone <repository-url>

cd mindreader

### Create Virtual Environment

python -m venv venv

### Activate Environment

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

### Install Dependencies

pip install -r requirements.txt

### Run Application

python app.py

### Open Browser

http://127.0.0.1:5000

---

## 🎯 Learning Outcomes

This project helps understand:

* Flask Application Development
* Client-Server Communication
* Session Handling
* Artificial Intelligence Basics
* Decision Tree Logic
* Interactive Web Development
* Frontend and Backend Integration

---

## 📖 Future Enhancements

* Advanced NLP Integration
* Machine Learning-Based Personality Analysis
* Voice Input Support
* Speech Synthesis Responses
* User Authentication
* Chat History Storage
* Database Integration
* Sentiment Analysis
* Emotion Detection

---

## 👨‍💻 Author

Developed as an educational project to demonstrate decision trees, lie detection, and interactive chatbot development using Flask.
