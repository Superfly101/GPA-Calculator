import tkinter as tk
from tkinter import ttk
import tkinter.font


class MyGUI(object):

    def __init__(self):

        self.root = tk.Tk()

        # Create canvas widget.
        self.canvas = tk.Canvas(self.root, width=570, height=500, bg="#263D42")
        self.canvas.pack()

        # Create Main frames.
        self.main_frame = tk.Frame(self.root, bg="light sky blue")
        self.sub_frame = tk.Frame(self.root, bg="alice blue")
        self.main_frame.place(relwidth=0.6, relheight=1, relx=0.4)
        self.sub_frame.place(relwidth=0.4, relheight=1)

        # CREATE MAIN FRAME WIDGETS.
        # Top label
        self.label_font = tkinter.font.Font(family="Helvetica", size='9', weight='bold')
        self.score_label = tk.Label(self.main_frame, text="TOTAL SCORES", bg='light sky blue', font=self.label_font)
        self.score_label.place(relx=0.15, rely=0.05)
        self.unit_label = tk.Label(self.main_frame, text="CREDIT UNIT", bg='light sky blue', font=self.label_font)
        self.unit_label.place(relx=0.61, rely=0.05)

        # Create entries
        self.create_entries()

        # SUB FRAME WIDGETS.
        # Buttons.
        self.button_font = tkinter.font.Font(family='Times', size='11')  # Font
        self.calc_button = tk.Button(self.sub_frame, text="Calculate GPA",
                                     bg="light sky blue", command=self.calc_GPA,
                                     height="2", width="15", font=self.button_font)
        self.calc_button.place(relx=0.21, rely=0.49)
        self.exitbutton_font = tkinter.font.Font(family='Times New Roman', size='10')
        self.quit_button = tk.Button(self.sub_frame, text="EXIT", bg="light sky blue",
                                     command=self.root.destroy, font=self.exitbutton_font,
                                     width='8')
        self.quit_button.pack(side="bottom")

        # Labels.
        self.result_label = tk.Label(self.sub_frame, text="GPA: ", bg="alice blue")
        self.GPA = tk.StringVar()
        self.GPA_label = tk.Label(self.sub_frame, textvariable=self.GPA)
        self.result_label.place(relx=0.3, rely=0.6)
        self.GPA_label.place(relx=0.45, rely=0.6)

        self.root.mainloop()

    def create_entries(self):

        Exams = {"Exam1": [0.18, 0.12, 0.62], "Exam2": [0.18, 0.20, 0.62],
                 "Exam3": [0.18, 0.28, 0.62], "Exam4": [0.18, 0.36, 0.62],
                 "Exam5": [0.18, 0.44, 0.62], "Exam6": [0.18, 0.52, 0.62],
                 "Exam7": [0.18, 0.60, 0.62], "Exam8": [0.18, 0.68, 0.62],
                 "Exam9": [0.18, 0.76, 0.62], "Exam10": [0.18, 0.84, 0.62],
                 "Exam11": [0.18, 0.92, 0.62]}
        x = 1

        self.score_list = []
        self.unit_list = []

        for i in Exams:
            txt = "Exam " + str(x) + ":"
            exam_label = tk.Label(self.main_frame, text=txt)
            exam_label.place(rely=Exams[i][1])
            score = tk.Entry(self.main_frame, width="10")
            score.place(relx=Exams[i][0], rely=Exams[i][1])
            unit = ttk.Combobox(self.main_frame, values=["0", "1", "2", "3", "4"], width="6")
            unit.place(relx=Exams[i][2], rely=Exams[i][1])
            unit.current(0)
            x += 1

            self.score_list.append(score)
            self.unit_list.append(unit)

    def calc_GPA(self):
        grade_point = 0
        credit_unit = 0

        valid_scores = [int(score.get()) for score in self.score_list if score.get() != ""]
        valid_units = [int(unit.get()) for unit in self.unit_list if unit.get() != "0" and unit.get() != ""]
        for value in valid_units:
            print(value)

        for i in range(len(valid_units)):
            try:
                grade_point += self.grade(valid_scores[i]) * valid_units[i]
                credit_unit += valid_units[i]
            except IndexError:
                grade_point += 0
                valid_units[i] = 0

        if credit_unit != 0:
            GPA = round(grade_point / credit_unit, 2)
            self.GPA.set(GPA)

    def grade(self, x):
        if 100 >= x >= 70:
            return 5
        elif x >= 60:
            return 4
        elif x >= 50:
            return 3
        elif x >= 45:
            return 2
        elif x >= 40:
            return 1
        else:
            return 0


# Create instance of the class.
my_gui = MyGUI()
