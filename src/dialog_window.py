import customtkinter as ctk
from customtkinter import CTkToplevel, CTkLabel, CTkButton, CTkFrame

class CreateDialog(CTkToplevel):
    def __init__(self, parent, selected_size):
        super().__init__(parent)
        self.selected_size = selected_size
        self.title("Создание карточек")
        self.geometry("400x300")
        self.resizable(False, False)
        self.configure(bg='#121212')

        # Делаем окно модальным
        self.transient(parent)
        self.grab_set()

        # Центрируем окно относительно родителя
        self.center_window()

        self.create_widgets()

    def center_window(self):
        """Центрирует окно относительно родительского"""
        self.update_idletasks()
        parent_x = self.master.winfo_x()
        parent_y = self.master.winfo_y()
        parent_width = self.master.winfo_width()
        parent_height = self.master.winfo_height()

        width = 400
        height = 300

        x = parent_x + (parent_width - width) // 2
        y = parent_y + (parent_height - height) // 2

        self.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):
        # Основной фрейм
        main_frame = CTkFrame(self, corner_radius=6)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Заголовок
        title_label = CTkLabel(main_frame,
                               text="Настройки создания",
                               text_color='#FFFFFF',
                               font=('Arial', 18))
        title_label.pack(pady=20)

        # Информация о выбранном размере
        size_label = CTkLabel(main_frame,
                              text=f"Выбранный размер: {self.selected_size}",
                              text_color='#FFFFFF',
                              font=('Arial', 14))
        size_label.pack(pady=10)

        # Кнопки действий
        button_frame = CTkFrame(main_frame, fg_color="transparent")
        button_frame.pack(pady=30)

        create_btn = CTkButton(button_frame,
                               text="Создать сейчас",
                               width=120,
                               height=40,
                               fg_color='#540070',
                               command=self.create_cards)
        create_btn.pack(side="left", padx=10)

        cancel_btn = CTkButton(button_frame,
                               text="Отмена",
                               width=120,
                               height=40,
                               fg_color='#666666',
                               command=self.destroy)
        cancel_btn.pack(side="left", padx=10)

    def create_cards(self):
        """Функция для создания карточек"""
        print(f"Создаем карточки с размером: {self.selected_size}")
        # Здесь ваша логика создания карточек
        self.destroy()