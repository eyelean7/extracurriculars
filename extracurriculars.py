student_activities = {}
#reads csv
import csv
with open (r"C:\Users\igorski\Desktop\ext day csv\K-1 Extended Day 2015-2016 Monday.csv") as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         student_activities.update({row['Name  ']: [row['Notes/Activities ']]})

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

#writes to csv
def csv_dict_writer():
    name = "Name  "
    activities = "Notes/Activities "
    with open("Finished K-1 Extended Day 2015-2016 Monday.csv", 'w', newline='') as out_file:
        writer = csv.DictWriter(out_file, (name, activities))
        writer.writeheader()
        for student in student_activities:
            row = {name: student, activities: ' '.join(student_activities[student])}
            writer.writerow(row)

