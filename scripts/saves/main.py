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
    
    POINT_CHEO = returnAllKeyPointsOfChoreography(jsonfiles)[0]
    L_0_1: list = [POINT_CHEO[0], POINT_CHEO[1]]
    L_0_15: list = [POINT_CHEO[0], POINT_CHEO[15]]
    L_0_16: list = [POINT_CHEO[0], POINT_CHEO[16]]
    L_15_17: list = [POINT_CHEO[15], POINT_CHEO[17]]
    L_16_18: list = [POINT_CHEO[16], POINT_CHEO[18]]
    L_1_2: list = [POINT_CHEO[1], POINT_CHEO[2]]
    L_1_5: list = [POINT_CHEO[1], POINT_CHEO[5]]
    L_2_3: list = [POINT_CHEO[2], POINT_CHEO[3]]
    L_3_4: list = [POINT_CHEO[3], POINT_CHEO[4]]
    L_5_6: list = [POINT_CHEO[5], POINT_CHEO[6]]
    L_6_7: list = [POINT_CHEO[6], POINT_CHEO[7]]
    L_8_9: list = [POINT_CHEO[8], POINT_CHEO[9]]
    L_8_12: list = [POINT_CHEO[8], POINT_CHEO[12]]
    L_9_10: list = [POINT_CHEO[9], POINT_CHEO[10]]
    L_10_11: list = [POINT_CHEO[10], POINT_CHEO[11]]
    L_12_13: list = [POINT_CHEO[12], POINT_CHEO[13]]
    L_13_14: list = [POINT_CHEO[13], POINT_CHEO[14]]
    L_11_24: list = [POINT_CHEO[11], POINT_CHEO[24]]
    L_11_22: list = [POINT_CHEO[11], POINT_CHEO[22]]
    L_22_23: list = [POINT_CHEO[22], POINT_CHEO[23]]
    L_14_19: list = [POINT_CHEO[14], POINT_CHEO[19]]
    L_14_21: list = [POINT_CHEO[14], POINT_CHEO[21]]
    L_19_20: list = [POINT_CHEO[19], POINT_CHEO[20]]
    L_1_8: list = [POINT_CHEO[1], POINT_CHEO[8]]
    
    # list of all lists
    POINTS_LIST: list[list] = [L_0_1, L_0_15, L_0_16, L_15_17, L_16_18, L_1_2, L_1_5, L_2_3, L_3_4, 
    L_5_6, L_6_7, L_8_9, L_8_12, L_9_10, L_10_11, L_12_13, L_13_14, 
    L_11_24, L_11_22, L_22_23, L_14_19, L_14_21, L_19_20, L_1_8]

    # print all body parts and their coordinates
    print("\n--- body parts and their coordinates ---")
    for count, coordinates in enumerate(returnAllKeyPointsOfChoreography(jsonfiles)[0]): 
        print(f'{count}. {bodyParts[count]}: {coordinates}')
    
    # calculate slopes
    SLOPES: list[np.float64] = [calculateSlope(POINTS_LIST[c][0][0], POINTS_LIST[c][0][1], POINTS_LIST[c][1][0], POINTS_LIST[c][1][1]) for c in range(0, len(POINTS_LIST))]
    print(f"\n--- SLOPES ---\n{SLOPES}")
    
    # --- calculate important angles --- #
    
    BODY: np.float64 = calculateAngle(SLOPES[0], SLOPES[23], 0)
    ARM_RIGHT: np.float64 = calculateAngle(SLOPES[7], SLOPES[8], 1)
    ARM_LEFT: np.float64 = calculateAngle(SLOPES[9], SLOPES[10], 2)
    SHOULDER_RIGHT: np.float64 = calculateAngle(SLOPES[5], SLOPES[7] ,3)
    SHOULDER_LEFT: np.float64 = calculateAngle(SLOPES[6], SLOPES[9], 4)
    LEG_RIGHT: np.float64 = calculateAngle(SLOPES[13], SLOPES[14], 5)
    LEG_LEFT: np.float64 = calculateAngle(SLOPES[15], SLOPES[16], 6)
    HIP_RIGHT: np.float64 = calculateAngle(SLOPES[11], SLOPES[13], 7)
    HIP_LEFT: np.float64 = calculateAngle(SLOPES[12], SLOPES[15], 8)

    print("\n----ANGELS----")
    print(f"BODY: {BODY}°")
    print(f"ARM_RIGHT: {ARM_RIGHT}°")
    print(f"ARM_LEFT: {ARM_LEFT}°")
    print(f"SHOULDER_RIGHT: {SHOULDER_RIGHT}°")
    print(f"SHOULDER_LEFT: {SHOULDER_LEFT}°")
    print(f"LEG_RIGHT: {LEG_RIGHT}°")
    print(f"LEG_LEFT: {LEG_LEFT}°")
    print(f"HIP_RIGHT: {HIP_RIGHT}°")
    print(f"HIP_LEFT: {HIP_LEFT}°")

    endtime = time.time()
    elapsed_time = endtime - starttime
    print(f'Execution time: {elapsed_time:.2} seconds')

# --- functions --- #

@lru_cache(maxsize=None)
def readPaths(filepath: str) -> list: return glob(f"{filepath}/*.json")

def returnListofTuples(file: str,x) -> list:
    with open(file[x]) as f:
        data = json.load(f)
    posekeypoints = data["people"][0]["pose_keypoints_2d"]
    del posekeypoints[2::3]
   
    return [(posekeypoints[i], posekeypoints[i+1]) for i in range(0, len(posekeypoints), 2)]

def returnAllKeyPointsOfChoreography(file: str) -> list: return [returnListofTuples(file, x) for x in range(0, len(file))]

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

def calculateSlope(x1: np.float64, y1: np.float64, x2: np.float64, y2: np.float64) -> np.float64: return np.round_((y2 - y1) / (x2 - x1), decimals=2)

# def calculateAndPrintAngles():


if __name__ == "__main__":
    main()