__author__ = 'am004517'

class IPOGenerator:

    def __init__(self, strength, situations):
        self.strength = strength
        self.situations = situations
        self.tests = list()


    # Generates or expands a test set
    def generate(self, parameters, initialTestSet):
        pass


    def getNTuples(self, n, parameters):
        pass


    # Makes existing tests bigger by adding the parameter
    def horizontalGrowth(self, parameter):
        pass


    # Adds tests
    def verticalGrowth(self, remainingSituationsWithCurrentParameters):
        pass



    # Finds all situations covered by a test
    def _findSituationsCoveredByTest(self, test):
        for situation in self.situations:
            if situation.isCoveredByTest(test):
                yield situation


    # Removes situations covered by the test from the list of situations that still need to be covered
    def _removeSituationsCoveredByTest(self, test):
        for situation in self.situations:
            if situation.isCoveredByTest(test):
                self.situations.remove(situation)