exam_num= float(input("ENter your number: "))
if exam_num>=80:
    print("A")
elif exam_num>=70 and exam_num<=79:
    print("B")
elif exam_num>=60 and exam_num<=69:
    print("C")
elif exam_num>=50 and exam_num<=59:
  print("D")
elif exam_num<50:
    print("F")
elif exam_num<0 or exam_num>100:
    print("Ivalid Marks")