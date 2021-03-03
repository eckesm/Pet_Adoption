from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "abc123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
toolbar = DebugToolbarExtension(app)


@app.route('/')
def show_home_page():
    """Show home page."""

    pets = Pet.query.all()
    return render_template('home.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Show add pet form or add form data to adopt database."""

    form = AddPetForm()
    if form.validate_on_submit():
        # name = form.name.data
        # species = form.species.data
        # photo_url = form.photo_url.data
        # if photo_url == '':
        #     photo_url = None
        # age = form.age.data
        # notes = form.notes.data
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        if data['photo_url'] == '':
            data['photo_url'] = None
        # pet = Pet(name=name, species=species,
        #           photo_url=photo_url, age=age, notes=notes)
        pet=Pet(**data)
        db.session.add(pet)
        db.session.commit()
        flash(f"{data['name']} has been added!", "alert-info")
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)


@app.route('/<int:id>', methods=['GET', 'POST'])
def show_edit_pet_details(id):
    """Show pet details ana edit pet details form; accept submission of edit pet details form"""

    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        photo_url = form.photo_url.data
        if photo_url == '':
            pet.photo_url = None
        else:
            pet.photo_url = photo_url
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"{pet.name} has been updated!", "alert-info")
        return redirect(f'/{id}')
    else:
        return render_template('details.html', form=form, pet=pet)
