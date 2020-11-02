import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
##mex_19.to_csv(r'MexiFront_sinIndex_2019.csv', index = False)

front =  pd.read_csv("fronteras.csv")
border = front['Border'] == 'US-Canada Border'
fecha = front['Date'].isin(['1/1/2019 00:00','2/1/2019 00:00','3/1/2019 00:00','4/1/2019 00:00','5/1/2019 00:00','6/1/2019 00:00','7/1/2019 00:00','8/1/2019 00:00','9/1/2019 00:00','10/1/2019 00:00','11/1/2019 00:00','12/1/2019 00:00'])
frontDT = front[border & fecha]

df = frontDT.drop(frontDT.columns.difference(['State', 'Port Name', 'Measure', 'Value', 'Date']),1)
dff = df[df.State != 'AK']
dff['Date'] =  pd.to_datetime(dff['Date'], format='%m/%d/%Y %H:%M')
#estado = dff.groupby('State').count()

'''
id = dff[dff.State == 'ID']
idG = id.groupby('Date').sum()
idG.plot()
plt.show()
'''

#Pregunta 1
def grafica_estados(state1, code):
    print('A continuacion se imprimira la grafica de '+ state1 + '\n\n')
    state = dff[dff.State == code]
    state = state[state.Measure == 'Personal Vehicles']
    idG = state.groupby('Date').sum()
    idG.plot()
    plt.title(state1 , fontdict=None, loc='center', pad=None)
    plt.show()

print('A continuacion se imprimiran las graficas de Personal Vehicles\n\n\n\n')
grafica_estados('Idaho', 'ID')
grafica_estados('Maine', 'ME')
grafica_estados('Michigan', 'MI')
grafica_estados('Minnesota', 'MN')
grafica_estados('Montana', 'MT')
grafica_estados('North_Dakota', 'ND')
grafica_estados('New_York', 'NY')
grafica_estados('Ohio', 'OH')
grafica_estados('Vermont', 'VT')
grafica_estados('Washington', 'WA')

#Pregunta 2
def scatt_estados(state1, code, sets):
    print('A continuacion se imprimira la grafica de '+ state1 + '\n\n\n\n')
    state = dff[dff.State == code]
    state = state[state.Measure == 'Pedestrians']
    idG = state.groupby('Port Name').sum()
    plt.scatter(sets, idG['Value'] )
    plt.title(state1 , fontdict=None, loc='center', pad=None)
    plt.show()

set1= ['Eastport', 'Porthill']
set2= ['Calais','Eastport','Fort Kent','Houlton','Jackman','Madawaska','Van Buren','Vanceboro']
set3 =['Detroit','Port Huron']
set4 = ['Baudette','International Falls-Ranier','Warroad']
set5 = ['Del Bonita', 'Morgan', 'Opheim', 'Piegan', 'Raymond', 'Roosville','Sweetgrass','Turner', 'Willow Creek']
set6 = ['Noonan','Northgate','Portal','Sarles']
set7 = ['Buffalo-Niagara Falls','Champlain-Rouses Pont','Massena']
#set8 = ['Toledo-Sandusky']
set9 = ['Derby Line','Norton']
set10 = ['Boundary','Danville','Ferry','Frontier','Lynden','Metaline Falls','Nighthawk','Oroville','Point Roberts', 'Sumas']
print('A continuacion se imprimiran las graficas de pedestrians\n\n\n\n')
scatt_estados('Idaho', 'ID', set1)
scatt_estados('Maine', 'ME', set2)
scatt_estados('Michigan', 'MI', set3)
scatt_estados('Minnesota', 'MN',set4)
scatt_estados('Montana', 'MT',set5)
scatt_estados('North_Dakota', 'ND', set6)
scatt_estados('New_York', 'NY', set7)
# no hay pedestrians en ohio scatt_estados('Ohio', 'OH', set8)
scatt_estados('Vermont', 'VT', set9)
scatt_estados('Washington', 'WA', set10)


#Pregunta 3
def grafica_estados(state1, code):
    print('A continuacion se imprimira la grafica de '+ state1 + '\n\n')
    state = dff[dff.State == code]
    stateV = state[state.Measure == 'Personal Vehicles']
    stateP = state[state.Measure == 'Personal Vehicle Passengers']
    print(stateV)
    print(stateP)
    stateTot = stateV.append(stateP(stateP['Measure'], stateP['Value']))
    print('\n\n\n', stateTot)
    idG = state.groupby(['Port Name' ,'Measure'],as_index=False).sum()
    print(idG)
    print(type(idG))
    idG.plot.bar(x= 'Port Name')
    plt.title(state1 , fontdict=None, loc='center', pad=None)
    plt.show()

print('A continuacion se imprimiran las graficas de Personal Vehicles\n\n\n\n')
#grafica_estados('Idaho', 'ID')
grafica_estados('Maine', 'ME')
'''grafica_estados('Michigan', 'MI')
grafica_estados('Minnesota', 'MN')
grafica_estados('Montana', 'MT')
grafica_estados('North_Dakota', 'ND')
grafica_estados('New_York', 'NY')
grafica_estados('Ohio', 'OH')
grafica_estados('Vermont', 'VT')
grafica_estados('Washington', 'WA')'''

#Pregunta 4
def hist_estados(state1, code):
    print('A continuacion se imprimira la grafica de '+ state1 + '\n')
    state = dff[dff.State == code]
    state = state[state.Measure == 'Bus Passengers']
    idG = state.groupby('Port Name').sum()
    plt.hist(idG['Value'])
    print(idG)
    plt.title(state1 , fontdict=None, loc='center', pad=None)
    plt.show()

print('A continuacion se imprimiran las graficas de Personal Vehicles\n\n\n\n')
hist_estados('Idaho', 'ID')
hist_estados('Maine', 'ME')
hist_estados('Michigan', 'MI')
hist_estados('Minnesota', 'MN')
hist_estados('Montana', 'MT')
hist_estados('North_Dakota', 'ND')
hist_estados('New_York', 'NY')
hist_estados('Ohio', 'OH')
hist_estados('Vermont', 'VT')
hist_estados('Washington', 'WA')
'''
#fechas = (['1/1/2019','2/1/2019','3/1/2019','4/1/2019','5/1/2019','6/1/2019','7/1/2019','8/1/2019','9/1/2019','10/1/2019','11/1/2019','12/1/2019'])

def grafica_estados(state1, code):
    print('A continuacion se imprimira la grafica de '+ state1 + '\n\n')
    state = dff['State'] == code
    state = state['Measure'].isin(['Personal Vehicles','Personal Vehicles Passengers'])
    print(state)
    idG = state.groupby(['Measure', 'Port Name']).sum()
    print(idG)
    idG.plot.bar(x='Port Name')
    plt.title(state1 , fontdict=None, loc='center', pad=None)
    plt.show()




#Pregunta 3
def grafica_estados(state1, code):
    print('A continuacion se imprimira la grafica de '+ state1 + '\n\n')
    state = dff[dff.State == code]
    state = state[(state.Measure == 'Personal Vehicles') | (state.Measure == 'Personal Vehicle Passengers')]
    print(state)
    idG = state.groupby(['Port Name' ,'Measure'],as_index=False).sum()
    print(idG)
    print(type(idG))
    idG.plot.bar(x= 'Port Name')
    plt.title(state1 , fontdict=None, loc='center', pad=None)
    plt.show()

'''
