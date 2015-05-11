__author__ = 'Austin Havens'

from InputParsers import SleepySettingsQmlParser
from TestSetGeneration.SituationGenerator import SituationGenerator
from TestSetGeneration.IPOGenerator import IPOGenerator
from Examples import printTestsInGenerator
from TestCodeGeneration import BugPyScpiTestCodeGenerator

def analyzeCoverage(testGenerator, situations):
    for situation in situations:
        for test in testGenerator.tests:
            if situation.isCoveredByTest(test):
                test.addNewSituationCovered(situation)
                break


parameters = SleepySettingsQmlParser.processFile()


situationGenerator = SituationGenerator(2, parameters)

situations = list(situationGenerator.generatePairwiseSituations())

print len(situations)
copySituations = []
for situation in situations:
    copySituations.append(situation)

testGenerator = IPOGenerator(situations)

testGenerator.generate(parameters)

#printTestsInGenerator(testGenerator)
print len(copySituations)
analyzeCoverage(testGenerator, copySituations)
BugPyScpiTestCodeGenerator.generateTestFile(testGenerator)

