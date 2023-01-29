from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)   
app.secret_key = 'notasecret'

# Main page
@app.route('/')
def index():
    if 'count' not in session:
        session['count']=1
    else:
        session['count']+=1
    return render_template("index.html", count= session['count'])

# Clear route
@app.route('/clear')
def clear():
        session.clear()
        return redirect('/')

# Posting route
@app.route("/count", methods=["POST"])
def view_count():

    if request.form["change"]=="add":
        session["count"] += 1
        return redirect('/')

    elif request.form["change"]=="reset":
        session["count"] = 0
        return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)