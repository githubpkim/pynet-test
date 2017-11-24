#!/usr/bin/env python

class PartyAnimal(object):
    x = 0
    def __init__(self, nam):
        x = 100
        self.name = nam
        print self.name+": constructed"
    def party(self):
        self.x = self.x + 1
        print self.name+" party count:",self.x
#
class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print self.name+" points:",self.points
    def func1(self):
        y = 10
        print "inside func1"
