from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

variables = []
@app.route("/", methods=["POST", "GET"])
def home():
    global variables
    if request.method == "POST":
        try:
            variables.append(request.form["kilometer"])
            variables.append(request.form["meter"])
            variables.append(request.form["celsius"])
            return redirect(url_for("results", state=0))
        
        except:
            variables.append(request.form["mile"])
            variables.append(request.form["foot"])
            variables.append(request.form["fahrenheit"])
            return redirect(url_for("results", state=1))
    return render_template("index.html")

@app.route("/results+<state>")
def results(state):
    global variables

    if state == "0":
        finish = {
            "mile": float(variables[0])/1.61,
            "foot": float(variables[1])*3.28,
            "fahrenheit": 32.00+float(variables[2])*1.80
        }

    if state == "1":
        if variables[2].find(",") != -1:
            variables[2] = variables[2].replace(",", ".")
        finish = {
            "kilometer": float(variables[0])*1.61,
            "meter": float(variables[1])/3.28,
            "celsius": round((float(variables[2])-32)/1.80)
        }
    return render_template("results.html", old=variables, variables=finish)


if __name__ == '__main__':
    app.run(debug=True)