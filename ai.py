import pandas as pd
import tensorflow as tf


import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from keras import regularizers
from keras.models import Sequential
from keras.layers import Dense


def calculate_reward(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    if mse < 100:
        reward = 10
    elif 100 <= mse < 200:
        reward = 5
    else:
        reward = 1
    
    return reward


def ai_create_data():
    # Загрузка данных из первого файла xlsx (данные за год)
    data1 = pd.read_excel('data/СВОД 2022.xlsx')

    # Загрузка данных из второго файла xlsx (данные за следующий год)
    data2 = pd.read_excel('data/СВОД 2023 6 мес.xlsx')

    # Объединение данных из двух файлов
    data = pd.concat([data1, data2])
    print(data)


    # Учет инфляции 10% годовых
    # data['Итого сумма билета'] = data['Итого сумма билета'] * 1.1

    # Выбор нужных столбцов для обучения
    features = data[['Месяц операции', 'Тип обсл', 'Кол-во прод мест', 'Расстояние']]

    # Выбор столбца с целевой переменной (ценой билета)
    target = data['Итого сумма билета']

    # Разделение данных на обучающую и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)


    # Создание нейронной сети
    model = Sequential()    
    model.add(Dense(16, activation='relu', kernel_regularizer=regularizers.l2(0.01)))
    model.add(Dense(8, activation='relu', kernel_regularizer=regularizers.l2(0.01)))
    model.add(Dense(1, activation='linear'))
    model.compile(optimizer="adam", loss='mean_squared_error', metrics=['mean_absolute_error'])
    

    rewards = []
    for epoch in range(1):
        # Компиляция и обучение модели
        model.fit(X_train, y_train, epochs=140, batch_size=32, verbose=1, callbacks=[tf.keras.callbacks.History()])
        
        predictions = model.predict(X_test)
        reward = calculate_reward(y_test, predictions)
        rewards.append(reward)
    print("Reward for neural network model:", reward)

    # Оцените прогнозы
    mse = mean_squared_error(y_test, predictions)
    print('Mean Squared Error:', mse)

  
    plt.figure(figsize=(10, 6))
    plt.scatter(range(len(y_test)), y_test, label='True values', marker='o')
    plt.scatter(range(len(predictions)), predictions, label='Predicted values', marker='x')
    plt.xlabel('Sample index')
    plt.ylabel('Value')
    plt.title('Comparison of true and predicted values')
    plt.legend()

    # Добавление графика награды
    plt.twinx()
    plt.plot(rewards, color='red', label='Reward')
    plt.ylabel('Reward')

    plt.legend()
    plt.show()
    
    # Вывод значений

    return predictions.tolist()


