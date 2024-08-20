from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import os

def calculate_mcu():
    def submit():
        total_mcu = 0
        malt_mcu_values = []
        
        beer_name = entry_beer_name.get().strip()  
        f_vol_str = entry_final_volume.get().strip()
        
        if not beer_name:
            messagebox.showerror("Error", "Please enter a beer name.")
            return
        
        if not f_vol_str:
            messagebox.showerror("Error", "Please enter a valid final volume.")
            return

        try:
            f_vol = float(f_vol_str)
        except ValueError:
            messagebox.showerror("Error", "Invalid final volume. Please enter a valid number.")
            return

        for entry in malt_entries:
            malt_name = entry[0].get().strip()
            grain_weight_str = entry[1].get().strip()
            l_degrees_str = entry[2].get().strip()

            if not malt_name:
                continue
            
            if grain_weight_str and l_degrees_str:
                try:
                    grain_weight = float(grain_weight_str)
                    l_degrees = float(l_degrees_str)
                except ValueError:
                    messagebox.showerror("Error", "Invalid input for grain weight or ºL. Please enter valid numbers.")
                    return

                # Calculating the partial MCU (Malt Colour Units)
                mcu = (grain_weight * (l_degrees * 2.205) / (f_vol * 0.264))
                
                # Appending the partial MCU value to the list
                malt_mcu_values.append((malt_name, mcu))
                
                # Each time the MCU is calculated, it is added to the total_mcu
                total_mcu += mcu

        if not malt_mcu_values:
            messagebox.showerror("Error", "Please enter at least one malt information.")
            return

        result = "\nPartial MCU values:\n"
        for malt, mcu in malt_mcu_values:
            result += "MCU for {}: {:.2f} SRM\n".format(malt, mcu)
        result += "\nTotal MCU for {}: {:.2f} SRM".format(beer_name, total_mcu)
        
        messagebox.showinfo("MCU Calculation Result", result)
        display_beer_colors(total_mcu)

        
    def add_malt_entry():
        new_frame = tk.Frame(frame_malt_info)
        new_frame.grid(row=len(malt_entries) + 1, column=0, columnspan=2, padx=5, pady=2, sticky="we")
        malt_name_label = tk.Label(new_frame, text="Malt Name:")
        malt_name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        malt_name_entry = tk.Entry(new_frame)
        malt_name_entry.grid(row=0, column=1, padx=5, pady=5)
        grain_weight_label = tk.Label(new_frame, text="Weight (kg):")
        grain_weight_label.grid(row=0, column=2, padx=5, pady=5, sticky="w")
        grain_weight_entry = tk.Entry(new_frame)
        grain_weight_entry.grid(row=0, column=3, padx=5, pady=5)
        l_degrees_label = tk.Label(new_frame, text="ºL (Degrees Lovibond):")
        l_degrees_label.grid(row=0, column=4, padx=5, pady=5, sticky="w")
        l_degrees_entry = tk.Entry(new_frame)
        l_degrees_entry.grid(row=0, column=5, padx=5, pady=5)
        malt_entries.append((malt_name_entry, grain_weight_entry, l_degrees_entry))

    window_calc_mcu = tk.Toplevel(root)
    window_calc_mcu.title("Calculate MCU")
    
    label_beer_name = tk.Label(window_calc_mcu, text="Beer Name:")
    label_beer_name.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    entry_beer_name = tk.Entry(window_calc_mcu)
    entry_beer_name.grid(row=0, column=1, padx=5, pady=5)

    label_final_volume = tk.Label(window_calc_mcu, text="Final Volume (L):")
    label_final_volume.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    entry_final_volume = tk.Entry(window_calc_mcu)
    entry_final_volume.grid(row=1, column=1, padx=5, pady=5)

    label_malt_info = tk.Label(window_calc_mcu, text="Malt Information:")
    label_malt_info.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    frame_malt_info = tk.Frame(window_calc_mcu)
    frame_malt_info.grid(row=3, column=0, columnspan=2)

    malt_entries = []
    malt_frame = tk.Frame(frame_malt_info)
    malt_frame.grid(row=0, column=0, columnspan=2, padx=5, pady=2, sticky="we")
    malt_name_label = tk.Label(malt_frame, text="Malt type:")
    malt_name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    malt_name_entry = tk.Entry(malt_frame)
    malt_name_entry.grid(row=0, column=1, padx=5, pady=5)
    grain_weight_label = tk.Label(malt_frame, text="Weight (kg):")
    grain_weight_label.grid(row=0, column=2, padx=5, pady=5, sticky="w")
    grain_weight_entry = tk.Entry(malt_frame)
    grain_weight_entry.grid(row=0, column=3, padx=5, pady=5)
    l_degrees_label = tk.Label(malt_frame, text="ºL (Degrees Lovibond):")
    l_degrees_label.grid(row=0, column=4, padx=5, pady=5, sticky="w")
    l_degrees_entry = tk.Entry(malt_frame)
    l_degrees_entry.grid(row=0, column=5, padx=5, pady=5)
    malt_entries.append((malt_name_entry, grain_weight_entry, l_degrees_entry))

    button_add_malt = tk.Button(window_calc_mcu, text="Add Malt", command=add_malt_entry)
    button_add_malt.grid(row=4, columnspan=2, padx=5, pady=5)

    button_submit = tk.Button(window_calc_mcu, text="Submit", command=submit)
    button_submit.grid(row=5, columnspan=2, padx=5, pady=5)

def display_img(sizex, sizey, img_png):
    image = Image.open(img_png)
    img_resized = image.resize((sizex, sizey))
    img = ImageTk.PhotoImage(img_resized)
    return img

def display_beer_colors(srm_val):
   
    srm_ranges = [
        (1, 3.5, "Palestraw.png"),
        (3.5, 5.5, "Straw.png"),
        (5.5, 7.5, "Palegold.png"),
        (7.5, 11.5, "Deepgold.png"),
        (11.5, 15.5, "Paleamber.png"),
        (15.5, 19.5, "Mediumamber.png"),
        (19.5, 25.5, "Deepamber.png"),
        (25.5, 32.5, "Amberbrown.png"),
        (32.5, 38.5, "Brown.png"),
        (38.5, 46.5, "Rubybrown.png"),
        (46.5, 57.5, "Deepbrown.png"),
        (57.5, 100, "Black.png")
    ]
    
    for lower, upper, img_file in srm_ranges:
        if lower <= srm_val <= upper:
            top = tk.Toplevel(root)
            top.title("Estimated beer color")
            
            img = display_img(100, 100, img_file)
            panel = tk.Label(top, image=img)
            panel.image = img  # reference
            panel.pack(side="top", fill="x", expand="yes")
            break



def convert_units():
    def submit():
        try:
            value_2_be_converted = float(entry_value.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
            return

        user_input = combobox_units.get()
        result = ""
        
        if user_input == "EBC to SRM":
            SRM = value_2_be_converted * 0.508
            result = "SRM: {:.2f}".format(SRM)
        elif user_input == "SRM to EBC":
            EBC = value_2_be_converted * 1.97
            result = "EBC: {:.2f}".format(EBC)
        elif user_input == "ºL to SRM":
            SRM = (1.3546 * value_2_be_converted) - 0.76
            result = "SRM: {:.2f}".format(SRM)
        elif user_input == "SRM to ºL":
            lovibond = (value_2_be_converted + 0.76) / 1.3546
            result = "ºL: {:.2f}".format(lovibond)
        elif user_input == "EBC to ºL":
            SRM = value_2_be_converted * 0.508
            lovibond = (SRM + 0.76) / 1.3546
            result = "ºL: {:.2f}".format(lovibond)
        
        messagebox.showinfo("Conversion Result", result)

    window_convert_units = tk.Toplevel(root)
    window_convert_units.title("Convert Units")
    
    label_value = tk.Label(window_convert_units, text="Value:")
    label_value.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    entry_value = tk.Entry(window_convert_units)
    entry_value.grid(row=0, column=1, padx=5, pady=5)

    label_units = tk.Label(window_convert_units, text="Units:")
    label_units.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    units = ["EBC to SRM", "SRM to EBC", "ºL to SRM", "SRM to ºL", "EBC to ºL"]
    combobox_units = tk.StringVar()
    combobox_units.set(units[0])
    combobox = tk.OptionMenu(window_convert_units, combobox_units, *units)
    combobox.grid(row=1, column=1, padx=5, pady=5)

    button_submit = tk.Button(window_convert_units, text="Submit", command=submit)
    button_submit.grid(row=2, columnspan=2, padx=5, pady=5)

# Initializing the main window
root = tk.Tk()
root.title("Brewery System")
root.geometry("800x800")

label_title = tk.Label(root, text="By Luiza Stein, Mariana Linck and Nicolas Heller", font=("Arial", 10))
label_title.pack(pady=7)

frame_image = tk.Frame(root)
frame_image.pack(side="top", fill="x", expand="no")

image = Image.open('welcome.png')
img_resized = image.resize((550, 550))  
image = ImageTk.PhotoImage(img_resized)
panel = tk.Label(frame_image, image=image)
panel.pack(side="top", fill="x", expand="no")

frame_buttons = tk.Frame(root)
frame_buttons.pack(side="top", fill="both", expand=True, pady=5)  

# buttons
button_mcu = tk.Button(frame_buttons, text="Calculate MCU", command=calculate_mcu)
button_mcu.pack(pady=5)

button_units = tk.Button(frame_buttons, text="Convert Units", command=convert_units)
button_units.pack(pady=5)

button_exit = tk.Button(frame_buttons, text="Exit", command=root.quit)
button_exit.pack(pady=5)

# Run the main loop
root.mainloop()
