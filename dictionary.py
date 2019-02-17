# A simple database
people = {
    'Alice': {
        'phone': '2344',
        'addr': '23, Numbr street'
    },
    'Beth': {
        'phone': '98765',
        'addr': '87,jhqwhjdqw,bjqwjhdqw'
    },
    'Cecil': {
        'phone': '09754356',
        'addr': '89,t qwjdqw'
    }
}
labels = {
    'phone': 'phone number',
    'addr': 'address'
}
name = input('Name: ')
request = input('Phone Number(p), address (a)? ')
if request == 'p': key = 'phone'
if request == 'a': key = 'address'
if name in people:
    print("{}'s {} is {}.".format(name, labels[key], people[name][key]))
