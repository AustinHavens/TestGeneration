__author__ = 'Austin Havens'
from collections import OrderedDict

# TODO: this may not be needed?
class Test:

    def __init__(self, steps):
        self.newSituationsCovered = []
        self.steps= list()
        for step in steps:
            self.steps.append(step)


    def addStep(self, step):
        self.steps.append(step)

    def addNewSituationCovered(self, situation):
        self.newSituationsCovered.append(situation)


