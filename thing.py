'''
A class of array things
'''
class Thing:
    def __init__(self, things):
        self.things = things

    def print_things(self):
        for t in self.things:
            print(t)


food = [
    'foo',
    'bar',
    'baz'
]

t = Thing(food)
t.print_things()
