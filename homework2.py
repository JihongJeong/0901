import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

N = 31

final = np.array([0, 0, 0, 0, 0, 0, 0, 0])
final2 = np.array([0, 0, 0, 0])

for i in range(1, N+1):
    if i<10:
        study = pd.read_csv('C:\\Users\\JihongJeong\\DMdata\\DM0'+str(i)+'\\DM0'+str(i)+'_study.txt', sep = '\t')
        test = pd.read_csv('C:\\Users\\JihongJeong\\DMdata\\DM0'+str(i)+'\\DM0'+str(i)+'_test.txt', sep = '\t')
    else:
        study = pd.read_csv('C:\\Users\\JihongJeong\\DMdata\\DM'+str(i)+'\\DM'+str(i)+'_study.txt', sep = '\t')
        test = pd.read_csv('C:\\Users\\JihongJeong\\DMdata\\DM'+str(i)+'\\DM'+str(i)+'_test.txt', sep = '\t')
        
    study = study.reset_index()
    study = pd.DataFrame([study['Trial'], study['ObjID']])
    study = study.transpose()
    study.columns = ['ObjID', 'LocID']

    test = test.reset_index()
    test = pd.DataFrame([test['index'], test['Trial'], test['Object_ID'], test['RT1'], test['RT2']])
    test = test.transpose()
    test.columns = ['Trial', 'ObjID', 'Task_Type', 'Res1', 'Res2']

    test.sort_values(by = 'ObjID', ascending = True, inplace = True)
    test = test.reset_index(drop = True)

    study = pd.concat([study, study])
    study.sort_values(by = 'ObjID', ascending = True, inplace = True)
    study = study.reset_index(drop = True)

    location = pd.DataFrame([study['LocID']])
    location = location.transpose()
    test = pd.concat([test, location], axis = 1)

    test.sort_values(by = 'Res1', ascending = True, inplace = True)
    df = test.reset_index(drop = True)

    df2 = df[df['Res2']!=0]

    ##'HIT-HC' : old_certain + old : Res1 == 1, Task_Type == 0
    ##'HIT-LC' : old_uncertain + old : Res1 == 2, Task_Type == 0
    ##'MISS-LC' : old_uncertain + new : Res1 == 2, Task_Type == 1 
    ##'MISS-HC' : old_certain + new : Res1 == 1, Task_Type == 1 
    ##'FA-HC' : new_certain + new : Res1 == 4, Task_Type == 0
    ##'FA-LC' : new_uncertain + new : Res1 == 3, Task_Type == 0
    ##'CR-LC' : new_uncertain + old : Res1 == 3, Task_Type == 1
    ##'CR-HC' : new_certain + old : Res1 == 4, Task_Type == 1

    HIT_HC = df[(df['Res1'] == 1) & (df['Task_Type']==0)]
    HIT_LC = df[(df['Res1'] == 2) & (df['Task_Type']==0)]
    MISS_LC = df[(df['Res1'] == 2) & (df['Task_Type']==1)]
    MISS_HC = df[(df['Res1'] == 1) & (df['Task_Type']==1)]
    FA_HC = df[(df['Res1'] == 4) & (df['Task_Type']==0)]
    FA_LC = df[(df['Res1'] == 3) & (df['Task_Type']==0)]
    CR_LC = df[(df['Res1'] == 3) & (df['Task_Type']==1)]
    CR_HC = df[(df['Res1'] == 4) & (df['Task_Type']==1)]

    HIT_HC2 = df[(df['Res1'] == 1) & (df['Res2'] == df['LocID']) & (df['Task_Type']==0)]
    HIT_LC2 = df[(df['Res1'] == 2) & (df['Res2'] == df['LocID']) & (df['Task_Type']==0)]
    MISS_LC2 = df[(df['Res1'] == 2) & (df['Res2'] != df['LocID']) & (df['Task_Type']==0)]
    MISS_HC2 = df[(df['Res1'] == 1) & (df['Res2'] != df['LocID']) & (df['Task_Type']==0)]

    ans = np.array([len(HIT_HC)/len(df), len(HIT_LC)/len(df),len(MISS_LC)/len(df),len(MISS_HC)/len(df),len(FA_HC)/len(df),len(FA_LC)/len(df),len(CR_LC)/len(df),len(CR_HC)/len(df)])
    final = np.vstack([final, ans])

    ans2 = np.array([len(HIT_HC2)/len(df2), len(HIT_LC2)/len(df2), len(MISS_LC2)/len(df2), len(MISS_HC2)/len(df2)])
    final2 = np.vstack([final2, ans2])

final = final[1:N+1,]
final2 = final2[1:N+1,]
df = pd.DataFrame(final)
df2 = pd.DataFrame(final2)
df.columns = ['HIT-HC', 'HIT-LC', 'MISS-LC', 'MISS-HC', 'FA-HC', 'FA-LC', 'CR-LC', 'CR-HC']
df2.columns = ['HIT-HC', 'HIT-LC', 'MISS-LC', 'MISS-HC']

##df.to_excel('homework2.xlsx')
##name = ['HIT-HC', 'HIT-LC', 'MISS-LC', 'MISS-HC', 'FA-HC', 'FA-LC', 'CR-LC', 'CR-HC']
##hist = [df['HIT-HC'].mean(), df['HIT-LC'].mean(), df['MISS-LC'].mean(), df['MISS-HC'].mean(), df['FA-HC'].mean(), df['FA-LC'].mean(), df['CR-LC'].mean(), df['CR-HC'].mean()]
##error = [30.52399021,6.202670254, 38.98692916, 28.59069704, 63.83298099, 57.41286057, 38.21056545, 26.78516681]

ax1 = plt.subplot(121)
sns.barplot(data = df)

ax2 = plt.subplot(122)
sns.barplot(data = df2)
plt.axhline(0.25, color="black", linestyle=':', alpha=0.5)

plt.show()
 
