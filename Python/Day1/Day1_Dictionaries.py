students = [
    {"name": "Somchai", "score": 75},
    {"name": "Somsri",  "score": 92},
    {"name": "Somboon", "score": 58}
]

def check_grade(s):
    if s < 60:
        return "F"
    elif s < 70:
        return "C"
    elif s < 80:
        return "B"
    elif s >= 80:
        return "A"
    
for s in students:
    name = s["name"]
    grade= check_grade(s["score"])
    print(f"Student: {name}, Grade: {grade}")