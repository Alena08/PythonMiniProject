
import tkinter as tk
from tkinter import ttk, messagebox

# --- ФУНКЦИИ ЛОГИКИ ---

def calculate_results():
    """Считывает оценки, вычисляет сумму и среднее, и обновляет метки."""
    
    grades = []
    # Попытка считать оценки из всех полей ввода
    try:
        # Получаем значения из полей ввода и конвертируем в float
        math_grade = float(math_entry.get())
        german_grade = float(german_entry.get())
        bio_grade = float(bio_entry.get())
        physics_grade = float(physics_entry.get())

        grades = [math_grade, german_grade, bio_grade, physics_grade]
        
    except ValueError:
        messagebox.showerror("Ошибка ввода", "Пожалуйста, введите корректные числа для всех оценок.")
        # Сбрасываем результат при ошибке
        result_sum_label.config(text="Сумма: N/A")
        result_avg_label.config(text="Среднее: N/A")
        return

    # Фильтруем только положительные оценки
    valid_grades = [g for g in grades if g >= 0]
    
    if not valid_grades:
        result_sum_label.config(text="Сумма: 0")
        result_avg_label.config(text="Среднее: 0")
        return

    # Вычисления
    total_sum = sum(valid_grades)
    count = len(valid_grades)
    average = total_sum / count

    # Обновление меток с результатами
    result_sum_label.config(text=f"Сумма: {total_sum:.2f}")
    result_avg_label.config(text=f"Среднее: {average:.2f}")
    
    # Для демонстрации раздельного вывода, как на макете:
    result_line1.config(text=f"Сумма: {total_sum:.2f}, Среднее: {average:.2f}")
    result_line2.config(text=f"Среднее: {average:.2f}, Сумма: {total_sum:.2f}")


def calculate_sum():
    """Вызывает основную функцию для вычисления и отображения суммы."""
    calculate_results()

def calculate_avg():
    """Вызывает основную функцию для вычисления и отображения среднего."""
    calculate_results()


# --- НАСТРОЙКА ОКНА ---
root = tk.Tk()
root.title("Программа ввода оценок")
# Стиль фона, как на макете (серый)
root.configure(bg='#cccccc') 

# --- НАСТРОЙКА GRID ---
# Колонка 0 (Метки) и Колонка 1 (Поля ввода)
root.grid_columnconfigure(0, weight=1) 
root.grid_columnconfigure(1, weight=1) 


# --- СОЗДАНИЕ ЭЛЕМЕНТОВ ФОРМЫ (МЕТКИ И ПОЛЯ ВВОДА) ---

# Функция для создания строки предмета
def create_subject_row(parent, subject_name, row):
    # Метка (стиль, как синий прямоугольник)
    label = ttk.Label(parent, text=subject_name, background="#87CEEB", foreground="black", 
                      anchor="center", padding=5, width=10)
    label.grid(row=row, column=0, padx=20, pady=10, sticky="ew")

    # Поле ввода (закругленное, как на макете)
    entry = ttk.Entry(parent, justify='center')
    entry.grid(row=row, column=1, padx=20, pady=10, sticky="ew")
    return entry

# 1. Mathe
math_entry = create_subject_row(root, "Mathe", 0)

# 2. Deutsch
german_entry = create_subject_row(root, "Deutsch", 1)

# 3. Bio
bio_entry = create_subject_row(root, "Bio", 2)

# 4. Physik
physics_entry = create_subject_row(root, "Physik", 3)


# --- КНОПКИ ---

# Фрейм для размещения кнопок по центру под полями ввода
button_frame = ttk.Frame(root, style='Background.TFrame')
# Объединяем фрейм кнопок в одну строку, занимающую обе колонки
button_frame.grid(row=4, column=0, columnspan=2, pady=20) 
button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)

# Создаем стиль для кнопок (имитация синих овалов)
style = ttk.Style()
# Создаем кастомный синий стиль, но Tkinter ttk не поддерживает нативные овалы без изображений
style.configure("Blue.TButton", background="#4169E1", foreground="white", 
                padding=10, relief="raised", font=('Arial', 10, 'bold'))
style.configure("Background.TFrame", background="#cccccc")


# Кнопка "Calculate Sum"
sum_button = ttk.Button(button_frame, text="Calculate Sum", command=calculate_sum, style="Blue.TButton")
sum_button.grid(row=0, column=0, padx=10, pady=5)

# Кнопка "Calculate Avg"
avg_button = ttk.Button(button_frame, text="Calculate Avg", command=calculate_avg, style="Blue.TButton")
avg_button.grid(row=0, column=1, padx=10, pady=5)


# --- РЕЗУЛЬТАТЫ ---

# Итоговая строка 1 (имитация нижнего синего прямоугольника)
result_line1 = ttk.Label(root, text="Сумма: 0.00, Среднее: 0.00", 
                        background="#87CEEB", foreground="black", anchor="center", 
                        padding=10, font=('Arial', 10, 'bold'))
result_line1.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

# Итоговая строка 2 (для дублирования, как на макете)
result_line2 = ttk.Label(root, text="Среднее: 0.00, Сумма: 0.00", 
                        background="#87CEEB", foreground="black", anchor="center", 
                        padding=10, font=('Arial', 10, 'bold'))
result_line2.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="ew")


root.mainloop()