# import tkinter as tk
# import matplotlib.pyplot as plt
# from PIL import Image
#
# # Define state-dish mapping
# state_dish_mapping = {
#     "Jammu and Kashmir": "Kashmiri Wazwan",
#     "Himachal Pradesh": "Siddu",
#     "Punjab": "Sarson ka Saag and Makki di Roti",
#     "Chandigarh": "Chole Bhature",
#     "Uttar Pradesh": "Biryani and Kebabs",
#     "Haryana": "Sarson da Saag and Makki di Roti",
#     "Delhi": "Butter Chicken",
#     "Rajasthan": "Dal Bati Churma",
#     "Gujarat": "Dhokla and Fafda",
#     "Madhya Pradesh": "Poha Jalebi",
#     "Chhattisgarh": "Bhel Puri",
#     "Bihar": "Litti Chokha",
#     "Jharkhand": "Pitha",
#     "West Bengal": "Mishti and Roshogolla",
#     "Odisha": "Gupchup",
#     "Sikkim": "Momos",
#     "Arunachal Pradesh": "Bamboo Shoot Curry",
#     "Nagaland": "Axone",
#     "Manipur": "Singju",
#     "Mizoram": "Iromba",
#     "Tripura": "Mukhuni",
#     "Meghalaya": "Doh Khlei",
#     "Assam": "Pitha",
# }
#
# # Create the main GUI window
# root = tk.Tk()
# root.title("India's Famous Dishes")
# root.geometry("800x600")
#
# # Load and display the India map
# india_map = Image.open("C://Users//Asus//Downloads//MAP.jpg")
# india_map_resized = india_map.resize((600, 400))
# india_map_label = tk.Label(root, image=india_map_resized)
#
# india_map_label.pack()
#
# # Function to handle state selection
# def handle_state_selection(state_name):
#     dish_name = state_dish_mapping[state_name]
#     dish_image = Image.open(f"{dish_name}.jpg")
#     dish_image_resized = dish_image.resize((200, 200))
#     dish_image_label = tk.Label(root, image=dish_image_resized)
#     dish_image_label.pack()
#
#     dish_description_label = tk.Label(root, text=f"{dish_name} is a famous dish of {state_name}.")
#     dish_description_label.pack()
#
# # Create state buttons and bind click events
# for state_name in state_dish_mapping.keys():
#     state_button = tk.Button(root, text=state_name, command=lambda: handle_state_selection(state_name))
#     state_button.pack()
#
# # Run the GUI application
# root.mainloop()
import os
import tkinter as tk
from PIL import Image, ImageTk

# Define state-dish mapping
state_dish_mapping = {
     "Jammu and Kashmir": "Kashmiri Wazwan",
     "Himachal Pradesh": "Siddu",
     "Punjab": "Sarson ka Saag and Makki di Roti",
     "Chandigarh": "Chole Bhature",
     "Uttar Pradesh": "Biryani and Kebabs",
     "Haryana": "Sarson da Saag and Makki di Roti",
     "Delhi": "Butter Chicken",
     "Rajasthan": "Dal Bati Churma",
     "Gujarat": "Dhokla and Fafda",
     "Madhya Pradesh": "Poha Jalebi",
    "Chhattisgarh": "Bhel Puri",
    "Bihar": "Litti Chokha",
     "Jharkhand": "Pitha",
     "West Bengal": "Mishti and Roshogolla",
     "Odisha": "Gupchup",
     "Sikkim": "Momos",
     "Arunachal Pradesh": "Bamboo Shoot Curry",
     "Nagaland": "Axone",
     "Manipur": "Singju",
     "Mizoram": "Iromba",
     "Tripura": "Mukhuni",
     "Meghalaya": "Doh Khlei",
     "Assam": "Pitha",
}

# Load images
india_map = Image.open(os.path.join("C:/Users/Asus/Downloads", "MAP.jpg"))
india_map_resized = india_map.resize((600, 400))

dish_images = {}
for dish_name in state_dish_mapping.values():
    dish_image = Image.open(os.path.join(f"{dish_name}.jpg"))
    dish_images[dish_name] = dish_image.resize((200, 200))

# Create the main GUI window
root = tk.Tk()
root.title("India's Famous Dishes")
root.geometry("800x600")

# Display the India map
india_map_label = tk.Label(root, image=ImageTk.PhotoImage(india_map_resized))
india_map_label.pack()

# Frame for displaying dish image and description
dish_frame = tk.Frame(root)
dish_frame.pack()

# Function to handle state selection
def handle_state_selection(state_name):
    dish_name = state_dish_mapping[state_name]

    # Clear the dish_frame
    for widget in dish_frame.winfo_children():
        widget.destroy()

    # Display dish image
    dish_image_label = tk.Label(dish_frame, image=ImageTk.PhotoImage(dish_images[dish_name]))
    dish_image_label.pack()

    # Display dish description
    dish_description_label = tk.Label(dish_frame, text=f"{dish_name} is a famous dish of {state_name}.")
    dish_description_label.pack()

# Create state buttons and bind click events
for state_name in state_dish_mapping.keys():
    state_button = tk.Button(root, text=state_name, command=lambda name=state_name: handle_state_selection(name))
    state_button.pack()

# Run the GUI application
root.mainloop()
