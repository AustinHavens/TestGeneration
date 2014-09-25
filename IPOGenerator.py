__author__ = 'am004517'

class IPOGenerator:

    def __init__(self, strength):
        self.strength = strength


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


    # Situation is probably going to be an unordered tuple but I want to leave the name of the method general since
    # I would like to extend the algorithm to ordered sets.
    def _testContainsSituation(self, test, situation):
        pass


    # Finds all situations covered by a test
    def _findSituationsCoveredByTest(self, test):
        pass


    # Removes situations covered by the test from the list of situations that still need to be covered
    def _removeSituationsCoveredByTest(self, test):
        pass