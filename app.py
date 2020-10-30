from flask import Flask
from flask import render_template, request
import backend

app = Flask(__name__)

@app.route('/')
def home_page():
    animals = backend.get_animals()
    return render_template('home.html', animals=animals)


@app.route('/search')
def animal_attributes():
    search_animal = request.args.get('animal')
    if not search_animal:
        return 'Must specify animal', 400
    
    try:
        attributes = backend.get_attributes(search_animal)
    except Exception as e:
        # log info about error 
        return 'Error searching', 500

    if not attributes:
        return 'Animal not found', 404
    return render_template('animal.html', animal=search_animal, attributes=attributes)


@app.route('/like', methods=['POST'])
def like_animal():
    animal = request.form.get('animal')
    if not animal:
        return 'No animal provided', 400
    else:
        try:
            liked = backend.like(animal)
            if not liked:
                return 'Animal not found', 404
            return render_template('like.html', animal=animal)
        except Exception as e:  # database exceptions
            print(e)
            # log information about error eg. logging.exception(f'Error liking animal {animal}')
            return 'Error saving', 500  # database method should also log information for developer 
        

if __name__ == '__main__':
    Flask.run(app)
    