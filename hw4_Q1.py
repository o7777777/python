weight=int(input("請使用者輸入體重"))
height=(int(input("請使用者輸入身高")))*0.01
bmi=weight/(height)**2
print(bmi)
if bmi>30:
    print('肥胖')
elif bmi>25:
    print('過重')
elif bmi>18.5:
    print('正常')
else:
    print("過輕")
