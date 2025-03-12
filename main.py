from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enabling CORS (For fixing frontend request issues)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allowing all domains (Need to change this in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Defining input data model
class GradeInput(BaseModel):
    total_credit: int
    five: int
    four: int
    three: int
    two: int
    one: int
    pass_cred: int

# CGPA Calculation Function
def calculate_grade(total_credit, five, four, three, two, one, pass_cred):
    if total_credit <= pass_cred:  # Prevent division by zero
        return "Invalid Input: Total credits must be greater than pass/fail credits."
    return ((five * 5 * 5) + (four * 5 * 4) + (three * 5 * 3) + 
            (two * 5 * 2) + (one * 5 * 1)) / (total_credit - pass_cred)

# API Endpoint
@app.post("/calculate/")
def get_cgpa(data: GradeInput):
    cgpa = calculate_grade(data.total_credit, data.five, data.four, data.three, data.two, data.one, data.pass_cred)
    return {"CGPA": round(cgpa, 2) if isinstance(cgpa, float) else cgpa}