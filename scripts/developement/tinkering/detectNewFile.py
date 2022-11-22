import time

watchDirectory = "C:/Users/vince/Desktop/open-just-dance/FrameData/webcam"
pollTime = 1


def main():
    fileWatcher(watchDirectory, pollTime)
from os import listdir
from os.path import isfile, join

#function to return files in a directory
def fileInDirectory(my_dir: str):
    onlyfiles = [f for f in listdir(my_dir) if isfile(join(my_dir, f))]
    return(onlyfiles)

#function comparing two lists

def listComparison(OriginalList: list, NewList: list):
    differencesList = [x for x in NewList if x not in OriginalList] #Note if files get deleted, this will not highlight them
    return(differencesList)

def doThingsWithNewFiles(newFiles: list):
    # read and delete the file
    print()


def fileWatcher(my_dir: str, pollTime: int):
    while True:
        if 'watching' not in locals(): #Check if this is the first time the function has run
            previousFileList = fileInDirectory(watchDirectory)
            watching = 1
        
        time.sleep(pollTime)
        
        newFileList = fileInDirectory(watchDirectory)
        
        fileDiff = listComparison(previousFileList, newFileList)
        
        previousFileList = newFileList
        if len(fileDiff) == 0: continue
        doThingsWithNewFiles(fileDiff)

if __name__ == "__main__":
    main()