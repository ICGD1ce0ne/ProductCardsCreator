import customtkinter as ctk
from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkScrollableFrame

MainWindow = ctk.CTk()

MainWindow.title('ProductCardsCreator')
MainWindow.geometry('1485x865')
MainWindow.resizable(False, False)

MainWindow.configure(bg='#121212')

LeftFramesPositionFromX = 15
RightFramesPositionFromX = 890

# Высота левых фреймов
product_label_height = 60
product_scroll_height = 670
product_button_height = 70

# Отступы между фреймами
top_margin = 15
between_margin = 15
bottom_margin = 15

# Общая высота левых фреймов с отступами
total_left_height = (product_label_height + product_scroll_height +
                     product_button_height + between_margin * 2)

# Высота для правого фрейма
settings_frame_height = total_left_height



ProductLabelFrame = CTkFrame(MainWindow,
                             width=860,
                             height=product_label_height,
                             corner_radius=6)
ProductLabelFrame.place(x=LeftFramesPositionFromX, y=top_margin)

ProductLabel = CTkLabel(ProductLabelFrame,
                        text='Добавленные карточки',
                        text_color='#FFFFFF',
                        font=('Arial', 20))

MainWindow.update()
frame_width_product_label = ProductLabelFrame.winfo_reqwidth()
label_width_product = ProductLabel.winfo_reqwidth()
position_product_label_x = (frame_width_product_label - label_width_product) // 2

frame_height_product_label = ProductLabelFrame.winfo_reqheight()
label_height_product = ProductLabel.winfo_reqheight()
position_product_label_y = (frame_height_product_label - label_height_product) // 2

ProductLabel.place(x=position_product_label_x, y=position_product_label_y)



ProductScrollBarFrame = CTkFrame(MainWindow,
                                 width=860,
                                 height=product_scroll_height,
                                 corner_radius=6)
ProductScrollBarFrame.place(x=LeftFramesPositionFromX, y=top_margin + product_label_height + between_margin)

ProductScrollableFrame = CTkScrollableFrame(MainWindow,
                                          width=840,
                                          height=product_scroll_height - 5,
                                          corner_radius=6)
ProductScrollableFrame.place(x=LeftFramesPositionFromX, y=top_margin + product_label_height + between_margin)



ProductAddButtonFrame = CTkFrame(MainWindow,
                                 width=860,
                                 height=product_button_height,
                                 corner_radius=6,
                                 fg_color="transparent")
ProductAddButtonFrame.place(x=LeftFramesPositionFromX,
                            y=top_margin + product_label_height + between_margin + product_scroll_height + between_margin)

# Создаем обе кнопки в основном фрейме
ProductButtonAdd = CTkButton(ProductAddButtonFrame,
                             width=330,
                             height=55,
                             text_color='#FFFFFF',
                             font=('Arial', 18),
                             text="Добавить",
                             fg_color='#540070',
                             corner_radius=9)

ProductButtonCreate = CTkButton(ProductAddButtonFrame,
                                width=330,
                                height=55,
                                text_color='#FFFFFF',
                                font=('Arial', 18),
                                text="Создать",
                                fg_color='#540070',
                                corner_radius=9)

# Обновляем окно для получения актуальных размеров
MainWindow.update()

# Получаем размеры фрейма и кнопок
frame_width_product = ProductAddButtonFrame.winfo_reqwidth()
frame_height_product = ProductAddButtonFrame.winfo_reqheight()

add_product_button_width = ProductButtonAdd.winfo_reqwidth()
add_product_button_height = ProductButtonAdd.winfo_reqheight()

# Отступ между кнопками
button_spacing = 12

# Общая ширина двух кнопок с отступом
total_buttons_width = add_product_button_width * 2 + button_spacing

# Позиционирование по Y (одинаково для обеих кнопок)
position_y = (frame_height_product - add_product_button_height) // 2

# Позиционирование по X для первой кнопки (левая)
position_button_add_x = (frame_width_product - total_buttons_width) // 2

# Позиционирование по X для второй кнопки (правая)
position_button_create_x = position_button_add_x + add_product_button_width + button_spacing

# Размещаем кнопки в основном фрейме
ProductButtonAdd.place(x=position_button_add_x, y=position_y)
ProductButtonCreate.place(x=position_button_create_x, y=position_y)



SettingsFrame = CTkFrame(MainWindow,
                         width=580,
                         height=settings_frame_height,
                         corner_radius=6)
SettingsFrame.place(x=RightFramesPositionFromX, y=top_margin)

SettingsLabel = CTkLabel(SettingsFrame,
                         text='Выбор шаблона',
                         text_color='#FFFFFF',
                         font=('Arial', 20))

MainWindow.update()
frame_width_settings = SettingsFrame.winfo_reqwidth()
label_width_settings = SettingsLabel.winfo_reqwidth()
position_settings_label = (frame_width_settings - label_width_settings) // 2

SettingsLabel.place(x=position_settings_label, y=position_product_label_y)

MainWindow.mainloop()