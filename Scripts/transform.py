import json

NUM_FILES = 500

ends = []

for N in range(NUM_FILES):
    with open(f'data/brandedDownload{N}.txt', mode='r', encoding='utf-8') as file:

        lines = []

        for line in file:
            lines.append(line.strip())
    
        
        with open(f'newData/brandedDownload{N}.json', mode='w', encoding='utf-8') as file:

            file.write("{\"BrandedFoods\": [\n")

            for line in lines[1:-2]:
                file.write(line + "\n")
            
            if (N == NUM_FILES - 1):
                file.write(lines[-2] + "\n")
            else:
                file.write(lines[-2][:-1] + "\n")
            
            if (N != NUM_FILES - 1):
                file.write("]}\n")
            else:
                file.write(lines[-1])
        
        
        pair = [lines[0], lines[-1]]
        ends.append(pair)


lines = []
for N in range(NUM_FILES - 1):
    line = ends[N][1] + ends[N+1][0]
    lines.append(line)

with open(f'newData/brandedDownload{NUM_FILES}.json', mode='w', encoding='utf-8') as file:
    file.write("{\"BrandedFoods\": [\n")

    for line in lines[:-1]:
        file.write(line + "\n")
    
    file.write(lines[-1][:-1])

    file.write("]}\n")