import os
import pathlib


def GetFilesFromDirectoryWithExtention(path, extension):
    filesList = []
    for path, subdirs, files in os.walk(path):
        for name in files:
            if extension == "" or pathlib.Path(name).suffix == extension:
                filesList.append(os.path.join(path, name))
    return filesList



