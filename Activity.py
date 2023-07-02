class Activity():
  def __init__(self, number, duration, description, predecessors):
    self.number = number
    self.duration = duration
    self.description = description
    self.predecessors = predecessors
    self.early_start = None
    self.early_finish = None
    self.late_start = None
    self.late_finish = None
    self.slack = None

  def calculate_early_finish(self):
    self.early_finish = self.duration + self.early_start

  def calculate_late_start(self):
    self.late_start = self.late_finish - self.duration

  def calculate_early_start(self):
    # if no predecessors, its the first node
    if len(self.predecessors) == 0:
      self.early_start = 0
      self.calculate_early_finish()
      return

    for predecessor in self.predecessors:
      if self.early_start == None:
        self.early_start = predecessor.early_finish
      if predecessor.early_finish > self.early_start:
        self.early_start = predecessor.early_finish

  def calculate_late_finish(self):
    for predecessor in self.predecessors:
      if predecessor.late_finish == None:
        predecessor.late_finish = self.late_start
      if predecessor.late_finish >= self.late_start:
        predecessor.late_finish = self.late_start

  def calculate_slack(self):
    self.slack = self.late_finish - self.early_finish

  def print(self):
    print(f"Actividad Act. {self.number}, duración: {self.duration}, descripción: {self.description}")
