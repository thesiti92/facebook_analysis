import pandas as pd 
import json

mb = ["Malcolm McCann", "JJ Batt", "Jack Daley", "Noah Cheng", "Tyler Piazza", "Henry Westerman", "Eli Burnes", "Henry Burnes", "James Dunn", "Mateen Tabatabaei", "Marshall Sloane", "Caleb Rhodes", "Silas Monahan", "Alex Iansiti"]

users = pd.read_pickle("users-messages.pd").set_index("user")
users = users.loc[mb]
# messages = messages.set_index('user')
counter = []
for index, user in users.iterrows():
    gabs = 0
    for message in user['message']:
        message = str(message)
        gabs += message.count('gab')
    counter.append({'user': index, 'references': gabs})

counter = pd.DataFrame.from_dict(counter).set_index("user")

print(counter)