import json

with open('foundationDownload.json') as f:
    data = json.load(f)

    # print("len(data): ", len(data)) # 1
    # print("data.keys(): ", data.keys()) # 'FoundationFoods'
    # print("data['FoundationFoods']: ", data['FoundationFoods']) # too big
    # print("len(data['FoundationFoods']): ", len(data['FoundationFoods'])) # 256, each record is a different food

    # print("data['FoundationFoods'][0]: ", data['FoundationFoods'][0]) # too big
    # print("len(data[FoundationFoods'][0]): ", len(data['FoundationFoods'][0])) # 13, each record has 13 properties
    # print("data['FoundationFoods'][0].keys(): ", data['FoundationFoods'][0].keys()) # see all of the properties

    # print("data['FoundationFoods'][0]['foodClass']: ", data['FoundationFoods'][0]['foodClass']) # don't need
    # # # print("data['FoundationFoods'][0]['description']: ", data['FoundationFoods'][0]['description']) # yes need, Hummus in this case
    # # # print("data['FoundationFoods'][0]['Nutrients']: ", data['FoundationFoods'][0]['foodNutrients']) # too big, yes need
    # print("data['FoundationFoods'][0]['foodAttributes']: ", data['FoundationFoods'][0]['foodAttributes']) # empty, don't know
    # # # print("data['FoundationFoods'][0]['nutrientConversionFactors']: ", data['FoundationFoods'][0]['nutrientConversionFactors']) # yes need
    # print("data['FoundationFoods'][0]['isHistoricalReference']: ", data['FoundationFoods'][0]['isHistoricalReference']) # don't need
    # print("data['FoundationFoods'][0]['ndbNumber']: ", data['FoundationFoods'][0]['ndbNumber']) # don't know
    # print("data['FoundationFoods'][0]['dataType']: ", data['FoundationFoods'][0]['dataType']) # don't need
    # print("data['FoundationFoods'][0]['foodCategory']: ", data['FoundationFoods'][0]['foodCategory']) # maybe need
    # print("data['FoundationFoods'][0]['fdcId']: ", data['FoundationFoods'][0]['fdcId']) # don't know
    # # # print("data['FoundationFoods'][0]['foodPortions']: ", data['FoundationFoods'][0]['foodPortions']) # yes need
    # print("data['FoundationFoods'][0]['publicationDate']: ", data['FoundationFoods'][0]['publicationDate']) # don't need
    # print("data['FoundationFoods'][0]['inputFoods']: ", data['FoundationFoods'][0]['inputFoods']) # too big, don't need, found in docs


    # # # print("data['FoundationFoods'][0]['description']: ", data['FoundationFoods'][0]['description']) # yes need, Hummus in this case
    # # # print("data['FoundationFoods'][0]['Nutrients']: ", data['FoundationFoods'][0]['foodNutrients']) # too big, yes need
    # # # print("data['FoundationFoods'][0]['nutrientConversionFactors']: ", data['FoundationFoods'][0]['nutrientConversionFactors']) # yes need
    # # # print("data['FoundationFoods'][0]['foodPortions']: ", data['FoundationFoods'][0]['foodPortions']) # yes need
    