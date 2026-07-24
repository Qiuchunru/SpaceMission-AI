# 🚀 SpaceMission AI

AI-powered mission planning and space data interpretation assistant using Generative AI, FastAPI, React, and IBM Granite.

---

## 🌌 Project Overview

Space exploration missions generate massive amounts of scientific and engineering data. Mission teams need fast and reliable decision-support systems to analyze information, identify risks, and optimize mission operations.

**SpaceMission AI** is an AI-powered assistant designed to help engineers, researchers, and space enthusiasts understand mission requirements, evaluate risks, and generate mission planning recommendations.

This project was created for the **IBM AI Builders Challenge - August 2026: Advance Space Exploration with AI**.

---

# 🎯 Challenge Theme

## Advance Space Exploration with AI

This project focuses on:

- AI-powered mission planning assistants
- Space data interpretation tools
- Decision-support systems for complex environments
- Making space information easier to understand

---

# ❓ Problem Statement

Space missions involve complex decisions involving:

- Limited resources
- Communication delays
- Environmental risks
- Large amounts of telemetry data

Traditional analysis requires significant engineering time and expertise.

There is a need for AI systems that can transform complex space information into actionable insights.

---

# 💡 Solution Description

SpaceMission AI provides an intelligent assistant that can:

### 🚀 Mission Planning Assistance

Users provide:

- Mission target
- Mission objective
- Mission constraints

The AI generates:

- Mission recommendations
- Risk assessment
- Resource optimization suggestions


### 🛰️ Space Telemetry Interpretation

The system can analyze spacecraft information such as:

- Temperature
- Battery status
- Communication signals

and provide possible system insights and recommendations.

---

# 🏗️ System Architecture


```
User
 |
 |
React Frontend
 |
 |
FastAPI Backend
 |
 |
AI Processing Layer
 |
 |
IBM Granite (Integration Ready)
 |
 |
Mission Analysis Result
```

---

# 🤖 AI Approach

The project uses:

- Generative AI
- Prompt Engineering
- Large Language Model reasoning


The AI system uses structured prompts to guide the model to analyze:

- Mission objectives
- Operational constraints
- Potential risks
- Engineering recommendations


---

# 🧠 IBM Granite Integration

The project architecture is designed for IBM Granite integration.

Current workflow:

```
User Input

↓

Prompt Construction

↓

IBM Granite Model

↓

AI Generated Mission Analysis
```

The AI module contains a dedicated integration layer where IBM Granite API calls can be connected.

---

# 🛠️ Technology Stack


## Backend

- Python
- FastAPI
- Pydantic


## Frontend

- React
- Vite
- Axios


## AI Technologies

- IBM Granite
- Prompt Engineering
- Generative AI


## Development Tools

- GitHub
- IBM Bob
- VS Code

---

# 🤖 How IBM Bob Was Used

IBM Bob was used as an AI-assisted development tool throughout the project.

Examples:

- Generating initial project structure
- Understanding implementation requirements
- Assisting with FastAPI development
- Debugging frontend and backend issues
- Improving documentation
- Planning AI workflow architecture

---

# 📂 Project Structure

```
SpaceMission-AI

├── backend
│   ├── main.py
│   ├── ai.py
│   ├── prompts.py
│   ├── requirements.txt
│   └── .env.example
│
├── frontend
│   ├── App.jsx
│   ├── main.jsx
│   ├── index.html
│   └── package.json
│
├── data
│   └── sample_mission.txt
│
├── tests
│   └── test_ai.py
│
├── README.md
└── LICENSE
```

---

# ▶️ How to Run

## Backend

Navigate to backend:

```bash
cd backend
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start API:

```bash
uvicorn main:app --reload
```

Backend runs at:

```
http://localhost:8000
```

---

## Frontend

Navigate to frontend:

```bash
cd frontend
```

Install packages:

```bash
npm install
```

Start React application:

```bash
npm run dev
```

---

# 🧪 Testing

Install pytest:

```bash
pip install pytest
```

Run:

```bash
pytest
```

---

# 📸 Demo

Screenshots and demo videos will be added here.

---

# 🔮 Future Improvements

Future versions may include:

- Real IBM Granite API integration
- Satellite data analysis
- Space weather monitoring
- Real telemetry anomaly detection
- Vector database for mission knowledge retrieval


---

# 📜 License

This project is licensed under the MIT License.
