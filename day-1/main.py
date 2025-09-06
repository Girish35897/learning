from data_model import NewStudent, UpdateStudent
from fastapi import FastAPI

# Instantiate the app
app = FastAPI(
    title="My FastAPI Application",
    description="This is a sample FastAPI application with CRUD operations.",
    version="0.0.1",
)

# Dummy database
students = {
    1: {"name": "Alice", "age": 21, "course": "Mathematics"},
    2: {"name": "Bob", "age": 22, "course": "Physics"},
    3: {"name": "Charlie", "age": 23, "course": "Chemistry"},
}


# Create endpoints
@app.get("/")  # Get - To retrieve / fetch / read the data
def index():
    return {"message": "Welcome to the FastAPI application!"}


@app.get("/students")
def get_students():
    return students


@app.get("/students/{student_id}")
def get_student(student_id: int):  # Data type declaration useful for validation
    """
    Get a student by their ID.
    Parameters:
    - student_id: The ID of the student to retrieve.
    Returns: A dictionary with student details or an error message if not found.

    Input data will be validated based on the type hints provided.

    Example:
    - Request: GET /students/1
    - Response: {"name": "Alice", "age": 21, "course": "Mathematics"}
    """
    return students.get(
        student_id, {"error": f"No student found with the Id provided {student_id}"}
    )


# Endpoints for creating, updating, and deleting students can be added similarly.
@app.post("/add-student")  # Post - To create / add new data
def create_student(stu: NewStudent):
    if not students:
        student_id = 1
    else:
        student_id = max(students.keys()) + 1

    students[student_id] = stu.model_dump()
    return students[student_id]


@app.put("/update-student/{student_id}")  # Put - To update existing data
def update_student(student_id: int, stu: UpdateStudent):
    if student_id in students:
        if stu.name is not None:
            students[student_id]["name"] = stu.name
        if stu.age is not None:
            students[student_id]["age"] = stu.age
        if stu.course is not None:
            students[student_id]["course"] = stu.course
        return students[student_id]
    else:
        return {"error": f"No student found with the Id provided {student_id}"}


@app.delete("/delete-student/{student_id}")  # Delete - To delete existing data
def delete_student(student_id: int):
    if student_id in students:
        del students[student_id]
        return {"message": f"Student with ID {student_id} has been deleted."}
    else:
        return {"error": f"No student found with the Id provided {student_id}"}
