from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

# Import the functions from the previous code snippet
from converter import coordinate_to_hanzi, hanzi_to_coordinate

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert_to_hanzi', methods=['POST'])
def convert_to_hanzi():
    try:
        latitude = float(request.form['latitude'])
        longitude = float(request.form['longitude'])
    except ValueError:
        return render_template('index.html', error='经纬度输入无效，请输入有效的经纬度。')
    
    if latitude < -90 or latitude > 90 or longitude < -180 or longitude > 180:
        return render_template('index.html', error='经纬度输入无效，请输入有效的经纬度。')

    hanzi_address = coordinate_to_hanzi(latitude, longitude)
    return render_template('index.html', hanzi_address=hanzi_address, latitude=latitude, longitude=longitude)

@app.route('/convert_to_coordinates', methods=['POST'])
def convert_to_coordinates():
    try:
        hanzi_string = request.form['hanzi_string']
        hanzi_address = hanzi_string
        latitude, longitude = hanzi_to_coordinate(hanzi_string)
    except ValueError:
        return render_template('index.html', error='七言地址输入无效，请输入有效的七言地址。')
    return render_template('index.html',hanzi_address=hanzi_address, hanzi_string=hanzi_string, latitude=latitude, longitude=longitude)

if __name__ == '__main__':
    app.run(debug=True)