from tkinter import Listbox, END, ANCHOR, BOTTOM

import customtkinter as tk

import main

tk.set_appearance_mode("System")
tk.set_default_color_theme("dark-blue")

root = tk.CTk()
root.geometry("1000x1150")

cocktailList = main.df['Cocktail Name'].iloc[main.indexList].to_list()


#  Update listbox
def update(data):
    #  Clear listbox
    myList.delete(0, END)

    for item in data:
        myList.insert(END, item)


#  Fill cocktail entry box
def fill(e):
    purchasedCocktail.delete(0, END)
    purchasedCocktail.insert(0, myList.get(ANCHOR))


#  Check entry vs listbox
def check(e):
    typed = purchasedCocktail.get()

    if typed == '':
        data = cocktails
    else:
        data = []
        for item in cocktails:
            if typed.lower() in item.lower():
                data.append(item)

    #  Update list with data
    update(data)


def getRecommendedDrinks(entry):
    print("Getting Recommendations...")
    topFive, topFiveIndices = main.getRecommendedDrinks(entry)

    recommendationsList.configure(state="normal")

    if recommendationsList:
        recommendationsList.delete("0.0", END)

    i = 0
    for cocktail in topFive:
        recommendationsList.insert("0.0", cocktail + ":  " +
                                   main.df['Ingredients'].iloc[topFiveIndices[i]] + "\n\n")
        i += 1

    recommendationsList.configure(state="disable")


#  Top frame
topFrame = tk.CTkFrame(master=root)
topFrame.pack(pady=40, padx=60, fill="both", expand=False)

#  Bottom Frame
bottomFrame = tk.CTkFrame(master=root)
bottomFrame.pack(pady=20, padx=100, fill="both", expand=False)

#  Top Label
label = tk.CTkLabel(master=topFrame, text="Cocktail Recommender", font=("Helvetica", 30, "bold"))
label.pack(pady=20, padx=10)

#  Entry box
purchasedCocktail = tk.CTkEntry(master=topFrame, placeholder_text="Cocktail Name", width=300,
                                font=("Helvetica", 13, "bold"))
purchasedCocktail.pack(pady=40, padx=10)

#  Search list
myList = Listbox(master=topFrame, width=75, height=10, background="#212121", fg="white", font=("Helvetica", 10, "bold"))
myList.pack()
cocktails = cocktailList

#  Binding on listbox click
myList.bind("<<ListboxSelect>>", fill)

#  Create binding on entry box
purchasedCocktail.bind("<KeyRelease>", check)

#  Get Suggestions Button
button = tk.CTkButton(master=topFrame, text="Get Suggestions",
                      command=lambda: getRecommendedDrinks(purchasedCocktail.get()), font=("Helvetica", 12, "bold"))
button.pack(pady=30)

#  Recommendations Label
recommendationsLabel = tk.CTkLabel(master=bottomFrame, text="Recommendations", font=("Helvetica", 30, "bold"))
recommendationsLabel.pack(pady=20, padx=10)

#  Recommendations List
recommendationsList = tk.CTkTextbox(master=bottomFrame, width=500, height=300, wrap="word",
                                    font=("Helvetica", 12, "bold"), yscrollcommand=False)
recommendationsList.pack(pady=120)
recommendationsList.configure(state="disabled")

#  Add drinks to list
update(cocktails)

root.mainloop()
