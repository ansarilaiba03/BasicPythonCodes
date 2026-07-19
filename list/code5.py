#check if a list is sorted or not

a = [1,2,3,1,7,8]

# len(a)-1 because if i type len(a) then while comparing a[i+1] it will compare a[5] with a[6] but a[6] does not exist so it is an error, hence we will compare only till a[5] 

for i in range(1, len(a)-1, 1):
        if a[i] < a[i+1]:
            continue
        else: 
            print("not sorted")
            break #if break statement worked then else will not work otherwise else statement will work

else:
     print("sorted")


    