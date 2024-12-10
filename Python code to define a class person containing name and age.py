class Person:
    def __init__(data):
        data.name = ""
        data.age = 0
    def setdata(data, name, age):
        data.name = name
        data.age = age
    def display(data):
        print(f"Name: {data.name}")
        print(f"Age: {data.age}")
person1 = Person()
person1.setdata("Paul", 25)
person1.display()
