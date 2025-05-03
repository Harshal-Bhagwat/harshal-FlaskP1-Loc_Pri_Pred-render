from flask import *
from pickle import *

f = open("model.pkl", "rb")
model = load(f)
f.close()

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
	if request.method == "POST":
		area = float(request.form["area"])
		loc = int(request.form["loc"])

		if loc == 1:
			d = [[area, 1, 0, 0]]
		elif loc == 2:
			d = [[area, 0, 1, 0]]
		else:
			d = [[area, 0, 0, 1]]

		price = model.predict(d)
		msg = "Predicted Price = " + str(round(price[0], 2))
		return render_template("home.html", msg = msg)
	else:
		return render_template("home.html")

if __name__ == "__main__":
	app.run(use_reloader = True, debug = True)


















