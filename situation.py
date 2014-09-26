__author__ = 'Austin Havens'

class UnorderedSituation:

    def __init__(self, assignments):
        self.assignments = assignments


    def IsCoveredByTest(self, test):
        for requiredAssignment in self.assignments :
            currentAssignmentCovered = False
            for coveredAssignment in test :
                if (requiredAssignment.name == coveredAssignment.name) & (requiredAssignment.value == coveredAssignment.value):
                    currentAssignmentCovered = True
                    break

            if not currentAssignmentCovered:
                return False

        return True



class OrderedSituation:

    def __init__(self):
        pass

    def IsCoveredByTest(self, test):
        return False