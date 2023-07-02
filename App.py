from Activity import Activity
from Interface import Interface
import tkinter as tk

ACTIVITY_LIST = []
ACTIVITY_DICT = {}

def forward_pass():
  for activity in ACTIVITY_LIST:
    activity.calculate_early_start()
    activity.calculate_early_finish()

def backward_pass():
  activities_copy = ACTIVITY_LIST
  critical_path = []
  _activities = []
  # reverses the list to traverse it from finish to start
  activities_copy.reverse()
  # traverses the list
  for activity in activities_copy:
    if is_end(activity):
      activity.late_finish = activity.early_finish
      activity.late_start = activity.early_start
    activity.calculate_late_start()
    activity.calculate_late_finish()
    activity.calculate_slack()
    _activities.append(activity)
    # if there is no slack, then it ir in the critical path
    if activity.slack == 0: critical_path.append(activity)

def create_activity(
    number: str,
    duration: int,
    description: str,
    predecessors: list=[]
  ):
  if activity_exists(number): return 'Ya existe la actividad'
  ACTIVITY_LIST.append(Activity(number, duration, description, predecessors))
  ACTIVITY_DICT[number] = predecessors
  return 'Actividad agregada'

def activity_exists(number: str):
  return number in ACTIVITY_DICT.keys()

def is_end(activity: Activity):
  for item in ACTIVITY_DICT.values():
    for sub_item in item:
      if sub_item.number == activity.number:
        return False

  return True

def App():
  interface = Interface()
  interface.create_window(ACTIVITY_DICT, ACTIVITY_LIST, create_activity)
  interface.initialize_screen()

App()

