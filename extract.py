"""
Author: Joseph Armstrong

"""

import json
import jsonlines

DATA_INPUT_FILE = "branded_download.json"
DATA_OUTPUT_FILE = "branded_data.jsonl"

def extract_data():

    extracted_data = []

    with open(DATA_INPUT_FILE, 'r') as dataFile:
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

            extracted_data.append(foodData)
            count += 1
            if (count % 100 == 0):
                print(f'count: {count}')

            if(endFlag): break
        
    with jsonlines.open(DATA_OUTPUT_FILE, 'w') as sampleFile:
        sampleFile.write_all(extracted_data)

def numBrandOwners():

    brandOwners = set()
    num = 0

    with open(DATA_OUTPUT_FILE, encoding='utf-8', mode='r') as dataFile:
        start = dataFile.readline() # first line contains no information
        endFlag = False
        saveLine = dataFile.readline()
        count = 0

        while(True):
            try:
                nextLine = dataFile.readline()
                if (nextLine == ""): endFlag = True
                line = saveLine
                saveLine = nextLine

                food = json.loads(line)

                count += 1

                if (food['brandOwner'] in brandOwners):
                    continue
                else:
                    num += 1
                    brandOwners.add(food['brandOwner'])

                print(f"count: {count} and {num}")

                if(endFlag): break
            except:
                continue

if __name__ == "__main__":
    numBrandOwners()