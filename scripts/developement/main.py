import time
import scoring as sc
import readAndCalculate as rc
import scoring_v2 as sc_v2

# --- main start --- #

def main():
   
    starttime = time.time()
    # output_dir: str = "C:/Users/vince/Desktop/open-just-dance/FrameData/dance/v1/reference/"
    # input_dir: str = "C:/Users/vince/Desktop/open-just-dance/FrameData/dance/v1/actual/"
    output_dir: str = "C:/Users/vince/Desktop/open-just-dance/openpose/reference"
    input_dir: str = "C:/Users/vince/Desktop/open-just-dance/openpose/choreo"
    # list of strings containing the file location of each/every json file
    jsonfiles: str = rc.readPaths(output_dir)
    inputfiles: str = rc.readPaths(input_dir)

    # -------------------------------------------- #
    
    print("score_v1:")
    
    # check one by one
    score = sc.score(rc.returnListOfAngles(jsonfiles), rc.returnListOfAngles(inputfiles))
    print(f'score = {score}/1000000')

    print("\n")
    print("score_v2:")

    # check with tolerance
    score = sc_v2.score(rc.returnListOfAngles(jsonfiles), rc.returnListOfAngles(inputfiles), 30)
    print(f'score = {score}/1000000')

    
    # -------------------------------------------- #
    print("\n")
    endtime = time.time()
    elapsed_time = endtime - starttime
    print(f'Execution time: {elapsed_time:.2f} seconds')

# --- main end --- #

if __name__ == "__main__":
    main()