from datetime import datetime
import matplotlib.pyplot as plt
from application.salary import calculate_salary
from application.db.people import get_employees

def print_current_date():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")

def plot_grath():
    # Задаем значения
    x = [2, 4, 7]
    y = [4, 8, 3]
    # Создаем график
    plt.plot(x, y, marker ='o')
    # Называем всё
    plt.title("Зависимость x от y")
    plt.xlabel("X ось")
    plt.ylabel("Y ось")
    # Команда вывода графика
    plt.show()



if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print_current_date()
    plot_grath()