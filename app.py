from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import text
from database import engine

app = Flask(__name__)


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    result_all = result.all()
    jobs = []
    for row in result_all:
      jobs.append(row._mapping)
    return jobs


@app.route("/")
def home():
  jobs = load_jobs_from_db()
  return render_template("home.html", jobs=jobs)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80, debug=True)
