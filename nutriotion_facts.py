import requests
import json
import tkinter as tk

# API configuration
api_url = 'https://api.calorieninjas.com/v1/nutrition?query='

def getfacts():
    query = fooden.get()
    response = requests.get(api_url + query, headers={'X-Api-Key': 'bh97Lwh8H63GPaepHMFYyQ==emRjdzsFg0U2XWV5'})
    if response.status_code == requests.codes.ok:
        data = response.json()
        items = data.get('items', [])
        if items:
            item = items[0]
            # Extract nutrition facts
            nutrition_facts = [
                f"Nutrition Facts for {item.get('name', 'N/A')}:",
                f"Calories: {item.get('calories', 'N/A')}",
                f"Total Fat: {item.get('fat_total_g', 'N/A')}g",
                f"Saturated Fat: {item.get('fat_saturated_g', 'N/A')}g",
                f"Protein: {item.get('protein_g', 'N/A')}g",
                f"Sodium: {item.get('sodium_mg', 'N/A')}mg",
                f"Potassium: {item.get('potassium_mg', 'N/A')}mg",
                f"Cholesterol: {item.get('cholesterol_mg', 'N/A')}mg",
                f"Carbohydrates: {item.get('carbohydrates_total_g', 'N/A')}g",
                f"Fiber: {item.get('fiber_g', 'N/A')}g",
                f"Sugar: {item.get('sugar_g', 'N/A')}g",
            ]
            # Clear the Listbox and insert new items
            listbox.delete(0, tk.END)
            for fact in nutrition_facts:
                listbox.insert(tk.END, fact)
        else:
            listbox.delete(0, tk.END)
            listbox.insert(tk.END, "No data found for the entered query.")
    else:
        listbox.delete(0, tk.END)
        listbox.insert(tk.END, f"Error: {response.status_code}")

# GUI setup
root = tk.Tk()
root.title("Nutrition Facts")

# Input fields and button
label = tk.Label(root, text="Food:")
fooden = tk.Entry(root)
getbtn = tk.Button(root, text="Get Facts", command=getfacts)

# Listbox to display nutrition facts
listbox = tk.Listbox(root, width=50, height=15)

# Layout
label.pack()
fooden.pack()
getbtn.pack()
listbox.pack()

root.mainloop()
