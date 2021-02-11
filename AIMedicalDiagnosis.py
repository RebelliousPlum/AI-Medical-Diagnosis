import tkinter.messagebox
import sys
from tkinter import Radiobutton
from tkinter import Tk
from tkinter import Label
from tkinter import IntVar
from tkinter import Button
from tkinter import messagebox
from tkinter import Message




COUNT  = [10]

class Node(object):
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def ask_multiple_choice_question(prompt, options):
    master = Tk()
    #
    w = 300
    h = 200
    ws = master.winfo_screenwidth()
    hs = master.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    master.geometry('%dx%d+%d+%d' % (w,h,x,y))
    master.title('Medical Diagnosis')

    # exit program on Quit
    def on_close():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            sys.exit()

    # Label asks questions and radiobutton are the options looped through.
    if prompt:
        Label(master, text=prompt, width = 30, height = 5).pack()
    v = IntVar()
    for i, option in enumerate(options):
        Radiobutton(master, text=option, variable=v, value=i,indicatoron= 0).pack(anchor="w")

    #Submit answers
    Button(text="Submit", command=master.destroy).pack()

    master.protocol("WM_DELETE_WINDOW", on_close)
    master.mainloop()

    #return answer.
    return options[v.get()]

# Function to print binary tree in 2D
# It does reverse inorder traversal
def print2DUtil(root, space):
    # Base case
    if (root == None):
        return

    # Increase distance between levels
    space += COUNT[0]

    # Process right child first
    print2DUtil(root.right, space)

    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.val)

    # Process left child
    print2DUtil(root.left, space)


# Wrapper over print2DUtil()
def print2D(root):
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)




def Illness():

    result = ask_multiple_choice_question("What illness do you think you have?", ["Flu", "Coronavirus", "Colon Cancer", "CommonCold" ])

    if result == 'Colon Cancer':

        root = Node("Did you have any change in your bowels?")
        root.left = Node("Is there blood?")
        root.right = Node("Are you having any cramps?")
        root.left.left = Node("Do you have any weakness or fatigue?")
        root.left.right = Node("Experiencing unexplained weightloss?")
        root.left.left.left = Node("You have colon cancer.")
        root.left.left.right = Node("Are you african american?")
        root.left.right.left = Node("Are you gassy?")
        root.left.right.right = Node("You do not have colon cancer.")
        root.right.left = Node("Did you have anything to eat?")
        root.right.right = Node("Are you above the age of 60?")
        root.right.left.left = Node("You have colon cancer.")
        root.right.left.right = Node("You do not have colon cancer.")
        root.right.right.left = Node("You have colon cancer.")
        root.left.left.right.left = Node("You have colon cancer.")
        root.left.left.right.right = Node("You do not have colon cancer.")
        root.left.right.left.left = Node("You have colon cancer.")
        root.left.right.left.right = Node("You do not have colon cancer.")
        root.right.right.right = Node("You do not have colon cancer.")

        questionOne = ask_multiple_choice_question(root.val, ["Yes", "No", 'Reset' ])
        if questionOne == 'Yes':
            questionTwo = ask_multiple_choice_question(root.left.val, ["Yes", "No", "Reset"])
            if questionTwo == "Yes":
                questionThree = ask_multiple_choice_question(root.left.left.val, ["Yes", "No", 'Reset'])
                if questionThree == "Yes":
                    master = Tk()
                    w = 300
                    h = 100
                    ws = master.winfo_screenwidth()
                    hs = master.winfo_screenheight()

                    x = (ws / 2) - (w / 2)
                    y = (hs / 2) - (h / 2)
                    master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                    master.title("Diagnosed Illness")

                    w = Message(master, text = root.left.left.left.val,font = 16)
                    w.pack()
                    master.mainloop()

                elif questionThree == "Reset":
                    Illness()


                elif questionThree == "No":
                    questionFour = ask_multiple_choice_question(root.left.left.right.val, ["Yes","No",'reset'])
                    if questionFour == "Yes":
                        master = Tk()
                        w = 300
                        h = 100
                        ws = master.winfo_screenwidth()
                        hs = master.winfo_screenheight()

                        x = (ws / 2) - (w / 2)
                        y = (hs / 2) - (h / 2)
                        master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                        master.title("Diagnosed Illness")

                        w = Message(master, text=root.left.left.right.left.val, font=16)
                        w.pack()
                        master.mainloop()


                    elif questionFour == "No":

                        master = Tk()
                        w = 300
                        h = 100
                        ws = master.winfo_screenwidth()
                        hs = master.winfo_screenheight()

                        x = (ws / 2) - (w / 2)
                        y = (hs / 2) - (h / 2)
                        master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                        master.title("Diagnosed Illness")

                        w = Message(master, text=root.left.left.right.right.val, font=16)
                        w.pack()
                        master.mainloop()

                        print(root.left.left.right.right.val)

                    elif questionFour == "Reset":
                        Illness()
            elif questionTwo == "No":
                questionThree = ask_multiple_choice_question(root.left.right.val, ["Yes", "No", 'Reset'])
                if questionThree == "Yes":
                    questionFour = ask_multiple_choice_question(root.left.right.left.val, ["Yes", "No", "Reset"])
                    if questionFour == "Yes":
                        master = Tk()
                        w = 300
                        h = 100
                        ws = master.winfo_screenwidth()
                        hs = master.winfo_screenheight()

                        x = (ws / 2) - (w / 2)
                        y = (hs / 2) - (h / 2)
                        master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                        master.title("Diagnosed Illness")

                        w = Message(master, text=root.left.right.left.left.val, font=16)
                        w.pack()
                        master.mainloop()

                        print(root.left.right.left.left.val)
                    elif questionFour == "No":

                        master = Tk()
                        w = 300
                        h = 100
                        ws = master.winfo_screenwidth()
                        hs = master.winfo_screenheight()

                        x = (ws / 2) - (w / 2)
                        y = (hs / 2) - (h / 2)
                        master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                        master.title("Diagnosed Illness")

                        w = Message(master, text=root.left.right.left.right.val, font=16)
                        w.pack()
                        master.mainloop()

                        print(root.left.right.left.right.val)
                elif questionThree == "No":

                    master = Tk()
                    w = 300
                    h = 100
                    ws = master.winfo_screenwidth()
                    hs = master.winfo_screenheight()

                    x = (ws / 2) - (w / 2)
                    y = (hs / 2) - (h / 2)
                    master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                    master.title("Diagnosed Illness")

                    w = Message(master, text=root.left.right.right.val, font=16)
                    w.pack()
                    master.mainloop()

                    print(root.left.right.right.val)
            elif questionTwo == "Reset":
                Illness()


        elif questionOne == "No":
            questionTwo = ask_multiple_choice_question(root.right.val, ["Yes", "No"])
            if questionTwo == "Yes":
                questionThree = ask_multiple_choice_question(root.right.left.val, ["Yes", "No"])
                if questionThree == "Yes":
                    master = Tk()
                    w = 300
                    h = 100
                    ws = master.winfo_screenwidth()
                    hs = master.winfo_screenheight()

                    x = (ws / 2) - (w / 2)
                    y = (hs / 2) - (h / 2)
                    master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                    master.title("Diagnosed Illness")

                    w = Message(master, text=root.right.left.left.val, font=16)
                    w.pack()
                    master.mainloop()

                    print(root.right.left.left.val)
                elif questionThree == "No":

                    master = Tk()
                    w = 300
                    h = 100
                    ws = master.winfo_screenwidth()
                    hs = master.winfo_screenheight()

                    x = (ws / 2) - (w / 2)
                    y = (hs / 2) - (h / 2)
                    master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                    master.title("Diagnosed Illness")

                    w = Message(master, text=root.right.left.right.val, font=16)
                    w.pack()
                    master.mainloop()

                    print(root.right.left.right.val)
            elif questionTwo == "No":
                questionThree = ask_multiple_choice_question(root.right.right.val, ["Yes", "No"])
                if questionThree == "Yes":
                    master = Tk()
                    w = 300
                    h = 100
                    ws = master.winfo_screenwidth()
                    hs = master.winfo_screenheight()

                    x = (ws / 2) - (w / 2)
                    y = (hs / 2) - (h / 2)
                    master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                    master.title("Diagnosed Illness")

                    w = Message(master, text=root.right.right.left.val, font=16)
                    w.pack()
                    master.mainloop()

                    print(root.right.right.left.val)
                elif questionThree == "No":
                    master = Tk()
                    w = 300
                    h = 100
                    ws = master.winfo_screenwidth()
                    hs = master.winfo_screenheight()

                    x = (ws / 2) - (w / 2)
                    y = (hs / 2) - (h / 2)
                    master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                    master.title("Diagnosed Illness")

                    w = Message(master, text=root.right.right.right.val, font=16)
                    w.pack()
                    master.mainloop()

                    print(root.right.right.right.val)
                    input('Press Enter to exit')
        elif questionOne == "Reset":
            Illness()



    elif result == 'Coronavirus':
        root = Node("Are you above the age of 60?")
        root.left = Node("Do you have a cough?")
        root.left.left = Node("Do you have a fever?")
        root.left.left.left = Node("You have the Coronavirus")
        root.left.left.right = Node("You do not have the Coronavirus")
        root.left.right = Node("Are you having difficulty breathing?")
        root.left.right.left = Node("You have the Coronavirus")
        root.left.right.right = Node("You do not have the Coronavirus")
        root.right = Node("Do you have a runny nose?")
        root.right.left = Node("Do you have a sore throat?")
        root.right.left.left = Node("Are you experiencing fatigue?")
        root.right.left.left.left = Node("You have the Coronavirus.")
        root.right.left.left.right = Node("You do not have the Coronavirus.")
        root.right.left.right = Node("You do not have the Coronavirus.")
        root.right.right = Node("Are you sneezing a lot?")
        root.right.right.left = Node("You have the Coronavirus.")
        root.right.right.right = Node("Do you feel any tingles on your skin?")
        root.right.right.right.left = Node("You have the Coronavirus.")
        root.right.right.right.right = Node("You do not have the Coronavirus.")

        questionOne = ask_multiple_choice_question(root.val, ["Yes", "No"])
        if questionOne == "Yes":
            questionTwo = ask_multiple_choice_question(root.left.val, ["Yes", "No"])
            if questionTwo == "Yes":
                questionThree = ask_multiple_choice_question(root.left.left.val, ["Yes", "No"])
                if questionThree == "Yes":
                    master = Tk()
                    w = 300
                    h = 100
                    ws = master.winfo_screenwidth()
                    hs = master.winfo_screenheight()

                    x = (ws / 2) - (w / 2)
                    y = (hs / 2) - (h / 2)
                    master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                    master.title("Diagnosed Illness")

                    w = Message(master, text=root.left.left.left.val, font=16)
                    w.pack()
                    master.mainloop()
                    print(root.left.left.left.val)
                elif questionThree == "No":
                    master = Tk()
                    w = 300
                    h = 100
                    ws = master.winfo_screenwidth()
                    hs = master.winfo_screenheight()

                    x = (ws / 2) - (w / 2)
                    y = (hs / 2) - (h / 2)
                    master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                    master.title("Diagnosed Illness")

                    w = Message(master, text=root.left.left.right.val, font=16)
                    w.pack()
                    master.mainloop()
                    print(root.left.left.right.val)
            elif questionTwo == "No":
                questionThree = ask_multiple_choice_question(root.left.right.val, ["Yes","No"])
                if questionThree == "Yes":
                    master = Tk()
                    w = 300
                    h = 100
                    ws = master.winfo_screenwidth()
                    hs = master.winfo_screenheight()

                    x = (ws / 2) - (w / 2)
                    y = (hs / 2) - (h / 2)
                    master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                    master.title("Diagnosed Illness")

                    w = Message(master, text=root.left.right.left.val, font=16)
                    w.pack()
                    master.mainloop()
                    print(root.left.right.left.val)
                elif questionThree == "No":
                    master = Tk()
                    w = 300
                    h = 100
                    ws = master.winfo_screenwidth()
                    hs = master.winfo_screenheight()

                    x = (ws / 2) - (w / 2)
                    y = (hs / 2) - (h / 2)
                    master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                    master.title("Diagnosed Illness")

                    w = Message(master, text=root.left.right.right.val, font=16)
                    w.pack()
                    master.mainloop()
                    print(root.left.right.right.val)
        elif questionOne == "No":
            questionTwo = ask_multiple_choice_question(root.right.val, ["Yes", "No"])
            if questionTwo == "Yes":
                questionThree = ask_multiple_choice_question(root.right.left.val, ["Yes", "No"])
                if questionThree == "Yes":
                    questionFour = ask_multiple_choice_question(root.right.left.left.val, ["Yes", "No"])
                    if questionFour  == "Yes":
                        master = Tk()
                        w = 300
                        h = 100
                        ws = master.winfo_screenwidth()
                        hs = master.winfo_screenheight()

                        x = (ws / 2) - (w / 2)
                        y = (hs / 2) - (h / 2)
                        master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                        master.title("Diagnosed Illness")

                        w = Message(master, text=root.right.left.left.left.val, font=16)
                        w.pack()
                        master.mainloop()
                        print(root.right.left.left.left.val)
                    elif questionFour == "No":
                        master = Tk()
                        w = 300
                        h = 100
                        ws = master.winfo_screenwidth()
                        hs = master.winfo_screenheight()

                        x = (ws / 2) - (w / 2)
                        y = (hs / 2) - (h / 2)
                        master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                        master.title("Diagnosed Illness")

                        w = Message(master, text=root.right.left.left.right.val, font=16)
                        w.pack()
                        master.mainloop()
                        print(root.right.left.left.right.val)
                elif questionThree == "No":
                    master = Tk()
                    w = 300
                    h = 100
                    ws = master.winfo_screenwidth()
                    hs = master.winfo_screenheight()

                    x = (ws / 2) - (w / 2)
                    y = (hs / 2) - (h / 2)
                    master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                    master.title("Diagnosed Illness")

                    w = Message(master, text=root.right.left.right.val, font=16)
                    w.pack()
                    master.mainloop()
                    print(root.right.left.right.val)
            elif questionTwo == "No":
                questionThree = ask_multiple_choice_question(root.right.right.val, ["Yes", "No"])
                if questionThree == "Yes":
                    master = Tk()
                    w = 300
                    h = 100
                    ws = master.winfo_screenwidth()
                    hs = master.winfo_screenheight()

                    x = (ws / 2) - (w / 2)
                    y = (hs / 2) - (h / 2)
                    master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                    master.title("Diagnosed Illness")

                    w = Message(master, text=root.right.right.left.val,font=16)
                    w.pack()
                    master.mainloop()
                    print(root.right.right.left.val)
                elif questionThree == "No":
                    questionFour = ask_multiple_choice_question(root.right.right.right.val, ["Yes", "No"])
                    if questionFour == "Yes":
                        master = Tk()
                        w = 300
                        h = 100
                        ws = master.winfo_screenwidth()
                        hs = master.winfo_screenheight()

                        x = (ws / 2) - (w / 2)
                        y = (hs / 2) - (h / 2)
                        master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                        master.title("Diagnosed Illness")

                        w = Message(master, text=root.right.right.right.left.val, font=16)
                        w.pack()
                        master.mainloop()
                    elif questionFour == "No":
                        master = Tk()
                        w = 300
                        h = 100
                        ws = master.winfo_screenwidth()
                        hs = master.winfo_screenheight()

                        x = (ws / 2) - (w / 2)
                        y = (hs / 2) - (h / 2)
                        master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                        master.title("Diagnosed Illness")

                        w = Message(master, text=root.right.right.right.right.val, font=16)
                        w.pack()
                        master.mainloop()
    elif result == "Flu":

        root = Node("Sudden experience of Symptoms?")
        root.left = Node("Do you have a Fever above 100F?")
        root.left.left = Node("Severe Aches in Muscles?")
        root.left.right = Node("Chills?")

        root.left.left.left = Node("You have the flu.")
        root.left.left.right = Node("You do not have the flu.")

        root.left.right.left = Node("You have the flu.")
        root.left.right.right = Node("You do not have the flu.")

        root.right = Node("Do you have a headache?")
        root.right.left = Node("Do you have severe vomiting?")
        root.right.right = Node("Do you have weakness or fatigue?")

        root.right.left.left = Node("You have the flu.")
        root.right.left.right = Node("You do not have the flu")

        root.right.right.right = Node("You do not have the flu.")
        root.right.right.left = Node("Do you have trouble breathing?")

        root.right.right.left.left = Node("You have the flu.")
        root.right.right.left.right = Node("You do not have the flu.")

        questioneOne = ask_multiple_choice_question(root.val, ["Yes", "No"])
        if questioneOne == "Yes":
            questionTwo = ask_multiple_choice_question(root.left.val, ["Yes", "No"])
            if questionTwo == "Yes":
                questionThree = ask_multiple_choice_question(root.left.left.val , ["Yes","No"])
                if questionThree == "Yes":
                    master = Tk()
                    w = 300
                    h = 100
                    ws = master.winfo_screenwidth()
                    hs = master.winfo_screenheight()

                    x = (ws / 2) - (w / 2)
                    y = (hs / 2) - (h / 2)
                    master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                    master.title("Diagnosed Illness")

                    w = Message(master, text=root.left.left.left.val, font=16)
                    w.pack()
                    master.mainloop()
                    print(root.left.left.left.val)
                elif questionThree == "No":
                    master = Tk()
                    w = 300
                    h = 100
                    ws = master.winfo_screenwidth()
                    hs = master.winfo_screenheight()

                    x = (ws / 2) - (w / 2)
                    y = (hs / 2) - (h / 2)
                    master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                    master.title("Diagnosed Illness")

                    w = Message(master, text=root.left.left.right.val, font=16)
                    w.pack()
                    master.mainloop()
                    print(root.left.left.right.val)
            elif questionTwo == "No":
                questionThree = ask_multiple_choice_question(root.left.right.val, ["Yes","No"])
                if questionThree == "Yes":
                    master = Tk()
                    w = 300
                    h = 100
                    ws = master.winfo_screenwidth()
                    hs = master.winfo_screenheight()

                    x = (ws / 2) - (w / 2)
                    y = (hs / 2) - (h / 2)
                    master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                    master.title("Diagnosed Illness")

                    w = Message(master, text=root.left.right.left.val, font=16)
                    w.pack()
                    master.mainloop()
                    print(root.left.right.left.val)
                elif questionThree == "No":
                    master = Tk()
                    w = 300
                    h = 100
                    ws = master.winfo_screenwidth()
                    hs = master.winfo_screenheight()

                    x = (ws / 2) - (w / 2)
                    y = (hs / 2) - (h / 2)
                    master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                    master.title("Diagnosed Illness")

                    w = Message(master, text=root.left.right.right.val, font=16)
                    w.pack()
                    master.mainloop()
                    print(root.left.right.right.val)
        elif questioneOne == "No":
            questioneTwo = ask_multiple_choice_question(root.right.val, ["Yes","No"])
            if questioneTwo == "Yes":
                questionThree = ask_multiple_choice_question(root.right.left.val, ["Yes", "No"])
                if questionThree == "Yes":
                    master = Tk()
                    w = 300
                    h = 100
                    ws = master.winfo_screenwidth()
                    hs = master.winfo_screenheight()

                    x = (ws / 2) - (w / 2)
                    y = (hs / 2) - (h / 2)
                    master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                    master.title("Diagnosed Illness")

                    w = Message(master, text=root.right.left.left.val, font=16)
                    w.pack()
                    master.mainloop()
                    print(root.right.left.left.val)
                elif questionThree == "No":
                    master = Tk()
                    w = 300
                    h = 100
                    ws = master.winfo_screenwidth()
                    hs = master.winfo_screenheight()

                    x = (ws / 2) - (w / 2)
                    y = (hs / 2) - (h / 2)
                    master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                    master.title("Diagnosed Illness")

                    w = Message(master, text=root.right.left.right.val, font=16)
                    w.pack()
                    master.mainloop()
                    print(root.right.left.right.val)
            elif questioneTwo == "No":
                questionThree = ask_multiple_choice_question(root.right.right.val, ["Yes", "No"])
                if questionThree == "Yes":
                    questionFour = ask_multiple_choice_question(root.right.right.left.val, ["Yes", "No"])
                    if questionFour == "Yes":
                        master = Tk()
                        w = 300
                        h = 100
                        ws = master.winfo_screenwidth()
                        hs = master.winfo_screenheight()

                        x = (ws / 2) - (w / 2)
                        y = (hs / 2) - (h / 2)
                        master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                        master.title("Diagnosed Illness")

                        w = Message(master, text=root.right.right.left.left.val, font=16)
                        w.pack()
                        master.mainloop()
                        print(root.right.right.left.left.val)
                    elif questionFour == "No":
                        master = Tk()
                        w = 300
                        h = 100
                        ws = master.winfo_screenwidth()
                        hs = master.winfo_screenheight()

                        x = (ws / 2) - (w / 2)
                        y = (hs / 2) - (h / 2)
                        master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                        master.title("Diagnosed Illness")

                        w = Message(master, text=root.right.right.left.right.val, font=16)
                        w.pack()
                        master.mainloop()
                        print(root.right.right.left.right.val)
                elif questionThree == "No":
                    master = Tk()
                    w = 300
                    h = 100
                    ws = master.winfo_screenwidth()
                    hs = master.winfo_screenheight()

                    x = (ws / 2) - (w / 2)
                    y = (hs / 2) - (h / 2)
                    master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                    master.title("Diagnosed Illness")

                    w = Message(master, text=root.right.right.right.val, font=16)
                    w.pack()
                    master.mainloop()
                    print(root.right.right.right.val)
    elif result == "CommonCold":
        root = Node("Do you have a cough? ")
        root.left = Node("Do you have a runny nose?")
        root.left.left = Node("Are you sneezing?")
        root.left.right = Node("Are you feeling fatigued?")

        root.left.left.left = Node("You have a cold.")
        root.left.left.right = Node("You do not have a cold.")

        root.left.right.left = Node("You have a cold.")
        root.left.right.right = Node("You do not have a cold.")

        root.right = Node("Do you have a fever?")
        root.right.left = Node("Is your fever above 102F?")
        root.right.left.left = Node("You have a severe cold.")
        root.right.left.right = Node("You do not have a cold.")

        root.right.right = Node("Any earache?")
        root.right.right.left = Node("You have a severe cold.")
        root.right.right.right = Node("You don't have a cold.")

        questionOne = ask_multiple_choice_question(root.val, ["Yes","No"])
        if questionOne == "Yes":
            questionTwo = ask_multiple_choice_question(root.left.val, ["Yes", "No"])
            if questionTwo == "Yes":
                questionThree = ask_multiple_choice_question(root.left.left.val, ["Yes", "No"])
                if questionThree == "Yes":
                    master = Tk()
                    w = 300
                    h = 100
                    ws = master.winfo_screenwidth()
                    hs = master.winfo_screenheight()

                    x = (ws / 2) - (w / 2)
                    y = (hs / 2) - (h / 2)
                    master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                    master.title("Diagnosed Illness")

                    w = Message(master, text=root.left.left.left.val, font=16)
                    w.pack()
                    master.mainloop()

                    print(root.left.left.left.val)
                elif questionThree == "No":
                    master = Tk()
                    w = 300
                    h = 100
                    ws = master.winfo_screenwidth()
                    hs = master.winfo_screenheight()

                    x = (ws / 2) - (w / 2)
                    y = (hs / 2) - (h / 2)
                    master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                    master.title("Diagnosed Illness")

                    w = Message(master, text=root.left.left.right.val, font=16)
                    w.pack()
                    master.mainloop()

                    print(root.left.left.right.val)
            elif questionTwo == "No":
                questionThree = ask_multiple_choice_question(root.left.right.val, ["Yes", "No"])
                if questionThree == "Yes":
                    master = Tk()
                    w = 300
                    h = 100
                    ws = master.winfo_screenwidth()
                    hs = master.winfo_screenheight()

                    x = (ws / 2) - (w / 2)
                    y = (hs / 2) - (h / 2)
                    master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                    master.title("Diagnosed Illness")

                    w = Message(master, text=root.left.right.left.val, font=16)
                    w.pack()
                    master.mainloop()

                    print(root.left.right.left.val)
                elif questionThree == "No":
                    master = Tk()
                    w = 300
                    h = 100
                    ws = master.winfo_screenwidth()
                    hs = master.winfo_screenheight()

                    x = (ws / 2) - (w / 2)
                    y = (hs / 2) - (h / 2)
                    master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                    master.title("Diagnosed Illness")

                    w = Message(master, text=root.left.right.right.val, font=16)
                    w.pack()
                    master.mainloop()

                    print(root.left.right.right.val)
        elif questionOne == "No":
            questionTwo = ask_multiple_choice_question(root.right.val, ["Yes", "No"])
            if questionTwo == "Yes":
                questionThree = ask_multiple_choice_question(root.right.left.val, ["Yes", "No"])
                if questionThree == "Yes":
                    master = Tk()
                    w = 300
                    h = 100
                    ws = master.winfo_screenwidth()
                    hs = master.winfo_screenheight()

                    x = (ws / 2) - (w / 2)
                    y = (hs / 2) - (h / 2)
                    master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                    master.title("Diagnosed Illness")

                    w = Message(master, text=root.right.left.left.val, font=16)
                    w.pack()
                    master.mainloop()

                    print(root.right.left.left.val)
                elif questionThree == "No":
                    master = Tk()
                    w = 300
                    h = 100
                    ws = master.winfo_screenwidth()
                    hs = master.winfo_screenheight()

                    x = (ws / 2) - (w / 2)
                    y = (hs / 2) - (h / 2)
                    master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                    master.title("Diagnosed Illness")

                    w = Message(master, text=root.right.left.right.val, font=16)
                    w.pack()
                    master.mainloop()

                    print(root.right.left.right.val)
            elif questionTwo == "No":
                questionThree = ask_multiple_choice_question(root.right.right.val, ["Yes", "No"])
                if questionThree == "Yes":
                    master = Tk()
                    w = 300
                    h = 100
                    ws = master.winfo_screenwidth()
                    hs = master.winfo_screenheight()

                    x = (ws / 2) - (w / 2)
                    y = (hs / 2) - (h / 2)
                    master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                    master.title("Diagnosed Illness")

                    w = Message(master, text=root.right.right.left.val, font=16)
                    w.pack()
                    master.mainloop()

                    print(root.right.right.left.val)
                elif questionThree == "No":
                    master = Tk()
                    w = 300
                    h = 100
                    ws = master.winfo_screenwidth()
                    hs = master.winfo_screenheight()

                    x = (ws / 2) - (w / 2)
                    y = (hs / 2) - (h / 2)
                    master.geometry('%dx%d+%d+%d' % (w, h, x, y))
                    master.title("Diagnosed Illness")

                    w = Message(master, text=root.right.right.right.val, font=16)
                    w.pack()
                    master.mainloop()

                    print(root.right.right.right.val)



Illness()