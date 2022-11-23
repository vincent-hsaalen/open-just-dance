import numpy as np

x = np.linspace(0,0.01,1)
y = 4*x-3
 # function/curve that maps similarity to score (<0.75 similarity is 0% of score per angle, 
 # whereas >0.75 similarity is 100% of score per angle)

# calculates the score in dependence of the similarity with a linear function -> y = 4x-3
def score(referenceAngleList, actualAngleList):
    totalAngles = len(referenceAngleList[0]) * len(referenceAngleList)
    maxScore = 1000000
    scoreForAngle = maxScore / totalAngles
    score = 0

    # print(f'totalAngles = {totalAngles} \nscoreForAngle = {scoreForAngle}') 

    for referenceAngles, actualAngles in zip(referenceAngleList, actualAngleList):
        # print(f'referenceAngles: {referenceAngles}')
        # print(f'actualAngles: {actualAngles}')
        for referenceAngle, actualAngle in zip(referenceAngles, actualAngles):
            similarity = checkSimilarity(referenceAngle, actualAngle)
            scoreMultiplier = 4*similarity-3
            if (similarity >= 0.75):
                score += scoreForAngle * scoreMultiplier
            else:
                score += 0
        
    return round(score)
       
def checkSimilarity(referenceAngle, actualAngle):
    # 180 degrees is the maximum angle -> 180 degrees = 100% similarity
    # 0 degrees is the minimum angle -> 0 degrees = 0% similarity
    if referenceAngle >= actualAngle:
        similarity = round(1 - (abs(referenceAngle - actualAngle) / referenceAngle), 2)
        return similarity
    else:
        similarity = round(1 - (abs(referenceAngle - actualAngle) / actualAngle), 2)
        return similarity