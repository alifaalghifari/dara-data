from config import configuration, http


app = http.create_app(configuration.Configuration)

port = int(configuration.Configuration.PORT)

# from flask import Flask, render_template, request, redirect
# import pandas as pd
# from utils.creation_inspection import read_csv
# import os

# app = Flask(__name__)


# UPLOAD_FOLDER = 'uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/pemodelan')
# def pemodelan():
#     return render_template('pemodelan.html')

# @app.route('/visualisasi')
# def visualisasi():
#     return render_template('visualisasi.html')

# @app.route('/upload', methods=['POST'])
# def upload():
#     # return render_template('pemodelan.html')
    
#     if 'file' not in request.files:
#         return redirect('/')
    
#     file = request.files['file']
#     if file.filename == '':
#         return redirect('/')
    
#     # filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#     # file.save(filename)

#     data = read_csv(file)
#     # Perform pandas operations here as needed
#     # return data

#     return render_template('index.html', tables=[data.to_html(classes='data')], titles=file.filename)

# @app.errorhandler(404)
# def page_not_found(error):
#     return 'Page not found', 404


if __name__ == '__main__':
    app.run(debug=True)
