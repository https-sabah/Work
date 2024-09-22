import  mysql.connector as  mysql
import  random
db=mysql.connect(host="localhost",user="root",password='sql123',charset="ascii")
cursor=db.cursor()
def check_acc(account_no):
    cursor.execute("select * from management where account={}".format(account_no))
    data=cursor.fetchall()
    if len(data)==0:
        return True
    else:
        return False
def generate_Account():
    l1=["4","1","8","5","6"]
    random.shuffle(l1)
    acc=''.join(l1)
    return acc


def open_acc():
    name=input("ENTER ACCOUNT HOLDERS NAME")
    print("ENTER DATE IN THIS FORMAT :-yyyy-mm-dd")
    dob=input("ENTER YOUR DATE OF BIRTH")
    add=input("ENTER YOUR ADDRESS")
    phone=input("ENTER YOUR PHONE NUMBER")
    email=input("ENTER YOUR EMAIL ID")
    balance=0
    acc=generate_Account()
    check=check_acc(acc)
    while not(check):
        if check:
            break
        else:
            acc=generate_Account()
    cursor.execute("insert into management values('{}','{}','{}','{}','{}','{}','{}')".format(name,dob,add,phone,email,str(acc),balance))
    db.commit()
    print("ACCOUNT CREATED!!!")
    print("THE NAME OF ACCOUNT HOLDER IS >",name)
    print(" ACCOUNT NUMBER ALLOTTED IS >",acc)
def update():
    print("1   UPDATE FROM ACCOUNT NUMBER.")
    print("              OR                ")
    print("2   UPDATE BY ACCOUNT HOLDER's NAME")
    ch=int(input("Enter the choice."))
    global column
    cursor.execute("desc management")
    c=cursor.fetchall()
    column=[i[0] for i in c]
    print("THE FIELDS ARE >",column)
    if ch==1:
        acc=input("Enter the account no of the holder   >")
        col=input("enter the column name    >")
        val=input("Enter the value to be updated    >")
        cursor.execute("update management set {}={} where account={}".format(col,val,acc))
        db.commit()
    else:
        acc=input("Enter the name of the holder")
        col=input("ente the column name    >")
        val=input("Enter the value to be updated    >")
        cursor.execute("update management set {}={} where name={}".format(col,val,acc))
        db.commit()
def  delete():
    ch=input("Enter the Account number to be deleted    >")
    cursor.execute("delete  from management where account={}".format(ch))
    print("ACCOUNT SUCCESFULLY DELETED")
def  search():
    cursor.execute("desc management")
    c=cursor.fetchall()
    column=[i[0] for i in c]
    print(column)
    ch=input("Enter the field from you want to search")
    val=input("Enter the value of that field")
    cursor.execute("select * from management where {}='{}'".format(ch,val))
    data=cursor.fetchall()
    print(column)
    print(data[0])

def deposit():
    print("1   DEPOSITE")
    print("2   WITHDRAW")
    ch=int(input("ENTER YOUR CHOICE. >"))
    acc=input("ENTER YOUR ACCOUNT NUMBER   >")
    if ch==1:
        print("ENTER THE AMOUNT IN INTEGER   !")
        money=int(input("ENTER THE AMOUNT TO BE DEPOSITED   >"))
        cursor.execute("select balance from management where account={}".format(acc))
        data=int(cursor.fetchall()[0][0])
        new_val=data+money
        print(new_val)
        cursor.execute("update management set balance='{}' where account='{}'".format(str(new_val),acc))
        db.commit()
        print("Amount Successfully Deposited  ",new_val,"to account number  >",acc)
    else:
        print("ENTER THE AMOUNT IN INTEGER ")
        money=int(input("ENTER THE AMOUNT TO BE WITHDRAWN   >"))
        cursor.execute("select balance from management where account={}".format(acc))
        data=int(cursor.fetchall()[0][0])
        new_val=data-money
        cursor.execute("update management set balance='{}' where account='{}'".format(str(new_val),acc))
        db.commit()
        print("Amount Successfully Withdrawed")
    
def check_bal():
    acc=input("Enter the account number     > ")
    cursor.execute("select account,balance from management where account='{}'".format(acc))
    print(cursor.fetchall())
    
def account_list():
    cursor.execute("Select name,account,balance from management")
    l1=cursor.fetchall()
    print(("Account holder name","Account number","Balance")   )
    for i in l1:
        print(i)
        
def choice():
    print("1)CREATE YOUR ACCOUNT")
    print("2)DELETE ACCOUNT")
    print("3)UPDATE YOUR ACCOUNT")
    print("4)SEARCH FOR YOUR ACCOUNT")
    print("5)WITHDRAW OR DEPOSITE FROMYOUR ACCOUNT")
    print("6)CHECK BALANCE IN YOUR ACCOUNT")
    print("7)LIST OF ALL ACCOUNT")
    print("8)EXIT  FROM BANK MANAGER")
    
if db.is_connected():
    print("\t\t\t\t\tCONNECTION GRANTED!!!")
    print("\t\t\t\t This project is  made by SABAH")
    cursor.execute("create database if not exists bank_manager")
    cursor.execute("use bank_manager")
    cursor.execute("create table if not exists management(name varchar(30),Date_of_birth date,address varchar(100),phone_no varchar(15),email_id varchar(30),account varchar(5) not null,Balance varchar(10) default '0')")
    db.commit()
    print("\t\t^^^^^^^_____________W E L C O M E ______________^^^^^^^^^^^")
    while True:
        choice()
        ch=int(input("Enter The Choice   >(1,2,3,4,5,6,7,8)"))
        if  ch==1:
            open_acc()
        elif ch==2:
            delete()
        elif  ch==3:
            update()
        elif  ch==4:
            search()
        elif  ch==5:
            deposit()
        elif  ch==6:
            check_bal()
        elif  ch==7:
            account_list()
        elif  ch==8:
            break
        else:
            print("CONNECTION FAILED")
    
print("PROGRAM END ")  
