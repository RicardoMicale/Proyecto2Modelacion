from Activity import Activity
import tkinter as tk

ACTIVITY_LIST = []

def forward_pass(activities: list):
  for activity in activities:
    activity.calculate_early_start()
    activity.calculate_early_finish()

def backward_pass(activities: list):
  critical_path = []
  _activities = []
  # reverses the list to traverse it from finish to start
  activities.reverse()
  # traverses the list
  for activity in activities:
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
    activity_dict: dict,
    predecessors: list=[]
  ):
  if activity_exists(number, activity_dict): return 'Ya existe la actividad'
  return Activity(number, duration, description, predecessors)

def populate_dict(dict: dict, activities: list):
  for activity in activities:
    dict[activity.number] = activity.predecessors

  return dict

def activity_exists(number: str, activity_dict: dict):
  return number in activity_dict.keys()

def is_end(activity: Activity, activity_dict: dict):
  for item in activity_dict.items():
    if item.number == activity.number:
      return False

  return True

def App():
  list_of_activities = ACTIVITY_LIST
  
  activity_dict = populate_dict({}, )

