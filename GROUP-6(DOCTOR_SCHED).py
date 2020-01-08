correctusername="admin"
correctpassword="admin@123"
loop='true'
while(loop=='true'):
    username=raw_input("userid")
    if(username==correctusername):
        password=raw_input("password")
        if(password==correctpassword):
            print("login succeesful"+username)
            loop='false'
        else:
            print("password incorrect")
    else:
        print("userid incorrect")
import MySQLdb
db=MySQLdb.connect('localhost','root','kavya@123')
cursor=db.cursor();
cursor.execute("CREATE DATABASE IF NOT EXISTS DOCTOR_SCHED")
cursor.execute("USE DOCTOR_SCHED")
while(1):                
    print("\n (1)ENTER DOCTOR DETAILS\n (2) ENTER PATIENT DETAILS\n (3) SET APPOINTMENT\n (4) PRODUCE BILL\n (5)CHART OF PATIENT SUFFERING FROM A PARTICULAR DISEASE ")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    choice=int(input("enter your choice"))
    if(choice==1):
        cursor.execute("CREATE TABLE IF NOT EXISTS DOCTOR(D_ID VARCHAR(20) PRIMARY KEY,D_NAME VARCHAR(20),D_AGE INT,D_DIS VARCHAR(20),D_NUMBER INT)")
        d_id=raw_input("enter doctor id")
        d_name=raw_input("enter doctor name")
        d_age=int(input("enter doctor age"))
        print("1)GENERAL PHYSICIAN-->(GP)\n 2)PULMONOLOGIST-->(PUL)\n 3)ENT SPECIALIST-->(ENT)\N 4)UROLOGIST-->(URO)5)NEUROLOGIST-->(NEURO)\n 6)OPTHALMOLOGIST-->(OPH)\n 7)PEDIATRICIAN-->(PAED)\n 8)GYNAECOLOGIST-->(GYN)\n 9)OBSTETRICIAN-->(OBS)\n 10)ORTHOPAEDIST-->(ORTHO)")
        d_dis=raw_input("enter doctor SPECIALISATION")
        d_num=int(input("enter doctor number"))
        cursor.execute("INSERT INTO DOCTOR(D_ID,D_NAME,D_AGE,D_DIS,D_NUMBER) VALUES('%s','%s','%d','%s','%d')"%(d_id,d_name,d_age,d_dis,d_num))
        cursor.execute("CREATE TABLE IF NOT EXISTS DOCTORA(D_ID VARCHAR(20),START VARCHAR(10),END VARCHAR(10),SNO INT NOT NULL AUTO_INCREMENT,TOKEN INT,FOREIGN KEY(D_ID) REFERENCES DOCTOR(D_ID),PRIMARY KEY(SNO))")
        d_id1=raw_input("enter id")
        if(d_id==d_id1):
            print("1)ADD SLOT")
            while(1):
                choice1=int(input("enter your choice"))
                if(choice1==1):
                    d_start=raw_input("enter slot from ")
                    d_end=raw_input("enter slot to ")
                    d_token=int(input("enter token number"))
                    cursor.execute("INSERT INTO DOCTORA(D_ID,START,END,TOKEN)VALUES('%s','%s','%s','%d')"%(d_id1,d_start,d_end,d_token))
                else:
                    break
    elif(choice==2):
        cursor.execute("CREATE TABLE IF NOT EXISTS PATIENT(P_ID VARCHAR(20) PRIMARY KEY,P_NAME VARCHAR(20),P_AGE INT,P_DIS VARCHAR(20),P_NUMBER INT,P_SEX VARCHAR(10),START VARCHAR(10))")
        p_id=raw_input("enter PATIENT id")
        p_name=raw_input("enter PATIENT name ")
        p_age=int(input("enter PATIENT age "))
        print("1)GENERAL PHYSICIAN(GP)-->COLD,FEVER,DIARRHEA,COUGH,FATIGUE\n 2)PULMONOLOGIST(PUL)-->BREATHLESSNESS,FATIGUE,COUGH\n 3)ENT SPECIALIST(ENT)-->EAR,NOSE,THROAT DISCOMFORTS 4)UROLOGIST(URO)-->DIFFICULTY IN MICTURITON\n 5)NEUROLOGIST(NEURO)-->ABNORMAL MOVEMENTS OF BODY OR UNCONCIOUSNESS\n 6)OPTHALMOLOGIST(OPH)-->DIMINISHED VISION,DOUBLE VISION\n 7)PEDIATRICIAN(PAED)\n 8)GYNAECOLOGIST(GYN)-->PELVIC PAIN,VAGINAL BLEEDING\n 9)OBSTETRICIAN(OBS)-->PREGNANCY\n 10)ORTHOPAEDIST-->FRACTURE,TRAUMA")
        p_dis=raw_input("WHICH DOCTOR HE/SHE WANTS TO MEET")
        p_num=int(input("enter PATIENT number "))
        p_sex=raw_input("enter PATIENT sex ")
        p_start=raw_input("enter PATIENT arrival time ")
        p_suffer=raw_input("suffering from")
        cursor.execute("INSERT INTO PATIENT(P_ID,P_NAME,P_AGE,P_DIS,P_NUMBER,P_SEX,START) VALUES('%s','%s','%d','%s','%d','%s','%s')"%(p_id,p_name,p_age,p_dis,p_num,p_sex,p_start))
        cursor.execute("CREATE TABLE IF NOT EXISTS PATIENTSUFFER(P_ID VARCHAR(20) PRIMARY KEY,P_DIS VARCHAR(20),FOREIGN KEY(P_ID) REFERENCES PATIENT(P_ID))")
        cursor.execute("INSERT INTO PATIENTSUFFER(P_ID,P_DIS) VALUES('%s','%s')"%(p_id,p_suffer)) 
    elif(choice==3):
        cursor.execute("DROP TABLE IF EXISTS HAMP")
        cursor.execute("CREATE TABLE IF NOT EXISTS HAMP AS (SELECT D.D_ID,P.P_ID,DA.SNO,D.D_DIS,P.P_DIS,DA.START,P.START AS P_A FROM DOCTOR D JOIN PATIENT P ON D.D_DIS=P.P_DIS JOIN DOCTORA DA ON DA.D_ID=D.D_ID AND DA.START=P.START) ")
        cursor.execute("SELECT P_ID,SNO FROM HAMP")
        for x in cursor:
            print(x)
    elif(choice==4):
        cursor.execute("CREATE TABLE IF NOT EXISTS BILL(SNO INT PRIMARY KEY AUTO_INCREMENT,P_ID VARCHAR(10),AMT FLOAT,AMT_PAID FLOAT,AMT_DUE FLOAT,AMT_CHANGE FLOAT,FOREIGN KEY(P_ID) REFERENCES PATIENT(P_ID))")
        p_id=raw_input("enter patient id")        
        total_amt=0
        consult=float(input("enter consultancy fee"))
        amt=float(input("enter treatment fee"))        
        total_amt=amt+consult
        print('TOTAL AMOUNT TO BE=',total_amt)
        amt_paid=float(input("enter amount paid="))
        amt_due=float(input("enter amount due="))
        amt_change=float(input("enter balance to be given by you="))
        cursor.execute("INSERT INTO BILL(P_ID,AMT,AMT_PAID,AMT_DUE,AMT_CHANGE)VALUES('%s','%f','%f','%f','%f')"%(p_id,total_amt,amt_paid,amt_due,amt_change))
    elif(choice==5):
        cursor.execute("SELECT P_DIS,COUNT(P_DIS) FROM PATIENT GROUP BY P_DIS")
        tup=cursor.fetchall()
        print(tup)
        d=dict(tup)
        print(d)
        list1=d.keys()
        list2=d.values()
        print(list1,list2)
        import matplotlib.pyplot as plt
        plt.pie(list2,labels=list1,startangle=90,shadow=True)
        plt.legend()
        plt.show()
    else:
        print("Enter valid choice")