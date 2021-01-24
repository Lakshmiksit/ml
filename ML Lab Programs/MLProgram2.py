
import numpy as np
import pandas as pd


data = pd.DataFrame(data=pd.read_csv('2ce.csv'))


concepts = data.iloc[:,0:-1].values

target =data.iloc[:,-1].values
def learn(concepts, target):
    specific_h = concepts[0].copy()
    general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
    
   
    for i, h in enumerate(concepts):
        
       
        if target[i] == "Yes":
            for x in range(len(specific_h)):
                
               
                if h[x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] = '?'
    
        if target[i] == "No":
            for x in range(len(specific_h)):
                print(f"specific={specific_h[x]}")
               
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                 
                else:
                    general_h[x][x] = '?'

    indices = [i for i,val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]
    for i in indices:
       
        general_h.remove(['?', '?', '?', '?', '?', '?'])
        
   
    return specific_h, general_h
s_final, g_final = learn(concepts, target)
print("Final S:", s_final, sep="\n")
print("Final G:", g_final, sep="\n")