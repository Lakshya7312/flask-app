from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [{
    "ID": 1,
    "name": u"person 1",
    "contact": 9513210209,
    "done": False
},
    {
    "ID": 2,
    "name": u"person 2",
    "contact": 7516436506,
    "done": False
},
    {
    "ID": 3,
    "name": u"person 3",
    "contact": 8542456505,
    "done": False
},
    {
    "ID": 4,
    "name": u"person 4",
    "contact": 9426722004,
    "done": False
}]


@app.route("/add_data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "Error",
            "message": "There are no contacts data!"
        }, 400)

    task = {
        "ID": contacts[-1]["ID"] + 1,
        "name": request.json["name"],
        "contact": request.json.get("contact", ""),
        "done": False
    }

    contacts.append(task)
    return jsonify({
        "status": "Success",
        "message": "The contact has been added successfully"
    })


@app.route("/get-data")
def get_tasks():
    return jsonify({
        "data": contacts
    })


if __name__ == '__main__':
    app.run(debug=True)
