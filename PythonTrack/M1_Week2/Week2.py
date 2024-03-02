student = dict()

def add():
    print("Enter your name")
    name = input()

    print("Enter your age")
    age = input()

    print("Enter your grade")
    grade = input()

    student[name] = [name, age, grade]

def view():
    print("NAME  AGE  GRADE")
    for i in student.values():
            for j in i:
                print (j,end="  ")
            print("\n")
                

def update():
    print("Enter the name")
    uname = input()
    if(student.get(uname, 0)):
        print("studet found")
        print("Enter 1 to update name")
        print("Enter 2 to update age")
        print("Enter 3 to update grade")
        c2 = int(input())
        if c2 == 1:
            print("Enter name")
            student[uname][0] = input()
        elif c2 == 2:
            print("Enter age")
            student[uname][1] = input()
        elif c2 == 3:
            print("Enter grade")
            student[uname][2] = input()
    else:
        print("Student not found")

def delete():
    print("Enter the name")
    dname = input()
    del student[dname]
    print(dname, " has been deleted")

control = bool(int(input("Enter 1 to start, 0 to stop: ")))

while(control):
    print("1, Add a student\n2, Update data\n3, View\n4, Delete a student")
    cho = int(input())

    if cho == 1:
        add()
        control = bool(int(input("Enter 1 to continue, 0 to stop: ")))
    elif cho == 2: 
        update()
        control = bool(int(input("Enter 1 to continue, 0 to stop: ")))
    elif cho == 3:  
        print("1, View specific student")
        print("2, View all students")
        choi = int(input())  
        if choi == 1:
            print("Enter his name")
            name = input()
            print("NAME  AGE  GRADE")
            for i in student[name]:
                print (i,end="  ")
            
            control = bool(int(input("\nEnter 1 to continue, 0 to stop: ")))
        else:
            view()
            control = bool(int(input("\nEnter 1 to continue, 0 to stop: ")))
    elif cho == 4:
        delete()
        control = bool(int(input("\nEnter 1 to continue, 0 to stop: ")))


    

