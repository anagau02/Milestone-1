class Course:
    
    def __init__(self, course_code="", credits=0, students=[]):
        '''Initialize Course obj'''
        self.course_code = course_code
        self.credits = credits
        self.students = students
    
    def add_student(self, student):
        '''Add student to course'''
        self.students.append(student)
    
    def get_student_count(self):
        return len(self.students)
    
class Student:

    def __init__(self, student_id="", name="", courses=dict()):
        '''Initialize Student obj'''
        self.student_id = student_id
        self.name = name
        self.courses = courses # {object:grade}
    
    def enroll(self, course, grade):
        '''Enroll student in course'''
        self.courses[course] = grade

# Currently working on Task 2
