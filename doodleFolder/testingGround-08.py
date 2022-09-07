simple_list = [1,2,3,4,5]
print("simple_list: ", simple_list)
list = [1,2,"els",4,5,'something',[0,9]]
print("list: ", list)

x = [1,2,3,'els',5,[6,7]]
print("length of x: ", len(x))
print("x[0]: ", x[0])
print("x[-1]: ", x[-1])
print("x[3:]: ", x[3:])

x[0] = "now is a string"

print("x: ", x)

x + ["new element"]

y = x[2:4]

print("y: ", y)

print("\nNew Page")
x = [1,2,3]
x.append("new")
print("x: ", x)

y = [7,8]
x.append(y)
print("x", x)

x.extend(y)
print("x: ", x)

x.insert(2, "between")
print("x: ", x)

print("\nNew Page")

x = [1,2,3,4,"els",5,6]
print("del x[2]")
del x[2]
print("x: ", x)

print("del x[2]")
del x[2]
print("x: ", x)

print("del x[2:]")
del x[2:]
print("x: ", x)
print("x[1:2] = []")
x[1:2] = []
print("x[1:2] = ", x)

print("\nNew Page")

x = [1,2,3,"els",2,1]
print("x.remove(3)")
x.remove(3)
print(x)

print("x.remove(2)")
x.remove(2)
print(x)

print("x.remove(\"els\")")
x.remove("els")
print(x)

print("x.remove(3)")
x.remove(3)
print(x)