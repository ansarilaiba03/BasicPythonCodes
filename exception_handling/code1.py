a = int(input("enter a number: "))

try:
    print(10/a)

except Exception as err:
    print(f"there is an error : {err}")

else:
    print("there was no error")

finally:
    print('i will always run')

print("end")