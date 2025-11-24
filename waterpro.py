import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
d=pd.read_excel("C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python313\\waterpro.xlsx")
df=pd.DataFrame(d)
print("Hello welcome to the water station")
number=int(input("enter your number"))
a=df[df["Number"]==number].index.tolist()
b=df.loc[a,"C"].tolist()
c=b[0]
def withDraw(c):
    if c!=0:
        c-=1
        df.loc[a,"C"]=c
        return balance(c)
    else:
        print("please recharge first:")
        return main(number)
def recharge(c):
    print("enter your amount")
    print("1:300")
    print("2:900")
    print("3:3600")
    amount=int(input("enter your amount:"))
    if amount==300 or amount==900 or amount==3600:
        if amount==300:
            c+=amount//10
            df.loc[a,"C"]=c
        elif amount==900:
            c+=amount//10
            df.loc[a,"C"]=c
        elif amount==3600:
            c+=amount//10
            df.loc[a,"C"]=c
        else:
            print("choose correct plans")
        return balance(c)
    else:
        print("enter valid amount")
        main(number)
def balance(c):
    print("your remaining balance is:",c)
def main(number):
        print("1.GetWater")
        print("2.Balance")
        print("3.Recharge")
        choose=int(input("enter your choose"))
        if choose==1:
            withDraw(c)
        elif choose==2:
            balance(c)
        elif choose==3:
            recharge(c)
main(number)
df.to_excel("C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python313\\waterpro.xlsx",index=False)

    



    
        
