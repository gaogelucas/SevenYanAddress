from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# Assuming these functions are correctly implemented in the 'converter' module
from converter import coordinate_to_hanzi, hanzi_to_coordinate

# Page Rendering Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert_to_hanzi', methods=['POST'])
def convert_to_hanzi():
    try:
        latitude = float(request.form['latitude'])
        longitude = float(request.form['longitude'])
    except ValueError:
        return render_template('index.html', error='Invalid input. Please enter valid latitude and longitude.')
    
    if latitude < -90 or latitude > 90 or longitude < -180 or longitude > 180:
        return render_template('index.html', error='Latitude or longitude values are out of range.')

    hanzi_address = coordinate_to_hanzi(latitude, longitude)
    return render_template('index.html', hanzi_address=hanzi_address, latitude=latitude, longitude=longitude)

@app.route('/convert_to_coordinates', methods=['POST'])
def convert_to_coordinates():
    try:
        hanzi_string = request.form['hanzi_string']
        latitude, longitude = hanzi_to_coordinate(hanzi_string)
    except ValueError:
        return render_template('index.html', error='Invalid Hanzi address. Please enter a valid Hanzi address.')
    return render_template('index.html', hanzi_address=hanzi_string, latitude=latitude, longitude=longitude)

# RESTful API Endpoints
@app.route('/api/hanzi/', methods=['POST'])
def api_hanzi_from_coordinates():
    data = request.get_json()
    if not data or 'latitude' not in data or 'longitude' not in data:
        return jsonify({'error': 'Missing latitude or longitude in request'}), 400

    try:
        latitude = float(data['latitude'])
        longitude = float(data['longitude'])
    except ValueError:
        return jsonify({'error': 'Invalid latitude or longitude values'}), 400

    if latitude < -90 or latitude > 90 or longitude < -180 or longitude > 180:
        return jsonify({'error': 'Latitude or longitude values are out of range'}), 400

    hanzi_address = coordinate_to_hanzi(latitude, longitude)
    return jsonify({'hanzi_address': hanzi_address})

@app.route('/api/coordinates/', methods=['POST'])
def api_coordinates_from_hanzi():
    data = request.get_json()
    if not data or 'hanzi_string' not in data:
        return jsonify({'error': 'Missing hanzi_string in request'}), 400

    try:
        hanzi_string = data['hanzi_string']
        latitude, longitude = hanzi_to_coordinate(hanzi_string)
    except ValueError:
        return jsonify({'error': 'Invalid Hanzi address provided'}), 400

    return jsonify({'latitude': latitude, 'longitude': longitude})

if __name__ == '__main__':
    app.run(debug=True)