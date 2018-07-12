import pandas as pd

fileN = input("Enter the file path of Emergency Data : ")
Emergency = pd.read_csv(fileN, delimiter = '\t', header=4)



print(Emergency.head())

print(Emergency['PostMarker'].head())