#write a python to determine grade of the students
#a:score>=90
#score>=80 and score<90
#score>=70

score=float(input("enter the grade of the student:"))
if(score>=90):
    print("you get grade A in the test")
elif(score>=80 and score<90):
    print("you get grade B in the test")
elif(score>=70 and score<80):
    print("you get a grade c in the test")
elif(score>=60 and score<70):
    print("you get a grade D in test")
else:
    print("you get a grade E in the test")
#write a python program to clculate a discount for a customer based on the pur using tkinter
#conditions:
#purchase>=$500:20% discount
#purchase>200 and <$500:10% discount
#purchase<$200:No discount
#input: Text box in tkinter window
def purchase_discount(purchase_mount,total_mount):
    if(purchase_mount>=500):
        print("you will get a discount of 20% on the purchase")
        discount=20/100
    elif(purchase_mount>200 and purchase_mount<500):
        print("you will get discount of 10% on the purchase")
        discount=10/100
    else:
        print("discount is not appliable on your purchase")
        discount=0
        mount_to_be_paid=purchase_mount-(purchase_mount*discount)
        print("amount to be paid is :$","amount_to_be_paid")


