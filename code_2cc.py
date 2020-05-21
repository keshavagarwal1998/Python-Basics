import numpy as np
import pandas as pd 
import sklearn as sklearn
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import re

data = pd.read_csv("database.csv")

attributes=(list(data))
attributes
species = data["Species Name"]
species_count=species.value_counts()
print(species_count)

top_species = ["UNKNOWN MEDIUM BIRD","UNKNOWN SMALL BIRD","MOURNING DOVE", "GULL","UNKNOWN BIRD","KILLDEER", "AMERICAN KESTREL","BARN SWALLOW"]
top_species = species[species.isin(top_species)]
sns.countplot(top_species)
plt.title("Top Species")
plt.xticks(rotation='vertical')

damage_x=[]
strike_x=[]
dam=".*Damage$"
stri=".*Strike$"
for i in attributes:
    if (re.match(dam, i)):
        damage_x.append(i)
    elif (re.match(stri, i)):
        strike_x.append(i)
damage_x=damage_x[1:]

damage_y=[]
strike_y=[]
for i in strike_x:
    strike_y.append(data[i].sum())

for i in damage_x:
    damage_y.append(data[i].sum())

plt.bar(damage_x,damage_y, color='red')
plt.title("Parts Damaged in the Aircraft")
plt.xticks(rotation='vertical')

plt.bar(strike_x,strike_y,color='red')
plt.title("Parts Striked in the Aircraft")
plt.xticks(rotation='vertical')
print("Keshav agarwal 17BIT0067")
