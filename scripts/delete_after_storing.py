import os

path = 'openpose/output_jsons/jd_000000000001_keypoints.json'

with open(path) as f:
  for l in f:
    print(l)

os.remove(path)