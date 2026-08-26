# in this code snippet i will be storing and ENSURING student name id distionary is saved as string
from pydantic import BaseModel,EmailStr, Field
from typing import Optional

class Student(BaseModel):
    
    name: str = 'Abdul Rehman'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0,lt=10, default=5, description="A decimal value representing the cgpa of the sstudent")
    
new_student = {'age':'32','email':'abc@gmail.com'}

student = Student(**new_student)

student_dict = dict(student)

print(student_dict['age'])