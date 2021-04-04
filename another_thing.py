'''
An array Things
'''
class AnotherThing:
    def __init__(self, the_data):
        '''
        very simple class with some data
        '''
        self.the_data = the_data

    def print_the_data(self):
        '''
        print the data
        '''
        print(self.the_data)


'''
Make some things
'''
foo = AnotherThing('foo')
bar = AnotherThing('bar')
baz = AnotherThing('baz')

'''
Put them in an array
'''
array_of_things = [
    foo,
    bar,
    baz
]

'''
Do something with everything in the array
'''
for t in array_of_things:
    t.print_the_data()
