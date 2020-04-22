with open('USPopulation.txt', 'r') as f:  # some magic with files
    data = [l.strip() for l in f.readlines()] # data is  now a list of the population numbers

print(data)
