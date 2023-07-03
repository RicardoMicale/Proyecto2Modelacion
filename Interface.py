import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt

class Interface():
  def __init__(self):
    self.root = tk.Tk()
    self.activity_options = {}
    self.activity_list = []
    self.create_activity = None
    self.critical_path = None
    self.get_slack = None

  def initialize_screen(self):
    self.root.mainloop()

  def create_window(
    self,
    activity_options: dict,
    activity_list: list,
    create_activity,
    critical_path,
    get_slack
  ):
    # initializes the values
    self.activity_options = activity_options
    self.activity_list = activity_list
    self.create_activity = create_activity
    self.critical_path = critical_path
    self.get_slack = get_slack

    self.root.geometry("200x200+20+20")
    self.root.configure(bg="lightblue")

    # creates window elements

    # button to create activity
    tk.Button(master=self.root, text="Agregar actividad", command=self.activity_window).grid(row=2, column=1, padx=10, pady=10, sticky="w")

    #button to visualize critical path
    tk.Button(master=self.root, text="Ver ruta critica", command=self.route_window).grid(row=4, column=1, padx=10, pady=10, sticky="w")

    # button to visualize graph
    tk.Button(master=self.root, text="Ver grafo", command=self.graph_window).grid(row=6, column=1, padx=10, pady=10, sticky="w")

    # button to visualize slack
    tk.Button(master=self.root, text="Ver holguras", command=self.slack_window).grid(row=8, column=1, padx=10, pady=10, sticky="w")

  def activity_window(self):
    # creates window for the activity creation
    master = Interface()
    master.root.title("Agregar actividad")
    master.root.configure(bg="lightblue")

    # windows elements
    tk.Label(master.root, text="Identificador (Letra):", bg="lightblue").grid(row=2, column=1, padx=10, pady=10, sticky="w")
    number = tk.Entry(master.root)
    number.grid(row=2, column=2, padx=10, pady=10, sticky="w")

    tk.Label(master.root, text="Duración: ", bg="lightblue").grid(row=4, column=1, padx=10, pady=10, sticky="w")
    duration = tk.Entry(master.root)
    duration.grid(row=4, column=2, padx=10, pady=10, sticky="w")

    tk.Label(master.root, text="Descripción: ", bg="lightblue").grid(row=6, column=1, padx=10, pady=10, sticky="w")
    description = tk.Entry(master.root)
    description.grid(row=6, column=2, padx=10, pady=10, sticky="w")

    # dynamic buttons depending on the activities array
    tk.Label(master.root, text="Predecesor(es): ", bg="lightblue").grid(row=2, column=4, padx=10, pady=10, sticky="w")
    tk.Label(master.root, text="Seleccione todos y luego presione el botón. ", bg="lightblue").grid(row=3, column=4, padx=10, pady=10, sticky="w")
    # starting row for the predecessor options
    dynamic_row = 4
    # checkbox variables
    predecessor_vars = {}
    selected_predecessors = []

    def select_option(number):
      predecessor_vars[number].set(1)
      # clears the selected array
      selected_predecessors.clear()
      items = predecessor_vars.values()
      for i, var in enumerate(items):
        if var.get() == 1:
          selected_predecessors.append(self.activity_list[i])

    for activity in self.activity_list:
      check = tk.IntVar()
      check.set(0)
      predecessor = tk.Checkbutton(master.root, text=activity.number, variable=check, command=lambda num=activity.number: select_option(num), offvalue=0, onvalue=1, bg="lightblue")
      predecessor.grid(row=dynamic_row, column=4, padx=10, pady=10, sticky="w")
      predecessor_vars[activity.number] = check
      dynamic_row += 1

    # button to add predecessors
    # tk.Button(master.root, text="Agregar predecesor", command=select_option).grid(row=dynamic_row + 1, column=4)

    def add_activity():
      self.create_activity(number.get(), int(duration.get()), description.get(), selected_predecessors)
      master.root.destroy()

    # button to create activity
    tk.Button(master.root, text="Agregar actividad", command=add_activity).grid(row=dynamic_row + 3, column=4, padx=10, pady=10, sticky="w")

    master.root.mainloop()

  def graph_window(self):
    # map activity list array
    # map its corresponding predecessor array
    # store the value as a tuple in the form (source, end, duration of source)
    edges = []
    for activity in self.activity_list:
      for predecessor in self.activity_options[activity.number]:
        edges.append((activity.number, predecessor.number, activity.duration))

    # creates graph
    graph = nx.DiGraph()

    # adding the edges
    for source, end, duration in edges:
      graph.add_edge(source, end, weight=duration)

    # gets the critical path
    path = self.critical_path()

    # creating the layout
    layout = nx.spring_layout(graph)

    # making the graph
    plt.figure(figsize=(8, 6))
    nx.draw_networkx(graph, layout, with_labels=True, node_size=500, node_color="lightblue",
                 font_size=12, font_weight="bold", width=1.5, edge_color="gray")

    # highlighting the critical path nodes
    path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    nx.draw_networkx_edges(graph, layout, edgelist=path_edges, width=2, edge_color="aquamarine")

    nx.draw_networkx_nodes(graph, layout, nodelist=path, node_color="aquamarine", node_size=500)

    plt.title("Camino critico")
    plt.axis("off")
    plt.tight_layout()
    plt.show()

  def route_window(self):
    path = self.critical_path()
    path.reverse()
    path_string = ''

    for i, number in enumerate(path):
      if i == len(path) - 1:
        path_string += number
        continue

      path_string += f'{number}, '


    master = Interface()
    master.root.title("Ruta critica")
    master.root.configure(bg="lightblue")

    tk.Label(master.root, text=path_string, bg="lightblue").pack()

    master.root.mainloop()
    return

  def slack_window(self):
    master = Interface()
    master.root.title("Holguras")
    master.root.configure(bg="lightblue")

    slack_string = ''
    for activity in self.get_slack():
      slack_string += f'Actividad: Act. {activity.number}, holgura: {activity.slack}\n'

    tk.Label(master.root, text=slack_string, bg="lightblue").pack()

    master.root.mainloop()


