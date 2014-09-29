__author__ = 'Austin Havens'

from TestSetGeneration.IPOGenerator import IPOGenerator
from TestSetGeneration.Parameter import Parameter
from TestSetGeneration.SituationGenerator import SituationGenerator


def exampleOne():
    parameterOne = Parameter('param1', ['p1v1', 'p1v2'])
    parameterTwo = Parameter('param2', ['p2v1', 'p2v2', 'p2v3'])
    parameterThree = Parameter('param3', ['p3v1', 'p3v2'])
    parameters = [parameterOne, parameterTwo, parameterThree]

    situationGenerator = SituationGenerator(2, parameters)
    situations = list(situationGenerator.generatePairwiseSituations())

    generator = IPOGenerator( situations)

    generator.generate(parameters)
    printTestsInGenerator(generator)


def printTestsInGenerator(generator):
    testIndex = 1
    for test in generator.tests:
        print('\nTest number ' + str(testIndex))
        testIndex += 1
        for step in test.steps:
            print(step.name + ': ' + str(step.value))


if __name__ == "__main__":
    exampleOne()