class person:
    def __init__(self, name ,age,marital_status,school,course,reg_no):
        self.name = name 
        self.age = age 
        self.marital_status = marital_status
        self.school = school 
        self.course = course
        self.reg_no = reg_no
    
    def get_student_info(self):
        return(f" Name :{self.name}  ")


student1  = person("Christopher Bundi",23,"Single","Kibabii University","Bsc in Computer Science", "COM/0016/22")
print(student1.get_student_info())

        