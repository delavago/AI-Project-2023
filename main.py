import Diagnosis_form

from tkinter import *
import customtkinter
from pyswip import Prolog


prolog = Prolog()

# connects the prolog to python
# change file name to file path on your machine

prolog.consult(
    'data/knowledge_base.pl')
#c = list(prolog.query("illness(Who)"))

# Home Page of Expert Systems
customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window


app.title("Covid-19 Diagnosis System")
app.geometry("650x500")
app.resizable(False, False)


title_head = customtkinter.CTkFont(family="Helvetica", size=18, weight="bold")
head = customtkinter.CTkLabel(app,
             text="Welcome to the Ministry of Health's Covid-19 patient Diagnosis System", font=title_head, anchor="center")

first = customtkinter.CTkButton(app,
                                width=200,
                                 height=100,
                                 border_width=0,
                                 corner_radius=8,
               text="Diagnose Patient",
               command=Diagnosis_form.Diagnosis
               )

def view_stats():
    Stats = list(prolog.query("stats_display_python"))

    print(Stats)


second = customtkinter.CTkButton(app,
                                width=200,
                                 height=100,
                                 border_width=0,
                                 corner_radius=8,
                text="Covid Statistics",
                command=view_stats
                )
first.grid(row=1, column=0, padx=5, pady=20)
second.grid(row=2, column=0, padx=5, pady=20)
head.grid(row=0, column=0, padx=10, pady=20)
app.mainloop()
