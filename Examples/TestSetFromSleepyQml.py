__author__ = 'Austin Havens'

from InputParsers import SleepySettingsQmlParser
from TestSetGeneration.SituationGenerator import SituationGenerator
from TestSetGeneration.IPOGenerator import IPOGenerator
from Examples import printTestsInGenerator

parameters = SleepySettingsQmlParser.processFile()
situationGenerator = SituationGenerator(2, parameters)

situations = list(situationGenerator.generatePairwiseSituations())

testGenerator = IPOGenerator(situations)

testGenerator.generate(parameters)

printTestsInGenerator(testGenerator)