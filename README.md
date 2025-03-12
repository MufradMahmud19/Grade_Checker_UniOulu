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

### 📌 Usage Instructions
- Open the frontend (index.html).
- Enter the total credits and your grades.
- Click "Calculate CGPA".
- Click "Refresh" to reset inputs.

### 🚀 Future Improvements
✅ Deploying online using Vercel or Render
✅ Storing results in localStorage
✅ Adding dark mode UI
✅ Allowing CSV file upload for bulk calculations

### 🏆 Contributor
[Mufrad Mahmud] – Developer

⭐ If you found this project useful, give it a star!
