print("Choose an optino: \n\t1) sum\n\t2) sub\n\t0) exit")
u_value = input("Enter an option: ")
if u_value == "0":
    print("Bye")
elif u_value == "1":
    print("sum operations")
elif u_value == "2":
    print("sub operations")
else:
    print("Wrong option")