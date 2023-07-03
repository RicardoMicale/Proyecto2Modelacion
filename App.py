from Activity import Activity
from Interface import Interface
import tkinter as tk

ACTIVITY_LIST = []
ACTIVITY_DICT = {}
CRITICAL_PATH = []

def forward_pass():
  for activity in ACTIVITY_LIST:
    activity.calculate_early_start()
    activity.calculate_early_finish()

def backward_pass():
  activities_copy = ACTIVITY_LIST
  _activities = []

  if len(CRITICAL_PATH) > 0:
    CRITICAL_PATH.clear()
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
    # if there is no slack, then it is in the critical path
    if activity.slack == 0: CRITICAL_PATH.append(activity.number)

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

def critical_path():
  if len(ACTIVITY_LIST) == 0:
    return []

  if len(ACTIVITY_LIST) == 1:
    return [ACTIVITY_LIST[0].number]
  forward_pass()
  backward_pass()
  critical_path = CRITICAL_PATH
  return critical_path

def get_slack():
  activities_with_slack = []

  for activity in ACTIVITY_LIST:
    if activity.slack != 0:
      activities_with_slack.append(activity)

  return activities_with_slack

def App():
  interface = Interface()
  interface.create_window(ACTIVITY_DICT, ACTIVITY_LIST, create_activity, critical_path, get_slack)
  interface.initialize_screen()

