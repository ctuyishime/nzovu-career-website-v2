from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db


app = Flask(__name__)

'''
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
'''

@app.route("/")
def home():
    jobs = load_jobs_from_db()
    return render_template("home.html", jobs=jobs)

@app.route("/api/jobs") # Create an api end point
def data():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Not Found", 404
    return render_template("jobpage.html", job = job)

@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data = request.form
  job = load_job_from_db(id)
  add_application_to_db(id, data)
  return render_template('application_submitted.html', 
                         application=data,
                         job=job)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)

# 3:42
