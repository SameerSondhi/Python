from flask_app import app
from flask_app.models.user_model import User
from flask import render_template,redirect,request

@app.route("/")
def all_users():
    # call the get all classmethod to get all users
    all_users = User.get_all()
    print(all_users)
    return render_template("all_users.html", all_users = all_users)


# Adding a User
@app.route('/users/create', methods=["POST"])
def create():
    User.create(request.form)
    return redirect('/')


# Create form
@app.route("/users/new")
def new_user_form():
    return render_template("add_user.html")

# Show one user
@app.route("/users/<int:id>/view")
def get_one(id):
    data = {
        'id': id
    }
    one_user = User.get_one(data)
    return render_template("one_user.html", one_user = one_user)

# Update/Edit user 
@app.route("/users/<int:id>/edit")
def edit_user(id):
    this_user = User.get_one({'id': id})
    return render_template("users_edit.html",  this_user=this_user)

@app.route("/users/<int:id>/update", methods=["POST"])
def update_user(id):
    data = {
        "id": id,
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.update(data)
    return redirect("/")

# Delete a User
@app.route("/users/<int:id>/delete")
def delete_user(id):
    User.delete({'id':id})
    return redirect("/")





