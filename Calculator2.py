def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
print("Select operation.")

print("1.Addition")

print("2.Subtraction")
choice = input("Enter choice(1/2): ")
n1=int(input("enter first operand:"))
n2=int(input("enter second operand:"))
if choice == '1':
    print(n1, "+", n2, "=", add(n1, n2))
else:
    print(n1, "-", n2, "=", subtract(n1, n2))



