print("    /\\")
print("   /  \\")
print("  /    \\")
print(" /      \\")
print("/________\\")
human="zed"
print(human)
print(human.upper())
print(human.lower())
print(human.isupper())
print(human.replace("z", "M"))
#calculator
a=input("Enter the number:")
b=input("Enter the second number:")
c=input("Enter the operator:")
if c=="+":
    result=(int(a)+int(b))
elif c=="-":
    result=(int(a)-int(b))
elif c=="*":
    result=(int(a)*int(b))
elif c=="/":
    result=(int(a)/int(b))
print("The result is:", result )
# As u say
who=input("Name of a profession:")
who2=input("Common noun:")
place=input("Place:")
print("Despite the fact that", who," are relatively harmless, many" ,who2," continue to believe the pervasive myth that",who," are dangerous to", who2,". This impression of", who, " is exacerbated by their mischaracterization in", place)

#list
friends=["jin", "jimin", "jhope", "rm", "taehyung", "suga", "jungkook"]
print(friends[5])
#list 2.0
lucky_numbers=[4,8,15,16,23,42]
friends=["jin", "jimin", "jhope", "rm", "taehyung", "suga", "jungkook"]
friends.extend(lucky_numbers)

friends.append('zed')
friends.insert(0, "maitreyee")
friends.remove("taehyung")
friends.pop()
print(friends.count("jimin"))

#functions
def cube(num):
    return num*num*num
num= int(input("Enter a number to cube:"))
result= cube(num)
print(result)
#IF
is_male=False
is_tall=True
if is_male and is_tall:
    print("You are a male or talll or bothh")
elif is_male and not(is_tall):
    print("You are a")
else:
    print("you are not a male nor tall")

#loops
numbers=[(1, "odd"), (2, "even"), (3, " odd"), (4, "even"), (5, "odd"), (6, "even"), (7, "odd"), (8, "even"), (9, "odd"), (10, "even")]
for number in numbers:
    print(number) 
    
for number in range(1,11):
    if number % 2 == 0:
        print(number, " even")
    else:
        print(number, " odd")
for index, name in enumerate(friends):
        print(index, name)
#dictionary
phone_book={
    "Maitreyee": "123-456-7890",
    "Zed": "987-654-3210",
    "Jimin": "555-555-5555",
    "graceie": "111-222-3333",  
    "gargi": "444-555-6666",
}
name=input("Enter the name to search:")
if name in phone_book:
    print("Phone number:", phone_book[name])
else:
    print("Contact not found.")
# Tuples
city=("delhi", "chandigarh", "new york", "paris", "london")
print(city[2])
#sets
fruits={"apple", "banana", "cherry", "orange", "kiwi", "mango"}
fruits.add("grapes")
fruits.remove("banana")
print(fruits)
#file handeling 
with open("notes.txt", "w") as file:
    file.write("1st.\n")
    file.write("2nd.\n")
    file.write("3rd.\n")
with open("notes.txt", "r") as file:
    print(file.read())
with open("notes.txt", "a") as file:
    file.write("\nThis is a new line added to the file.")
with open("notes.txt", "r") as file:
    print(file.read())
    # error handeling
try:
    num=int(input("enter a number: "))
    print(10/num)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Please enter valid numbers only  ")
finally:
    print("Program finished")


