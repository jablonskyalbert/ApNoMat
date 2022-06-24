def main():
    natureNdvi = []
    citiesNdvi = []
    with open ('output.txt', encoding='utf-8') as f:
        while(True):
            line = f.readline()
            if not line:
                break

            splitedLine = line.split(';')            
            if(splitedLine[2].strip() == 'None'):
                natureNdvi.append(float(splitedLine[1]))
            else:
                citiesNdvi.append(float(splitedLine[1]))

    with open ('analysis.txt', 'a', encoding='utf-8') as f:
        f.write(f'average NDVI in nature: {sum(natureNdvi)/len(natureNdvi)}\n')
        f.write(f'average urban NDVI: {sum(citiesNdvi)/len(citiesNdvi)}\n')
        f.write(f'the lowest NDVI in nature: {min(natureNdvi)}\n')
        f.write(f'the highest NDVI in nature: {max(natureNdvi)}\n')
        f.write(f'the lowest urban NDVI: {min(citiesNdvi)}\n')
        f.write(f'the highest urban NDVI: {max(citiesNdvi)}\n')
        

main()