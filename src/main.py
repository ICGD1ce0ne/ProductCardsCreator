import customtkinter as ctk
from customtkinter import CTkFrame

MainWindow = ctk.CTk()
MainWindow.title('ProductCardsCreator')
MainWindow.geometry('1485x900')
MainWindow.configure(bg='#121212')
MainWindow.resizable(False, False)

ProductFrame = CTkFrame(MainWindow,
                        width=860,
                        height=870,
                        corner_radius=6,
                        bg_color='#1A1A1A')
ProductFrame.place(x=15, y=15)

SettingsFrame = CTkFrame(MainWindow,
                         width=580,
                         height=870,
                         corner_radius=6,
                         bg_color='#1A1A1A'
                         )
SettingsFrame.place(x=890, y=15)
MainWindow.mainloop()
