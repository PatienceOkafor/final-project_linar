#a program to calculate the average attendance of student within a 2 month lesson period and demonstrating the averages using different charts


class Students:
    total_students= 5
    lecture_days = 24
    name = input("enter name of student")
    gender = input("enter student's gender")
    code = input("enter student's code")
    student_count = int(input("enter the number of times students attended lectures ")) #sum of all students available in class
    merits = input("student validations:")
    attendance_average = lecture_days / student_count
    total_students += 1 
   
    def showcount():
        print("Total students",Students.total_students)
    
    def showstudents():
        print("Name:",Students.name, "Gender:", Students.gender, "code:",Students.code, "merits:",Students.merits) 
    
    def showattendance():
        print("name:",Students.name, "attendance:",Students.attendance_average)

student1= Students()
student2 = Students()
student3 = Students()
student4 = Students()
student5 = Students() 
student1.showattendance, student1.showstudents, student1.showcount

print("Average attendance of sudents is:",Students.attendance_average)