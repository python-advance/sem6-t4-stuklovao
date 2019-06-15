# На основе кода, позволяющего визуализировать данные о ценах на недвижимость (точечная диаграмма), 
# отобразить с помощью библиотеки matplotlib полиномиальный график (степеней полинома 3, 4, 10) изменений цен на недвижимость.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
    
"""
    Считываем данные с файла
"""
df = pd.read_csv('data1.tsv', sep='\t', header=None)

X, Y = df[0], df[1]

x = list(X)
y = list(Y)


for i in range(len(y)):
    if math.isnan(y[i]):
        y[i] = 0
    else:
        y[i] = y[i]
"""
    Отображение координат точек из файла
"""
plt.scatter(x, y, c ='b', label = u'Данные из файла')

#print(df)


numpy_x = np.array(x)
numpy_y = np.array(y)



"""
    Отображении функций в зависимости от степени полиномы (3,4 и 10)
"""

func1 = np.poly1d(np.polyfit(numpy_x, numpy_y, 3))
plt.plot(x1, func1(x1),"r", label = u'Изображение полинома 3-ей степени')
func2 = np.poly1d(np.polyfit(numpy_x, numpy_y, 4))
plt.plot(x1, func2(x1),'y', label = u'Изображение полинома 4-ой степени')
func3 = np.poly1d(np.polyfit(numpy_x, numpy_y, 10))
plt.plot(x1, func3(x1), 'w',label = u'Изображение полинома 10-ой степени')

plt.title('Графики')
plt.grid(False)
plt.legend()
plt.xlabel('Ось x')
plt.ylabel('Ось y')
plt.show()
