from TestSetGeneration import IPOGenerator, Parameter, SituationGenerator

__author__ = 'Austin Havens'


def exampleOne():
    parameterOne = Parameter('param1', ['p1v1', 'p1v2'])
    parameterTwo = Parameter('param2', ['p2v1', 'p2v2', 'p2v3'])
    parameterThree = Parameter('param3', ['p3v1', 'p3v2'])
    parameters = [parameterOne, parameterTwo, parameterThree]

    situationGenerator = SituationGenerator(2, parameters)
    situations = list(situationGenerator.generatePairwiseSituations())

    generator = IPOGenerator( 2, situations)

    generator.generate(parameters)
    printTestsInGenerator(generator)


def printTestsInGenerator(generator):
    testIndex = 1
    for test in generator.tests:
        print('\nTest number ' + str(testIndex))
        testIndex = testIndex +1
        for step in test.steps:
            print(step.name + ': ' + step.value )

exampleOne()