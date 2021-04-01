class ClassA():
    a,b=10,20
    def display():
        print("hi Iam from class A")
class classB(classA):
    c,d = 23,24
    def show():
        print("Iam from class B")
obj= ClassB
print(obj.a)