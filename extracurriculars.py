student_activities = {
    "alice" :    ["math", "art"],
    "bob" :      ["art", "music"],
    "charlie" :  ["craft", "math"]
    }

# adds an activity to 
def add_roster(activity, roster):
    for name in roster:
        if name not in student_activities:
            student_activities[name] = [activity]
        else:
            student_activities[name].append(activity)
        




# deletes an activity from everyone's schedule
def delete_activity(activity_to_delete):
    for student in student_activities:
        activities = student_activities[student]
        updated_activities=[activity for activity in activities if activity is not activity_to_delete]
        student_activities[student] = updated_activities

