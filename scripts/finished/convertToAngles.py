# folder structure

# open-just-dance/
# ├── scripts/
# │   ├── convertToAngles.py
# │   └── main.py
# ├── output/
# │   ├── dance/
# │   └── webcam/
# ├── scripts/
# └── readme.md

# configurable settings
# - frame rate of the video and webcam (1 -10)
# default: 1

# how it works
# openpose captures the skeleton of a person and saves it as a json file
# the json file is then read by the convertToAngles.py script and the angles are calculated