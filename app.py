from flask import Flask, render_template, jsonify


app = Flask(__name__)

JOBS = [
    {
        'id':1,
        'title': 'Data Science',
        'location': 'Austin, USA',
        'salary': '$100,000'
    },
    {
        'id':2,
        'title': 'Music Produce',
        'location': 'Nyanza, Rwanda',
        'salary': '1,023,000 Franc'
    },
    {
        'id':3,
        'title': 'Umushumba',
        'location': 'Kibuye, Rwanda',
    }
]

@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBS, company_name="Nzovu Media")

@app.route("/api/jobs") # Create an api end point
def data():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
