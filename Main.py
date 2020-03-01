import os
import pathlib
import DirectoryService
import TextService

mainPath = "D:\\Browsers Download\\"
extension = ".txt"
fileList = DirectoryService.GetFilesFromDirectoryWithExtention(mainPath, extension)
res = []
for file in fileList:
    openedFile = open(file, "r+")
    scenariosList = TextService.ClearTextByTrash(openedFile.read().split('\n@'))
    openedFile.seek(0)
    result = TextService.MoveTagsToExamples(scenariosList)
    for el in result:
        if type(el) is list:
            for let in el:
                openedFile.write(let)
                openedFile.write("\n")

        else:
            openedFile.write(el)
        openedFile.write("\n\n")
