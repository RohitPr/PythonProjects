# write a program that tests the compatibility between two people.

"""
Take both people's names and check for the number of times the letters in the word TRUE occurs.
Then check for the number of times the letters in the word LOVE occurs.
Then combine these numbers to make a 2 digit number.
"""

print("Welcome to Love Calculator\n")
person1_name = input("Enter the name of the first person : ").lower()
person2_name = input("Enter the name of the second person : ").lower()

combined_names = person1_name + " " + person2_name

t = combined_names.count('t')
r = combined_names.count('r')
u = combined_names.count('u')
e = combined_names.count('e')
true_count = t + r + u + e

l = combined_names.count('l')
o = combined_names.count('o')
v = combined_names.count('v')
e = combined_names.count('e')
love_count = l + o + v + e

total_count = str(true_count) + str(love_count)
total_count = int(total_count)

if total_count < 10 or total_count > 90:
    print(
        f"\nYour score is {total_count}, you go together like coke and mentos.")
elif (total_count >= 40) and (total_count <= 50):
    print(
        f"\nYour score is {total_count}, you are alright together.")
else:
    print(
        f"\nYour score is {total_count}")
