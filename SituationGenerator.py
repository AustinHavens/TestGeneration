__author__ = 'Austin Havens'
from ParameterAssignment import ParameterAssignment
from Situation import UnorderedSituation
class SituationGenerator:

    def __init__(self, strength, parameters):
        self.strength = strength
        self.parameters = parameters

    def generatePairwiseSituations(self):
        # TODO: Ignoring strength for now and just using 2
        parameterCount = len(self.parameters)

        for firstParameterIndex in range(0, parameterCount):
            for secondParameterIndex in range(firstParameterIndex+1, parameterCount):
                for valueOfFirstParameter in self.parameters[firstParameterIndex].values:
                    for valueOfSecondParameter in self.parameters[secondParameterIndex].values:
                        firstParameterName = self.parameters[firstParameterIndex].name
                        secondParameterName = self.parameters[secondParameterIndex].name
                        yield UnorderedSituation([ParameterAssignment(firstParameterName, valueOfFirstParameter), ParameterAssignment(secondParameterName, valueOfSecondParameter)])

