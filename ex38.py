ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not ten things in that lists. Lets fix that"

stuff = ten_things.split(" ")
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now" % len(stuff)

print "There we go: " , stuff

print "Lets do somethings with stuff."

print stuff[1]

print stuff[-1]

print stuff.pop()

print ' '.join(stuff) #what cool!
print '#'.join(stuff[3:5])
