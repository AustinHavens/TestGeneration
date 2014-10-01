__author__ = 'Austin Havens'
import os
from TestSetGeneration.IPOGenerator import IPOGenerator
from TestSetGeneration.ParameterAssignment import ParameterAssignment

testOutputFileLocation = '../generatedTests.py'

def generateLineFromScpiAssignment(assignment):
    scpiWrite = '    dut._connection.sendWriteCommand('
    command = '"' + assignment.name + ' '
    value = str(assignment.value) + '")\n'
    return scpiWrite + command + value


def generateCodeForTest(test, testIndex):
    testCode = 'def test_' +str(testIndex) + '(dut):\n'

    for assignment in test.steps:
        testCode += generateLineFromScpiAssignment(assignment)

    # Give some time for sweeps to happen
    testCode += '    time.sleep(2)\n'

    # TODO: improve the pass/fail check
    testCode += '    dut._connection.sendQueryCommand("*idn?")\n'

    testCode += "\n\n"
    return testCode


def generateTestFile(generator):
    file = open(testOutputFileLocation, 'w')

    testIndex = 0
    for test in generator.tests:
        testIndex += 1
        testCode = generateCodeForTest(test, testIndex)
        file.write(testCode)