# 🩺 Blood Test Analyzer - Debugged Version

This project takes in a blood test report (`.pdf`) and returns medical, nutritional, and fitness advice based on the report using AI agents.

---

## ✅ Final Fixes Summary

| File        | Buggy Issue                                      | Fix Applied                                                          |
| ----------- | ------------------------------------------------ | -------------------------------------------------------------------- |
| `tools.py`  | Hardcoded file path                              | Converted to accept dynamic file uploads                             |
| `agents.py` | Only `doctor` agent defined                      | Defined `verifier`, `nutritionist`, and `exercise_specialist` agents |
| `task.py`   | Tasks were unsafe, hallucinating, and misaligned | Rewritten with safe, aligned task descriptions and outputs           |
| `main.py`   | Used only 1 agent-task pair and flawed flow      | Refactored to handle all agents/tasks and correct request flow       |

---

## 🐞 Bug Analysis and Fixes

### 1. `tools.py`

**Bug:**

* Original version used hardcoded sample file paths and lacked flexibility.
* Incompatible or undefined decorators (`tool`) were imported.

**Fix:**

* Rewrote to use `@tool` from `crewai_tools` properly.
* File path is now passed dynamically via API/file upload.

---

### 2. `agents.py`

**Bug:**

* Only `doctor` agent was defined.
* No `verifier`, `nutritionist`, or `exercise_specialist` agents.
* No usage of `.env` variables.

**Fix:**

* Defined all four agents with proper roles and tools.
* Environment loading logic retained (`load_dotenv()` optional depending on deployment).

---

### 3. `task.py`

**Bug:**

* Extremely unsafe, unprofessional task descriptions.
* Encouraged fake data, URLs, and misdiagnosis.

**Fix:**

* Rewrote all four tasks with professional, medically safe logic.
* Tasks now use correct agents and tools with proper purpose and expected outputs.

---

### 4. `main.py`

**Bug:**

* Only handled `doctor` and a single task.
* No flexibility in agent/task triggering.
* API response unclear and unstructured.

**Fix:**

* Handles 4 tasks and 4 agents based on uploaded file and user query.
* Uses FastAPI for robust API interaction.
* Standardized async execution and response formatting.

---

## 🚀 Setup Instructions

### 1. Clone & Setup

```bash
cd blood-test-analyser
python -m venv myenv
source myenv/bin/activate  # or myenv\Scripts\activate on Windows
```

### 2. Install Required Packages

```bash
pip install -r requirements.txt
```

**Dependencies:**

* `crewai`
* `crewai-tools`
* `fastapi`
* `python-multipart`
* `uvicorn`

### 3. Add .env (Optional)

```bash
OPENAI_API_KEY=your_openai_key
```

### 4. Run the App

```bash
uvicorn main:app --reload
```

---

## 🎯 API Usage

### Endpoint: `/analyze`

**Method:** `POST`

**Form Data:**

* `file`: Blood test file (`.txt`, `.pdf`)
* `query`: User question (e.g., "What does this report indicate?")

**Response:**

```json
{
  "Medical": "...",
  "Nutrition": "...",
  "Exercise": "..."
}
```

---

## ✅ Example Query

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/analyze' \
  -F 'query="What are my abnormalities?"' \
  -F 'file=@sample_blood_report.txt'
```

---

## 📂 Folder Structure

```
├── main.py
├── tools.py
├── agents.py
├── task.py
├── requirements.txt
├── README.md
└── data/sample_blood_report.txt
```

---

## 🧠 Powered By

* [CrewAI](https://github.com/joaomdmoura/crewai)
* [FastAPI](https://fastapi.tiangolo.com/)

---

## 📬 Contact

For issues, raise a GitHub Issue or email: `your-email@example.com`

---

## ✅ Status: Production Ready
