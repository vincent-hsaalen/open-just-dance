import os
from functools import lru_cache

def main():
    dir:str = "C:/Users/vince/Desktop/open-just-dance/openpose/output_jsons"

# function to get all the files in the directory ()
@lru_cache(maxsize=None)
def readPaths(path_:str) -> list: return [os.path.join(path_, file) for file in os.listdir(path_)]

if __name__ == "__main__":
    main()


