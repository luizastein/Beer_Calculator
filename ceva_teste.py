import tkinter as tk
from tkinter import messagebox

def calculate_mcu():
    def submit():
        total_mcu = 0
        malt_mcu_values = []
        
        beer_name = entry_beer_name.get().strip()  # Remove leading/trailing whitespaces
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
                
                # Append the partial MCU value to the list
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

    label_malt_info = tk.Label(window_calc_mcu, text="Malt Information (Name, Weight(kg), ºL):")
    label_malt_info.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    frame_malt_info = tk.Frame(window_calc_mcu)
    frame_malt_info.grid(row=3, column=0, columnspan=2)

    malt_entries = []
    malt_frame = tk.Frame(frame_malt_info)
    malt_frame.grid(row=0, column=0, columnspan=2, padx=5, pady=2, sticky="we")
    malt_name_label = tk.Label(malt_frame, text="Malt Name:")
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

def convert_units():
    def submit():
        value_2_be_converted = float(entry_value.get())
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
            ºL = (value_2_be_converted + 0.76) / 1.3546
            result = "ºL: {:.2f}".format(ºL)
        elif user_input == "EBC to ºL":
            SRM = value_2_be_converted * 0.508
            ºL = (SRM + 0.76) / 1.3546
            result = "ºL: {:.2f}".format(ºL)
        
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

def exit_program():
    root.quit()

root = tk.Tk()
root.title("Brewery System")
root.geometry("600x400")

label_title = tk.Label(root, text="Welcome to the Brewery System", font=("Arial", 14))
label_title.pack(pady=10)

button_mcu = tk.Button(root, text="Calculate MCU", command=calculate_mcu)
button_mcu.pack(pady=5)

button_units = tk.Button(root, text="Convert Units", command=convert_units)
button_units.pack(pady=5)

button_exit = tk.Button(root, text="Exit", command=exit_program)
button_exit.pack(pady=5)

root.mainloop()
