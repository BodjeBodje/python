"""
input : marks int
70 and above -> A
60-69 -> B
50-59 -> C
<50 -> D
"""

marks = int(input("Enter your marks: "))
marks=int(marks)

#decide grade

if marks >= 70:
    print("A")
elif marks >= 60:
    print("B")
elif marks >= 50:
    print("C")
elif marks < 50:
    print("D")