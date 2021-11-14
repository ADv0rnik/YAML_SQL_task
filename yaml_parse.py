import yaml

with open('games.yaml', 'r') as stream:
    data_loaded = yaml.load(stream, Loader=yaml.SafeLoader)

    template = 'INSERT INTO games (game_id, name, date) VALUES ({}, {}, {})'
    statements = [template.format(n['id'], n['name'], n['date']) for n in data_loaded['games']]


    print(statements[1])
print(type(statements))

