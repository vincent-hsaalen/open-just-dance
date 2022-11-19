import os
from functools import lru_cache
import json
import time

def main():

    # runtime start
    starttime = time.time()

    # variables
    output_dir:str = "C:/Users/vince/Desktop/open-just-dance/output/choreographies/dance"
    jsonfiles = readPaths(output_dir)

    print(len(returnAllKeyPointsOfChoreography(jsonfiles)))

    endtime = time.time()
    elapsed_time = endtime - starttime
    print('Execution time:', elapsed_time, 'seconds')


   


# function to get all the files in the directory ()
@lru_cache(maxsize=None)
def readPaths(filepath:str) -> list: return [os.path.join(filepath, file) for file in os.listdir(filepath)]

def returnListofTuples(file,x) -> list:
    with open(file[x]) as f:
        data = json.load(f)
    posekeypoints = data["people"][0]["pose_keypoints_2d"]

    del posekeypoints[2::3]
   
    # listoftuples = []
    # for i in range(0, len(posekeypoints), 2):
    #     listoftuples.append((posekeypoints[i], posekeypoints[i+1]))

    listoftuples: list = [(posekeypoints[i], posekeypoints[i+1]) for i in range(0, len(posekeypoints), 2)]
    return listoftuples

def returnAllKeyPointsOfChoreography(file):
    keypoint = []

    for x in range(0, len(file)):
        a = returnListofTuples(file,x)
        keypoint.append(a)
    return keypoint

if __name__ == "__main__":
    main()


