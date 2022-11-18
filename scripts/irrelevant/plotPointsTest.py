import os
from functools import lru_cache
import json
import matplotlib.pyplot as plt
import time

def main():

    # runtime start
    starttime = time.time()

    # variables
    output_dir:str = "C:/Users/vince/Desktop/open-just-dance/output/choreographies/dance"
    jsonfiles = readPaths(output_dir)
    listwithparts = ["Nose", "Neck", "RShoulder", "RElbow", "RWrist", "LShoulder", "LElbow", "LWrist", "MidHip", "RHip", "RKnee", "RAnkle", "LHip", "LKnee", "LAnkle", "REye", "LEye", "REar", "LEar", "LBigToe", "LSmallToe", "LHeel", "RBigToe", "RSmallToe", "RHeel", "Background"]
    count=0
    for coordinates in returnAllKeyPointsOfChoreography(jsonfiles)[84]: 
        
        # prints all coordinates from BODY_25
        # print(f'{count}. {listwithparts[count]}: {coordinates}')
        count+=1

    # 22 single function calls

    # von 0 zu 1
    # von 1 zu 8 
   
    # von 1 zu 2
    # von 1 zu 5
    # von 2 zu 3
    # von 3 zu 4
    # von 5 zu 6
    # von 6 zu 7
    # von 8 zu 9
    # von 8 zu 12
    # von 9 zu 10
    # von 10 zu 11
    # von 12 zu 13

    plotPointsasLine(listwithparts[0], listwithparts[1])
    plotPointsasLine(listwithparts[1], listwithparts[8])
    plotPointsasLine(listwithparts[1], listwithparts[2])
    plotPointsasLine(listwithparts[1], listwithparts[5])

    
    plt.show()

    # reference = returnAllKeyPointsOfChoreography(jsonfiles)[0]
    # print(len(reference))

    endtime = time.time()
    elapsed_time = endtime - starttime
    print('Execution time:', elapsed_time, 'seconds')

def plotPointsasLine(point_1, point_2):
    x_values = [point_1[0], point_2[0]]
    y_values = [point_1[1], point_2[1]]
    plt.plot(x_values, y_values)

# function to get all the files in the directory ()
@lru_cache(maxsize=None)
def readPaths(filepath:str) -> list: return [os.path.join(filepath, file) for file in os.listdir(filepath)]

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

def printcoordinates():
    print("nothing")

if __name__ == "__main__":
    main()

