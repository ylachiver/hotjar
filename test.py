#!/usr/bin/env python

class People:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __repr__(self):
        return '{}: {}'.format(self.name, self.age)

def main():
    a = People(12, 'a')
    b = People(54, 'b')
    c = People(32, 'y')

    l = [a, b, c]
    l.sort(key=lambda x:x.age)

    print l

if __name__ == '__main__':
    main()
