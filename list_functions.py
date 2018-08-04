friends = ["Alex", "Jack", "Kevin", "Jim", "Toby", "Oscar"]

lucky_numbers = [4, 18, 15, 16, 23, 42]

print(friends)
print(lucky_numbers)

# new_friends = friends.extend(lucky_numbers)
friends.extend(lucky_numbers)
print(friends)

friends.append("Tom")
print(friends)
friends.insert(1,"Kelly")
print("-------------")
print(friends)
print("------------")
friends.remove("Jim")
print(friends)
friends.pop()
print(friends)
print(friends.index("Kevin"))
# friends.clear()
# This can clear the list

print(friends.count("Kevin"))

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

new_lucky_numbers = lucky_numbers.copy()
print(new_lucky_numbers)