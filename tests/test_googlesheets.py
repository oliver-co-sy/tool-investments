from utils import GoogleSheets

sheet = GoogleSheets(service_account_json_file="../key.json")
sheet.open(title="google-sheets-test")
sheet.set_headers(["First Name", "Last Name", "Age"])
sheet.set_records([
    ["Bruce", "Wayne", 25],
    ["Richard", "Grayson", 19],
    ["Damian", "Wayne", 10],
    ["Jason", "Todd", 18],
    ["Timothy", "Drake", 16]
])

sheet.add_worksheet(title="Villains", rows=10, cols=50)
sheet.set_headers(["First Name", "Last Name", "Age"])
sheet.set_records([
    ["Selena", "Kyle", 21],
    ["Lex", "Luthor", 29],
    ["Harleen", "Quinzel", 23],
    ["Jason", "Todd", 18],
    ["Timothy", "Drake", 16]
])

sheet.select_worksheet(title="Villains")
sheet.clear_records()

sheet.select_worksheet(title="Villains")
sheet.delete_worksheet()

sheet.new(title="marvel-heroes", email="oliver.co.sy@gmail.com")
sheet.set_headers(["First Name", "Last Name", "Age"])
sheet.set_records([
    ["Peter", "Parker", 17],
    ["Steve", "Rogers", 25],
    ["Tony", "Stark", 25]
])
