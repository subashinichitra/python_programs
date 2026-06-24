arr = [10,20,30,40]
search = int(input("Enter value: "))
for i in range(len(arr)):
    if arr[i] == search:
        print("Index value =", i)
        break