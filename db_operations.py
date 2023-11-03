from tinydb import TinyDB, Query

db = TinyDB('db.json')
tournaments_table = db.table('tournaments')

def save_tournament(tournament):
    tournament_data = tournament.serialize()
    print(tournament_data)
    tournaments_table.insert(tournament_data)

def update_tournament(tournament):
    tournament_data = tournament.serialize()
    print(tournament_data)
    Tournament = Query()
    tournaments_table.update(tournament_data,Tournament.name==tournament_data["name"])
    