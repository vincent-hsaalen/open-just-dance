import os
from functools import lru_cache
import json
import time

def main():

    # runtime start
    starttime = time.time()

    # variables #

    # path to json files
    jsonDirectory = "C:/Users/vince/Desktop/open-just-dance/output/choreographies/dance"
    # list of strings containing the file location of each json file
    jsonFiles = readPaths(jsonDirectory)
    # total number of json files
    totalFiles = len(jsonFiles)

    inhalt = len(returnTotalKeyPoints(jsonFiles))

    # runtime end
    endtime = time.time()
    elapsed_time = endtime - starttime
    print(f'Runtime: {elapsed_time} seconds')


   


# get all  files in directory
@lru_cache(maxsize=None)
def readPaths(filepath): return [os.path.join(filepath, file) for file in os.listdir(filepath)]

# return list of key points (as tuples[x,y]) from json file at index and filters confidence values
def returnListofTuples(file,index):

    # list that will contain all the key x,y and c values for one file
    listoftuples = []
    # open json file at index and fully read it
    with open(file[index]) as jsonFile:
        data = json.load(jsonFile)

    # get ONLY the keypoints from the json file
    keyPoints = data["people"][0]["pose_keypoints_2d"]

    # delete the c (confidence) values from list
    del keyPoints[2::3]
   
   # create a list of tuples with the x,y values
   # --> [(x1,y1),(x2,y2),(x3,y3),...]
    for i in range(0, len(keyPoints), 2):
        listoftuples.append((keyPoints[i], keyPoints[i+1]))

    return listoftuples

# returns a list with total key points (as tuples[x,y]) for each file/frame
def returnTotalKeyPoints(listofjsonfiles):
    keyPointList = []
    for count, data in enumerate(listofjsonfiles):
        keyPointList.append(returnListofTuples(listofjsonfiles, count))
        # print(f'File {count} of {totalJsonFiles} done')
        # print(f'Data: {data}')
    # print(f'keyPointList: {keyPointList[0]}')
    # print(f'keyPointList: {keyPointList[60]}')
    return keyPointList

if __name__ == "__main__":
    main()


