import tkinter as tk

class Interface():
  def __init__(self, activity_options):
    self.root = tk.Tk()
    self.activity_options = activity_options

  def initialize_screen(self):
    self.root.mainloop()

  def activity_window(self):
    # creates window for the activity creation
    master = Interface()

    # windows elements
    tk.Label(master, text="Identificador (Letra):").grid(row=2, column=1)
    number = tk.Entry(master)
    number.grid(row=2, column=2)

    tk.Label(master, text="Duracion: ").grid(row=4, column=1)
    duration = tk.Entry(master)
    duration.grid(row=4, column=2)

    tk.Label(master, text="Descripción: ").grid(row=6, column=1)
    description = tk.Entry(master)
    description.grid(row=6, column=2)

    # dynamic buttons depending on the activities array
    tk.Label(master, text="Predecesor(es): ").grid(row=2, column=4)


