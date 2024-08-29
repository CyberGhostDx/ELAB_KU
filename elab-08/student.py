class Student:
    def __init__(self, id, firstname, lastname):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.advisor = None
        self.major = None
        self.num_course = 0
        self.courses = []
        self.total_credit = 0

    def add_course(self, course):
        if (
            self.total_credit + course.credit <= 25
            and not course.course_id in self.courses
        ):
            if len(self.courses):
                if not self.courses[0]:
                    self.courses[0] = course.course_id
                    self.num_course += 1
                    self.total_credit += course.credit
                    return True
            self.courses.append(course.course_id)
            self.num_course += 1
            self.total_credit += course.credit
            return True
        return False

    def drop_course(self, course):
        if course.course_id in self.courses:
            if len(self.courses) == 1:
                self.courses = [""]
            else:
                self.courses.remove(course.course_id)
            self.total_credit -= course.credit
            self.num_course -= 1
            return True
        return False

    def set_advisor(self, advisor):
        self.advisor = advisor

    def set_major(self, major):
        self.major = major

    def __str__(self):
        id = f"Student ID: {self.id}"
        name = f"Name: {self.firstname} {self.lastname}"
        major = f"Major: {self.major}"
        advisor = f"Advisor: {self.advisor}"
        courses = f"Courses: {' '.join(self.courses)}"
        return f"{id}\n{name}\n{major}\n{advisor}\n{courses}"
