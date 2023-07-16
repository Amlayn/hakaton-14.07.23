import numpy as np
import matplotlib.pyplot as plt
import math


class Sigmoid:
    def __init__(self):
        self.max_price = 10000
        self.initial_price = 1500
        self.sigmoid_factor = 10  # Изменяем фактор для настройки крутизны сигмоиды
        self.demand_threshold = 0.95  # Устанавливаем порог спроса для переломной точки
    
    def adjust_ticket_price(self, num_tickets, num_sold):
        demand_percentage = num_sold / num_tickets  # Вычисляем процент спроса
        
        if demand_percentage >= self.demand_threshold:
            remaining_percentage = 0.05  # Устанавливаем оставшийся процент (3-5%, в данном случае 5%)
            demand_percentage = self.demand_threshold + remaining_percentage
        
        price_range = self.max_price - self.initial_price  # Вычисляем диапазон изменения цены

        # Применяем сигмоидную функцию к проценту спроса
        price_adjustment = price_range * (1 / (1 + math.exp(-self.sigmoid_factor * (demand_percentage - self.demand_threshold))))  # Меняем параметры сигмоида

        adjusted_price = self.initial_price + price_adjustment  # Корректируем цену
        
        return adjusted_price
    
    def graph(self, num_tickets):
        
        # Создаем массив значений для процента спроса от 0 до 1
        demand_percentages = np.linspace(0, 1, 100)

        # Вычисляем корректировку цены для каждого значения процента спроса
        adjusted_prices = [self.adjust_ticket_price(num_tickets, num_sold) for num_sold in demand_percentages * num_tickets]
        
        # Построение графика
        plt.plot(demand_percentages, adjusted_prices)
        plt.xlabel('Процент спроса')
        plt.ylabel('Корректировка цены')
        plt.title('График корректировки цены в зависимости от процента спроса')
        plt.axvline(x=self.demand_threshold, linestyle='--', color='r', label='Переломная точка (95%)')
        plt.legend()
        plt.show()


# def main():
#     sigma = Sigmoid()
#     sigma.adjust_ticket_price(800, 200)
#     sigma.graph(800)


# if __name__ == "__main__":
#     main()
 

