height=input("你的身高是___m")
weight=input("你的体重是___kg")
h=float(height)
w=float(weight)
BMI=w/(h*h)
if BMI <18.5:
    print("过轻")
elif 18.5<=BMI<24:
    print("正常")
elif 24<=BMI<28:
    print("超重")
else:
    print("肥胖")