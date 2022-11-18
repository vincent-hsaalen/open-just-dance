import os
from functools import lru_cache
import json
import matplotlib.pyplot as plt

def main():

    # variables
    output_dir:str = "C:/Users/vince/Desktop/open-just-dance/output/choreographies/1"
    jsonfiles = readPaths(output_dir)
    data = []

    # open json file and assigns its data to a dictionary
    
    a = returnListofTuples(jsonfiles,6000)
    b = returnListofTuples(jsonfiles,6060)

    ab = [a,b]
    red = "red"
    blue = "blue"
    count = 0;

    for lists in ab:
        
        for coordinates in lists:
            if(count==0):
                print("blue")
                plt.scatter(coordinates[0],coordinates[1],color=blue)
            elif(count==1):
                print("red")
                plt.scatter(coordinates[0],coordinates[1],color=red)
                print(count)
        count+=1
    
    
    

    plt.show()


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

if __name__ == "__main__":
    main()


