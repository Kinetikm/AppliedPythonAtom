#!flask/bin/python
import os
from flask import Flask, jsonify, redirect, url_for, flash, render_template, abort
from flask import request
from werkzeug.utils import secure_filename
from time import time
from timer_log import timer_log


UPLOAD_FOLDER = '/Users/markantipin/Desktop/Atom_project/photos'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'ico'])


app = Flask(__name__, static_folder='photos')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


people = [
    {
        'id': 1,
        'vk_url': 'Speedy Gonzales',
        'vk_photo': 'Speedy-Gonzales-icon.png'
    },
    {
        'id': 2,
        'vk_url': 'Bugs Bunny',
        'vk_photo': 'sykonist-looney-tunes-bugs-bunny-king.ico'
    },
    {
        'id': 3,
        'vk_url': 'Sam',
        'vk_photo': 'Yosemite-Sam-Knight-icon.png'
    }
]


@app.route('/atom_project/api/v1.0/people', methods=['GET'])
def get_people():
    t0 = time()
    if len(people) == 0:
        abort(404)
    t1 = time()
    timer_log(t1-t0, 'get')
    return render_template('get_people.html', people=people)


@app.route('/atom_project/api/v1.0/people/<int:id>', methods=['GET'])
def get_person(id):
    t0 = time()
    person = None
    if len(people) == 0:
        abort(404)

    for i in people:
        if i['id'] == id:
            person = i

    if person is None:
        abort(404)

    photo_path = person['vk_photo']
    vk_url = person['vk_url']
    t1 = time()
    timer_log(t1 - t0, 'get')
    return render_template('get_person.html', vk_url=vk_url, photo_path=photo_path, id=id)


@app.route('/atom_project/api/v1.0/people/delete/<int:id>', methods=['DELETE'])
def delete_person(id):
    t0 = time()
    person = None
    for i in people:
        if i['id'] == id:
            person = i
    if person is None:
        abort(404)

    if not os.path.exists(person['vk_photo']):
        abort(404)

    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], person['vk_photo']))

    people.remove(person)
    t1 = time()
    timer_log(t1 - t0, 'delete')
    return 'person deleted'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/atom_project/api/v1.0', methods=['POST', 'GET'])
def add_person():
    t0 = time()
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        vk_url = request.form['text']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            person = {
                'id': people[-1]['id'] + 1,
                'vk_url': vk_url,
                'vk_photo': filename
            }

            people.append(person)
            t1 = time()
            timer_log(t1 - t0, 'post')
            return redirect(url_for('add_person',
                                    filename=filename)), 201

    return render_template('add_person.html')


@app.route('/atom_project/api/v1.0/people/put/<int:id>', methods=['PUT', 'GET'])
def put_person(id):
    t0 = time()
    if request.method == 'PUT':
        person = None
        for i in people:
            if i['id'] == id:
                person = i

        if person is None:
            abort(404)

        if not os.path.exists(person['vk_photo']):
            abort(404)

        vk_url = request.form['text']
        file = request.files['file']

        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], person['vk_photo']))
        filename = secure_filename(file.filename)

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        person['vk_url'] = vk_url
        person['vk_photo'] = filename
        t1 = time()
        timer_log(t1 - t0, 'put')
        return redirect(url_for('put_person',
                                filename=filename))

    return render_template('put_person.html')


if __name__ == '__main__':
    app.run(debug=True)
