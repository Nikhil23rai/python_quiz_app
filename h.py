# arr1=[2,3,4,5,8]
# arr2=[]
# maxi=max(arr1)
# for i in range(len(arr1)):
#      arr2.append(arr1[i]+maxi)
#      arr2[i]*=maxi
# print(arr2)

# for i in range(len(arr1)):
#     arr2.append(arr1[i]+max)
# #

#         arr2[i]*=max
# print(arr2)
# arr=[2,3,4,58]
# maxi=arr[0]
# for i in arr:
#     if i>=maxi:
#         maxi=i
# print(maxi)
# print('Q1: Which one is the fruit in the given options?')
# print("Q2: City of lake ?")
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

