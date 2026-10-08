# Write a program to find out whether a student has passed or failed if it requires a total of
# 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an
# input from the user.

sub3 = int(input("Enter the marks percentage in Bio: "))
sub2 = int(input("Enter the marks percentage in phy: "))
sub1 = int(input("Enter the marks percentage in Maths: "))

if(sub1>33 and sub2>33 and sub3> 33):
    print("The student has passed the exam")

else:
    print ("The student has failed the exam")

