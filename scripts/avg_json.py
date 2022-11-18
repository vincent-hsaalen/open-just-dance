import os
from functools import lru_cache
import json
import time
from matplotlib import pyplot as plt

def main():

    # runtime start
    starttime = time.time()

    # variables
    output_dir:str = "C:/Users/vince/Desktop/open-just-dance/output/choreographies/1"
    jsonfiles = readPaths(output_dir)
    data = []

    # open json file and assigns its data to a dictionary
    print(jsonfiles[100])
    with open(jsonfiles[100]) as f:
        data = json.load(f)
        # print(type(data))
        # print(data["people"][0]["pose_keypoints_2d"])
        # Body part locations (x, y) and detection confidence (c) formatted as x0,y0,c0,x1,y1,c1,

    print(len(data["people"][0]["pose_keypoints_2d"]))

    posekeypoints = data["people"][0]["pose_keypoints_2d"]
    # print(posekeypoints)

    # delete confidence values from list
    n = 3
    del posekeypoints[n-1::n]
    # print(posekeypoints)
    # print(len(posekeypoints))

    # splits list into new list with tuples containing x and y values
    listoftuples = []
    for i in range(0, len(posekeypoints), 2):
        listoftuples.append((posekeypoints[i], posekeypoints[i+1]))
    print(len(listoftuples))
        
    # for files in jsonfiles:
    #     with open(files, "r") as file:
    #         data.append(json.load(file))
    #         file.close()

    # runtime end
    endtime = time.time()
    elapsed_time = endtime - starttime
    print('Execution time:', elapsed_time, 'seconds')


# function to get all the files in the directory ()
@lru_cache(maxsize=None)
def readPaths(filepath:str) -> list: return [os.path.join(filepath, file) for file in os.listdir(filepath)]

if __name__ == "__main__":
    main()


