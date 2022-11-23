import numpy as np

x = np.linspace(0,0.01,1)
y = 4*x-3

def score(referenceAngleList, actualAngleList, tolerance):

    """
    Calculates score with a linear function (y = 4x-3) in dependence of the similarity of the angles.

    referenceAngleList: list of lists containing the reference angles
    actualAngleList: list of lists containing the actual angles
    tolerance: tolerance for the user by taking the highest similary for x frames because of latency (0 = no tolerance)
    returns: total score (max=1000000)

    """

    totalAngles = (len(referenceAngleList[0]) * len(referenceAngleList)) / tolerance
    maxScore = 1000000
    scoreForAngle = maxScore / totalAngles
    score = 0

    # added variables for tolerance
    similarityList = []
    similarityLists = []
    listofsums = []
    # counter to check how many times loop is executed
    counter = 0
    counter2 = 0
    # bool to check if iterated once
    index = 0

    for referenceAngles, actualAngles in zip(referenceAngleList, actualAngleList):

        for referenceAngle, actualAngle in zip(referenceAngles, actualAngles):

            similarity = checkSimilarity(referenceAngle, actualAngle)
            similarityList.append(similarity)

        similarityLists.append(similarityList)
        similarityList = [] 

        if len(similarityLists) == tolerance:
            index = findMaxInListOfLists(similarityLists)
            
            # # --- debug --- # 
            # # print(f'index with highest sim: = {index}')
            # counter+=1
            # print(f'iteration nr. {counter}\nsimilarityLists = {similarityLists}\nlength of similarityLists = {len(similarityLists)}\n')
            # # --- debug --- #

            
            for sim in similarityLists[index]:
                if sim >= 0.75:
                    scoreMultiplier = 4*sim-3
                    score += scoreForAngle*scoreMultiplier
                else:
                    score+=0









            # reset
            similarityLists = []


    return round(score)



def checkSimilarity(referenceAngle, actualAngle):
    if referenceAngle >= actualAngle:
        similarity = round(1 - (abs(referenceAngle - actualAngle) / referenceAngle), 2)
        return similarity
    else:
        similarity = round(1 - (abs(referenceAngle - actualAngle) / actualAngle), 2)
        return similarity

def findMaxInListOfLists(listOfLists):
    sumOfList = []
    sumLisTotal = []
    for lst in listOfLists:
        sumOfList = sum(lst)
        sumLisTotal.append(sumOfList)

    return sumLisTotal.index(max(sumLisTotal))