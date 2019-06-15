# Задание 4.1

import pandas as pd 
import matplotlib.pyplot as plt

"""
    Загрузка данных
"""
df = pd.read_csv('data.csv', header = None) 
x, y = df[0], df[1] 
#print(df)

"""
    Строим линейную функцию по двум точка
"""
x1,y1 = [0,22.5],[0,25]


"""
    Визуализация данных
"""


fig = plt.scatter(x, y, s = x, c ='green', label = u'Данные из файла') 
fig1 = plt.plot(x1, y1, 'r', label = u'Линейная функция') 

plt.savefig('plot.png', format='png')
plt.title('График 1')
plt.grid(False)
plt.legend()
plt.ylabel('Ось y')
plt.xlabel('Ось x')
