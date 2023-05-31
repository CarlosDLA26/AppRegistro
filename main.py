from flask import(
    Flask,
    make_response,
    redirect,
    render_template,
    flash,
    url_for
)

from app import(
    db,
    log
)
from app.models import Persona

from app.forms.FormPerson import FormPerson 
from app import create_app

app = create_app()

@app.route('/')
def index():
    """Índice de la aplicación web

    Returns:
        Response: redireccionamos al usuario al form
            user para que comience con los registros
    """
    response = make_response(redirect('form_user'))
    return response


@app.route("/form_user", methods=['GET', 'POST'])
def form_person():
    """formulario para que la persona registre
    los datos de nombre, email y ciudad

    Returns:
        Redirigimos a la persona al formulario y se muestra
        un mensaje de registro exitoso de una persona
    """
    person_form = FormPerson()

    context = {
        'person_form': person_form
    }

    if person_form.validate_on_submit():
        """Si se registran todos los datos y se presiona
        enviar re registran los datos en la base de datos
        y en el archivo de logs.txt
        """
        nombre = person_form.name.data
        email = person_form.email.data
        ciudad = person_form.ciudad.data

        persona = Persona(
            name=nombre,
            email=email,
            city=ciudad,
        )

        msg = f'Persona Registrada: {nombre}'

        db.session.add(persona)
        db.session.commit()

        flash(message=msg, category='info')
        log.add_log(nombre=nombre, email=email, ciudad=ciudad,)

        return redirect(url_for('form_person'))

    return render_template('person_form.html', **context)


@app.route('/show_people')
def show_people():
    """Mostrar todas las personas que se han
    registrado en la aplicación en una tabla de datos

    Returns:
        Redirigimos a la persona a la tabla con los datos
    """
    consultas = db.session.query(Persona).all()

    context = {
        'consultas': consultas,
    }

    return render_template('show_all_people.html', **context)


@app.errorhandler(404)
def error_404(error):
    return render_template('404.html', error=error)
