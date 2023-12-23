from flask import Flask, render_template, jsonify
from database import load_jobs_from_db


app = Flask(__name__)

# JOBS = [
#     {
#         'id':1,
#         'title': 'Data Science',
#         'location': 'Austin, USA',
#         'salary': '$100,000'
#     },
#     {
#         'id':2,
#         'title': 'Music Producer',
#         'location': 'Nyanza, Rwanda',
#         'salary': '1,023,000 Franc'
#     },
#     {
#         'id':3,
#         'title': 'Kananga',
#         'location': 'Kibuye, Rwanda',
#         'salary': '$80,000'
#     }
# ]

@app.route("/")
def hello_world():
    jobs = load_jobs_from_db()
    return render_template("home.html", jobs=jobs, company_name="Nzovu Media")

@app.route("/api/jobs") # Create an api end point
def data():
    jobs = load_jobs_from_db()
    return jsonify(jobs)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)


# Data driven website
# 2:04 