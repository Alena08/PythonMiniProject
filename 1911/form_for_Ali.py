import json
import csv
import os
import tkinter as tk
from tkinter import messagebox, ttk
from typing import List, Dict, Any, Optional

# --- 1. Datenstruktur für eine Person ---
class Person:
    """Представляет одного сотрудника с основной информацией."""
    def __init__(self, vorname: str, nachname: str, personal_id: str):
        self.vorname = vorname
        self.nachname = nachname
        self.personal_id = personal_id

    def __str__(self) -> str:
        """Возвращает читабельное строковое представление для отображения в списке."""
        return f"ID: {self.personal_id:10} | Фамилия: {self.nachname:15} | Имя: {self.vorname:10}"

    def to_dict(self) -> Dict[str, str]:
        """Конвертирует объект Person в словарь (для JSON/CSV)."""
        return {
            "Vorname": self.vorname,
            "Nachname": self.nachname,
            "Personal-ID": self.personal_id
        }

# --- 2. Datenspeicher- und Serialisierungslogik ---
class DataStorage:
    """Управляет сохранением и загрузкой данных персонала в различных форматах."""
    
    STORAGE_FORMAT = "JSON"
    FILENAME = "personal_data"
    
    @staticmethod
    def set_format(format_choice: str):
        """Устанавливает формат сохранения (CSV, TXT, JSON)."""
        valid_formats = ["CSV", "TXT", "JSON"]
        if format_choice.upper() in valid_formats:
            DataStorage.STORAGE_FORMAT = format_choice.upper()
        
    @staticmethod
    def get_filepath() -> str:
        """Возвращает полный путь к файлу на основе выбранного формата."""
        ext = DataStorage.STORAGE_FORMAT.lower()
        return f"{DataStorage.FILENAME}.{ext}"

    @staticmethod
    def save(personen: List[Person]):
        """Сохраняет список сотрудников в выбранном формате."""
        filepath = DataStorage.get_filepath()
        data = [p.to_dict() for p in personen]

        try:
            if DataStorage.STORAGE_FORMAT == "JSON":
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
            
            elif DataStorage.STORAGE_FORMAT == "CSV":
                fieldnames = ["Vorname", "Nachname", "Personal-ID"]
                with open(filepath, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')
                    writer.writeheader()
                    writer.writerows(data)
            
            elif DataStorage.STORAGE_FORMAT == "TXT":
                with open(filepath, 'w', encoding='utf-8') as f:
                    for item in data:
                        f.write(f"{item['Vorname']}|{item['Nachname']}|{item['Personal-ID']}\n")
            
            return f"Данные успешно сохранены в формате {DataStorage.STORAGE_FORMAT} в '{filepath}'."
        
        except Exception as e:
            return f"Ошибка при сохранении данных: {e}"

    @staticmethod
    def load() -> List[Person]:
        """Загружает сотрудников из файла в выбранном формате."""
        filepath = DataStorage.get_filepath()
        personen = []
        
        if not os.path.exists(filepath):
            return []

        try:
            data: List[Dict[str, str]] = []
            
            if DataStorage.STORAGE_FORMAT == "JSON":
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            
            elif DataStorage.STORAGE_FORMAT == "CSV":
                with open(filepath, 'r', newline='', encoding='utf-8') as f:
                    reader = csv.DictReader(f, delimiter=';')
                    data = list(reader)
            
            elif DataStorage.STORAGE_FORMAT == "TXT":
                with open(filepath, 'r', encoding='utf-8') as f:
                    for line in f:
                        parts = line.strip().split('|')
                        if len(parts) == 3:
                            data.append({
                                "Vorname": parts[0],
                                "Nachname": parts[1],
                                "Personal-ID": parts[2]
                            })
            
            for item in data:
                personen.append(Person(
                    item["Vorname"],
                    item["Nachname"],
                    item["Personal-ID"]
                ))
            
            return personen

        except Exception:
            # Ошибка при загрузке (например, поврежден файл), возвращаем пустой список
            return []

# --- 3. Personalverwaltung (CRUD-Operationen) ---
class PersonalManager:
    """Управляет списком сотрудников и выполняет операции CRUD."""
    def __init__(self):
        self.personen = DataStorage.load()
        self.next_id = 1000 + len(self.personen)

    def _get_next_id(self) -> str:
        """Генерирует уникальный ID сотрудника."""
        current_id = self.next_id
        self.next_id += 1
        return f"P{current_id:04d}"

    def anlegen(self, vorname: str, nachname: str):
        """Создает нового сотрудника и добавляет в список."""
        personal_id = self._get_next_id()
        neue_person = Person(vorname, nachname, personal_id)
        self.personen.append(neue_person)
        return f"Сотрудник '{vorname} {nachname}' (ID: {personal_id}) добавлен."

    def anzeigen(self, personal_id: str) -> Optional[Person]:
        """Ищет и возвращает сотрудника по ID."""
        for p in self.personen:
            if p.personal_id == personal_id:
                return p
        return None

    def bearbeiten(self, personal_id: str, new_vorname: str, new_nachname: str) -> bool:
        """Обновляет данные существующего сотрудника."""
        for p in self.personen:
            if p.personal_id == personal_id:
                p.vorname = new_vorname
                p.nachname = new_nachname
                return True
        return False

    def loeschen(self, personal_id: str) -> bool:
        """Удаляет сотрудника по его ID."""
        initial_len = len(self.personen)
        self.personen = [p for p in self.personen if p.personal_id != personal_id]
        return len(self.personen) < initial_len

    def finden(self, suchbegriff: str, suchfeld: str) -> List[Person]:
        """Ищет сотрудников по заданному критерию."""
        ergebnisse = []
        suchbegriff = suchbegriff.lower()

        for p in self.personen:
            if suchfeld == "Vorname" and p.vorname.lower().startswith(suchbegriff):
                ergebnisse.append(p)
            elif suchfeld == "Nachname" and p.nachname.lower().startswith(suchbegriff):
                ergebnisse.append(p)
            elif suchfeld == "Personal-ID" and p.personal_id.lower().startswith(suchbegriff):
                ergebnisse.append(p)
        
        return ergebnisse

# --- 4. GUI-Anwendung mit Tkinter ---

class PersonalApp(tk.Tk):
    """Основное приложение для управления персоналом с графическим интерфейсом."""
    def __init__(self):
        super().__init__()
        self.title("Программа управления персоналом")
        self.geometry("800x600")
        
        # Переменные состояния
        self.manager = PersonalManager()
        self.storage_format_var = tk.StringVar(value=DataStorage.STORAGE_FORMAT)

        # Создаем Notebook (вкладки)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, padx=10, fill="both", expand=True)

        # Создаем вкладки
        self.tab_management = ttk.Frame(self.notebook)
        self.tab_settings = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_management, text=" Управление персоналом ")
        self.notebook.add(self.tab_settings, text=" Настройки и сохранение ")

        # Инициализируем элементы управления
        self._setup_management_tab()
        self._setup_settings_tab()
        
        # Обновляем список при запуске
        self._update_listbox()
        
        # Вывод приветственного сообщения
        if not self.manager.personen:
             messagebox.showinfo("Информация", "Список сотрудников пуст. Добавьте новых людей.")
        else:
             messagebox.showinfo("Информация", f"Загружено {len(self.manager.personen)} сотрудников из {DataStorage.STORAGE_FORMAT}.")

    # --- Установка вкладки Управление персоналом ---
    def _setup_management_tab(self):
        # Фрейм для ввода данных (слева)
        input_frame = ttk.LabelFrame(self.tab_management, text=" Данные сотрудника ")
        input_frame.pack(side="left", padx=10, pady=10, fill="y")
        
        # Поля ввода
        self.vorname_var = tk.StringVar()
        self.nachname_var = tk.StringVar()
        self.personal_id_var = tk.StringVar(value="ID") # Используется для отображения ID выбранного сотрудника

        ttk.Label(input_frame, text="Имя:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(input_frame, textvariable=self.vorname_var, width=25).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(input_frame, text="Фамилия:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(input_frame, textvariable=self.nachname_var, width=25).grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(input_frame, text="ID (выбранного):").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        ttk.Label(input_frame, textvariable=self.personal_id_var, width=15, anchor="w").grid(row=2, column=1, sticky="w", padx=5, pady=5)

        # Кнопки CRUD
        btn_frame = ttk.Frame(input_frame)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=10)
        
        ttk.Button(btn_frame, text="Добавить", command=self._anlegen).pack(fill="x", padx=5, pady=5)
        ttk.Button(btn_frame, text="Обновить", command=self._bearbeiten).pack(fill="x", padx=5, pady=5)
        ttk.Button(btn_frame, text="Удалить", command=self._loeschen).pack(fill="x", padx=5, pady=5)
        ttk.Button(btn_frame, text="Очистить поля", command=self._clear_input_fields).pack(fill="x", padx=5, pady=5)


        # Фрейм для списка и поиска (справа)
        list_search_frame = ttk.Frame(self.tab_management)
        list_search_frame.pack(side="right", padx=10, pady=10, fill="both", expand=True)
        
        # Поиск
        search_frame = ttk.LabelFrame(list_search_frame, text=" Поиск ")
        search_frame.pack(fill="x", padx=5, pady=5)
        
        self.search_term_var = tk.StringVar()
        self.search_field_var = tk.StringVar(value="Nachname") # По умолчанию поиск по Фамилии
        
        ttk.Label(search_frame, text="Поле:").pack(side="left", padx=5)
        ttk.Combobox(search_frame, textvariable=self.search_field_var, 
                     values=["Vorname", "Nachname", "Personal-ID"], state="readonly", width=12).pack(side="left", padx=5)
                     
        ttk.Label(search_frame, text="Запрос:").pack(side="left", padx=5)
        ttk.Entry(search_frame, textvariable=self.search_term_var, width=25).pack(side="left", padx=5, fill="x", expand=True)
        
        ttk.Button(search_frame, text="Найти", command=self._finden).pack(side="left", padx=5)
        ttk.Button(search_frame, text="Сброс", command=self._update_listbox).pack(side="left", padx=5)


        # Список сотрудников
        ttk.Label(list_search_frame, text="Список сотрудников:").pack(fill="x", padx=5, pady=(10, 0))
        self.listbox = tk.Listbox(list_search_frame, height=20, font=("Courier", 10))
        self.listbox.pack(fill="both", expand=True, padx=5, pady=5)
        self.listbox.bind('<<ListboxSelect>>', self._item_selected)

    # --- Установка вкладки Настройки и сохранение ---
    def _setup_settings_tab(self):
        settings_frame = ttk.LabelFrame(self.tab_settings, text=" Выбор формата данных ")
        settings_frame.pack(padx=20, pady=20, fill="x")

        # Radiobuttons для выбора формата
        formats = [("CSV", "CSV"), ("TXT", "TXT"), ("JSON", "JSON")]
        
        for text, mode in formats:
            ttk.Radiobutton(settings_frame, text=text, variable=self.storage_format_var, 
                            value=mode, command=self._set_storage_format).pack(anchor="w", padx=10, pady=5)
                            
        ttk.Label(settings_frame, textvariable=self.storage_format_var).pack(anchor="w", padx=10, pady=10)

        # Кнопки сохранения/загрузки
        save_load_frame = ttk.LabelFrame(self.tab_settings, text=" Управление файлами ")
        save_load_frame.pack(padx=20, pady=10, fill="x")
        
        ttk.Button(save_load_frame, text="Сохранить данные", command=self._save_data).pack(fill="x", padx=10, pady=5)
        ttk.Button(save_load_frame, text="Загрузить данные (переключить формат)", command=self._load_data).pack(fill="x", padx=10, pady=5)

    # --- Методы логики GUI ---

    def _update_listbox(self, personen_list: Optional[List[Person]] = None):
        """Обновляет содержимое Listbox."""
        self.listbox.delete(0, tk.END)
        
        if personen_list is None:
            personen_list = self.manager.personen

        for p in personen_list:
            self.listbox.insert(tk.END, str(p))
            
    def _clear_input_fields(self):
        """Очищает поля ввода."""
        self.vorname_var.set("")
        self.nachname_var.set("")
        self.personal_id_var.set("ID")
            
    def _item_selected(self, event):
        """Обрабатывает выбор элемента в списке."""
        selected_indices = self.listbox.curselection()
        if not selected_indices:
            return
            
        selected_item_index = selected_indices[0]
        # Используем индекс, чтобы получить объект Person из списка менеджера
        
        # Получаем данные из listbox (чтобы найти ID)
        listbox_text = self.listbox.get(selected_item_index)
        # Извлекаем ID (например, P1000)
        selected_id = listbox_text.split('|')[0].strip().split(': ')[1]
        
        person = self.manager.anzeigen(selected_id)
        if person:
            self.vorname_var.set(person.vorname)
            self.nachname_var.set(person.nachname)
            self.personal_id_var.set(person.personal_id)

    # --- Методы CRUD (связаны с менеджером) ---

    def _anlegen(self):
        """Создать новую Person."""
        vorname = self.vorname_var.get().strip()
        nachname = self.nachname_var.get().strip()
        
        if not vorname or not nachname:
            messagebox.showerror("Ошибка", "Имя и Фамилия не могут быть пустыми.")
            return

        result_message = self.manager.anlegen(vorname, nachname)
        messagebox.showinfo("Успех", result_message)
        self._clear_input_fields()
        self._update_listbox()
        
    def _bearbeiten(self):
        """Отредактировать выбранную Person."""
        pid = self.personal_id_var.get()
        new_vorname = self.vorname_var.get().strip()
        new_nachname = self.nachname_var.get().strip()

        if pid == "ID" or not pid:
            messagebox.showerror("Ошибка", "Сотрудник для обновления не выбран.")
            return

        if self.manager.bearbeiten(pid, new_vorname, new_nachname):
            messagebox.showinfo("Успех", f"Данные сотрудника ID {pid} обновлены.")
            self._clear_input_fields()
            self._update_listbox()
        else:
            messagebox.showerror("Ошибка", f"Не удалось найти сотрудника с ID {pid}.")
            
    def _loeschen(self):
        """Удалить выбранную Person."""
        pid = self.personal_id_var.get()
        
        if pid == "ID" or not pid:
            messagebox.showerror("Ошибка", "Сотрудник для удаления не выбран.")
            return
            
        if messagebox.askyesno("Подтверждение", f"Вы уверены, что хотите удалить сотрудника ID {pid}?"):
            if self.manager.loeschen(pid):
                messagebox.showinfo("Успех", f"Сотрудник ID {pid} удален.")
                self._clear_input_fields()
                self._update_listbox()
            else:
                messagebox.showerror("Ошибка", f"Не удалось найти сотрудника с ID {pid}.")

    def _finden(self):
        """Найти Person по заданным параметрам."""
        term = self.search_term_var.get().strip()
        field = self.search_field_var.get()
        
        if not term:
            messagebox.showinfo("Поиск", "Введите запрос для поиска.")
            self._update_listbox() # Показываем полный список
            return

        results = self.manager.finden(term, field)
        
        if results:
            self._update_listbox(results)
            messagebox.showinfo("Поиск", f"Найдено {len(results)} сотрудников.")
        else:
            self.listbox.delete(0, tk.END)
            self.listbox.insert(tk.END, "Ничего не найдено.")
            messagebox.showinfo("Поиск", "Ничего не найдено.")

    # --- Методы сохранения/загрузки ---

    def _set_storage_format(self):
        """Обновляет формат сохранения в классе DataStorage."""
        DataStorage.set_format(self.storage_format_var.get())
        messagebox.showinfo("Формат изменен", f"Формат сохранения установлен на {DataStorage.STORAGE_FORMAT}.")

    def _save_data(self):
        """Сохраняет данные в текущем формате и файле."""
        message = DataStorage.save(self.manager.personen)
        messagebox.showinfo("Сохранение", message)

    def _load_data(self):
        """Загружает данные, используя текущий формат (если он был только что изменен)."""
        # Сначала устанавливаем формат из RadioButton
        self._set_storage_format() 
        
        # Перезагружаем менеджер
        old_count = len(self.manager.personen)
        self.manager = PersonalManager()
        
        # Обновляем GUI
        self._update_listbox()
        new_count = len(self.manager.personen)
        
        messagebox.showinfo("Загрузка", 
                            f"Загрузка завершена. Загружено {new_count} сотрудников из {DataStorage.STORAGE_FORMAT}. (Предыдущий список был {old_count} чел.)")


# --- Запуск программы ---

if __name__ == "__main__":
    # В GUI-приложении не требуется отдельный логин, 
    # но можно вставить его перед запуском mainloop, если нужно
    # Для простоты, запускаем приложение сразу.
    app = PersonalApp()
    app.mainloop()