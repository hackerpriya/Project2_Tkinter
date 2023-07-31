import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import calendar  # Import the 'calendar' module separately


def show_selected_date():
    year = int(year_var.get())
    month = int(month_var.get())
    date = date_picker.selection_get()
    day = date.day
    cal = calendar.month(year, month)  # Use the 'calendar' module
    result_label.config(text=f"Date Picked: {year}-{month:02d}-{day:02d}")


# Create the main application window
app = tk.Tk()
app.title("Calendar Date Picker App")

# Year selection
year_label = ttk.Label(app, text="Select Year:")
year_label.pack(pady=5)
year_var = tk.StringVar()
year_combobox = ttk.Combobox(app, textvariable=year_var, values=list(range(2000, 2030)))
year_combobox.pack()

# Month selection
month_label = ttk.Label(app, text="Select Month:")
month_label.pack(pady=5)
month_var = tk.StringVar()
month_combobox = ttk.Combobox(app, textvariable=month_var, values=list(range(1, 13)))
month_combobox.pack()

# Date picker
date_picker_label = ttk.Label(app, text="Select Date:")
date_picker_label.pack(pady=5)
date_picker = Calendar(app, selectmode="day", date_pattern="yyyy-mm-dd")
date_picker.pack(pady=5)

# Show selected date button
show_button = ttk.Button(app, text="Show Date", command=show_selected_date)
show_button.pack(pady=10)

# Result display label
result_label = ttk.Label(app, text="")
result_label.pack()

# Start the main event loop
app.mainloop()
