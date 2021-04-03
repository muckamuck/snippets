'''
An array Things
'''
class AnotherThing:
    def __init__(self, the_data):
        self.the_data = the_data

    def print_the_data(self):
        print(self.the_data)


foo = AnotherThing('foo')
bar = AnotherThing('bar')
baz = AnotherThing('baz')

array_of_things = [
    foo,
    bar,
    baz
]

for t in array_of_things:
    t.print_the_data()
