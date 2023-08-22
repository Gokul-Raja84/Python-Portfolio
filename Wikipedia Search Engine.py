from tkinter import *
import wikipedia

def get_data():
    entry_value = entry.get()
    answer.delete(1.0, END)
    try:
        answer_value = wikipedia.summary(entry_value, features="lxml")
        answer.insert(INSERT, answer_value)
    except wikipedia.exceptions.DisambiguationError as e:
        answer.insert(INSERT, "Multiple results found. Please provide more specific query.")
    except wikipedia.exceptions.PageError as e:
        answer.insert(INSERT, "Page not found. Please check your input.")
    except:
        answer.insert(INSERT, "ERROR! Invalid input or poor internet connection")

win = Tk()
win.title("Wikipedia Search Engine")

# Top Frame
topframe = Frame(win)
topframe.pack(side=TOP, pady=20)

entry_label = Label(topframe, text="Enter a search query:")
entry_label.pack()

entry = Entry(topframe, width=40)
entry.pack()

button = Button(topframe, text="Search", command=get_data)
button.pack()

# Bottom Frame
bottomframe = Frame(win)
bottomframe.pack()

scroll = Scrollbar(bottomframe)
scroll.pack(side=RIGHT, fill=Y)

answer = Text(bottomframe, width=80, height=15, yscrollcommand=scroll.set, wrap=WORD)
scroll.config(command=answer.yview)
answer.pack()

win.mainloop()