import sqlite3
from flask import Flask
import json

app = Flask(__name__)


@app.route("/<id>")
def get_animal_by_id(id):
    con = sqlite3.connect("animal.db")
    cur = con.cursor()
    sql = f"SELECT animal_id, age_upon_outcome, name,  animals_types, breed  FROM animals " \
          f"where animal_id = '{id}'"
    result = cur.execute(sql).fetchall()
    result_dict = {
        "animal_id": result[0][0],
        "age_upon_outcome": result[0][1],
        "name": result[0][2],
        "animals_types": result[0][3],
        "breed": result[0][4]
    }
    return json.dumps(result_dict)


if __name__ == '__main__':
    app.run(port=5002)
