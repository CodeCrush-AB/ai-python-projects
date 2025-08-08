
friends = ["wafa", "hasan", "ishaq"]
print(friends[0:2])
# [0:2] means it will take from index 0 to 1 excluding 2

numbers = [4,6,8,24,46]
friends.extend(numbers)
#adds the two lists

friends.append("anas")
#adds a string to a list

friends.insert(2,"anas")
#anas is inserted in index 2 while rest are shifted right side

friends.remove("anas")
#removes a string from lists

friends.clear()
#removes all the elements

friends.pop()
#removes the last element

friends.index("anas")
#tells the index

friends.count("anas")
#tells how many times the element repeats

friends.sort()
#sorts in ascendind, order also works with no.

friends.reverse()
#reverse the order of lists

friends2=friends.copy()
#copys it