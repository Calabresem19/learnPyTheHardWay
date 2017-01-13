# create a mapping of state to abbreviation

states = {
    'Oregan':'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'

}

cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-' * 10
print "NY States has: ", cities['NY']
print "OR State has: ", cities['OR']

#print some States

print '-' * 10
print  "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states["Florida"]

# do it by using the state then cities dict

print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states["Florida"]]

# print every state abbreviation

print "-" * 10
for state, abbrev in states.items():
    print "%s state is abbreviated to %s and has city %s"  % (state, abbrev, cities[abbrev])
