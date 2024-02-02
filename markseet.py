m1= int(input("enter marks1:"))
m2= int(input("enter marks2:"))
m3= int (input("enter marks3:"))
if m1>=28 and m2>=28 and m3>=28:
    total=m1+m2+m3
    per=total/3
    result= "pass"
    if per>=80:
        grade="a"
    elif per>=70:
        grade="b"
    elif per>=60:
        grade="c"
    else:
        grade="d"
else:
    total=m1+m2+m3
    per="***"
    result="fail"
    grade="f"
print("total:",total)
print("presentage:",per)
print("result:",result)
print("grade:",grade)