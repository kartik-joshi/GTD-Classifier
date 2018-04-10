import pandas as pd
from datetime import datetime
import numpy as np
import itertools

# Uncomment this part to extract data from GTD excel and assign class for each terrorist group

# file = "GTD.xlsx"
#
# xl = pd.read_excel(file, sheetname='Data')
# Country_Code = xl['country']
# Attack_Code = xl['attacktype1']
# Target_Code= xl['targtype1']
# Weapon_Code= xl['weaptype1']
# Group= xl['gname']
# Group_Code  =[0]*len(Group)
# Group_Names = np.unique((Group)).tolist()
# for i in range (0,len(Group)):
#     Group_Code[i]= Group_Names.index(Group[i])
# xl = pd.DataFrame({'Country_Code':Country_Code, 'Attack_Code':Attack_Code, 'Target_Code' : Target_Code,'Weapon_Code':Weapon_Code})
# xl2 = pd.DataFrame({'Group_Code':Group_Code})
# xl.to_csv("GTD_Data.csv",index=False,header=False)
# xl2.to_csv("GTD_Target.csv",index=False,header=False)


# Code to extract data from GTD dataset and exclude Unknown class as terrorist group.

file = "GTD.xlsx"

xl = pd.read_excel(file, sheetname='Data')
Country_Code = xl['country']
Group= xl['gname']
CN_Code = []
Attack_Code = xl['attacktype1']
Atc_Code = []
Target_Code= xl['targtype1']
Tr_Code = []
Weapon_Code= xl['weaptype1']
We_Code = []
Group_Code  =[]
Group_Names = np.unique((Group)).tolist()
for i in range (0,len(Group)):
    if Group[i] != "Unknown":
        Group_Code.append(Group_Names.index(Group[i]))
        CN_Code.append(Country_Code[i])
        Atc_Code.append(Attack_Code[i])
        Tr_Code.append(Target_Code[i])
        We_Code.append(Weapon_Code[i])

xl = pd.DataFrame({'Country_Code':CN_Code, 'Attack_Code':Atc_Code, 'Target_Code' : Tr_Code,'Weapon_Code':We_Code})
xl2 = pd.DataFrame({'Group_Code':Group_Code})
xl.to_csv("GTD_Data_2.csv",index=False,header=False)
xl2.to_csv("GTD_Target_2.csv",index=False,header=False)