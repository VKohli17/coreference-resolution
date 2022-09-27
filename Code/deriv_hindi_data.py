import os
import pandas as pd

directory = 'Hindi-Coreference-Annotated-Data/Data'
directory1 = 'csvs'

for file in os.listdir(directory):
    if file.endswith(".norm"):
        dataset = []
        file1 = open(os.path.join(directory, file), "r")
        file1.seek(0)
        for line in file1:
            dataset.append(line.split())
        dataset = [x for x in dataset if x != []]
        #save the dataset in a csv file
        df = pd.DataFrame(dataset)
        df.to_csv(os.path.join(directory1, file[:-5] + '.csv'), index=False, header=False)

df = pd.DataFrame(dataset)
print(df.head())
#convert it to .csv file
df.to_csv('hindi_coref_data.csv', index=False)
#display size of dataframe
print(df.shape)