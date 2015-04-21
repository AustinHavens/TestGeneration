__author__ = 'Austin Havens'

from TestSetGeneration.Parameter import Parameter
from FrequencyParameter import FrequencyParameter

sleepyQmlSettingFileLocation = '../../superg/framework/src/application/spa/spacommands.qml'

# TODO: These can be parsed out and created using eval() instead of hardcoded
startFrequency = FrequencyParameter(100000, 3000000000, 100000)
stopFrequency = FrequencyParameter(100000, 3000000000, 3000000000)
span = FrequencyParameter(10,6000000000, 6000000000 )

replaceList = {"Infinity" : "float(\"inf\")", "NaN" : "float(\"nan\")", "false": "str(\"false\")"}

def getValueFromLine(line):
    # remove inline comments
    # remove square brackets
    content = line.split('//')[0].translate(None, '][')
    trimed= content.split(': ')[1].strip('\r\n" ')
    return reduce(lambda a, kv: a.replace(*kv), replaceList.iteritems(), trimed)


def getEvaluatedValueFromLine(line):
    lineValue = getValueFromLine(line)
    return eval(lineValue)


def parse(file):
    parameters = list()
    inSettingBlock = False
    currentSettingScpiCommand = ''
    currentSettingValues = list()

    for line in file:
        if '{' in line:
            # new setting
            currentSettingScpiCommand = ''
            currentSettingValues = list()
            inSettingBlock = True

        if '}' in line:
            # done with setting
            inSettingBlock = False
            settingValues = list(set(currentSettingValues))
            if len(settingValues) >0:
                if currentSettingScpiCommand.find("DEBug:")==-1:
                    parameters.append(Parameter(currentSettingScpiCommand, settingValues))

        if inSettingBlock and ('commandString:' in line):
            # parsing SCPI command line
            localValue = getValueFromLine(line)
            #get rid of optional stuff with |
            splits = localValue.split(':')
            recombine = ""
            for split in splits:
                recombine += ':'+split.split('|')[0]
            currentSettingScpiCommand = recombine.lstrip(':')

        if inSettingBlock and ('minValue:' in line):
            # parsing a hopefully numeric value line
            currentSettingValues.append(getEvaluatedValueFromLine(line))

        if inSettingBlock and ('maxValue:' in line):
            # parsing a hopefully numeric value line
            currentSettingValues.append(getEvaluatedValueFromLine(line))

        if inSettingBlock and ('defaultValue:' in line):
            # parsing a hopefully numeric value line
            currentSettingValues.append(getEvaluatedValueFromLine(line))

        if inSettingBlock and ('valueNames:' in line):
            # parsing and enum setting
            validValues = getValueFromLine(line)
            for value in validValues.split('|'):
                currentSettingValues.append(value)

    return parameters


def printParameters(parameters):
    for parameter in parameters:
        print('\nParameter: ' + parameter.name)
        for value in parameter.values:
            print value


def processFile():
    qmlFile = open(sleepyQmlSettingFileLocation, 'r')
    parameters = parse(qmlFile)
    return parameters
    printParameters(parameters)

def evaluateFile():
    qmlFile = open(sleepyQmlSettingFileLocation, 'r')
    parameters = parse(qmlFile)
    printParameters(parameters)

if __name__ == "__main__":
    evaluateFile()