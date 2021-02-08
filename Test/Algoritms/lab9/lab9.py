from sklearn import datasets
import pandas as pd
import numpy as np

# Загрузка основной инфы для ирисов
iris = datasets.load_iris()
print(iris)
# Создаём двумерную таблицу, и вставляем инфу о длине\ширине чашелистика, и о длине\ширине лепестка
iris_frame = pd.DataFrame(iris.data)
# Подписываем индексы
iris_frame.columns = iris.feature_names

# Добавляем столбец с целевой переменной (0 - setosa, 1 - versicolor, 2 - virginica)
iris_frame['target'] = iris.target
# Для наглядности добавляем столбец с сортами
iris_frame['name'] = iris_frame.target.apply(lambda x: iris.target_names[x])

#iris_frame

alpha = 0.00003

weight_1_2 = np.random.randn(4, 4)
weight_2_3 = np.random.randn(4, 4)
weight_3_4 = np.random.randn(4, 4)
weight_4_5 = np.random.randn(4, 1)

print(weight_1_2, weight_2_3, weight_3_4, weight_4_5, sep="\n\n")

for iteration in range(250):
    for i in range(len(iris_frame["sepal length (cm)"])):
        inp = [iris_frame["sepal length (cm)"][i], iris_frame["sepal width (cm)"][i],
               iris_frame["petal length (cm)"][i], iris_frame["petal width (cm)"][i]]
        goal_pred = iris_frame["target"][i]

        layer_2 = np.dot(inp, weight_1_2)
        layer_3 = np.dot(layer_2, weight_2_3)
        layer_4 = np.dot(layer_3, weight_3_4)
        pred = np.sum(np.dot(layer_4, weight_4_5))
        if iteration % 100 == 0:
            if pred <= 0.5:
                print("It is a - setosa", goal_pred, pred)
            elif pred > 0.7 and pred <= 1.5:
                print("It is a - versicolor", goal_pred, pred)
            elif pred > 1.7 and pred <= 2.5:
                print("It is a - virginica", goal_pred, pred)
            else:
                print("I dont know", goal_pred, pred)

        error = (pred - goal_pred) ** 2
        layer_5_delta = pred - goal_pred
        layer_4_delta = np.sum(np.dot(layer_5_delta, weight_4_5))
        layer_3_delta = np.sum(np.dot(layer_4_delta, weight_3_4))
        layer_2_delta = np.sum(np.dot(layer_3_delta, weight_2_3))

        weight_delta_1_2 = np.zeros(weight_1_2.shape)
        weight_delta_2_3 = np.zeros(weight_2_3.shape)
        weight_delta_3_4 = np.zeros(weight_3_4.shape)
        weight_delta_4_5 = np.zeros(weight_4_5.shape)

        for k in range(len(weight_delta_1_2)):
            for j in range(len(weight_delta_1_2[k])):
                weight_delta_1_2[k][j] = inp[k] * layer_2_delta

        for k in range(len(weight_delta_2_3)):
            for j in range(len(weight_delta_2_3[k])):
                weight_delta_2_3[k][j] = np.sum(layer_2.T[j]) * layer_3_delta

        for k in range(len(weight_delta_3_4)):
            for j in range(len(weight_delta_3_4[k])):
                weight_delta_3_4[k][j] = np.sum(layer_3.T[j]) * layer_4_delta

        for k in range(len(weight_delta_4_5)):
            weight_delta_4_5[k] = np.sum(layer_4.T[k]) * layer_5_delta

        for k in range(len(weight_1_2)):
            for j in range(len(weight_1_2)):
                weight_1_2[k][j] -= weight_delta_1_2[k][j] * alpha

        for k in range(len(weight_2_3)):
            for j in range(len(weight_2_3)):
                weight_2_3[k][j] -= weight_delta_2_3[k][j] * alpha

        for k in range(len(weight_3_4)):
            for j in range(len(weight_3_4)):
                weight_3_4[k][j] -= weight_delta_3_4[k][j] * alpha

        for k in range(len(weight_4_5)):
            weight_4_5[k] -= weight_delta_4_5[k] * alpha

    print(iteration, error, sep=" --- ")

    for i in range(len(iris_frame["sepal length (cm)"])):
        inp = [iris_frame["sepal length (cm)"][i], iris_frame["sepal width (cm)"][i],
               iris_frame["petal length (cm)"][i], iris_frame["petal width (cm)"][i]]
        goal_pred = iris_frame["target"][i]

        layer_2 = np.dot(inp, weight_1_2)
        layer_3 = np.dot(layer_2, weight_2_3)
        layer_4 = np.dot(layer_3, weight_3_4)
        pred = np.sum(np.dot(layer_4, weight_4_5))
        if pred <= 0.5:
            print("It is a - setosa", goal_pred, pred)
        elif pred > 0.5 and pred <= 1.7:
            print("It is a - versicolor", goal_pred, pred)
        elif pred > 1.7:
            print("It is a - virginica", goal_pred, pred)
        else:
            print("I dont know", goal_pred, pred)