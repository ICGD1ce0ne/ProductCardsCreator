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
                        text='Выбор шаблона',
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
                                 corner_radius=6)
ProductAddButtonFrame.place(x=LeftFramesPositionFromX,
                            y=top_margin + product_label_height + between_margin + product_scroll_height + between_margin)

ProductAddButton = CTkButton(ProductAddButtonFrame,
                             width=330,
                             height=55,
                             text_color='#FFFFFF',
                             font=('Arial', 18),
                             text="Добавить",
                             fg_color='#540070',
                             corner_radius=9)

MainWindow.update()
frame_height_product = ProductAddButtonFrame.winfo_reqheight()
add_product_button_height = ProductAddButton.winfo_reqheight()
position_add_product_button_y = (frame_height_product - add_product_button_height) // 2

frame_width_product = ProductAddButtonFrame.winfo_reqwidth()
add_product_button_width = ProductAddButton.winfo_reqwidth()
position_add_product_button_x = (frame_width_product - add_product_button_width) // 2

ProductAddButton.place(x=position_add_product_button_x, y=position_add_product_button_y)

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