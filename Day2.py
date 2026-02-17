# stype = input("Enter Student Type (MSDS, MSH, MGSD): ").strip().lower()
# if stype not in ["msds", "msh", "mgsd"]:
#     print("Invalid student type entered. Please enter MSDS, MSH, or MGSD.")
#     exit()

# while True:
#     try:
#         tuition = float(input("Enter Tuition Fee: "))
#         break
#     except:
#         print("Invalid input! Please enter a numeric value.")

# if stype == "msds":
#     while True:
#         try:
#             college = float(input("Enter College Fee: "))
#             break
#         except:
#             print("Invalid input! Please enter a numeric value.")
#     hostel = 0
# elif stype in ["msh", "mgsd"]:
#     while True:
#         try:
#             hostel = float(input("Enter Hostel Fee: "))
#             break
#         except:
#             print("Invalid input! Please enter a numeric value.")
#     college = 0

# if stype == "msds":
#     total = tuition + college
# elif stype == "msh":
#     total = tuition + hostel
# else: 
#     total = 1.5 * tuition + hostel

# print(f"Total Fee for {stype.upper()}: {total}")

# account_balance=int(input('enter the account balance='))
# withdrawl_amount=int(input('enter the withdrawl amount='))
# if (withdrawl_amount>account_balance):
#      print('insufficiant fund')
# elif (withdrawl_amount>10000):
#      print('limit exceeded')
# else :
#      print('allow withdrawl')

# account_pin=9486
# x=int(input('enter the pin='))
# if(x==account_pin):
#     print('pin is correct')
#     withdrawl_amount=int(input('enter the withdrawl amount='))
#     if (withdrawl_amount>account_balance):
#         print('insufficiant fund')
#     elif (withdrawl_amount>10000):
#         print('limit exceeded')
#     elif (withdrawl_amount<=0):
#         print('invalid amount')
#     else :
#         print('allow withdrawl')
#         balance_amount=account_balance-withdrawl_amount
#         print('the balance amount is=',balance_amount)
# else:
#     print('wrong pin')

    
# age=int(input('enter your age='))
# show=input('enter the show time(mng,eve)=')
# child=150
# adult=250
# senior=200
# if (age<=4):
#     print('free entry')
# elif (age>=5) or (age<=16):
#     if (show == "mng"):
#         child_mng=0.5*child
#         print('the ticket price is=',child_mng)
#     else:
#         print('the ticket price is=',child)

# elif (age>=17) or (age<=59):
#     if (show == "mng"):
#         adult_mng=0.5*adult
#         print('the ticket price is=',adult_mng)
#     else:
#         print('the ticket price is=',adult)
# else:
#     if (show == "mng"):
#         senior_mng=0.5*senior
#         print('the ticket price is=',senior_mng)
#     else:
#         print('the ticket price is=',senior)
 

#  loop


# odd_number=0
# for number in range(1,100,2):
#     print(number)
#     odd_number+=number
# print("the sum of the odd numbers is:",odd_number)    


# even_number=0
# for number in range(2,100,2):
#   print(number)
#   even_number+=number
# print("the sum of the odd numbers is:",even_number)    

# number=0
# for number in range(5,55,5):
#     print(number)
#     number+=number

# def printTable(n):
    # for i in range (1, 11): 
        # print ("%d * %d = %d" % (n, i, n * i))
# if __name__ == "__main__":
#   n = 5
#   printTable(n)  

# tam=int(input("enter the mark"))
# eng=int(input("enter the mark"))
# math=int(input("enter the mark"))
# sci=int(input("enter the mark"))
# soc=int(input("enter the mark"))
# total=tam+eng+math+sci+soc
# print("total mark",total)
# avg=total/5
# print("averge is:",avg)

# rows = 5
# for i in range(1, rows +1):
#         print("*"*i)

# rows = 5
# for i in range(rows, 0,-1):
#         print("*"*i)

# n=1
# i=n
# while i<100:
#     print(i)
#     n=n+i
#     i=i+2
# print("") 

# n=0
# i=n
# while i<100:
#     print(i)
#     n=n+i
#     i=i+2


# i=1
# while i<6:
#     print("*"*i)
#     i=i+1 

# i=5
# while i>0:
#     print("*"*i)       
#     i=i-1

# i=5
# while i<55:
#     print(i)
#     i+=5

def book_seats():
    total_seats=10
    current_seat=1
    while current_seat<=total_seats:
        pass_name=input("enter the name")
        print(f"seat {current_seat} booked for {pass_name}")
        current_seat +=1
    print("ALL SEATS ARE BOOKED")
if __name__== "__main__":
    book_seats()