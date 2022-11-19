import os
from functools import lru_cache
import json
import numpy as np
import time
import os
from glob import glob
def main():
   
    # --- runtime start --- #
    starttime = time.time()

    # --- variables --- #

    # path to json files
    output_dir: str = "C:/Users/vince/Desktop/open-just-dance/output/single"
    # list of strings containing the file location of each json file
    jsonfiles: str = readPaths(output_dir)
    # list with body parts
    bodyParts: list[str] = ["Nose", "Neck", "RShoulder", "RElbow", "RWrist", "LShoulder", "LElbow", "LWrist", "MidHip", "RHip", "RKnee", "RAnkle", "LHip", "LKnee", "LAnkle", "REye", "LEye", "REar", "LEar", "LBigToe", "LSmallToe", "LHeel", "RBigToe", "RSmallToe", "RHeel", "Background"]
    
    skeletonPoints = returnListofTuples(jsonfiles,0)
    # lists that contain two points that are in relation to each other 
    # (e.g. Neck and RShoulder/Neck and LShoulder) --> [(x1,y1),(x2,y2)]
    L_0_1: list = [skeletonPoints[0], skeletonPoints[1]]
    L_0_15: list = [skeletonPoints[0], skeletonPoints[15]]
    L_0_16: list = [skeletonPoints[0], skeletonPoints[16]]
    L_15_17: list = [skeletonPoints[15], skeletonPoints[17]]
    L_16_18: list = [skeletonPoints[16], skeletonPoints[18]]
    L_1_2: list = [skeletonPoints[1], skeletonPoints[2]]
    L_1_5: list = [skeletonPoints[1], skeletonPoints[5]]
    L_2_3: list = [skeletonPoints[2], skeletonPoints[3]]
    L_3_4: list = [skeletonPoints[3], skeletonPoints[4]]
    L_5_6: list = [skeletonPoints[5], skeletonPoints[6]]
    L_6_7: list = [skeletonPoints[6], skeletonPoints[7]]
    L_8_9: list = [skeletonPoints[8], skeletonPoints[9]]
    L_8_12: list = [skeletonPoints[8], skeletonPoints[12]]
    L_9_10: list = [skeletonPoints[9], skeletonPoints[10]]
    L_10_11: list = [skeletonPoints[10], skeletonPoints[11]]
    L_12_13: list = [skeletonPoints[12], skeletonPoints[13]]
    L_13_14: list = [skeletonPoints[13], skeletonPoints[14]]
    L_11_24: list = [skeletonPoints[11], skeletonPoints[24]]
    L_11_22: list = [skeletonPoints[11], skeletonPoints[22]]
    L_22_23: list = [skeletonPoints[22], skeletonPoints[23]]
    L_14_19: list = [skeletonPoints[14], skeletonPoints[19]]
    L_14_21: list = [skeletonPoints[14], skeletonPoints[21]]
    L_19_20: list = [skeletonPoints[19], skeletonPoints[20]]
    L_1_8: list = [skeletonPoints[1], skeletonPoints[8]]
    
    # list of all lists
    pointsRelationList: list[list] = [L_0_1, L_0_15, L_0_16, L_15_17, L_16_18, L_1_2, L_1_5, L_2_3, L_3_4, 
    L_5_6, L_6_7, L_8_9, L_8_12, L_9_10, L_10_11, L_12_13, L_13_14, 
    L_11_24, L_11_22, L_22_23, L_14_19, L_14_21, L_19_20, L_1_8]

    # --- DEBUGGING --- #

    # print all body parts and their coordinates
    # print(printBodyPartsAndCoordinatesForDebuggingForOneFile(jsonfiles, 0))
    
    # prints lists of all slopes for every line
    # print(returnSlopes(pointsRelationList))

    # prints list of all angles (in degrees)
    print(returnAngles(returnSlopes(pointsRelationList)))

    # --- runtime end --- #
    endtime = time.time()
    elapsed_time = endtime - starttime
    print(f'Execution time: {elapsed_time:.2} seconds')

# --- functions --- #

@lru_cache(maxsize=None)
def readPaths(filepath: str) -> list: return glob(f"{filepath}/*.json")

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

# calculates angles of two lines by using the slope of the lines and calculating the arctan
def calculateAngle(m1: np.float64, m2: np.float64, body_id:int) -> (np.float64 | None):

    angle_bg = np.arctan((m1 - m2) / (1+m1*m2))
    angle_gr = 180 - np.degrees(angle_bg)

    # contains body parts that need to be flipped (because of the way the angle is calculated)
    WARN_LIST: list = [2, 5]
    if body_id in WARN_LIST: 
        angle_gr = 360 - angle_gr

    # we dont want angles that are bigger than 180° so we take the smaller one (180° - angle)
    else:
        if angle_gr >  180: angle_gr = angle_gr - 180

    return np.round_(angle_gr, decimals=2)

# calculates the slope of two points by using the formula: m = (y2-y1)/(x2-x1)
def calculateSlope(x1: np.float64, y1: np.float64, x2: np.float64, y2: np.float64) -> np.float64: 
    return np.round_((y2 - y1) / (x2 - x1), decimals=2)

# only for debugging
def printBodyPartsAndCoordinatesForDebuggingForOneFile(jsonfiles, index):
    parts: list[str] = ["Nose", "Neck", "RShoulder", "RElbow", "RWrist", 
    "LShoulder", "LElbow", "LWrist", "MidHip", "RHip", "RKnee", "RAnkle", 
    "LHip", "LKnee", "LAnkle", "REye", "LEye", "REar", "LEar", "LBigToe", 
    "LSmallToe", "LHeel", "RBigToe", "RSmallToe", "RHeel", "Background"]

    print("\n--- body parts and their coordinates ---")
    for count, coordinates in enumerate(returnListofTuples(jsonfiles, index)): 
        print(f'{count}. {parts[count]}: {coordinates}')

# returns list of slopes --> [m1, m2, m3, ...] input: pointsRelationList
def returnSlopes(listofpoints):
    # calculate slopes
    slopes: list[np.float64] = [calculateSlope(listofpoints[c][0][0], listofpoints[c][0][1], listofpoints[c][1][0], listofpoints[c][1][1]) for c in range(0, len(listofpoints))]

    # print all slopes for debugging
    # print(f"\n--- SLOPES ---\n{slopes}")

    return slopes
    
# returns list of angles --> [a1, a2, a3, ...] input: SLOPES
def returnAngles(listOfSlopes):
    BODY: np.float64 = calculateAngle(listOfSlopes[0], listOfSlopes[23], 0)
    ARM_RIGHT: np.float64 = calculateAngle(listOfSlopes[7], listOfSlopes[8], 1)
    ARM_LEFT: np.float64 = calculateAngle(listOfSlopes[9], listOfSlopes[10], 2)
    SHOULDER_RIGHT: np.float64 = calculateAngle(listOfSlopes[5], listOfSlopes[7] ,3)
    SHOULDER_LEFT: np.float64 = calculateAngle(listOfSlopes[6], listOfSlopes[9], 4)
    LEG_RIGHT: np.float64 = calculateAngle(listOfSlopes[13], listOfSlopes[14], 5)
    LEG_LEFT: np.float64 = calculateAngle(listOfSlopes[15], listOfSlopes[16], 6)
    HIP_RIGHT: np.float64 = calculateAngle(listOfSlopes[11], listOfSlopes[13], 7)
    HIP_LEFT: np.float64 = calculateAngle(listOfSlopes[12], listOfSlopes[15], 8)

    listOfAngles = [BODY, ARM_RIGHT, ARM_LEFT, SHOULDER_RIGHT, SHOULDER_LEFT, LEG_RIGHT, LEG_LEFT, HIP_RIGHT, HIP_LEFT]

    # print all angles for debugging

    # print("\n--- ANGELS ---")
    # print(f"BODY: {BODY}°")
    # print(f"ARM_RIGHT: {ARM_RIGHT}°")
    # print(f"ARM_LEFT: {ARM_LEFT}°")
    # print(f"SHOULDER_RIGHT: {SHOULDER_RIGHT}°")
    # print(f"SHOULDER_LEFT: {SHOULDER_LEFT}°")
    # print(f"LEG_RIGHT: {LEG_RIGHT}°")
    # print(f"LEG_LEFT: {LEG_LEFT}°")
    # print(f"HIP_RIGHT: {HIP_RIGHT}°")
    # print(f"HIP_LEFT: {HIP_LEFT}°")

    return listOfAngles

if __name__ == "__main__":
    main()