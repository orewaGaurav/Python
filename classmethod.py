# Write a program to count how many objects of a class are created.
class student():
    counter = 0
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        student.counter +=1
       
    def msg(self):
        print(f"Hello {self.name} you got {self.marks}% marks")
    @classmethod
    def object_count(cls):
        return cls.counter
s1 = student("Gaurav Mehta",95)
s2 = student("Priyanshu Chaudhary",96)
s3 = student("Lavesh Gaur",97)
print(s1.object_count())
print(student.object_count())
s1.msg()
s2.msg()
s3.msg()
