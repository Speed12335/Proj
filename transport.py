import mysql.connector as msc
con=msc.connect(host='localhost',user='root',passwd='tiger',database='bls10')##give a &name 
cur=con.cursor()
cur.execute("create table transport (VCode int(3) not null primary key, Vehicle varchar(15) not null,DriverPhNo bigint(10), rpkm int(2), Passengers int(2)) ")
cur.execute("insert into transport values(%s,'%s',%s,%s,%s)"%(541,"Maruti WagonR",9784536859,5,4))
cur.execute("insert into transport values(%s,'%s',%s,%s,%s)"%(542,"Maruti Swift",8976790798,8,4))
cur.execute("insert into transport values(%s,'%s',%s,%s,%s)"%(543,"Tata Altroz",7845306789,10,5))
cur.execute("insert into transport values(%s,'%s',%s,%s,%s)"%(544,"Tata Tiago",9583858693,11,5))
cur.execute("insert into transport values(%s,'%s',%s,%s,%s)"%(545,"Mercedes S450",9785683438,30,5))
cur.execute("insert into transport values(%s,'%s',%s,%s,%s)"%(546,"Honda City",7584957385,15,5))
cur.execute("insert into transport values(%s,'%s',%s,%s,%s)"%(547,"Toyota Innova",8679586950,17,7))
cur.execute("insert into transport values(%s,'%s',%s,%s,%s)"%(548,"Lexus LX",9274664828,40,7))
cur.execute("insert into transport values(%s,'%s',%s,%s,%s)"%(549,"Mahindra XUV700",9799830685,25,7))
cur.execute("insert into transport values(%s,'%s',%s,%s,%s)"%(550,"Jeep Meridian",9394853829,28,8))
cur.execute("insert into transport values(%s,'%s',%s,%s,%s)"%(551,"Traveller",7238539232,30,18))
cur.execute("insert into transport values(%s,'%s',%s,%s,%s)"%(552,"Tour Bus",8439889424,35,40))
acc=[]
tlog=[]
def login():
    print("Please Log In")
    global g
    g=input("Enter your Mail ID")
    if len(acc)==0:
    	print("No account yet. Press \"Y\" then enter 1 to create and account")
    	return False
    for i in acc:
        if i['Mail']==g:
            ps=int(input("Enter your passcode"))
            if ps==i['Pass_Code']:
                return True
            else:
                print("Sorry wrong Mail ID or Pass Code")
                return False
    else:
        print("Looks you don't have an account yet. Press \"Y\" then enter 1 to create and account")
ans="Y"
print("********WELCOME TO ATLAS HOTEL'S TRANSPORT BOOKING APPLICATION********")
while ans=='Y' or ans=='y':
    print("New here?, Create an account by entering 1")
    print("Need to go somewhere?, Book a vehicle by entering 2")
    print("Want to check your travel log?, enter 3")
    print("Want to view your account?, enter 4")
    print("Want to make changes to your account?, enter 5")
    ch=int(input("Enter your choice"))
    if ch==1:
        print("Let's get started by creating an account for you")
        ac={}
        tl={}
        ac['Name']=input("Enter your name")
        ac['Phone']=int(input("Enter your number"))
        ac['Mail']=input("Enter your Mail ID")
        ac['Pass_Code']=int(input("Enter a 4 digit pass code for your account"))
        print(ac)
        acc.append(ac)
        print("Account created successfully")
        tl['Mail']=ac['Mail']
        tl['Previous_VCode']=None
        tl['Total_Distance']=0
        tl['Last Travel Date']=None
        tlog.append(tl)
    if ch==2:
        b=login()
        if b==True:
            cur.execute("select * from transport")
            tab=cur.fetchall()
            le=len(tab)
            for i in range(le):
                j=tab[i]
                print("VCode:",j[0])
                print("Vehicle:",j[1])
                print("Driver's Phone No.:",j[2])
                print("Rate:",j[3])
                print("No. of Passengers:",j[4])
            vc=int(input("Enter the vcode of your desired vehicle"))
            cur.execute("select rpkm from transport where vcode=%s"%(vc,))
            rate=cur.fetchone()
            k=int(input("Enter the distance you want to travel in km"))
            cur.execute("select curdate()")
            dt=str(cur.fetchone())
            #payment(rate[0]*k) your function "payment"
            for i in range(len(tlog)):
                j=tlog[i]
                if j['Mail']==g:
                    j['Previous_VCode']=vc
                    j['Total_Distance']+=k
                    j['Last Travel Date']=dt[15:27]
    if ch==3:
        b=login()
        if b==True:
            for i in range(len(tlog)):
                j=tlog[i]
                if j['Mail']==g:
                    if j['Total_Distance']==0:
                        print("Looks like you haven't gone anywhere yet, Hit \"Y\" then enter 2 to book your first ride")
                    else:
                        print("Your Travel Log")
                        for key in j:
                            print(key,':',j[key])
    if ch==4:
        b=login()
        if b==True:
            pos=-1
            for i in range(len(acc)):
                j=acc[i]
                if j['Mail']==g:
                    pos=i
                    break
            if pos==-1:
                print("Looks like you don't have an account yet, Hit \"Y\" then enter 1 to create your account and get started")
            else:
                print("Your Account Details")
                for key in j:
                    print(key,':',j[key])
    if ch==5:
        b=login()
        if b==True:
            print("How would you like us to help you edit your account?")
            print("Enter \"Name\" to change your name")
            print("Enter \"Phone\" to change your mobile number")
            print("Enter \"Mail\" to  change your Mail ID")
            print("Enter \"Pass_Code\" to change your pass code")
            ke=input("Enter your choice")
            for i in acc:
                if i['Mail']==g:
                    print("Enter new ",ke )
                    i[ke]=eval(input())
                    print("Account Edited Successfully")
                    break
    ans=input("Would you like to continue, type \"Y\" if yes, type \"N\" if no")
else:
    print("Thank you for choosing Atlas Hotels, we are glad to have served you ")
    print("Have a great day ahead!")
con.close() 
