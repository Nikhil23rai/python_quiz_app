
que={'Q1:Which one is the fruit in the given options?':"a",
    "Q2 :City of lake ?":'c',
    'Q3:which one is animal ?':'b',
    'Q4: Vegetable name?':"d"}
ans={'a':'mango','b':'lion','c':'bhopal','d':'potato'}
score=0
for key,value in que.items():
    print(key)
    for key,val in ans.items():
        print(key,")",val )
    n=str(input("enter option: "))
    if(  value==n):
        print('<<CORRECT>>')
        score+=1
    else:
        print("<<INCORRECT>>")
print(f"score:{score}")       

