from tkinter import messagebox, Canvas, StringVar
import customtkinter
from pyswip import Prolog


# Patient Diagnositics Form

# customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
# customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

def Diagnosis():
    window = customtkinter.CTk()
    window.title("Covid-19 Diagnosis System")
    window.geometry("1000x500")
    window.resizable(True, True)
    
    
    scrollable_frame = customtkinter.CTkScrollableFrame(window, width=1000, height=500)
    scrollable_frame.grid(row=0, column=0, sticky="nsew")
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    namelabel = customtkinter.CTkLabel(scrollable_frame, text="Full Name: ")
    agelabel = customtkinter.CTkLabel(scrollable_frame, text="Age: ")
    templabel = customtkinter.CTkLabel(scrollable_frame, text="Temperature (Celsius): ")
    genderlabel = customtkinter.CTkLabel(scrollable_frame, text="Gender: ")
    syslabel = customtkinter.CTkLabel(scrollable_frame, text="Systolic Reading: ")
    dialabel = customtkinter.CTkLabel(scrollable_frame, text="Diastolic Reading: ")
    symlabel = customtkinter.CTkLabel(
        scrollable_frame, text="Have you experienced any of the following symptoms? ")
    diasym1 = customtkinter.CTkLabel(scrollable_frame, text="Dizziness")
    diasym2 = customtkinter.CTkLabel(scrollable_frame, text="Fainting")
    diasym3 = customtkinter.CTkLabel(scrollable_frame, text="Blurred Vision")
    covidlabel = customtkinter.CTkLabel(
        scrollable_frame, text="Have you experienced any of the following symptoms lately?")
    covid_symptom1 = customtkinter.CTkLabel(scrollable_frame, text="Fever")
    covid_symptom2 = customtkinter.CTkLabel(scrollable_frame, text="Cough")
    covid_symptom3 = customtkinter.CTkLabel(scrollable_frame, text="Fatigue")
    covid_symptom4 = customtkinter.CTkLabel(scrollable_frame, text="Loss of Taste")
    covid_symptom5 = customtkinter.CTkLabel(scrollable_frame, text="Headache")
    covid_symptom6 = customtkinter.CTkLabel(scrollable_frame, text="Runny Nose")
    covid_symptom7 = customtkinter.CTkLabel(scrollable_frame, text="Sore Throat")
    covid_symptom8 = customtkinter.CTkLabel(scrollable_frame, text="Muscle Pain")
    covid_symptom9 = customtkinter.CTkLabel(scrollable_frame, text="Difficulty Breathing")
    covid_symptom10 = customtkinter.CTkLabel(scrollable_frame, text="Sneezing")
    covid_symptom11 = customtkinter.CTkLabel(scrollable_frame, text="Chest Pain")
    covid_symptom12 = customtkinter.CTkLabel(scrollable_frame, text="Burst of Confusion")
    covid_symptom13 = customtkinter.CTkLabel(scrollable_frame, text="Loss of Speech or Mobility")
    underlyinglabel = customtkinter.CTkLabel(
        scrollable_frame, text="Do you or your family have a history of any of the following conditions?")
    underlyingsymp1 = customtkinter.CTkLabel(scrollable_frame, text="Cancer")
    underlyingsymp2 = customtkinter.CTkLabel(scrollable_frame, text="Stroke")

    underlyingsymp4 = customtkinter.CTkLabel(scrollable_frame, text="Sickle Cell")

    underlyingsymp6 = customtkinter.CTkLabel(scrollable_frame, text="Heart Conditions")
    underlyingsymp7 = customtkinter.CTkLabel(scrollable_frame, text="Diabetes")
    underlyingsymp8 = customtkinter.CTkLabel(scrollable_frame, text="Alzheimers")

    underlyingsymp10 = customtkinter.CTkLabel(scrollable_frame, text="Cystic Fibrosis")
    underlyingsymp11 = customtkinter.CTkLabel(scrollable_frame, text="Lung Disease")
    underlyingsymp12 = customtkinter.CTkLabel(scrollable_frame, text="Liver Disease")
    underlyingsymp13 = customtkinter.CTkLabel(scrollable_frame, text="Kidney Disease")

    nameentry = customtkinter.CTkEntry(scrollable_frame)
    ageentry = customtkinter.CTkEntry(scrollable_frame)
    tempentry = customtkinter.CTkEntry(scrollable_frame)
    sysentry = customtkinter.CTkEntry(scrollable_frame)
    diaentry = customtkinter.CTkEntry(scrollable_frame)

    w = Canvas(scrollable_frame, width=2, height=220)
    w.create_rectangle(0, 0, 220, 220, fill="black")

    s = Canvas(scrollable_frame, width=2, height=220)
    s.create_rectangle(0, 0, 220, 220, fill="black")

    gender = StringVar(scrollable_frame)
    dizzy = StringVar(scrollable_frame)
    faint = StringVar(scrollable_frame)
    blur = StringVar(scrollable_frame)
    fever = StringVar(scrollable_frame)
    cough = StringVar(scrollable_frame)
    fatigue = StringVar(scrollable_frame)
    l_o_t = StringVar(scrollable_frame)
    head = StringVar(scrollable_frame)
    run_nose = StringVar(scrollable_frame)
    sore = StringVar(scrollable_frame)
    muscle = StringVar(scrollable_frame)
    diff_breath = StringVar(scrollable_frame)
    sneeze = StringVar(scrollable_frame)
    chest = StringVar(scrollable_frame)
    b_o_c = StringVar(scrollable_frame)
    losm = StringVar(scrollable_frame)

    fgender = customtkinter.CTkRadioButton(
        scrollable_frame,
        text='Female',
        variable=gender,
        value="female"
    )
    mgender = customtkinter.CTkRadioButton(
        scrollable_frame,
        text='Male',
        variable=gender,
        value="male"
    )

    diz_option1 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text='Yes',
        onvalue='Yes',
        offvalue='No',
        variable=dizzy
    )
    diz_option2 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text='No',
        onvalue='No',
        offvalue='Yes',
        variable=dizzy
    )

    faint_option1 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text='Yes',
        onvalue='Yes',
        offvalue='No',
        variable=faint
    )
    faint_option2 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text='No',
        onvalue='No',
        offvalue='Yes',
        variable=faint
    )

    vision_option1 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text='Yes',
        onvalue='Yes',
        offvalue='No',
        variable=blur
    )
    vision_option2 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text='No',
        onvalue='No',
        offvalue='Yes',
        variable=blur
    )

    symp1_option1 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text='Yes',
        onvalue='Yes',
        offvalue='No',
        variable=fever
    )
    symp1_option2 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="No",
        onvalue='No',
        offvalue='Yes',
        variable=fever
    )

    symp2_option1 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="Yes",
        onvalue='Yes',
        offvalue='No',
        variable=cough

    )
    symp2_option2 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="No",
        onvalue='No',
        offvalue='Yes',
        variable=cough
    )

    symp3_option1 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="Yes",
        onvalue='Yes',
        offvalue='No',
        variable=fatigue
    )
    symp3_option2 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="No",
        onvalue='No',
        offvalue='Yes',
        variable=fatigue
    )

    symp4_option1 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="Yes",
        onvalue='Yes',
        offvalue='No',
        variable=l_o_t
    )
    symp4_option2 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="No",
        onvalue='No',
        offvalue='Yes',
        variable=l_o_t
    )

    symp5_option1 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="Yes",
        onvalue='Yes',
        offvalue='No',
        variable=head
    )
    symp5_option2 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="No",
        onvalue='No',
        offvalue='Yes',
        variable=head
    )

    symp6_option1 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="Yes",
        onvalue='Yes',
        offvalue='No',
        variable=run_nose
    )
    symp6_option2 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="No",
        onvalue='No',
        offvalue='Yes',
        variable=run_nose
    )

    symp7_option1 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="Yes",
        onvalue='Yes',
        offvalue='No',
        variable=sore,
    )
    symp7_option2 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="No",
        onvalue='No',
        offvalue='Yes',
        variable=sore
    )

    symp8_option1 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="Yes",
        onvalue='Yes',
        offvalue='No',
        variable=muscle
    )
    symp8_option2 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="No",
        onvalue='No',
        offvalue='Yes',
        variable=muscle
    )

    symp9_option1 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="Yes",
        onvalue='Yes',
        offvalue='No',
        variable=diff_breath
    )
    symp9_option2 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="No",
        onvalue='No',
        offvalue='Yes',
        variable=diff_breath
    )

    symp10_option1 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="Yes",
        onvalue='Yes',
        offvalue='No',
        variable=sneeze
    )
    symp10_option2 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="No",
        onvalue='No',
        offvalue='Yes',
        variable=sneeze
    )

    symp11_option1 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="Yes",
        onvalue='Yes',
        offvalue='No',
        variable=chest
    )
    symp11_option2 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="No",
        onvalue='No',
        offvalue='Yes',
        variable=chest
    )

    symp12_option1 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="Yes",
        onvalue='Yes',
        offvalue='No',
        variable=b_o_c
    )
    symp12_option2 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="No",
        onvalue='No',
        offvalue='Yes',
        variable=b_o_c
    )

    symp13_option1 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="Yes",
        onvalue='Yes',
        offvalue='No',
        variable=losm
    )
    symp13_option2 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="No",
        onvalue='No',
        offvalue='Yes',
        variable=losm
    )

    cancer = StringVar(scrollable_frame)
    stroke = StringVar(scrollable_frame)

    sick = StringVar(scrollable_frame)

    heart = StringVar(scrollable_frame)
    dia = StringVar(scrollable_frame)
    alz = StringVar(scrollable_frame)

    cys = StringVar(scrollable_frame)
    lung = StringVar(scrollable_frame)
    liver = StringVar(scrollable_frame)
    kid = StringVar(scrollable_frame)

    underlyingsymp1_option1 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="Yes",
        onvalue='Yes',
        offvalue='No',
        variable=cancer
    )
    underlyingsymp1_option2 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="No",
        onvalue="No",
        offvalue="Yes",
        variable=cancer
    )

    underlyingsymp2_option1 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="Yes",
        onvalue="Yes",
        offvalue="No",
        variable=stroke
    )
    underlyingsymp2_option2 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="No",
        onvalue="No",
        offvalue="Yes",
        variable=stroke
    )

    underlyingsymp4_option1 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="Yes",
        onvalue="Yes",
        offvalue="No",
        variable=sick
    )
    underlyingsymp4_option2 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="No",
        onvalue="No",
        offvalue="Yes",
        variable=sick
    )

    underlyingsymp6_option1 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="Yes",
        onvalue="Yes",
        offvalue="No",
        variable=heart
    )
    underlyingsymp6_option2 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="No",
        onvalue="No",
        offvalue="Yes",
        variable=heart
    )

    underlyingsymp7_option1 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="Yes",
        onvalue="Yes",
        offvalue="No",
        variable=dia
    )
    underlyingsymp7_option2 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="No",
        onvalue="No",
        offvalue="Yes",
        variable=dia
    )

    underlyingsymp8_option1 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="Yes",
        onvalue="Yes",
        offvalue="No",
        variable=alz
    )
    underlyingsymp8_option2 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="No",
        onvalue="No",
        offvalue="Yes",
        variable=alz
    )

    underlyingsymp10_option1 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="Yes",
        onvalue="Yes",
        offvalue="No",
        variable=cys
    )
    underlyingsymp10_option2 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="No",
        onvalue="No",
        offvalue="Yes",
        variable=cys
    )

    underlyingsymp11_option1 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="Yes",
        onvalue="Yes",
        offvalue="No",
        variable=lung
    )
    underlyingsymp11_option2 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="No",
        onvalue="No",
        offvalue="Yes",
        variable=lung
    )

    underlyingsymp12_option1 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="Yes",
        onvalue="Yes",
        offvalue="No",
        variable=liver
    )
    underlyingsymp12_option2 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="No",
        onvalue="No",
        offvalue="Yes",
        variable=liver
    )

    underlyingsymp13_option1 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="Yes",
        onvalue="Yes",
        offvalue="No",
        variable=kid
    )
    underlyingsymp13_option2 = customtkinter.CTkCheckBox(
        scrollable_frame,
        text="No",
        onvalue="No",
        offvalue="Yes",
        variable=kid
    )

    def GetInfo():
        prolog = Prolog()
        if all(entry.get() for entry in (nameentry, ageentry, tempentry, sysentry, diaentry, dizzy, faint, blur, fever, fatigue, head, sore, diff_breath, chest, losm, cough, l_o_t, run_nose, muscle, sneeze, b_o_c, cancer, stroke, sick, heart, dia, alz, cys, lung, liver, kid)):
                status = list(prolog.query(f"save_patient_python({nameentry.get()}, {ageentry.get()}, {gender.get()}, {tempentry.get()}, {dizzy.get()}, {faint.get()}, {blur.get()}, {sysentry.get()}, {diaentry.get()}, {fever.get()}, {fatigue.get()}, {head.get()}, {sore.get()}, {diff_breath.get()}, {chest.get()}, {losm.get()}, {cough.get()}, {l_o_t.get()}, {run_nose.get()}, {muscle.get()}, {sneeze.get()}, {b_o_c.get()}, {cancer.get()}, {dia.get()}, {lung.get()}, {kid.get()}, {stroke.get()}, {sick.get()}, {heart.get()}, {alz.get()}, {cys.get()}, {liver.get()})"))
                messagebox.showinfo("Success", "Patient has been saved")
                window.destroy()
        else:
            messagebox.showerror("Error", "Please fill in all the fields")
        print(status)


    submit_button = customtkinter.CTkButton(
        scrollable_frame,
        text="Submit",
        command=GetInfo

    )

    namelabel.grid(row=0, column=0, padx=2, pady=2)
    agelabel.grid(row=0, column=2,  padx=2, pady=2)
    genderlabel.grid(row=2, column=0,  padx=2, pady=2)
    templabel.grid(row=3, column=0,  padx=2, pady=2)

    symlabel.grid(row=4, column=0, columnspan=3, padx=2, pady=2)
    diasym1.grid(row=5, column=0, padx=2, pady=2)
    diasym2.grid(row=6, column=0, padx=2, pady=2)
    diasym3.grid(row=7, column=0, padx=2, pady=2)
    syslabel.grid(row=8, column=0, padx=2, pady=2)
    dialabel.grid(row=9, column=0, padx=2, pady=2)
    covidlabel.grid(row=10, column=0, columnspan=3, padx=2, pady=2)
    covid_symptom1.grid(row=11, column=0, padx=2, pady=2)
    covid_symptom2.grid(row=11, column=4, padx=2, pady=2)
    covid_symptom3.grid(row=12, column=0, padx=2, pady=2)
    covid_symptom4.grid(row=12, column=4, padx=2, pady=2)
    covid_symptom5.grid(row=13, column=0, padx=2, pady=2)
    covid_symptom6.grid(row=13, column=4, padx=2, pady=2)
    covid_symptom7.grid(row=14, column=0, padx=2, pady=2)
    covid_symptom8.grid(row=14, column=4, padx=2, pady=2)
    covid_symptom9.grid(row=15, column=0, padx=2, pady=2)
    covid_symptom10.grid(row=15, column=4, padx=2, pady=2)
    covid_symptom11.grid(row=16, column=0, padx=2, pady=2)
    covid_symptom12.grid(row=16, column=4, padx=2, pady=2)
    covid_symptom13.grid(row=17, column=0, padx=2, pady=2)
    underlyinglabel.grid(row=19, column=0, columnspan=3, padx=2, pady=10)
    underlyingsymp1.grid(row=20, column=0, padx=2, pady=2)
    underlyingsymp2.grid(row=20, column=4, padx=2, pady=2)

    underlyingsymp4.grid(row=21, column=0, padx=2, pady=2)

    underlyingsymp6.grid(row=21, column=4, padx=2, pady=2)
    underlyingsymp7.grid(row=22, column=0, padx=2, pady=2)
    underlyingsymp8.grid(row=22, column=4, padx=2, pady=2)

    underlyingsymp10.grid(row=23, column=0, padx=2, pady=2)
    underlyingsymp11.grid(row=23, column=4, padx=2, pady=2)
    underlyingsymp12.grid(row=24, column=0, padx=2, pady=2)
    underlyingsymp13.grid(row=24, column=4, padx=2, pady=2)

    nameentry.grid(row=0, column=1,  padx=2, pady=2)
    ageentry.grid(row=0, column=3,  padx=2, pady=2)
    tempentry.grid(row=3, column=1,  padx=2, pady=2)
    sysentry.grid(row=8, column=1, padx=2, pady=2)
    diaentry.grid(row=9, column=1, padx=2, pady=2)

    w.grid(row=8, column=3, rowspan=12)
    s.grid(row=18, column=3, rowspan=12)

    fgender.grid(row=2, column=1,  padx=2, pady=2)
    mgender.grid(row=2, column=2,  padx=2, pady=2)
    diz_option1.grid(row=5, column=1, padx=2, pady=2)
    diz_option2.grid(row=5, column=2, padx=2, pady=2)
    faint_option1.grid(row=6, column=1, padx=2, pady=2)
    faint_option2.grid(row=6, column=2, padx=2, pady=2)
    vision_option1.grid(row=7, column=1, padx=2, pady=2)
    vision_option2.grid(row=7, column=2, padx=2, pady=2)
    symp1_option1.grid(row=11, column=1, padx=2, pady=2)
    symp1_option2.grid(row=11, column=2, padx=2, pady=2)
    symp2_option1.grid(row=11, column=5, padx=2, pady=2)
    symp2_option2.grid(row=11, column=7, padx=2, pady=2)
    symp3_option1.grid(row=12, column=1, padx=2, pady=2)
    symp3_option2.grid(row=12, column=2, padx=2, pady=2)
    symp4_option1.grid(row=12, column=5, padx=2, pady=2)
    symp4_option2.grid(row=12, column=7, padx=2, pady=2)
    symp5_option1.grid(row=13, column=1, padx=2, pady=2)
    symp5_option2.grid(row=13, column=2, padx=2, pady=2)
    symp6_option1.grid(row=13, column=5, padx=2, pady=2)
    symp6_option2.grid(row=13, column=7, padx=2, pady=2)
    symp7_option1.grid(row=14, column=1, padx=2, pady=2)
    symp7_option2.grid(row=14, column=2, padx=2, pady=2)
    symp8_option1.grid(row=14, column=5, padx=2, pady=2)
    symp8_option2.grid(row=14, column=7, padx=2, pady=2)
    symp9_option1.grid(row=15, column=1, padx=2, pady=2)
    symp9_option2.grid(row=15, column=2, padx=2, pady=2)
    symp10_option1.grid(row=15, column=5, padx=2, pady=2)
    symp10_option2.grid(row=15, column=7, padx=2, pady=2)
    symp11_option1.grid(row=16, column=1, padx=2, pady=2)
    symp11_option2.grid(row=16, column=2, padx=2, pady=2)
    symp12_option1.grid(row=16, column=5, padx=2, pady=2)
    symp12_option2.grid(row=16, column=6, padx=2, pady=2)
    symp13_option1.grid(row=17, column=1, padx=2, pady=2)
    symp13_option2.grid(row=17, column=2, padx=2, pady=2)
    underlyingsymp1_option1.grid(row=20, column=1, padx=2, pady=2)
    underlyingsymp1_option2.grid(row=20, column=2, padx=2, pady=2)
    underlyingsymp2_option1.grid(row=20, column=5, padx=2, pady=2)
    underlyingsymp2_option2.grid(row=20, column=7, padx=2, pady=2)

    underlyingsymp4_option1.grid(row=21, column=1, padx=2, pady=2)
    underlyingsymp4_option2.grid(row=21, column=2, padx=2, pady=2)

    underlyingsymp6_option1.grid(row=21, column=5, padx=2, pady=2)
    underlyingsymp6_option2.grid(row=21, column=7, padx=2, pady=2)
    underlyingsymp7_option1.grid(row=22, column=1, padx=2, pady=2)
    underlyingsymp7_option2.grid(row=22, column=2, padx=2, pady=2)
    underlyingsymp8_option1.grid(row=22, column=5, padx=2, pady=2)
    underlyingsymp8_option2.grid(row=22, column=7, padx=2, pady=2)

    underlyingsymp10_option1.grid(row=23, column=1, padx=2, pady=2)
    underlyingsymp10_option2.grid(row=23, column=2, padx=2, pady=2)
    underlyingsymp11_option1.grid(row=23, column=5, padx=2, pady=2)
    underlyingsymp11_option2.grid(row=23, column=7, padx=2, pady=2)
    underlyingsymp12_option1.grid(row=24, column=1, padx=2, pady=2)
    underlyingsymp12_option2.grid(row=24, column=2, padx=2, pady=2)
    underlyingsymp13_option1.grid(row=24, column=5, padx=2, pady=2)
    underlyingsymp13_option2.grid(row=24, column=7, padx=2, pady=2)

    submit_button.grid(row=40, column=0, padx=2, pady=15)

    window.mainloop()
