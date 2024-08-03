n=int(input("Enter number of element:"))
arr=[]
print("Enter elements:")
for i in range(0,n):
    ele=int(input())
    arr.append(ele)
x=int(input("Enter searching ele:"))
def search(arr,x):
    for i in range(0,n):
        if(x==arr[i]):
            print(f"element found at index {i}")
            return
    print("Element not present")
print(search(arr,x))

