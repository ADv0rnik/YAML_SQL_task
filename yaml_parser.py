import yaml

with open('a.yaml', 'r') as stream:
    data_loaded = yaml.load(stream, Loader=yaml.SafeLoader)

    template = '''INSERT INTO games (game_id, name, date) VALUES ({}, '{}', '{}')'''
    statements = [template.format(n['id'], n['name'], n['date']) for n in data_loaded['games']]
    # checking the list of statements
    print(statements[1])