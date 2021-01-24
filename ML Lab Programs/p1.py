import numpy as np
import pandas as pd
data=pd.read_csv("1finds.csv")
concepts=data.iloc[:,0:-1].values
print("-------------------------")
print(concepts)
print("---------------------------")
target=data.iloc[:,-1]
print(target)
def train(concepts,target):
    count=0
    specific_h = concepts[0]
    for i,h in enumerate(concepts):
        if target[i]=="yes":
            for i in range(len(specific_h)):
                if h[x]==specific_h[x]:
                    pass
                else:
                    specific_h[x]=="?"
                count=count+1
                print(f"hypothesis of after same number:{count}proceed:{specific_h}")
        else:
             pass
             count=count+1
             print(f"negative same number:{count}:same hypothesis{specific_h}")
    return(specific_h)
specific_h=train(concepts,target)
    