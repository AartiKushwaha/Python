import mysql.connector as ms

d = ms.connect(
  host="localhost",
  user="root",
  password="aarti"
)

c = d.cursor()
c.execute("create database if not exists ONLINE_EXAMINATION;")
c.execute("use ONLINE_EXAMINATION;")
c.execute("create table if not exists QUESTIONS(QID int, question varchar(100), A varchar(100), B varchar(100), C varchar(100), D varchar(100), answer char(1));")
c.execute("create table if not exists STUDENTS(SID int, name varchar(20),date_of_exam char(20), ans1 char(1), ans2 char(1), ans3 char(1), ans4 char(1), ans5 char(1), ans6 char(1), ans7 char(1), ans8 char(1), ans9 char(1), ans10 char(1),score int);")

d.commit()


def generate_Ques():
    k1 = "insert into QUESTIONS values({},'{}','{}','{}','{}','{}','{}')".format(1,"What is moon", "Planet", "Satellite", "Rock", "Animal", "B")
    k2 = "insert into QUESTIONS values({},'{}','{}','{}','{}','{}','{}')".format(2,"What is tiger", "Planet", "Satellite", "Rock", "Animal", "D")
    k3 = "insert into QUESTIONS values({},'{}','{}','{}','{}','{}','{}')".format(3,"What is Rose", "Planet", "Flower", "Rock", "Animal", "B")
    k4 = "insert into QUESTIONS values({},'{}','{}','{}','{}','{}','{}')".format(4,"What is Sun", "Star", "Satellite", "Rock", "Animal", "A")
    k5 = "insert into QUESTIONS values({},'{}','{}','{}','{}','{}','{}')".format(5,"What is water", "Solid", "liquid", "Rock", "Animal", "B")
    k6 = "insert into QUESTIONS values({},'{}','{}','{}','{}','{}','{}')".format(6,"What is Jupiter", "Planet", "Satellite", "Rock", "Animal", "A")
    k7 = "insert into QUESTIONS values({},'{}','{}','{}','{}','{}','{}')".format(7,"What is Quartz", "Planet", "Satellite", "Rock", "Animal", "C")
    k8 = "insert into QUESTIONS values({},'{}','{}','{}','{}','{}','{}')".format(8,"What is Titan", "Planet", "Satellite", "Rock", "Animal", "B")
    k9 = "insert into QUESTIONS values({},'{}','{}','{}','{}','{}','{}')".format(9,"What is Human", "Planet", "Satellite", "Rock", "Animal", "D")
    k10 = "insert into QUESTIONS values({},'{}','{}','{}','{}','{}','{}')".format(10,"What is time", "Planet", "Satellite", "None", "Animal", "C")
    c.execute(k1)
    c.execute(k2)
    c.execute(k3)
    c.execute(k4)
    c.execute(k5)
    c.execute(k6)
    c.execute(k7)
    c.execute(k8)
    c.execute(k9)
    c.execute(k10)
    d.commit()

generate_Ques()
print("1) Press 1 for admin\n2) Press 2 for student")
mode = int(input())

if mode==1:
    
    while(True):
        pwd = input("Enter admin password: ")
        if pwd=="admin":
            break
        else:
            print("Wrong password!!!")

    while(True):
        print("Menu:-")
        print("1) Click 1 to view the questions")
        print("2) Click 2 to add more questions")
        print("3) Click 3 to modify answer")
        print("4) Click 4 to exit")

        ch = int(input("Enter your choice: "))
        if ch==1:
            print("The questions are: ")
            c.execute("select * from QUESTIONS;")
            for x in c:
                print(x)
                
        elif ch==2:
            i = int(input("Enter question id: "))
            q = input("Enter question: ")
            o1 = input("Enter option A: ")
            o2 = input("Enter option B: ")
            o3 = input("Enter option C: ")
            o4 = input("Enter option D: ")
            ans = input("Enter correct answer(A/B/C/D)")
            k = "insert into QUESTIONS values({}, '{}', '{}', '{}', '{}', '{}', '{}')".format(i, q, o1, o2, o3, o4, ans)
            c.execute(k)
            d.commit()

        elif ch==3:
            i1 = int(input("Enter question id: "))
            a = input("Enter new answer: ")
            l = "update QUESTIONS set answer='%s' where QID=%s"%(a, i1)
            c.execute(l)
            d.commit()

        elif ch==4:
            break
        else:
            print("Invalid input")
elif mode==2:
    while True:
        print("Menu:-")
        print("1) Click 1 to attempt test")
        print("2) Click 2 calcute score")
        print("3) Click 3 to exit")
        ch = int(input("Enter your choice: "))
        
        if ch==1:
            print("The question are: ")
            c.execute("select QID, question, A, B, C, D from QUESTIONS;")
            for x in c:
                print(x)
            print("Enter answers: ")
            i2 = int(input("Enter your id: "))
            na = input("Enter your name: ")
            da= input("enter date of examination")
            a1 = input("Enter answer 1: ")
            a2 = input("Enter answer 2: ")
            a3 = input("Enter answer 3: ")
            a4 = input("Enter answer 4: ")
            a5 = input("Enter answer 5: ")
            a6 = input("Enter answer 6: ")
            a7 = input("Enter answer 7: ")
            a8 = input("Enter answer 8: ")
            a9 = input("Enter answer 9: ")
            a10 = input("Enter answer 10: ")
            sc=10
            m = "insert into STUDENTS values({},'{}', '{}', '{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}',{})".format(i2,na,da,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,sc)
            c.execute(m)
            d.commit()
            ans_list = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]
            que_list=[]
            ca = "select answer from QUESTIONS";
            c.execute(ca)
            for x in c:
                que_list.append(x[0])
            marks=0
            for w in range(10):
                if ans_list[w]==que_list[w]:
                    marks+=1
            k = "update STUDENTS set score = %s where SID = %s"%(marks, i2)
            c.execute(k)
            d.commit()
            
        elif ch==2:
            i = int(input("Enter your id: "))
            ma = "select score from STUDENTS where SID=%s"%(i)
            c.execute(ma)
            marks=0
            for x in c:
                marks = x
            print("Marks obtained: ", marks[0])

        
        elif ch==3:
            break
        else:
            print("Invalid input!!")
else:
    print("INVALID")
            
            
            
            
                
                 
    
        

    
