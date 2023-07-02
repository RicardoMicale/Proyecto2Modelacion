import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt

class Interface():
  def __init__(self):
    self.root = tk.Tk()
    self.activity_options = {}
    self.activity_list = []
    self.create_activity = None

  def initialize_screen(self):
    self.root.mainloop()

  def create_window(self, activity_options: dict, activity_list: list, create_activity):
    # initializes the values
    self.activity_options = activity_options
    self.activity_list = activity_list
    self.create_activity = create_activity

    # creates window elements

    # button to create activity
    tk.Button(master=self.root, text="Agregar actividad", command=self.activity_window).grid(row=2, column=1)

    tk.Button(master=self.root, text="Conseguir ruta critica").grid(row=4, column=1)

  def activity_window(self):
    # creates window for the activity creation
    master = Interface()

    # windows elements
    tk.Label(master.root, text="Identificador (Letra):").grid(row=2, column=1)
    number = tk.Entry(master.root)
    number.grid(row=2, column=2)

    tk.Label(master.root, text="Duracion: ").grid(row=4, column=1)
    duration = tk.Entry(master.root)
    duration.grid(row=4, column=2)

    tk.Label(master.root, text="Descripción: ").grid(row=6, column=1)
    description = tk.Entry(master.root)
    description.grid(row=6, column=2)

    # dynamic buttons depending on the activities array
    tk.Label(master.root, text="Predecesor(es): ").grid(row=2, column=4)
    tk.Label(master.root, text="Seleccione todos y luego presione el botón. ").grid(row=3, column=4)
    # starting row for the predecessor options
    dynamic_row = 4
    # checkbox variables
    predecessor_vars = []
    selected_predecessors = []

    def select_option():
      # clears the selected array
      selected_predecessors.clear()
      for i, var in enumerate(predecessor_vars):
        if var.get() == 1:
          selected_predecessors.append(self.activity_list[i].number)

    for activity in self.activity_list:
      check = tk.IntVar()
      check.set(0)
      predecessor = tk.Checkbutton(master.root, text=activity.number, variable=check, command=lambda: check.set(1 if check.get() == 0 else 0))
      predecessor.grid(row=dynamic_row, column=4)
      predecessor_vars.append(check)
      dynamic_row += 1

    # button to add predecessors
    tk.Button(master.root, text="Agregar predecesor", command=select_option).grid(row=dynamic_row + 1, column=4)

    def add_activity():
      self.create_activity(number.get(), int(duration.get()), description.get(), selected_predecessors)
      master.root.destroy()

    # button to create activity
    tk.Button(master.root, text="Agregar actividad", command=add_activity).grid(row=dynamic_row + 3, column=4)

    master.root.mainloop()

  def route_window(self, activity_dict: dict, activity_list: list):
    # map activity list array
    # map its corresponding predecessor array
    # store the value as a tuple in the form (source, end, duration of source)
    edges = []
    for activity in activity_list:
      for predecessor in activity_dict[activity.number]:
        edges.append((activity.number, predecessor.number, activity.duration))

    # creates graph
    graph = nx.DiGraph()

    # adding the edges
    for source, end, duration in edges:
      graph.add_edge(source, end, weight=duration)




