'''
A class of array things
'''
class Thing:
    def __init__(self, things):
        '''
        things is just an array of stuff
        '''
        self.things = things

    def print_things(self):
        '''
        print the value of all the stuff in the array
        '''
        for t in self.things:
            print(t)


food = [
    'foo',
    'bar',
    'baz'
]

t = Thing(food)
t.print_things()
