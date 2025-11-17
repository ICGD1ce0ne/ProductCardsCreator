import customtkinter as ctk
from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkScrollbar

MainWindow = ctk.CTk()

MainWindow.title('ProductCardsCreator')
MainWindow.geometry('1485x900')
MainWindow.resizable(False, False)

MainWindow.configure(bg='#121212')


ProductFrame = CTkFrame(MainWindow,
                        width=860,
                        height=870,
                        corner_radius=6,
                        bg_color='#1A1A1A')
ProductFrame.place(x=15, y=15)

ProductCardLabel = CTkLabel(ProductFrame,
                            text='Карточки товаров',
                            text_color='#FFFFFF',
                            font=('Arial', 20))

MainWindow.update()
frame_width_product = ProductFrame.winfo_reqwidth()
label_width_product = ProductCardLabel.winfo_reqwidth()
position_settings_label = (frame_width_product - label_width_product) // 2

ProductCardLabel.place(x=position_settings_label, y=25)

ProductAddButton = CTkButton(ProductFrame,
                             width=330,
                             height=55,
                             text_color='#FFFFFF',
                             font=('Arial', 18),
                             text="Добавить",
                             fg_color='#540070',
                             corner_radius=9)

MainWindow.update()
frame_height_product = ProductFrame.winfo_reqheight()
add_product_button_height = ProductAddButton.winfo_reqheight()
position_add_product_button_y = (frame_height_product - add_product_button_height - 20)

frame_width_product = ProductFrame.winfo_reqwidth()
add_product_button_width = ProductAddButton.winfo_reqwidth()
position_add_product_button_x = (frame_width_product - add_product_button_width) // 2

ProductAddButton.place(x=position_add_product_button_x, y=position_add_product_button_y)



SettingsFrame = CTkFrame(MainWindow,
                         width=580,
                         height=870,
                         corner_radius=6,
                         bg_color='#1A1A1A'
                         )
SettingsFrame.place(x=890, y=15)

SettingsLabel = CTkLabel(SettingsFrame,
                         text='Выбор шаблона',
                         text_color='#FFFFFF',
                         font=('Arial', 20))

MainWindow.update()
frame_width_settings = SettingsFrame.winfo_reqwidth()
label_width_settings = SettingsLabel.winfo_reqwidth()
position_settings_label = (frame_width_settings - label_width_settings) // 2

SettingsLabel.place(x=position_settings_label, y=25)

MainWindow.mainloop()