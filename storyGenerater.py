import random
when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
name = ['Ali', 'Miriam','daniel', 'Hook', 'Starwalker']
residence = ['Barcelona','India', 'Germany', 'Venice', 'England']
went = ['cinema', 'university','seminar', 'school', 'laundry']
happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mystery', 'wrote a book']
random_when=random.choice(when)
random_who=random.choice(who)
random_residence=random.choice(residence)
random_went=random.choice(went)
random_happened=random.choice(happened)
print(f"{random_when} {random_who} that lived in {random_residence} went to the {random_went} and {random_happened}")
