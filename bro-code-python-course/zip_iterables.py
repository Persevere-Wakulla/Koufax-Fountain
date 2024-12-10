# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc)
#                   creates a zip object with paired elements stored in tuples for each element

usernames = ["Koufax", "Cameron", "Michael"] 
passwords = ["password", "abc123", "guest"]
login_date = ["1/1/2024","1/2/2024","1/3/2024"]

users = zip(usernames,passwords,login_date)

print(type(users))

for i in users:
    print(i)
    