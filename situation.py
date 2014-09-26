__author__ = 'Austin Havens'

class UnorderedSituation:

    def __init__(self, assignments):
        self.assignments = assignments


    def isCoveredByTest(self, test):
        for requiredAssignment in self.assignments :
            currentAssignmentCovered = False
            for coveredAssignment in test :
                if (requiredAssignment.name == coveredAssignment.name) & (requiredAssignment.value == coveredAssignment.value):
                    currentAssignmentCovered = True
                    break

            if not currentAssignmentCovered:
                return False

        return True

    def canExtendTest(self, test):
        pass


    def extendTest(self, test):
        pass



class OrderedSituation:

    def __init__(self):
        pass

    def isCoveredByTest(self, test):
        return False