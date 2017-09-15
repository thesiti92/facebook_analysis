import pandas as pd 

users = pd.DataFrame(pd.read_json('messages.json', orient = 'records').reset_index().groupby("user")['message'].apply(list).reset_index())

# messages = messages.set_index('user')

counter = []
for index, user in users.iterrows():
    fucks = 0
    for message in user['message']:
        message = str(message)
        if 'fuck' in message:
            fucks+=1
    counter.append({'user': user['user'], 'fucks': fucks})

counter = pd.DataFrame(counter)
counter = counter.sort_values('fucks', ascending=False)
print(counter)