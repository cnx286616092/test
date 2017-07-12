import os
import sys
import re
import sysconfig


class SpecUtil(object):
    def __init__(self, templatePath):
        self.fileContent = ''
        self.signalVariableParten = r"\{\{\s*(\w+)\s*\}\}"
        try:
            with open(templatePath, "r") as f:
                self.fileContent = f.read()
        except IOError as e:
            print e
            exit(1)

    def _getVariableFromTemplate(self):
        totalVariableList = re.findall(self.signalVariableParten, self.fileContent)

        return list(set(totalVariableList))

    def getVList(self):
        return self._getVariableFromTemplate()

    def setValue(self, variableList, variableValuesDict):
        if variableList.sort() != variableValuesDict.keys().sort():
            print "ERROR"
            return False

        for name in variableList:
            needRep = r"\{\{\s*%s\s*\}\}" % name
            self.fileContent = re.sub(needRep, variableValuesDict[name], self.fileContent)

        return True




filePath = r"D://test.txt"

ttt = {
    'aaa': '11111',
    'bbb': '22222',
    'ccc': '33333'
}
n = SpecUtil(filePath)
lll = n.getVList()
print lll
n.setValue(lll, ttt)
print n.fileContent



