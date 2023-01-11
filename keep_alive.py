from flask import Flask, render_template, request
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return render_template("index.html",title="NotifyNotice")

@app.route('/success', methods=["POST"])
def success():
  phno=request.form.get("ph_no")
  fName=request.form.get("fName")
  CRN=request.form.get("CRN")
  return render_template("success.html", title="Successful!", phno=phno, fName=fName, CRN=CRN)


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
