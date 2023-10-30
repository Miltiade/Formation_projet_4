from tinydb import TinyDB, Query

db = TinyDB('db.json')
tournaments_table = db.table('tournaments')

def save_tournament(tournament):
    tournament_data = tournament.serialize()
    tournaments_table.insert(tournament_data)