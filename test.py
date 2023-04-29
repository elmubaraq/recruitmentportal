import csv
from portal import db,app,test
with open("./failed.csv", 'r') as file1:
    csvreader = csv.reader(file1)
    with app.app_context():
        db.create_all()
        doc =test(name="failed", data=csvreader)
        db.session.add(doc)
        db.session.commit()
        print("Success")
        