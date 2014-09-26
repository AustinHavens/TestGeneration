__author__ = 'Austin Havens'
from ParameterAssignment import ParameterAssignment
from Test import Test

class IPOGenerator:

    def __init__(self, strength, situations):
        self.strength = strength
        self.situations = situations
        self.coveredSituations = list()
        self.tests = list()


    # Generates or expands a test set
    def generate(self, parameters, initialTestSet):
        while len(self.situations) > 0:
            for parameter in parameters:
                remainingSituationsWithParameter = self._findSituationsContainingParameter(parameter)

                # TODO: may want to check the inner loop here, the outer should guarantee coverage though
                self.verticalGrowth(remainingSituationsWithParameter)
                self.horizontalGrowth(parameter)

    def addParameterAssignmentToTest(self, testNumber, assignment):
        assert(not self.tests[testNumber].contains(assignment))
        self.tests[testNumber].addParameterAssignment(assignment)
        self._removeSituationsCoveredByTest(self.tests[testNumber])


    def horizontalGrowth(self, parameter):
        numberOfTestsInSet = len(self.tests)
        numberOfValuesForParameter = parameter.values.count()
        if numberOfTestsInSet <= numberOfValuesForParameter:
            for testNumber in range( 0, numberOfTestsInSet):
                newAssignment = ParameterAssignment(parameter.name, parameter.values[testNumber])
                self.addParameterAssignmentToTest(testNumber,newAssignment)
        else:
            for testNumber in range( 0, numberOfValuesForParameter):
                newAssignment = ParameterAssignment(parameter.name, parameter.values[testNumber])
                self.addParameterAssignmentToTest(testNumber,newAssignment)

            # Add the parameter to the rest of the tests
            for testNumber in range(numberOfValuesForParameter, numberOfTestsInSet):
                # determine which value of the parameter adds the most new coverage
                # TODO: this does not take into account order it may need to for the algorithm to not hang in some situations
                self.tests[testNumber] = self._findValueWithMaximumCoverageForTest(self.tests[testNumber], parameter)
                self._removeSituationsCoveredByTest(self.tests[testNumber])


    # Adds tests
    def verticalGrowth(self, remainingSituationsWithCurrentParameters):
        # For each remaining situation, if there is an existing situation, if there is an existing test which can be
        # extended to satisfy the situation, extend it, otherwise add a new test.

        # TODO: I think this was to prevent modifying existing tests in the set but may result in a larger test set
        newTests = list()

        # TODO: make sure that extending tests does not cause one of the previously covered situations to no longer be covered
        for situation in remainingSituationsWithCurrentParameters:
            anyTestExtended = False;
            for test in newTests:
                testExtended = situation.extendTest(test)
                self._removeSituationsCoveredByTest(test)
                remainingSituationsWithCurrentParameters.discard(situation)
                if testExtended:
                    anyTestExtended = True
                    break

            # If no test was extended add the situation as a new test
            if not anyTestExtended:
                newTests.append(Test(situation.asignments))
                self._removeSituationsCoveredByTest(test)
                remainingSituationsWithCurrentParameters.discard(situation)

        self.tests |= newTests


    # TODO: consider a "temporalGrowth" stage for increased efficiency of ordered situations


    def _findSituationsContainingParameter(self, parameter):
        for situation in self.situations:
            if situation.contains(parameter):
                yield situation


    # Finds all situations covered by a test
    def _findSituationsCoveredByTest(self, test):
        for situation in self.situations:
            if situation.isCoveredByTest(test):
                yield situation


    # Removes situations covered by the test from the list of situations that still need to be covered
    def _removeSituationsCoveredByTest(self, test):
        # TODO: This will not work for situations where some orders are not allowed
        for situation in self.situations:
            if situation.isCoveredByTest(test):
                self.situations.remove(situation)


    def _makePossibleModificationsOfTestWithNewParameter(self, test, parameter):
        assert(not test.contains(parameter))
        for parameterValue in parameter.values:
            localTest = Test(test.steps)
            newAssignment = ParameterAssignment(parameter.name, parameterValue)
            localTest.addStep(newAssignment)
            yield localTest


    def _findValueWithMaximumCoverageForTest(self, test, parameter):
        return max(self._makePossibleModificationsOfTestWithNewParameter(test, parameter), key=self._findSituationsCoveredByTest)

