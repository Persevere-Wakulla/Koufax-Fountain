# Python has hash tables, they're called dictionaries
book = dict()

book["apple"] = 0.67
book["milk"] = 1.49
book["avocado"] = 1.49
print(book["apple"])

phone_book = {}

phone_book["jenny"] = 8675309
phone_book["emergency"] = 911

print(phone_book["jenny"])


voted = {}

"""Suppose you’re running a voting booth. Naturally, every person can
vote just once. How do you make sure they haven’t voted before? When
someone comes in to vote, you ask for their full name. Then you check
it against the list of people who have voted.

If their name is on the list, this person has already voted—kick them
out! Otherwise, you add their name to the list and let them vote. Now
suppose a lot of people have come in to vote, and the list of people who
have voted is really long."""

def check_voter(name):
    if voted.get(name):
        print("Kick them out!")
    else:
        voted[name] = True
        print("Let them vote!")
        
