# Задание 4.1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

x, y, areas = [], [], []

with open("price.csv") as file:
    reader = csv.reader(file, delimiter=';')
    for line in reader:
        areas.append(line[0])
        x.append(int(line[1]))
        y.append(int(line[2]))


xy = range(len(areas))

# Помещаем кортеж, содержащий фигуру и объект осей в переменные
fig, ax = plt.subplots()

plt.scatter(xy, x, label=u'1-комнатные', color='b')
plt.scatter(xy, y, label=u'2-комнатные', color='k')

plt.xlabel('Районы Санкт-Петербурга')
plt.ylabel('Стоимость')
plt.title('Cтоимость квартир по районам СПб')
plt.xticks(xs, areas)
fig.autofmt_xdate(rotation=45)
plt.legend()
plt.savefig('img.png', format='png')
plt.show()
