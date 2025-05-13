# 🎓 Grade Checker (University of Oulu Grading System)

A simple **CGPA Calculator** built with **FastAPI** (backend) and **HTML + JavaScript** (frontend).  
I made it just for fun! 🤓 It allows users to enter their grades and calculates CGPA manually based on the **University of Oulu's grading system**.

🚀 **Live Calculation**: No need for manual calculations—just enter your grades, and get results instantly!  

---

## 🛠 **Technologies Used**

### Backend (FastAPI)
- **Python 3.9+**
- **FastAPI** (for API development)
- **Uvicorn** (for running the API server)
- **CORS Middleware** (to allow frontend-backend communication)

### Frontend
- **HTML, CSS, JavaScript**
- **Fetch API** (to send requests to FastAPI)

---

## 📌 **Setup Guide**

### 1️⃣ Install Dependencies
Ensure you have **Python 3.9+** installed, then install dependencies:

```bash
pip install fastapi uvicorn
```

### 2️⃣ Start Backend Server
Run:
```bash
uvicorn main:app --reload
```
You should see:
```bash
Uvicorn running on http://127.0.0.1:8000
```

### 3️⃣ Start Frontend Server
Run (in another terminal):
```bash
python -m http.server 8001
```

Then, in your browser run,
```bash
[http://127.0.0.1:8001](http://127.0.0.1:8000)
```

### 📌 Usage Instructions
- Open the frontend
  - Open index.html in your browser (you can run python -m http.server 8001 to serve it locally).

- Enter total credits
  - Input the total number of credits you've completed (including pass/fail courses).

- Enter pass/fail credits
  - Specify how many of those credits are from pass/fail courses (they'll be excluded from the CGPA).

- Add course credit types
  - Click the "Add Credit Type" button to enter courses with a specific credit value (e.g., 5, 3, etc.).
  - You might have to click "Add Credit Type" more than once if have taken courses with different credit value.

- Fill in grade counts
  - For each credit type, enter how many times you received each grade (from 5 to 1).

- Click "Calculate CGPA"
  - The app will compute your CGPA based on the University of Oulu's grading system.

- Click "Refresh" to reset inputs
  - This clears all fields and allows you to start over.

### 🚀 Future Improvements
✅ Deploying online using Vercel or Render

✅ Storing results in localStorage

✅ Adding dark mode UI

✅ Allowing CSV file upload for bulk calculations

### 🏆 Contributor
[Mufrad Mahmud] – Developer

⭐ If you found this project useful, give it a star!
