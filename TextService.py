import re


def ClearTextByTrash(list):
    result = []
    for el in list:
        lastIndex = el.rindex("\n")
        if not str.startswith(el, "Feature") and not str.startswith(el, "@") and not str.startswith(el, "#"):
            el = "@" + el
        result.append(el[0:lastIndex])
    return result


def MoveTagsToExamples(scenarios):
    result = []
    for scenario in scenarios:
        if not IsScenarioWithExamples(scenario) or str.startswith(scenario, "Feature"):
            result.append(scenario)
            continue
        tests = scenario.split("\n")
        tagsLine = None
        examplesHeaderLine = None
        testResultList = []
        findExamplesString = False
        for test in tests:
            if str.startswith(test, "@"):
                tagsLine = test
                continue
            if test.strip().startswith("Examples:"):
                testResultList.extend([tagsLine, test])
                findExamplesString = True
                continue
            if findExamplesString and examplesHeaderLine is None:
                testResultList.append(test)
                examplesHeaderLine = test
                continue
            if findExamplesString:
                testResultList.append(test)
                findExamplesString = False
                continue
            if findExamplesString is False and examplesHeaderLine is not None:
                testResultList.extend(["\n", tagsLine, "Examples:", examplesHeaderLine, test])
                continue
            testResultList.append(test)
        result.append(testResultList)
    return result


def IsScenarioWithExamples(scenario):
    if str.__contains__(scenario, "Scenario Outline:"):
        return True
    return False
