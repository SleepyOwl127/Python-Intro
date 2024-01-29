print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

result = float(num1) + float(num2)
print(result)

lucky_Numbers = [4,2,3,9,5,1,6]
friends = ["lol","meow","sleep"]
friends.extend(lucky_Numbers)
friends.append("Cat")
friends.insert(1, "Bob")
friends.pop()
lucky_Numbers.reverse()
friends2 = friends.copy
print(friends.index("lol")) 
print(friends.count("lol")) 
print(lucky_Numbers)
