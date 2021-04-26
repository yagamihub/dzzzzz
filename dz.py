class Student():
    def __init__(self,name='Ivan',age='18',groupnumber='10A'):
        self.name=name
        self.age=age
        self.groupnumber=groupnumber

    def getgroupnumber(self):

        print('Этот студент состоит в группе под номером',self.groupnumber)
    def setnameage(self):
        print('Этого студента звать',self.name,'и возраст его равен',self.age)

    def setgroupnumber(self):
        print('')
s1=Student('John','15','1')
s2=Student('Juan','20','2')
s3=Student('Julio','25','3')
s4=Student('Juanita','30','4')
s5=Student('Jose','35','5')

