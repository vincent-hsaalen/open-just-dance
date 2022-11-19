from glob import glob
from functools import lru_cache
import json
from time import time as ttime

# lists all key Pose Names from listwithparts and matches them with the coordinates

def main():

    # runtime start
    starttime = ttime()

    # variables
    output_dir:str = "C:/Users/vince/Desktop/open-just-dance/output/choreographies/dance"
    jsonfiles = readPaths(output_dir)
    listwithparts = ["Nose", "Neck", "RShoulder", "RElbow", "RWrist", "LShoulder", "LElbow", "LWrist", "MidHip", "RHip", "RKnee", "RAnkle", "LHip", "LKnee", "LAnkle", "REye", "LEye", "REar", "LEar", "LBigToe", "LSmallToe", "LHeel", "RBigToe", "RSmallToe", "RHeel", "Background"]
    count=0
    for coordinates in returnAllKeyPointsOfChoreography(jsonfiles)[0]: 
        
        print(f'{count}. {listwithparts[count]}: {coordinates}')
        count+=1

    # reference = returnAllKeyPointsOfChoreography(jsonfiles)[0]
    # print(len(reference))

    endtime = ttime()
    elapsed_time = endtime - starttime
    print('Execution time:', elapsed_time, 'seconds')

    
# function to get all the files in the directory ()
@lru_cache(maxsize=None)
def readPaths(filepath: str) -> list: return glob(f"{filepath}/*.json")

def returnListofTuples(file,x):
    with open(file[x]) as f:
        data = json.load(f)
    posekeypoints = data["people"][0]["pose_keypoints_2d"]
    n = 3
    del posekeypoints[n-1::n]
   
    listoftuples = []
    for i in range(0, len(posekeypoints), 2):
        listoftuples.append((posekeypoints[i], posekeypoints[i+1]))
    return listoftuples

def returnAllKeyPointsOfChoreography(file):
    keypoint = []

    for x in range(0, len(file)):
        a = returnListofTuples(file,x)
        keypoint.append(a)
    return keypoint

if __name__ == "__main__":
    main()


