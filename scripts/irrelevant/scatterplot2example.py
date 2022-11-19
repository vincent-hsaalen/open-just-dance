from functools import lru_cache
import json
import matplotlib.pyplot as plt
from glob import glob

def main():

    # variables
    output_dir:str = "C:/Users/vince/Desktop/open-just-dance/output/single"
    jsonfiles = readPaths(output_dir)

    # open json file and assigns its data to a dictionary
    plt.xlim(400)
    plt.ylim(400)
    a = returnListofTuples(jsonfiles,0)


    for count, coordinates in enumerate(a):
        if count == 10:
            plt.scatter(coordinates[0],coordinates[1], color="red")
        
        else:
            plt.scatter(coordinates[0],coordinates[1], color="blue")

        

    print(max(a))
    
    plt.show()

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

if __name__ == "__main__":
    main()


