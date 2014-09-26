__author__ = 'Austin Havens'

import pytest
from IPOGenerator import IPOGenerator

from Parameter import Parameter
from SituationGenerator import SituationGenerator

def checkGeneratedTestsForSituation(generator, situation):
    pass

def verifyPairIsInSituationsList(situations, paramOneName, paramOneValue, paramTwoName, paramTwoValue):
    for situation in situations:
        paramOneMatched = any(map(lambda assignment: (assignment.name == paramOneName) and (assignment.value == paramOneValue), situation.assignments))
        paramTwoMatched = any(map(lambda assignment: (assignment.name == paramTwoName) and (assignment.value == paramTwoValue), situation.assignments))
        if paramOneMatched and paramTwoMatched:
            return True

def verifyPairIsInATest(generator, paramOneName, paramOneValue, paramTwoName, paramTwoValue):
    for test in generator.tests:
        paramOneMatched = any(map(lambda step: (step.name == paramOneName) and (step.value == paramOneValue), test.steps))
        paramTwoMatched = any(map(lambda step: (step.name == paramTwoName) and (step.value == paramTwoValue), test.steps))
        if paramOneMatched and paramTwoMatched:
            return True

def test_pairwiseTestGeneration():
    parameterOne = Parameter('param1', ['P1V1', 'P1V2'])
    parameterTwo = Parameter('param2', ['P2V1', 'P2V2', 'P2V3'])
    parameterThree = Parameter('param3', ['P3V1', 'P3V2'])
    parameters = [parameterOne, parameterTwo, parameterThree]

    situationGenerator = SituationGenerator(2, parameters)
    situations = list(situationGenerator.generatePairwiseSituations())
    assert len(situations) == 16


# check situations
    assert(verifyPairIsInSituationsList(situations,"param1", "P1V1", "param2", "P2V1"))
    assert(verifyPairIsInSituationsList(situations,"param1", "P1V1", "param2", "P2V2"))
    assert(verifyPairIsInSituationsList(situations,"param1", "P1V1", "param2", "P2V3"))
    assert(verifyPairIsInSituationsList(situations,"param1", "P1V1", "param3", "P3V1"))
    assert(verifyPairIsInSituationsList(situations,"param1", "P1V1", "param3", "P3V2"))
    assert(verifyPairIsInSituationsList(situations,"param1", "P1V2", "param2", "P2V1"))
    assert(verifyPairIsInSituationsList(situations,"param1", "P1V2", "param2", "P2V2"))
    assert(verifyPairIsInSituationsList(situations,"param1", "P1V2", "param2", "P2V3"))
    assert(verifyPairIsInSituationsList(situations,"param1", "P1V2", "param3", "P3V1"))
    assert(verifyPairIsInSituationsList(situations,"param1", "P1V2", "param3", "P3V2"))
    assert(verifyPairIsInSituationsList(situations,"param2", "P2V1", "param3", "P3V1"))
    assert(verifyPairIsInSituationsList(situations,"param2", "P2V1", "param3", "P3V2"))
    assert(verifyPairIsInSituationsList(situations,"param2", "P2V2", "param3", "P3V1"))
    assert(verifyPairIsInSituationsList(situations,"param2", "P2V2", "param3", "P3V2"))
    assert(verifyPairIsInSituationsList(situations,"param2", "P2V3", "param3", "P3V1"))
    assert(verifyPairIsInSituationsList(situations,"param2", "P2V3", "param3", "P3V2"))

    generator = IPOGenerator( 2, situations)

    generator.generate(parameters)
    # check tests
    assert(verifyPairIsInATest(generator,"param1", "P1V1", "param2", "P2V1"))
    assert(verifyPairIsInATest(generator,"param1", "P1V1", "param2", "P2V2"))
    assert(verifyPairIsInATest(generator,"param1", "P1V1", "param2", "P2V3"))
    assert(verifyPairIsInATest(generator,"param1", "P1V1", "param3", "P3V1"))
    assert(verifyPairIsInATest(generator,"param1", "P1V1", "param3", "P3V2"))
    assert(verifyPairIsInATest(generator,"param1", "P1V2", "param2", "P2V1"))
    assert(verifyPairIsInATest(generator,"param1", "P1V2", "param2", "P2V2"))
    assert(verifyPairIsInATest(generator,"param1", "P1V2", "param2", "P2V3"))
    assert(verifyPairIsInATest(generator,"param1", "P1V2", "param3", "P3V1"))
    assert(verifyPairIsInATest(generator,"param1", "P1V2", "param3", "P3V2"))
    assert(verifyPairIsInATest(generator,"param2", "P2V1", "param3", "P3V1"))
    assert(verifyPairIsInATest(generator,"param2", "P2V1", "param3", "P3V2"))
    assert(verifyPairIsInATest(generator,"param2", "P2V2", "param3", "P3V1"))
    assert(verifyPairIsInATest(generator,"param2", "P2V2", "param3", "P3V2"))
    assert(verifyPairIsInATest(generator,"param2", "P2V3", "param3", "P3V1"))
    assert(verifyPairIsInATest(generator,"param2", "P2V3", "param3", "P3V2"))

    numberOfTests = len(generator.tests)
    print(str(numberOfTests) + ' tests generated')
    assert(numberOfTests == 10)





