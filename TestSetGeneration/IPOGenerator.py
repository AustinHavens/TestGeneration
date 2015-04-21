from TestSetGeneration.ParameterAssignment import ParameterAssignment
from TestSetGeneration.Test import Test

__author__ = 'Austin Havens'


class IPOGenerator:

    def __init__(self, situations):
        self.situations = situations
        self.coveredSituations = list()
        self.tests = list()


    # Generates or expands a test set
    def generate(self, parameters):
        # seed the generator with the first situation

        self.tests.append(Test(self.situations[0].assignments))
        self.coveredSituations.append(self.situations[0])
        self.situations.remove(self.situations[0])

        while len(self.situations) > 0:
            for parameter in parameters:
                remainingSituationsWithParameter = self._findSituationsContainingParameter(parameter)

                # TODO: may want to check the inner loop here, the outer should guarantee coverage though
                self.verticalGrowth(remainingSituationsWithParameter)
                self.horizontalGrowth(parameter)

    def addParameterAssignmentToTest(self, testNumber, assignment):
        #assert(not self.tests[testNumber].contains(assignment))\

        if assignment.name not in map(  lambda step: step.name, self.tests[testNumber].steps):
            self.tests[testNumber].addStep(assignment)
            self._removeSituationsCoveredByTest(self.tests[testNumber])


    def horizontalGrowth(self, parameter):
        numberOfTestsInSet = len(self.tests)
        numberOfValuesForParameter = len(parameter.values)
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
                # don't do anything if the test already has the parameter
                if parameter.name not in map(lambda step: step.name, self.tests[testNumber].steps):
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

                if testExtended:
                    self._removeSituationsCoveredByTest(test)
                    anyTestExtended = True
                    break

            # If no test was extended add the situation as a new test
            if not anyTestExtended:
                newTest = Test(situation.assignments)
                newTests.append(newTest)
                self._removeSituationsCoveredByTest(newTest)

        self.tests.extend( newTests)


    # TODO: consider a "temporalGrowth" stage for increased efficiency of ordered situations


    def _findSituationsContainingParameter(self, parameter):
        for situation in self.situations:
            if parameter.name in map( lambda assignment: assignment.name, situation.assignments):
                yield situation


    # Finds all situations covered by a test
    def _findSituationsCoveredByTest(self, test):
        for situation in self.situations:
            if situation.isCoveredByTest(test):
                yield situation


    def _countSituationsCoveredByTest(self, test):
        situations = list(self._findSituationsCoveredByTest(test))
        return len(situations)

    # Removes situations covered by the test from the list of situations that still need to be covered
    def _removeSituationsCoveredByTest(self, test):
        # TODO: This will not work for situations where some orders are not allowed
        for situation in self.situations:
            if situation.isCoveredByTest(test):
                self.coveredSituations.append(situation)
                self.situations.remove(situation)


    def _makePossibleModificationsOfTestWithNewParameter(self, test, parameter):
        assert(parameter.name not in map( lambda step: step.name, test.steps))
        for parameterValue in parameter.values:
            localTest = Test(test.steps)
            newAssignment = ParameterAssignment(parameter.name, parameterValue)
            localTest.addStep(newAssignment)
            yield localTest


    def _findValueWithMaximumCoverageForTest(self, test, parameter):
        assert(parameter.name not in map( lambda step: step.name, test.steps))
        return max(self._makePossibleModificationsOfTestWithNewParameter(test, parameter), key=self._countSituationsCoveredByTest)

