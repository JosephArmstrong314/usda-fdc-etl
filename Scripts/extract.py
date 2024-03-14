import json
import jsonlines

def getBrandedFoodsData():
    data_filePath = 'Data/RawData/brandedDownload.json'
    filePath = 'Data/FinalData/brandedData.jsonl'

    extractedData = []

    with open(data_filePath, 'r') as dataFile:
        start = dataFile.readline() # first line contains no information
        endFlag = False
        saveLine = dataFile.readline()
        count = 0

        while(True):
            nextLine = dataFile.readline()
            if (nextLine == ""): endFlag = True
            line = saveLine
            saveLine = nextLine

            if (line[-1] == '\n'): line = line[:-1]
            if (line[-1] == ','): line = line[:-1]

            if (endFlag):
                line = start + line
            else:
                line = start + line + ']}'

            food = json.loads(line)
            food = food['BrandedFoods'][0]

            foodData = {}
            foodData.update({'name': f'food{count}'})
            keys1 = ['description', 'brandedFoodCategory', 'brandOwner', 'servingSize', 'servingSizeUnit']
            keys2 = ['calories', 'protein', 'fat', 'carbohydrates', 'fiber', 'calcium', 'iron', 'sodium', 'cholesterol', 'sugars']

            for k1 in keys1:
                if k1 in food:
                    foodData.update({k1: food[k1]})
                else:
                    foodData.update({k1: 'Not Available'})
            
            if 'servingSize' in food:
                foodData.update({'servingSize': food['servingSize']})
            else:
                foodData.update({'servingSize': 'not available'})

            for k2 in keys2:
                if k2 in food['labelNutrients']:
                    foodData.update({k2: food['labelNutrients'][k2]['value']})
                else:
                    foodData.update({k2: -1})

            extractedData.append(foodData)
            count += 1
            if (count % 100 == 0):
                print(f'count: {count}')

            if(endFlag): break
        
    with jsonlines.open(filePath, 'w') as sampleFile:
        sampleFile.write_all(extractedData)

"""
def getSampleBrandedFoodsDataEnd():
    data_filePath = 'Data/RawData/brandedDownload.json'

    with open(data_filePath, 'r') as dataFile:
        saveline = dataFile.readline()

        while(True):
            line = dataFile.readline()
            if (line == ""):
                break
            saveline = line
"""

if __name__ == "__main__":
    getBrandedFoodsData()