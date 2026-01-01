import random as rd
import tabulate as tb
import datetime as dt
import mysql.connector as my
#Initial Welcome Message
print("                        ","-"*77)
print('\t                                                     ELECTRICITY BILL MANAGEMENT')
print("                        ","-"*77)

#Connecting python with mysql interface
try:
    con=my.connect(host='localhost',user='root',password='7002',database='electricity')
except my.Error as err:
    print(f"Error: Could not connect to Database {err}")
    exit() # Exit the Program if connection fails

def getcur():
    return con.cursor()
def getcom():
    return con.commit()

#Function for logging in
def login():
    while True:
        a=input('Are you an Employee or a Customer -  ').strip().lower()
        # Employee Login
        if a=='employee':
            un, pw=loginusernameandpass()  #Get Login Credentials
            p='select role from logins where username=%s and passw=%s and role in ("admin","user")'
            c=getcur()
            c.execute(p,(un,pw))
            rs=c.fetchone()
            if rs:
                role=rs[0]
                if role=='admin':
                    admin_menu()
                elif role=='user':
                    user_menu()
            else:
                print('Invalid Employee Credentials')
                continue
        # Customer Login
        elif a=='customer':
            while True:
                r=input('Do you have an account - ').strip().lower()
                if r in ('yes','y'):    
                    un, pw=loginusernameandpass() # Get Login Credentials for customer
                    p='select role from logins where username=%s and passw=%s and role="user"'
                    c=getcur()
                    c.execute(p,(un,pw))
                    rs=c.fetchone()
                    if rs:
                        user_menu() # Customer Login Successful
                    else:
                        print('Invalid Customer Credentials')
                        continue
                elif r in ('no','n'):
                    register_customer() # Register a New Customer
                else:
                    print(" Invalid Input ")
                    continue
        else: 
            print(" Invalid Input ") 
            continue
        break
    
# Function to get username and password from the user and validate them
def loginusernameandpass():
    while True:
        print('\t LOGIN')
        un = input('Enter UserName : ').strip()
        p='select username from logins'
        c=getcur()
        c.execute(p)
        rs=c.fetchall()
        s=[]
        t=[]
        for i in rs:
            a=list(i)
            s.append(a)
        for x in s:
            for y in x:
                t.append(y)
        if un not in t:
            print("Username Does Not Match. Please Try Again....")
            continue # Retry if username does not match
        break
    while True:
        pw = input('Enter Password : ').strip()
        a='select passw from logins'
        c=getcur()
        c.execute(a)
        rs=c.fetchall()
        k=[]
        f=[]
        for i in rs:
            b=list(i)
            k.append(b)
        for x in k:
            for y in x:
                f.append(y)
        if pw not in f:
            print("Wrong Password. Please Try Again....")
            continue # Retry If Password does not match
        break
    print("Login successful!")
    return un, pw

#Function to register a New Customer
def register_customer():
    print("\t REGISTER NEW CUSTOMER ")
    try:
        while True:
            un = input('Enter your Username: ').strip()
            if not validate_username(un):
                continue            
            c = getcur()
            p='select username from logins'
            c.execute(p)
            rs=c.fetchall()
            s=[]
            t=[]
            for i in rs:
                a=list(i)
                s.append(a)
            for x in s:
                for y in x:
                    t.append(y)
            if un in t:
                print("Username Already Exists. Please Try Again....")
                continue     
            break
        while True:
            pw = input('Enter your Password: ').strip()
            if not validate_password(pw):
                continue
            a='select passw from logins'
            c=getcur()
            c.execute(p)
            rs=c.fetchall()
            k=[]
            f=[]
            for i in rs:
                b=list(i)
                k.append(b)
            for x in k:
                for y in x:
                    f.append(y)
            if pw in f:
                print("Password Already exists. Please Try Again....")
                continue
            break
        # Insert new customer into the logins table
        p = "INSERT INTO logins (username, passw) VALUES (%s, %s)"
        val = (un, pw)
        c.execute(p, val)
        getcom()
        print('\t CUSTOMER ACCOUNT SUCCESSFULLY CREATED ')
        addcustomer() 
    except my.Error as err:
        print(f"Error: Could Not create customer account - {err}")

# Log Function for Customer Activity
def logcus(message):
    try:
        with open('log_customer.txt','a') as lgf:
            t=dt.datetime.now().strftime("%d-%m-%y %H:%M:%S")
            lgf.write(f"[{t}] {message}\n")
    except IOError as e:
         print(f"Error writing to log file: {e}")

# Log Function for Bill Generation
def logbill(message):
    try:
        with open('log_bills.txt','a') as lf:
            t=dt.datetime.now().strftime("%d-%m-%y %H:%M:%S")
            lf.write(f"[{t}] {message}\n")
    except IOError as e:
        print(f"Error writing to log file: {e}")

# Log function for complaints
def logcomp(message):
    try:
        with open('log_complaints.txt','a') as fi:
            t=dt.datetime.now().strftime("%d-%m-%y %H:%M:%S")
            fi.write(f"[{t}] {message}\n")
    except IOError as e:
        print(f"Error writing to log file: {e}")

# Function to display data in a tabular format
def show_tables(head,data):
    table=tb.tabulate(data, headers=head, tablefmt='github',colalign=('left',),stralign=('left',))
    print(table)

# Password Validation Function
def validate_password(password):
    if len(password)<8:
        print('Password must atleast be 8-characters long')
        return False
    return True

# Username Validation Function
def validate_username(username):
    if len(username)<3:
        print('Username must be at least 3-characters long')
        return False
    if not username.isalnum():
        print("Username can only contain letters and numbers")
        return False
    return True

# Phone Number Validation Function
def validate_phone(phone_number):
    if phone_number.isdigit() and len(phone_number)==10:
        return True
    # Inform the customer for 10 digist for phone number
    print("Invalid Phone Number -> It should be 10 Digits")
    return False

# Function to display list of admins
def showadmins():
    c=getcur()
    c.execute('Select username,passw from logins where role="admin"')
    res=c.fetchall()
    print('                      ','-'*48)
    print('                                             List of Admins')
    print('                      ','-'*48)
    # Define the headers for the displayed table
    head=['Usernames','Passwords']
    # Call the show_tables function to display the list of admins
    show_tables(head,res)

# Function to display list of Customers
def showusers():
    c=getcur()
    c.execute('Select username,passw from logins where role="user"')
    res=c.fetchall()
    print('                      ','-'*48)
    print('                                             List of Customers')
    print('                      ','-'*48)
    # Define the headers for the displayed table
    head=['Usernames','Passwords']
    # Call the show_tables function to display the Customers username and password
    show_tables(head,res)

# Admin Menu options
def admin_menu():
    while True:
        print("-"*50)
        print("\t CHOOSE AN OPERATION")
        print("-"*50)
        print("Press 1 - Add a New Customer")
        print("Press 2 - Deleting an Existing Customer")
        print("Press 3 - Show all Customers")
        print("Press 4 - Generate the Bill")
        print("Press 5 - Mark The Bill As Paid")
        print("Press 6 - Show All Unpaid Bills")
        print("Press 7 - Show Complaints")
        print("Press 8 - Mark As Rectified")
        print("Press 9 - Show Admins")
        print("Press 10 - Show Users")
        print("Press 11 - Quit")
        try:
            ch=int(input("Enter Your Choice : "))
        except ValueError:
            print("Invalid Output - Please enter a Valid Choice Number")
            continue
        if ch == 1:  
            addcustomer()
        elif ch == 2: 
            delcustomer()
        elif ch == 3: 
            showcustomers()
        elif ch == 4: 
            generatebill()
        elif ch == 5: 
            paybill()
        elif ch == 6: 
            showunpaid()
        elif ch == 7:  
            scomplaints()
        elif ch == 8:  
            markrect()
        elif ch == 9: 
            showadmins()  
        elif ch==10: 
            showusers()    
        elif ch==11:
            break 
        else:
            print('Invalid Choice')

# User menu options
def user_menu():
    while True:
        print("-"*50)
        print("\t CHOOSE AN OPERATION")
        print("-"*50)
        print("Press 1 - Pay the Bill")
        print("Press 2 - Generate the Bill")
        print("Press 3 - Raise Complaints")
        print("Press 4 - Quit")
        try:
            ch=int(input("Enter Your Choice : "))
        except ValueError:
            print('Invalid Choice - Enter a Valid Choice Number')
            continue
        if ch==1:
            paybill()
        elif ch==2:
            generatebill()
        elif ch==3:
            rscomplaints()
        elif ch==4:
            break
        else:
            print('Invalid Choice')    

# Function to delete a Customer
def delcustomer():
    print("*"*50)
    print('\t DELETING A CUSTOMER')
    print("*"*50)
    try:
        cd=input('Enter Customer Id : ')
        c=getcur()
        q="delete from customers where customer_id=%s"
        c.execute(q,(cd,))
        getcom()
        print(' CUSTOMER SUCCESSFULLY DELETED ')
    except my.Error as err:
        print(f"Error: Could not delete the customer {err}")

# Function to add a Customer
def addcustomer():
    print("*"*50)
    print('\t WELCOME TO ELECTRICITY MANAGEMENT ')
    print("*"*50)
    try:
        q='select customer_id from customers'
        c=getcur()
        c.execute(q)
        x=c.fetchall()
        # Function to generate a random customer ID
        def custid():
            return rd.randint(10000,99999)
        cd=custid()
        # Ensure the generated customer ID is unique 
        while (cd,) in x:
            cd=custid()
        cname=input('Enter Customer Name : ')
        addr=input('Enter Customer Address : ')
        pho=input('Enter Phone Number : ')
        if not validate_phone(pho):
            return
        email=input('Enter Email : ')
        mtr=input('Enter Meter Number: ')
        print("Your Customer ID : ",cd)
        print()
        c=getcur()
        q='Insert into customers values (%s,%s,%s,%s,%s,%s)'
        val=(cd,cname,addr,pho,email,mtr)
        c.execute(q,val)
        getcom()
        print(' CUSTOMER SUCCESSFULLY ADDED ')
        # Log the new customer addition for record-keeping
        logcus(f"NEW CUSTOMER - Customer ID: {cd},Name: {cname}, Address: {addr}, Phone: {pho}, Email: {email}, Meter No: {mtr}")
        t=input("Enter your Customer ID: ").strip()
        if t==str(cd):
            user_menu()
        else:
            un, pw=loginusernameandpass()
            p="select role from logins where username=%s and passw=%s"
            c=getcur()
            c.execute(p,(un,pw))
            rs=c.fetchone()
            if rs[0]=='admin':
                admin_menu()
            else:
                user_menu()
    except my.Error as err:
        print(f"Error: Could not add the customer {err}")
        # Log the error for record-keeping
        logcus(f"Failed to add customer - Name : {cname} Error: {err}")
    except ValueError:
        print('Invalid Input')

# Function to show all available customers
def showcustomers():
    c=getcur()
    c.execute('Select customer_id,customer_name,phone_number,meter_no,email from customers')
    res=c.fetchall()
    print("                           ","-"*48)
    print("                                               CUSTOMER DETAILS " )
    print("                           ","-"*48)
    headers=["ID","NAME","PHONE","METER NO","EMAIL"]
    show_tables(headers,res)

# Function to generate Electricity Bill
def generatebill():
    try:
        c=getcur()
        name=input('Enter Name: ')
        cid=int(input('Enter the Bill_ID : '))
        mtr=input('Enter Meter Number : ')
        query = "select customer_id, meter_no from customers where customer_name=%s"  
        val = (name,)  
        c.execute(query, val)  
        result = c.fetchone()  
        if result is None:  
            print("No customer found with that name.")  # Inform the user
            return  
        if (str(cid) == str(result[0]) and str(mtr) == str(result[1])):  
            pass  
        else:  
            print("Invalid Customer ID or Meter No")  # Inform the user of the invalid input
            return  # Exit the function
        dt=input("Enter the date of Bill Generation : ")
        cunits=int(input('Enter Current Units on Meter : '))
        punits=int(input('Enter Previous Units on Meter : '))
        if cunits<punits:
            print('Error: Current Units cannot be less than Previous units')
        consumed=cunits-punits
        if consumed<200:
            bill=4*consumed
        elif consumed<400:
            bill=6*consumed
        else:
            bill=8*consumed
        print("Total Units Consumed : ",consumed)
        print("Total Amount to be paid : ",bill)
        duedt=input('Enter the Due Date of Payment : ')
        q="Insert into bills values(%s,%s,%s,%s,%s,%s,%s,%s,'No')"
        vale=(bid,mtr,dt,cunits,punits,consumed,bill,duedt)
        c.execute(q,vale)
        print(" BILL GENERATED SUCCESSFULLY !! ")
        getcom()
        logbill(f"Generated bill for {name} - BILL ID: {bid}, METER NO: {mtr}, UNIT CONSUMED : {consumed}, AMOUNT: {bill}, DUE DATE: {duedt}")
    except my.Error as err:
        print(f"Error: Could not generate bill {err}")
        logbill(f"Failed to generate bill for Meter No: {mtr} Error: {err}")
    except ValueError:
        print('Invalid Input')
    except TypeError:
        print("Invalid Input")

# Function to display all unpaid bills
def showunpaid():
    c=getcur()
    c.execute('Select meter_no,bill_date,total_amount,due_date from bills where paid="No"')
    res=c.fetchall()
    if res==[]:
        print('------------NO UNPAID BILLS------------')
    else:
        print("                           ","-"*40)
        print("                                       LIST OF UNPAID BILLS ")
        print("                           ","-"*40)
        headers=["METER NO","BILL DATE","TOTAL AMOUNT","DUE DATE"]
        show_tables(headers,res)

# Function to pay the Bill
def paybill():
    try:
        c=getcur()
        mtr=input('Enter the Meter Number : ')
        name=input('Enter Customer Name : ')
        cide=int(input('Enter Customer ID : '))
        query = "select customer_id, meter_no from customers where customer_name=%s"  
        val = (name,) 
        c.execute(query, val)  
        result = c.fetchone()  
        if result is None:  # Check if any customer was found
            print("No customer found with that name.")  # Inform the user
            return  
        if (str(cide) == str(result[0]) and str(mtr) == str(result[1])):  
            pass  # Valid match, continue with payment processing
        else:  
            print("Invalid Customer ID or Meter No")  # Inform the user of the error
            return
        bdate=input('Enter the bill date for the bill to be paid : ')
        mp=input('Please Select The Mode of Payment (Cash/Cheque/Card) : ')
        if mp.lower()=='cash':
            mo=float(input('Enter the amount : '))
            print('₹ ',mo,' received')
        print(" -------------------------TRANSACTION COMPLETE------------------------- ")
        q="update bills set paid='Yes' where bill_date<%s and %s<due_date and meter_no=%s"
        val=(bdate,bdate,mtr)
        c.execute(q,val)
        getcom()
    except my.Error as err:
        print(f"Error: Could not mark the bill as paid {err}")
    except ValueError:
        print('Invalid Input')
    except TypeError:
        print('Invalid Input')

# Function to raise customer complaints
def rscomplaints():
    try:
        a=input("Enter Customer ID : ")
        b=input("Enter your Complaint : ")
        c=getcur()
        q='insert into complaints (Customer_ID,complaints) values (%s,%s)'
        val=(a,b)
        c.execute(q,val)
        getcom()
        print(' COMPLAINT SUCCESSFULLY GIVEN  ')
        logcomp(f"Complaint raised by Customer ID: {a}. Complaint : {b}")
    except my.Error as err:
        print(f"Error: Could not register Complaint {err}")
        logcomp(f"Error: Failed to register complaint for Customer ID: {a}. Error: {err}")
    except ValueError:
        print('Invalid Input')

# Function to Display all Compliants
def scomplaints():
    c=getcur()
    c.execute("Select customer_id,complaints from complaints where rectified='No'")
    res=c.fetchall()
    if res==[]:
        print('------------NO UNRECTIFIED COMPLAINTS------------')
    else:
        print("                           ","-"*40)
        print("                                       LIST OF UNRECTIFIED COMPLAINTS ")
        print("                           ","-"*40)
        headers=["CUSTOMER_ID","COMPLAINTS"]
        show_tables(headers,res)

# Function to mark out the Rectified Complaints
def markrect():
    c=getcur()
    q="update complaints set rectified='Yes'"
    c.execute(q)
    print(" -------------------------COMPLAINT RECTIFIED------------------------- ")
    getcom()

# Try block to attempt login
try:
    login() # Function to login
    con.close()
except Exception as err:
    # Catch any unexpected errors that occur during the login process
    print(f"Unexpected Error Occured: {err}") 
