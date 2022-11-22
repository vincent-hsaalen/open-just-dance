import time
import scoring 
import readAndCalculate as rc

# --- main start --- #

def main():
   
    starttime = time.time()
    output_dir: str = "C:/Users/vince/Desktop/open-just-dance/FrameData/dance"
    # list of strings containing the file location of each/every json file
    jsonfiles: str = rc.readPaths(output_dir)
    # -------------------------------------------- #
    
    # print(returnListOfAngles(jsonfiles))
    score = scoring.score(rc.returnListOfAngles(jsonfiles), rc.returnListOfAngles(jsonfiles))
    print(score)
    
    # -------------------------------------------- #
    endtime = time.time()
    elapsed_time = endtime - starttime
    print(f'Execution time: {elapsed_time:.2f} seconds')

# --- main end --- #

if __name__ == "__main__":
    main()