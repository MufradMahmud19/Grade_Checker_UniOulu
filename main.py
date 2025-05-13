from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for dev)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input model for each credit group
class GradeBlock(BaseModel):
    credit_val: int
    five: int
    four: int
    three: int
    two: int
    one: int

# Main input model
class GradeInput(BaseModel):
    total_credit: int
    pass_cred: int
    grades: List[GradeBlock]

# GPA calculation function
def calculate_cgpa(data: GradeInput):
    total_weighted_score = 0
    total_graded_credits = 0

    for block in data.grades:
        credit = block.credit_val
        total_weighted_score += (
            block.five * credit * 5 +
            block.four * credit * 4 +
            block.three * credit * 3 +
            block.two * credit * 2 +
            block.one * credit * 1
        )
        total_graded_credits += credit * (
            block.five + block.four + block.three + block.two + block.one
        )

    if total_graded_credits == 0:
        return "Invalid: No graded credits provided."

    return round(total_weighted_score / total_graded_credits, 2)

# API route
@app.post("/calculate/")
def get_cgpa(data: GradeInput):
    cgpa = calculate_cgpa(data)
    return {"CGPA": cgpa}
