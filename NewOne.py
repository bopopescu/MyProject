x=input("Enter a number")
l= len(x)//2
lt=len(x)-1
for i in range(l):
    p=int(x[i])
    q=int(x[lt-i])
    print(p)
    print(q)
    if p!=q :
        print("Not Pallinddrom")
        break
else:
    print("palindrom")
