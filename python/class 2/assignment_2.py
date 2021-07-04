print("'Welcome to Gpa calculator'")

mark = int(input("Enter your mark: "))

if mark >100 or mark<0:
    print("Wrong input.")
elif mark >= 80:
    print("Your grade is A+ & point: 4")
elif mark >= 75:
    print("Your grade is A & point: 3.75")
elif mark >= 70:
    print("Your grade is A- & point: 3.50")
elif mark >= 65:
    print("Your grade is B+ & point: 3.25")
elif mark >= 60:
    print("Your grade is B & point: 3.00")
elif mark >= 55:
    print("Your grade is B- & point: 2.75")
elif mark >= 50:
    print("Your grade is C+ & point: 2.50")
elif mark >= 45:
    print("Your grade is C & point: 2.25")
elif mark >= 40:
    print("Your grade is D & point: 2.00")
else:
    print("You have failed!")

