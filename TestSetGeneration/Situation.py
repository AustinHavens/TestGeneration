__author__ = 'Austin Havens'

class UnorderedSituation:

    def __init__(self, assignments):
        self.assignments = assignments


    def isCoveredByTest(self, test):
        for requiredAssignment in self.assignments :
            currentAssignmentCovered = False
            for coveredAssignment in test.steps :
                if (requiredAssignment.name == coveredAssignment.name) and (requiredAssignment.value == coveredAssignment.value):
                    currentAssignmentCovered = True
                    break

            if not currentAssignmentCovered:
                return False

        return True


    # Returns True if the test was extended
    def extendTest(self, test):
        tentativeAssignments = set()
        for assignment in self.assignments:
            #push the assignment
            tentativeAssignments.add(assignment)
            for step in test.steps:
                if assignment.name == step.name:
                    # The test already has the value
                    if assignment.value != step.value:
                        # The test has a different value for the assignment so it cannot be extended
                        return False
                    else:
                        # This assignment is already in the test so remove it from the list of tentative new assignments
                        tentativeAssignments.discard(assignment)
                        break

        for newAssignment in tentativeAssignments:
            test.addStep(newAssignment)

        return True


class OrderedSituation:

    def __init__(self):
        pass

    def isCoveredByTest(self, test):
        return False