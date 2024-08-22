class ClassRoom:
    def __init__(self, grade=0, homeRoomTeacher="", studentList=[], numStudents=0):
        self.grade = grade
        self.homeRoomTeacher = homeRoomTeacher
        self.studentList = studentList
        self.numStudents = numStudents

    def get_student_no(self, n):
        return self.studentList[n - 1]

    def add_student(self, student_name):
        if len(self.studentList) >= 10:
            return False

        self.studentList.append(student_name)
        self.numStudents += 1
        return True

    def change_student(self, n, new_name):
        if n <= 0 or n > len(self.studentList):
            return False

        self.studentList[n - 1] = new_name
        return True

    def remove_student(self, student_name):
        if student_name not in self.studentList:
            return False

        self.studentList.remove(student_name)
        self.numStudents -= 1
        return True

    def remove_student_no(self, n):
        if n <= 0 or n > len(self.studentList):
            return False
        self.studentList.pop(n - 1)
        self.numStudents -= 1
        return True

    def set_grade(self, new_grade):
        self.grade = new_grade

    def set_homeroom_teacher(self, new_homeroom_teacher):
        self.homeRoomTeacher = new_homeroom_teacher

    def set_student_list(self, new_student_list):
        self.studentList = new_student_list

    def set_num_student(self, new_num_student):
        self.numStudents = new_num_student

    def get_grade(self):
        return self.grade

    def get_homeroom_teacher(self):
        return self.homeRoomTeacher

    def get_student_list(self):
        return self.studentList

    def get_num_student(self):
        return self.numStudents

    def __str__(self):
        return f"Grade: {self.grade}\nHomeroom Teacher: {self.homeRoomTeacher}\nStudents: {', '.join(self.studentList)}"
