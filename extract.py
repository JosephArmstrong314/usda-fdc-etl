import json
import jsonlines

"""
with open('test.json') as file:
    data = json.load(file)

    brandedFoods = data['BrandedFoods']

    extractedData = []
    count = 0

    for f in brandedFoods:
        foodData = {}

        foodData.update({'name': f'food{count}'})
        
        servings = {}
        servings.update({'servingSize': f['servingSize']})
        servings.update({'servingSizeUnit': f['servingSizeUnit']})

        foodData.update({'nutrients': f['labelNutrients']})
        foodData.update({'description': f['description']})
        foodData.update({'category': f['brandedFoodCategory']})
        foodData.update({'brand': f['brandOwner']})
        foodData.update({'servings': servings})
        

        extractedData.append(foodData)
        count += 1
    
    main = {"main": extractedData}

    with open('data4.json', 'w') as file:
        json.dump(main, file, indent=2)
"""



with open('newData/brandedDownload0.json') as file:
    data = json.load(file)

    brandedFoods = data['BrandedFoods']

    extractedData = []
    count = 0

    for f in brandedFoods:
        foodData = {}

        foodData.update({'name': f'food{count}'})

        keys1 = ['description', 'brandedFoodCategory', 'brandOwner', 'servingSize', 'servingSizeUnit']
        keys2 = 'servingSize'
        keys3 = ['calories', 'protein', 'fat', 'carbohydrates', 'fiber', 'calcium', 'iron', 'sodium', 'cholesterol', 'sugars']

        for k1 in keys1:
            if k1 in f:
                foodData.update({k1: f[k1]})
            else:
                foodData.update({k1: 'Not Available'})
        
        if 'servingSize' in f:
            foodData.update({'servingSize': f['servingSize']})
        else:
            foodData.update({'servingSize': 'not available'})

        for k3 in keys3:
            if k3 in f['labelNutrients']:
                foodData.update({k3: f['labelNutrients'][k3]['value']})
            else:
                foodData.update({k3: -1})

        extractedData.append(foodData)
        count += 1
    
    main = {"main": extractedData}

    # with open('data10.json', 'w') as file:
        # json.dump(main, file, indent=2)
    
    with jsonlines.open('brandedDownload0a.jsonl', 'w') as file:
        file.write_all(extractedData)



"""
with open('newData/brandedDownload0.json') as file:
    data = json.load(file)

    brandedFoods = data['BrandedFoods']

    extractedData = []
    count = 0

    for f in brandedFoods:
        foodData = {}

        foodData.update({'id': f'food{count}'})

        servings = {}
        servings.update({'servingSize': f['servingSize']})
        servings.update({'servingSizeUnit': f['servingSizeUnit']})

        foodData.update({'nutrients': f['labelNutrients']})
        foodData.update({'description': f['description']})
        foodData.update({'category': f['brandedFoodCategory']})
        foodData.update({'brand': f['brandOwner']})
        foodData.update({'servings': servings})

        extractedData.append({f'food{count}': foodData})
        count += 1
    
    main = {'main': extractedData}
    
    with open('extractedBrandedDownload0a.json', 'w') as file:
        json.dump(main, file, indent=2)
"""


"""
NUM_FILES = 501

extractedData = []
count = 0

count_unavailable = 0

for N in range(NUM_FILES):
    
    with open(f'newData/brandedDownload{N}.json') as file:
        data = json.load(file)

        brandedFoods = data['BrandedFoods']

        for f in brandedFoods:
            foodData = {}

            foodData.update({'id': f'food{count}'})

            keys = ['nutrients', 'description', 'category', 'brand']
            servings_keys = ['servingSize', 'servingSizeUnit']
            data_keys = ['labelNutrients', 'description', 'brandedFoodCategory', 'brandOwner']

            for i in range(len(keys)):
                if (data_keys[i] in f):
                    foodData.update({keys[i]: f[data_keys[i]]})
                else:
                    print(f'{data_keys[i]} was not available {count_unavailable}')
                    count_unavailable += 1
                    foodData.update({keys[i]: "Not Available"})
            
            servings = {}
            
            for sk in servings_keys:
                if (sk in f):
                    servings.update({sk: f[sk]})
                else:
                    print(f'{sk} was not available {count_unavailable}')
                    count_unavailable += 1
                    servings.update({sk: "Not Available"})

            foodData.update({'servings': servings})

            extractedData.append(foodData)
            count += 1

main = {'main': extractedData}

with open('extractedBrandedDownload2.json', 'w') as file:
    json.dump(main, file, indent=2)
"""