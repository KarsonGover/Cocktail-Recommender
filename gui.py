from tkinter import Listbox, END, ACTIVE

import customtkinter as tk

import main

tk.set_appearance_mode("System")
tk.set_default_color_theme("dark-blue")

root = tk.CTk()
root.geometry("1000x1000")

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
    purchasedCocktail.insert(0, myList.get(ACTIVE))


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
    topFive = main.getRecommendedDrinks(entry)

    recommendations.configure(state="normal")

    if recommendations:
        recommendations.delete("0.0", END)

    recommendations.insert("0.0", topFive[0] + "\n"
                           + topFive[1] + "\n"
                           + topFive[2] + "\n"
                           + topFive[3] + "\n"
                           + topFive[4])

    recommendations.configure(state="disable")


#  Top frame
topFrame = tk.CTkFrame(master=root)
topFrame.pack(pady=60, padx=60, fill="both", expand=True)

bottomFrame = tk.CTkFrame(master=root)
bottomFrame.pack(pady=50, padx=240, fill="both", expand=True)

label = tk.CTkLabel(master=topFrame, text="Cocktail Recommender", font=("Times New Roman", 40))
label.pack(pady=20, padx=10)

#  Entry box
purchasedCocktail = tk.CTkEntry(master=topFrame, placeholder_text="Cocktail Name", width=300)
purchasedCocktail.pack(pady=12, padx=10)

myList = Listbox(master=topFrame, width=75, height=10, background="#212121", fg="white")
myList.pack(pady=40)
cocktails = cocktailList

#  Add drinks to list
update(cocktails)

#  Binding on listbox click
myList.bind("<<ListboxSelect>>", fill)

#  Create binding on entry box
purchasedCocktail.bind("<KeyRelease>", check)

button = tk.CTkButton(master=topFrame, text="Get Suggestions",
                      command=lambda: getRecommendedDrinks(purchasedCocktail.get()))
button.pack(pady=40, padx=10)

recommendationsLabel = tk.CTkLabel(master=bottomFrame, text="Recommendations", font=("Times New Roman", 40))
recommendationsLabel.pack(pady=20, padx=10)

recommendations = tk.CTkTextbox(master=bottomFrame, width=300, wrap="word")
recommendations.pack(pady=45)
recommendations.configure(state="disabled")

root.mainloop()
