import mysql.connector as x
import os
from datetime import date, datetime, timedelta
import random
import time
from tabulate import tabulate
from mysql.connector import Error, ProgrammingError
from prettytable import PrettyTable
import keyboard
from pyfiglet import figlet_format
import sys

abc = x.connect(host='localhost',user='riya',passwd='Lkjhgf@12345')

if abc.is_connected():
    c = abc.cursor()

    c.execute("create database if not exists timetable")
    c.execute("use timetable")
    
    def print_centered(text):
        width = 135
        print(text.center(width))


    text = ("WELCOME TO TIMEWISE")
    font = figlet_format(text,font = 'big', width=150)
    print_centered(font)

    welc = ("---------------------------     ---------------------------")
    print_centered(welc)

    today = date.today()
    day = today.strftime("%a")
    date_today = datetime.now().strftime("%Y_%m_%d")


    if day in ["Mon", "Tue", "Wed", "Thu", "Fri"]:
        c.execute(f"CREATE TABLE IF NOT EXISTS `12b_today` AS SELECT PeriodDay, {day} FROM `12b`")
    else:
        print("Today is weekend. Skipping timetable creation.")
        print("Have a nice day!")
        sys.exit()
        

    #RUN CHECK
    file_path = 'run_once_flag.txt'
    try:
        with open(file_path, 'r') as f:
            has_run_before = True
    except FileNotFoundError:
        has_run_before = False

    if not has_run_before:


        def safe_create_today_table(table_name):
            if day in ["Mon", "Tue", "Wed", "Thu", "Fri"]:
                c.execute(f"CREATE TABLE IF NOT EXISTS `{table_name}_today` AS SELECT PeriodDay, {day} FROM `{table_name}`")
            else:
                print(f"Skipping {table_name}_today because today is {day}")

        #12B timetable
        c.execute("create TABLE IF NOT EXISTS `12b` (PeriodDay varchar(20), Mon varchar(10), \
                    Tue varchar(10), Wed varchar(10), Thu varchar(10), Fri varchar(10))")
        
        c.execute("INSERT INTO `12b` VALUES ('1', 'phy', 'cs', 'chem', 'cs', 'eng')")
        c.execute("INSERT INTO `12b` VALUES ('2', 'chem', 'chem', 'math', 'chem', 'math')")
        c.execute("INSERT INTO `12b` VALUES ('3', 'math', 'phy', 'games', 'phy', 'cs')")
        c.execute("INSERT INTO `12b` VALUES ('4', 'chem', 'cs', 'phy', 'phy', 'cs')")
        c.execute("INSERT INTO `12b` VALUES ('5', 'eng', 'phy', 'cs', 'math', 'chem')")
        c.execute("INSERT INTO `12b` VALUES ('6', 'cs', 'eng', 'math', 'pe', 'phy')")
        c.execute("INSERT INTO `12b` VALUES ('7', 'math', 'math', 'eng', 'eng', 'chem')")

        c.execute(f"CREATE TABLE IF NOT EXISTS `12b_today` AS SELECT PeriodDay,{day} FROM `12b`")
                

        #Akash_kumar
        c.execute("create TABLE IF NOT EXISTS Akash (PeriodDay varchar(20), Mon varchar(10), \
                    Tue varchar(10), Wed varchar(10), Thu varchar(10), Fri varchar(10))")
        
        c.execute("INSERT INTO Akash VALUES ('1', `12b`, '11a', '11b', '$', '12a')")
        c.execute("INSERT INTO Akash VALUES ('2', '11a', '11a', '12a', '$', '11b')")
        c.execute("INSERT INTO Akash VALUES ('3', '$', `12b`, '11b', `12b`, '12a')")
        c.execute("INSERT INTO Akash VALUES ('4', '11b', '12a', `12b`, `12b`, '11a')")
        c.execute("INSERT INTO Akash VALUES ('5', '11a', `12b`, '$', '11b', '12a')")
        c.execute("INSERT INTO Akash VALUES ('6', '11b', '11a', '12a', '$', `12b`)")
        c.execute("INSERT INTO Akash VALUES ('7', '11a', '11a', '11b', '$', '12a')")

        c.execute(f"CREATE TABLE IF NOT EXISTS Akash_today AS SELECT PeriodDay,{day} FROM Akash")
            

        #Anu_Mehta
        c.execute("create TABLE IF NOT EXISTS Anu (PeriodDay varchar(20), Mon varchar(10), \
                    Tue varchar(10), Wed varchar(10), Thu varchar(10), Fri varchar(10))")
        
        c.execute("INSERT INTO Anu VALUES ('1', '12a', '11b', `12b`, '$', '11a')")
        c.execute("INSERT INTO Anu VALUES ('2', `12b`, `12b`, '$', `12b`, '12a')")
        c.execute("INSERT INTO Anu VALUES ('3', '11b', '12a', '11b', '12a', '$')")
        c.execute("INSERT INTO Anu VALUES ('4', `12b`, '12a', '$', '11a', '11b')")
        c.execute("INSERT INTO Anu VALUES ('5', '11a', '$', '12a', '11b', `12b`)")
        c.execute("INSERT INTO Anu VALUES ('6', '11a', '11b', '12a', '11b', '12a')")
        c.execute("INSERT INTO Anu VALUES ('7', '$', '11a', '11b', '12a', `12b`)")

        c.execute(f"CREATE TABLE IF NOT EXISTS Anu_today AS SELECT PeriodDay,{day} FROM Anu")
        

        #Ritu_Sood
        c.execute("create TABLE IF NOT EXISTS Ritu (PeriodDay varchar(20), Mon varchar(10), \
                    Tue varchar(10), Wed varchar(10), Thu varchar(10), Fri varchar(10))")
        
        c.execute("INSERT INTO Ritu VALUES ('1', '12f', `12b`, '11b', `12b`, '$')")
        c.execute("INSERT INTO Ritu VALUES ('2', '$', '11b', '$', '11b', '12f')")
        c.execute("INSERT INTO Ritu VALUES ('3', '11b', '12f', '$', '12f', `12b`)")
        c.execute("INSERT INTO Ritu VALUES ('4', '$', `12b`, '$', '$', `12b`)")
        c.execute("INSERT INTO Ritu VALUES ('5', '$', '$', `12b`, '$', '11b')")
        c.execute("INSERT INTO Ritu VALUES ('6', `12b`, '11b', '12f', '11b', '12f')")
        c.execute("INSERT INTO Ritu VALUES ('7', '$', '$', '11b', '12f', '11b')")

        c.execute(f"CREATE TABLE IF NOT EXISTS Ritu_today AS SELECT PeriodDay,{day} FROM Ritu")
            

        #DKP
        c.execute("create TABLE IF NOT EXISTS DKP (PeriodDay varchar(20), Mon varchar(10), \
                    Tue varchar(10), Wed varchar(10), Thu varchar(10), Fri varchar(10))")
        
        c.execute("INSERT INTO DKP VALUES ('1', '9a', '$', '11b', '$', '$')")
        c.execute("INSERT INTO DKP VALUES ('2', '$', '11b', `12b`, '11b', `12b`)")
        c.execute("INSERT INTO DKP VALUES ('3', `12b`, '9a', '$', '9a', '$')")
        c.execute("INSERT INTO DKP VALUES ('4', '$', '9c', '$', '9c', '$')")
        c.execute("INSERT INTO DKP VALUES ('5', '$', '9b', '$', `12b`, '11b')")
        c.execute("INSERT INTO DKP VALUES ('6', '$', '11b', `12b`, '11b', '9a')")
        c.execute("INSERT INTO DKP VALUES ('7', `12b`, `12b`, '11b', '9a', '11b')")

        c.execute(f"CREATE TABLE IF NOT EXISTS DKP_today AS SELECT PeriodDay,{day} FROM DKP")
        

        #Priya_Vadini
        c.execute(f"create TABLE IF NOT EXISTS Priya (PeriodDay varchar(20), Mon varchar(10), \
                    Tue varchar(10), Wed varchar(10), Thu varchar(10), Fri varchar(10))")
        
        c.execute("INSERT INTO Priya VALUES ('1', '12f', '$', '11f', '$', `12b`)")
        c.execute("INSERT INTO Priya VALUES ('2', '$', '11f', '$', '11c', '12f')")
        c.execute("INSERT INTO Priya VALUES ('3', '11f', '12f', '$', '12f', '$')")
        c.execute("INSERT INTO Priya VALUES ('4', '12f', '$', '11f', '$', '11e')")
        c.execute("INSERT INTO Priya VALUES ('5', `12b`, '$', '11c', '$', '11f')")
        c.execute("INSERT INTO Priya VALUES ('6', '$', `12b`, '12f', '11f', '12f')")
        c.execute("INSERT INTO Priya VALUES ('7', '$', '$', `12b`, `12b`, '11f')")

        c.execute(f"CREATE TABLE IF NOT EXISTS Priya_today AS SELECT PeriodDay,{day} FROM Priya")
        

        #Anushka
        c.execute(f"create TABLE IF NOT EXISTS Anushka (PeriodDay varchar(20), Mon varchar(10), \
                    Tue varchar(10), Wed varchar(10), Thu varchar(10), Fri varchar(10))")
        
        c.execute("INSERT INTO Anushka VALUES ('1', '12f', '11c', '12d', '11c', '$')")
        c.execute("INSERT INTO Anushka VALUES ('2', '$', '12d', '$', '12d', '12f')")
        c.execute("INSERT INTO Anushka VALUES ('3', '12d', '12f', '$', '12f', '11c')")
        c.execute("INSERT INTO Anushka VALUES ('4', '$', '11c', '$', '$', '11c')")
        c.execute("INSERT INTO Anushka VALUES ('5', '$', '$', '11c', '$', '12d')")
        c.execute("INSERT INTO Anushka VALUES ('6', '11c', '12d', '12f', '12d', '12f')")
        c.execute("INSERT INTO Anushka VALUES ('7', '$', '$', '12d', '12f', '11b')")

        c.execute(f"CREATE TABLE IF NOT EXISTS Anushka_today AS SELECT PeriodDay,{day} FROM Anushka")
        

        #Tushar
        c.execute(f"create TABLE IF NOT EXISTS Tushar (PeriodDay varchar(20), Mon varchar(10), \
                    Tue varchar(10), Wed varchar(10), Thu varchar(10), Fri varchar(10))")
        
        c.execute("INSERT INTO Tushar VALUES ('1', '12a', '$', '11a', '$', '$')")
        c.execute("INSERT INTO Tushar VALUES ('2', '$', '11b', '$', '11a', '$')")
        c.execute("INSERT INTO Tushar VALUES ('3', '10f', '$', `12b`, '12a', '11b')")
        c.execute("INSERT INTO Tushar VALUES ('4', '$', '12a', '$', '11a', '$')")
        c.execute("INSERT INTO Tushar VALUES ('5', '11a', '$', '$', '$', '$')")
        c.execute("INSERT INTO Tushar VALUES ('6', '$', '11a', '$', `12b`, '12a')")
        c.execute("INSERT INTO Tushar VALUES ('7', '$', '$', '11a', '10e', '11a')")

        c.execute(f"CREATE TABLE IF NOT EXISTS Tushar_today AS SELECT PeriodDay,{day} FROM Tushar")
        

        #Vijay
        c.execute("create TABLE IF NOT EXISTS Vijay (PeriodDay varchar(20), Mon varchar(10), \
                    Tue varchar(10), Wed varchar(10), Thu varchar(10), Fri varchar(10))")
        
        c.execute("INSERT INTO Vijay VALUES ('1', '12c', '$', '11d', '$', '10d')")
        c.execute("INSERT INTO Vijay VALUES ('2', '$', '11c', '$', '11d', '$')")
        c.execute("INSERT INTO Vijay VALUES ('3', '10a', '$', '12d', '12c', '11c')")
        c.execute("INSERT INTO Vijay VALUES ('4', '$', '12c', '$', '11d', '$')")
        c.execute("INSERT INTO Vijay VALUES ('5', '11d', '$', '$', '10c', '$')")
        c.execute("INSERT INTO Vijay VALUES ('6', '$', '11d', '$', '12d', '12c')")
        c.execute("INSERT INTO Vijay VALUES ('7', '$', '$', '11d', '10b', '11a')")

        c.execute(f"CREATE TABLE IF NOT EXISTS Vijay_today AS SELECT PeriodDay,{day} FROM Vijay")
        

        #Attendance
        c.execute(f"create TABLE IF NOT EXISTS Attendance (t_name CHAR(20))")
        
        c.execute("insert into Attendance(t_name) values('Akash')")
        c.execute("insert into Attendance(t_name) values('Anu')")
        c.execute("insert into Attendance(t_name) values('Ritu')")
        c.execute("insert into Attendance(t_name) values('DKP')")
        c.execute("insert into Attendance(t_name) values('Priya')")
        c.execute("insert into Attendance(t_name) values('Anushka')")
        c.execute("insert into Attendance(t_name) values('Tushar')")
        c.execute("insert into Attendance(t_name) values('Vijay')")
        

        try:
            c.execute(f'alter table Attendance add {date_today} CHAR(20)')
        except ProgrammingError:
            pass

        with open(file_path, 'w') as f:
            f.write("This code has already been executed.")

    def modify_timetable(o,i,u,y):
        table_name = o
        period_day = i
        period = u
        correct = y
        c.execute(f"UPDATE {table_name} SET  {period_day} = %s WHERE PeriodDay = %s", (correct,period))

    def modify_t_timetable(a,b,d):
        table_name = a
        period = b
        correct = d
        c.execute(f"UPDATE {table_name} SET  {day} = %s WHERE PeriodDay = %s",(correct,period))

        
    def add_teach(m,n):
        tea_name = m
        tea_sub = n
        c.execute(f"CREATE TABLE IF NOT EXISTS {tea_name} (PeriodDay varchar(20), Mon varchar(10), \
                    Tue varchar(10), Wed varchar(10), Thu varchar(10), Fri varchar(10))")
        c.execute(f"CREATE TABLE IF NOT EXISTS {tea_name}_today AS SELECT PeriodDay,{day} FROM {tea_name}")
        c.execute("insert into Attendance(t_name) values(%s)", (tea_name,))
        abc.commit()
        print()
        print()
        print_centered("PERIOD ENTRY")
        
        print("NOTE: For free period, type -> '$'")
        print()
        MON = []
        for i in range(1,8):
            i = str(i)
            mon = input("Enter "+i+" period for Monday : ")
            MON.append(mon)
            
        print()
        TUE = []
        for i in range(1,8):
            i = str(i)
            mon = input("Enter "+i+" period for Tuesday : ")
            TUE.append(mon)

        print()
        WED = []
        for i in range(1,8):
            i = str(i)
            mon = input("Enter "+i+" period for Wednesday : ")
            WED.append(mon)

        print()
        THU = []
        for i in range(1,8):
            i = str(i)
            mon = input("Enter "+i+" period for Thursday : ")
            THU.append(mon)

        print()
        FRI = []
        for i in range(1,8):
            i = str(i)
            mon = input("Enter "+i+" period for Friday : ")
            FRI.append(mon)
        
        for i in range(0,7):
            c.execute(f"INSERT INTO {tea_name} VALUES(%s,%s,%s,%s,%s,%s)", (i+1,MON[i],TUE[i],WED[i],THU[i],FRI[i]))

        sqlt(tea_name)


    
    def add_class(m):
        class_name = m
        c.execute(f"CREATE TABLE IF NOT EXISTS {class_name} (PeriodDay varchar(20), Mon varchar(10), \
                    Tue varchar(10), Wed varchar(10), Thu varchar(10), Fri varchar(10))")
        c.execute(f"CREATE TABLE IF NOT EXISTS {class_name}_today AS SELECT PeriodDay,{day} FROM {class_name}")
        print()
        print()
        print_centered("PERIOD ENTRY")
        
        print()
        MON = []
        for i in range(1,8):
            i = str(i)
            mon = input("Enter "+i+" period for Monday : ")
            MON.append(mon)
            
        print()
        TUE = []
        for i in range(1,8):
            i = str(i)
            mon = input("Enter "+i+" period for Tuesday : ")
            TUE.append(mon)

        print()
        WED = []
        for i in range(1,8):
            i = str(i)
            mon = input("Enter "+i+" period for Wednesday : ")
            WED.append(mon)

        print()
        THU = []
        for i in range(1,8):
            i = str(i)
            mon = input("Enter "+i+" period for Thursday : ")
            THU.append(mon)

        print()
        FRI = []
        for i in range(1,8):
            i = str(i)
            mon = input("Enter "+i+" period for Friday : ")
            FRI.append(mon)
        
        for i in range(0,7):
            c.execute(f"INSERT INTO {class_name} VALUES(%s,%s,%s,%s,%s,%s)", (i+1,MON[i],TUE[i],WED[i],THU[i],FRI[i]))

        sqlt(class_name)
    
    def present():
        global t
        t = []
        c.execute(f"select t_name,{date_today} from Attendance")
        e = c.fetchall()
        for i in e:
            name = i[0]
            atn = i[1]
            if atn != '$':
                t.append(name)
        return t


    #Attendance
    def mark_Attendance():
        global t
        t = []
        end_time = datetime.now().replace(hour=8, minute=30, second=0, microsecond=0)
        while datetime.now() < end_time:
            teach_name = input("Enter teacher's name to mark Attendance : ")
            teach_name = teach_name.title()
            if teach_name == 'No':
                break
            current_time = datetime.now().time()
            current_time_str = current_time.strftime("%H:%M:%S")
            attend = input("Is the teacher present%s (P/A): ")
            if attend.upper() == 'P':
                c.execute(f"UPDATE Attendance SET {date_today} = %s WHERE t_name = %s", (current_time_str,teach_name))
                abc.commit()
                t.append(teach_name)
                print(t)
                print("Attendance marked")
            elif attend.upper() == 'A':
                c.execute(f"UPDATE Attendance SET {date_today} = '$' WHERE t_name = %s", (teach_name,))
                print("Attendance marked")
            else:
                print("Enter P/A")

            #time.sleep(1)
        print()
        print_centered("Time: 8:30am, Attendance marking stopped")

        c.execute("SELECT * FROM Attendance")
        p = c.fetchall()
        for u in p:
            te_name = u[0]
            atten = u[1]
            if atten == None:
                c.execute(f"UPDATE Attendance SET {date_today} = '$' WHERE t_name = %s", (te_name,))

    print_centered("MARKING ATTENDANCE")
    print()
    mark_Attendance()

    def mark_attend_exp():
        global t
        t = []
        teach_name = input("Enter teacher's name to mark Attendance : ")
        teach_name = teach_name.title()
        
        current_time = datetime.now().time()
        current_time_str = current_time.strftime("%H:%M:%S")
        attend = input("Is the teacher present%s (P/A): ")
        if attend.upper() == 'P':
            c.execute(f"UPDATE Attendance SET {date_today} = %s WHERE t_name = %s", (current_time_str,teach_name))
            abc.commit()
            t.append(teach_name)
            print(t)
            print("Attendance marked")
        elif attend.upper() == 'A':
            c.execute(f"UPDATE Attendance SET {date_today} = '$' WHERE t_name = %s", (teach_name,))
            print("Attendance marked")
        else:
            print("Enter P/A")

    def sqlt(tab):
        c.execute(f"SELECT * FROM {tab}")
        columns = [description[0] for description in c.description]
        table = PrettyTable(columns)
        rows = c.fetchall()
        
        for row in rows:
            table.add_row(row)

        print(table)

    present()

    
    
    l = {'Akash':'phy', 'Anu':'chem', 'Ritu':'cs', 'DKP':'math', 'Priya':'eng', 'Tushar':'pe', 'Vijay':'pe'}
    
    #period alloting
    def period_al(idk):
        idk = t
        sqlt('Attendance')
        c.execute("SELECT * FROM '12b-today'")
        rows = c.fetchall()

        for i in rows:
            period = i[1]
            subject = i[0]
            teach_name = l.get(subject)

            if teach_name:
                c.execute(f"SELECT {date_today} FROM Attendance WHERE t_name = %s", (teach_name,))
                attend = c.fetchone()[0]

                if attend == '$':
                     if t:
                        assign = random.choice(t)
                        t.remove(assign)
                        c.execute("UPDATE '12b-today' SET {day} = %s WHERE PeriodDay = %s", (assign, period))                
                        c.execute(f"UPDATE {assign}_today SET {day} = %s WHERE PeriodDay = %s", ('12b', period))
                else:  
                    c.execute("UPDATE '12b-today' SET {day} = %s WHERE PeriodDay = %s", (teach_name, period))
                    c.execute(f"UPDATE {teach_name}_today SET {day} = %s WHERE PeriodDay = %s", ('12b', period))
                    
        abc.commit()


   
 

    def day_end():
        full_day = datetime.now().replace(hour=23, minute=59, second=59, microsecond=59)
        current_time = datetime.now()
        print("Program on standby, Press ENTER to resume...")
        while current_time < full_day:
        
            c.execute(f"CREATE TABLE IF NOT EXISTS '12b-today' AS SELECT {day} FROM 12b")
            try:
                c.execute(f'alter table Attendance add {date_today} time')
            except ProgrammingError:
                pass
            if keyboard.is_pressed('enter'):
                print()
                print("Key pressed, resuming...")
                break
            current_time = current_time\
                           
    k = "y"
    while k == "y":
        print()
        print_centered("======================")
        print_centered("WHAT DO YOU WISH TO DO")
        print_centered("======================")
        print()
        print("CLASS TIMETABLE FUNCTIONS:")
        print("Enter  1 :  CLASS'S TIMETABLE")
        print("Enter  2 :  ADD CLASS'S TIMETABLE")
        print("Enter  3 :  MODIFY CLASS'S TIMETABLE")
        print()
        print("TEACHER TIMETABLE FUNCTIONS:")
        print("Enter  4 :  TEACHER'S TIMETABLE")
        print("Enter  5 :  ADD TEACHER'S TIMETABLE")
        print("Enter  6 :  MODIFY TEACHERS'S TIMETABLE")
        print()
        print("Enter  7 :  MARK ATTENDANCE")
        print("Enter  8 :  SHOW ATTENDANCE")
        print("Enter  9 :  SHOW TODAY'S TIMETABLE")
        print("Enter 10 :  STANDBY THE PROGRAM")
        print("Enter 11 :  DELETE A TABLE")
        print("Enter  0 :  EXIT THE PROGRAM")
        print()
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            #Search class table
            class_tt = input("Enter which class's timetable :")
            sqlt(class_tt)

        elif choice == 2:
            #Add class table
            cl_name = input("Enter class's name :")
            add_class(cl_name)

        elif choice == 3:
            st_name = input("Enter Class's table name: ").title()
            stt_name = input("Which table do you want (today/general): ")
            
            period_day = input("Enter in which DAY you want to modify :")
            period = input("Enter in which PERIOD you want to modify :")
            correct = input("Enter what you want to correct :")
            
            if stt_name == 'today':
                st_name_today = st_name + '_today'
                modify_t_timetable(st_name_today,period,correct)
                
                if correct == '$':
                    pass
                else:
                    teac_name = l.get(correct)
                    modify_t_timetable(teac_name,period,st_name)
                sqlt(st_name + '_today')
            else:
                modify_timetable(st_name,period_day,period,correct)
                sqlt(st_name)

        elif choice == 4:
            #search teacher table
            te_name = input("Enter teacher's name: ").title()
            tee_name = input("Which table do you want (today/general): ")
            if tee_name == 'today':
                sqlt(te_name + '_today')
            else:
                sqlt(te_name)

        elif choice == 5:
            #Add teacher table
            teac_name = input("Enter teacher's name :")
            teac_sub = input("Which subject does "+teac_name+" teach? : ")
            if teac_name not in l:
                l[teac_sub] = teac_name
            add_teach(teac_name,teac_sub)
            
        elif choice == 6:
            tte_name = input("Enter Teacher's table name: ").title()
            ttee_name = input("Which table do you want (today/general): ")
            
            period_day = input("Enter in which DAY you want to modify : ").title()
            period = input("Enter in which PERIOD you want to modify : ")
            correct = input("Enter what you want to correct :")
            
            if ttee_name == 'today':
                modify_t_timetable(tte_name,period,correct)
                if correct == '$':
                    pass
                else:
                    subject = l.get(tte_name)
                    modify_t_timetable(correct,period,tte_name)
                sqlt(tte_name + '_today')
            else:
                modify_timetable(tte_name,period_day,period,correct)
                sqlt(tte_name)
                
        elif choice == 7:
            mark_attend_exp()

        elif choice == 8:
            sqlt('Attendance')

        elif choice == 9:
            which = input("Enter table name : ")
            which_t = which + '_today'
            sqlt(which_t)

        elif choice == 10:
            day_end()

        elif choice == 11:
            dell = input("Enter table name which you want to delete : ").title
            c.execute(f"DROP TABLE IF EXISTS `{dell}`")
            print("Table deleted!") 

        elif choice == 0:
            break
        
        k = input("Do you want to continue? (Y/A) : ")
        
