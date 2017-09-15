import pandas as pd 
import json

users = pd.DataFrame(pd.read_json('messages.json', orient = 'records').reset_index().groupby("user")['message'].apply(list).reset_index())
users = users.drop(users.index[len(users.message) < 50])
# messages = messages.set_index('user')
swears = json.load(open('swears.json'))
counter = []
for index, user in users.iterrows():
    fucks = 0
    swear_counts = {swear: 0 for swear in swears}
    for message in user['message']:
        message = str(message)
        for swear in swears:
            swear_counts[swear] += message.count(" "+swear+" ")
    swear_counts = pd.DataFrame.from_dict(swear_counts, orient='index').rename(columns={0 : 'count'})
    swear_counts = swear_counts.sort_values('count', ascending=False)
    swear_counts = swear_counts[:10]
    counter.append({'user': user['user'], 'swear_counts': swear_counts})

counter = pd.DataFrame.from_dict(counter).set_index("user")
mb = ["Malcolm McCann", "JJ Batt", "Jack Daley", "Noah Cheng", "Tyler Piazza", "Henry Westerman", "Eli Burnes", "Henry Burnes", "James Dunn", "Mateen Tabatabaei", "Marshall Sloane", "Caleb Rhodes", "Silas Monahan", "Alex Iansiti"]

for user, row in counter.loc[mb].iterrows():
    print('%s:\n %s' % (user, row['swear_counts']), file=open("mb_swears.txt", "a"))