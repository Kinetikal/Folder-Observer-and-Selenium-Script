import time
from os import listdir
from os.path import isfile, join

pollTime = 3
watchDirectory = "ENTER A PATH HERE"

# ---- Function to Return the files in a direcotry ---- #
def fileInDirectory(watchingPath: str):
    excelFile = [f for f in listdir(watchingPath) if isfile(join(watchingPath,f))]
    return(excelFile)

# ---- Function for Comparing two lists ---- #

def listComparison(originalList: list, newList: list):
    differencesList = [x for x in newList if x not in originalList] #Note if files get deleted, this will not highlight them
    return(differencesList)

def doThingsWithNewFiles(newFiles: list):
    
    global ticket_field_name
    global filename_without_extension
    global filename_with_extension
    
    filename_with_extension = newFiles[0]
    filename_without_extension = newFiles[0].split(".")[0]
    ticket_field_name = "[Ticket#" + filename_without_extension + "]"
    
    print(f">>>The Ticket Field is filled with: {ticket_field_name}")
    print(f">>>Filename with Extension: {filename_with_extension}")

def fileWatcher(watchingPath: str, pollTime: int):
    
    while True:
        if "watching" not in locals():
            previousFileList = fileInDirectory(watchDirectory)
            watching = 1
            
        time.sleep(pollTime)
        
        newFileList = fileInDirectory(watchDirectory)
        
        fileDiff = listComparison(previousFileList, newFileList)
        
        previousFileList = newFileList
        if len(fileDiff) == 0: continue
        doThingsWithNewFiles(fileDiff)

fileWatcher(watchDirectory, pollTime)