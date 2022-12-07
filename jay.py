import mysql.connector as ms
import time

while True:
    try:
        pwd = input("Enter SQL Password: ")
        d = ms.connect(
          host="localhost",
          user="root",
          password=pwd
        )
        print("Connecting....")
        print()
        time.sleep(2)
        break
    except :
        print("***WRONG PASSWORD***")


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

##generate_Ques()

print("1) Press 1 for admin")
print("2) Press 2 for student")

mode = int(input("Enter: "))

if mode==1:
    
    while(True):
        pwd = input("Enter admin password: ")
        if pwd=="admin":
            break
        else:
            print("!!!Wrong password!!!")

    while(True):
        print()
        print("Menu:-\n")
        print("1) Click 1 to view the questions")
        print("2) Click 2 to add more questions")
        print("3) Click 3 to modify answer")
        print("4) Click 4 to exit")
        print()

        try:
            ch = int(input("Enter your choice: "))
            print()
            
            if ch==1:
                print("The questions are:\n\n ")
##                c.execute("select * from QUESTIONS;")
##                for x in c:
##                    print(x)
                
                ques = []
                q = "select question from QUESTIONS";
                c.execute(q)
                for x in c:
                    ques.append(x[0])
                    
                options = []
                
                for w in range(10):
                    op = []
                    oa = "select A from QUESTIONS where QID=%s"%(w+1)
                    c.execute(oa)
                    
                    for x in c:
                        op.append(x[0])
                        
                    ob = "select B from QUESTIONS where QID=%s"%(w+1)
                    c.execute(ob)
                    
                    for x in c:
                        op.append(x[0])
                        
                    oc = "select C from QUESTIONS where QID=%s"%(w+1)
                    c.execute(oc)
                    
                    for x in c:
                        op.append(x[0])
                        
                    od = "select D from QUESTIONS where QID=%s"%(w+1)
                    c.execute(od)
                    
                    for x in c:
                        op.append(x[0])

                    options.append(op)
                    
                answers = []
                a = "select answer from QUESTIONS";
                c.execute(a)
                
                for x in c:
                    answers.append(x[0])

                cnt = 0
            
                print("\nQuestion 1")
                print(ques[cnt])
                
                choice = options[cnt]
                print("Option A: ",choice[0])
                print("Option B: ",choice[1])
                print("Option C: ",choice[2])
                print("Option D: ",choice[3])
                print()
                print("Correct Answer: ", answers[cnt])
                print()
                cnt+=1

                print("\nQuestion 2")
                print(ques[cnt])
                
                choice = options[cnt]
                print("Option A: ",choice[0])
                print("Option B: ",choice[1])
                print("Option C: ",choice[2])
                print("Option D: ",choice[3])
                print()
                print("Correct Answer: ", answers[cnt])
                print()

                cnt+=1

                print("\nQuestion 3")
                print(ques[cnt])
                
                choice = options[cnt]
                print("Option A: ",choice[0])
                print("Option B: ",choice[1])
                print("Option C: ",choice[2])
                print("Option D: ",choice[3])
                print()
                print("Correct Answer: ", answers[cnt])
                print()

                cnt+=1

                print("\nQuestion 4")
                print(ques[cnt])
                
                choice = options[cnt]
                print("Option A: ",choice[0])
                print("Option B: ",choice[1])
                print("Option C: ",choice[2])
                print("Option D: ",choice[3])
                print()
                print("Correct Answer: ", answers[cnt])
                print()

                cnt+=1

                print("\nQuestion 5")
                print(ques[cnt])
                
                choice = options[cnt]
                print("Option A: ",choice[0])
                print("Option B: ",choice[1])
                print("Option C: ",choice[2])
                print("Option D: ",choice[3])
                print()
                print("Correct Answer: ", answers[cnt])
                print()

                cnt+=1

                print("\nQuestion 6")
                print(ques[cnt])
                
                choice = options[cnt]
                print("Option A: ",choice[0])
                print("Option B: ",choice[1])
                print("Option C: ",choice[2])
                print("Option D: ",choice[3])
                print()
                print("Correct Answer: ", answers[cnt])
                print()

                cnt+=1

                print("\nQuestion 7")
                print(ques[cnt])
                
                choice = options[cnt]
                print("Option A: ",choice[0])
                print("Option B: ",choice[1])
                print("Option C: ",choice[2])
                print("Option D: ",choice[3])
                print()
                print("Correct Answer: ", answers[cnt])
                print()

                cnt+=1

                print("\nQuestion 8")
                print(ques[cnt])
                
                choice = options[cnt]
                print("Option A: ",choice[0])
                print("Option B: ",choice[1])
                print("Option C: ",choice[2])
                print("Option D: ",choice[3])
                print()
                print("Correct Answer: ", answers[cnt])
                print()

                cnt+=1

                print("\nQuestion 9")
                print(ques[cnt])
                
                choice = options[cnt]
                print("Option A: ",choice[0])
                print("Option B: ",choice[1])
                print("Option C: ",choice[2])
                print("Option D: ",choice[3])
                print()
                print("Correct Answer: ", answers[cnt])
                print()

                cnt+=1

                print("\nQuestion 10")
                print(ques[cnt])
                
                choice = options[cnt]
                print("Option A: ",choice[0])
                print("Option B: ",choice[1])
                print("Option C: ",choice[2])
                print("Option D: ",choice[3])
                print()
                print("Correct Answer: ", answers[cnt])
                print()

                cnt+=1
                    
            elif ch==2:
                
                i = int(input("Enter question id: "))
                q = input("Enter question: ")
                o1 = input("Enter option A: ")
                o2 = input("Enter option B: ")
                o3 = input("Enter option C: ")
                o4 = input("Enter option D: ")
                print()
                ans = input("Enter correct answer(A/B/C/D)")
                k = "insert into QUESTIONS values({}, '{}', '{}', '{}', '{}', '{}', '{}')".format(i, q, o1, o2, o3, o4, ans)

                c.execute(k)
                d.commit()

            elif ch==3:
                
                i1 = int(input("Enter question id for the question to be updated: "))
                qu = input("Enter new question: ")
                c1 = input("Enter option A: ")
                c2 = input("Enter option B: ")
                c3 = input("Enter option C: ")
                c4 = input("Enter option D: ")
                a = input("Enter new answer: ")
                
                l = "update QUESTIONS set answer='%s' where QID=%s"%(a, i1)
                c.execute(l)
                d.commit()
                
                m = "update QUESTIONS set question='%s' where QID=%s"%(qu, i1)
                c.execute(m)
                d.commit()
                
                n = "update QUESTIONS set A='%s' where QID=%s"%(c1, i1)
                c.execute(n)
                d.commit()
                
                o = "update QUESTIONS set B='%s' where QID=%s"%(c2, i1)
                c.execute(o)
                d.commit()
                p = "update QUESTIONS set C='%s' where QID=%s"%(c3, i1)
                c.execute(p)
                d.commit()
                
                q = "update QUESTIONS set D='%s' where QID=%s"%(c4, i1)
                c.execute(q)
                d.commit()
                
                print("Question updated sucessfully....")

            elif ch==4:
                break
        except:
            print("_____Integer Value required_____")
elif mode==2:
    
    while True:
        
        print("Menu:-\n")
        print("1) Click 1 to attempt test")
        print("2) Click 2 calcute score")
        print("3) Click 3 to exit")
        print()
        
        try:
            ch = int(input("Enter your choice: "))
            
            if ch==1:

                ques = []
                
    ##            print("The question are: ")
    ##            c.execute("select QID, question, A, B, C, D from QUESTIONS;")
    ##            for x in c:
    ##                print(x)
    ##            print("Enter answers: ")
                
                i2 = int(input("Enter your id: "))
                na = input("Enter your name: ")
                da= input("Enter date of examination(dd-mm-yyyy)")

                q = "select question from QUESTIONS";
                c.execute(q)
                for x in c:
                    ques.append(x[0])

                options = []
                for w in range(10):
                    op = []
                    oa = "select A from QUESTIONS where QID=%s"%(w+1)
                    c.execute(oa)
                    
                    for x in c:
                        op.append(x[0])
                        
                    ob = "select B from QUESTIONS where QID=%s"%(w+1)
                    c.execute(ob)
                    
                    for x in c:
                        op.append(x[0])
                        
                    oc = "select C from QUESTIONS where QID=%s"%(w+1)
                    c.execute(oc)
                    
                    for x in c:
                        op.append(x[0])
                    od = "select D from QUESTIONS where QID=%s"%(w+1)
                    c.execute(od)
                    
                    for x in c:
                        op.append(x[0])

                    options.append(op)
                    
                    
                cnt = 0
                
                print("\nQuestion 1")
                print(ques[cnt])
                
                choice = options[cnt]
                
                print("Option A: ",choice[0])
                print("Option B: ",choice[1])
                print("Option C: ",choice[2])
                print("Option D: ",choice[3])
                print()

                a1 = input("Enter your answer(A/B/C/D): ")
                cnt+=1

                print("\nQuestion 2")
                print(ques[cnt])
                
                choice = options[cnt]
                
                print("Option A: ",choice[0])
                print("Option B: ",choice[1])
                print("Option C: ",choice[2])
                print("Option D: ",choice[3])
                print()

                a2 = input("Enter your answer(A/B/C/D): ")
                cnt+=1

                print("\nQuestion 3")
                print(ques[cnt])
                
                choice = options[cnt]
                
                print("Option A: ",choice[0])
                print("Option B: ",choice[1])
                print("Option C: ",choice[2])
                print("Option D: ",choice[3])
                print()

                a3 = input("Enter your answer(A/B/C/D): ")
                cnt+=1

                print("\nQuestion 4")
                print(ques[cnt])
                
                choice = options[cnt]
                
                print("Option A: ",choice[0])
                print("Option B: ",choice[1])
                print("Option C: ",choice[2])
                print("Option D: ",choice[3])
                print()

                a4 = input("Enter your answer(A/B/C/D): ")
                cnt+=1

                print("\nQuestion 5")
                print(ques[cnt])
                
                choice = options[cnt]
                
                print("Option A: ",choice[0])
                print("Option B: ",choice[1])
                print("Option C: ",choice[2])
                print("Option D: ",choice[3])
                print()

                a5 = input("Enter your answer(A/B/C/D): ")
                cnt+=1

                print("\nQuestion 6")
                print(ques[cnt])
                
                choice = options[cnt]
                
                print("Option A: ",choice[0])
                print("Option B: ",choice[1])
                print("Option C: ",choice[2])
                print("Option D: ",choice[3])
                print()

                a6 = input("Enter your answer(A/B/C/D): ")
                cnt+=1

                print("\nQuestion 7")
                print(ques[cnt])
                
                choice = options[cnt]
                
                print("Option A: ",choice[0])
                print("Option B: ",choice[1])
                print("Option C: ",choice[2])
                print("Option D: ",choice[3])
                print()

                a7 = input("Enter your answer(A/B/C/D): ")
                cnt+=1

                print("\nQuestion 8")
                print(ques[cnt])
                
                choice = options[cnt]
                
                print("Option A: ",choice[0])
                print("Option B: ",choice[1])
                print("Option C: ",choice[2])
                print("Option D: ",choice[3])
                print()

                a8 = input("Enter your answer(A/B/C/D): ")
                cnt+=1

                print("\nQuestion 9")
                print(ques[cnt])
                
                choice = options[cnt]
                
                print("Option A: ",choice[0])
                print("Option B: ",choice[1])
                print("Option C: ",choice[2])
                print("Option D: ",choice[3])
                print()

                a9 = input("Enter your answer(A/B/C/D): ")
                cnt+=1

                print("\nQuestion 10")
                print(ques[cnt])
                
                choice = options[cnt]
                
                print("Option A: ",choice[0])
                print("Option B: ",choice[1])
                print("Option C: ",choice[2])
                print("Option D: ",choice[3])
                print()

                a10 = input("Enter your answer(A/B/C/D): ")
                cnt+=1
            
                
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
                try:
                    i = int(input("Enter your id: "))
                    ma = "select score from STUDENTS where SID=%s"%(i)
                    c.execute(ma)
                    
                    marks=0
                    name = ""
                    date_of_exam = ""
                    
                    for x in c:
                        marks = x
                        
                    na = "select name from STUDENTS where SID=%s"%(i)
                    c.execute(na)
                    for x in c:
                        name = x
                        
                    da = "select date_of_exam from STUDENTS where SID=%s"%(i)
                    c.execute(da)
                    for x in c:
                        date_of_exam = x

                    print()
                    print("Student ID: ", i)
                    print("Student Name: ", name[0])
                    print("Date of Examination: ", date_of_exam[0])
                    print("Marks obtained: ", marks[0])
                    print()
                    
                except:
                    print("_____Integer Value required_____")
            
            elif ch==3:
                break
        except:
            print("_____Integer Value required_____")
else:
    print("INVALID CHOICE")

        
        
        
        
            
                 
    
        

    
