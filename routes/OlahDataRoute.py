import json
import os
from flask import Blueprint, request, Response,flash, jsonify,redirect, render_template, url_for,send_from_directory
from controllers import OlahDataController
from utils.creation_inspection import read_csv
from utils.creation_inspection import CreationInspection

bp = Blueprint('OlahDataRoutes', __name__, static_folder='static')

olahDataRoutes = OlahDataController()

@bp.route('/', methods=['GET'])
def index():
        return render_template('index.html')

# @bp.route('/upload', methods=['POST'])
# def upload():
#     try:
#         csv_file = request.files['csvFile']
#         data = read_csv(csv_file)
#         message = "pd.read_csv('" + csv_file.filename  + "')"
#         return {'status': 'success', 'data' : [data.to_html(classes='data')], 'method' : 'pd.read_csv()', 'message' : message }
#     except Exception as e:
#         return {'status': 'error', 'message': str(e)}

@bp.route('/modify/<method>', methods=['POST'])
def modif(method):
    try:
        csv_file = request.files['csvFile']
        df_operations = CreationInspection(csv_file)
        
        # n = request.form.get('n')
        call_method = getattr(df_operations, method, None)

        # # CHECK IF METHOD AVAILABLE AND CALLABLE
        if call_method and callable(call_method):

            if request.form.get('n') is not None:
                n = request.form.get('n')
                data, message = call_method(int(n))
                
            else:
                data, message = call_method()
        else:
            return {'status': 'error', 'message': "Method not found or not callable"}

        return {'status': 'success', 'data' : data, 'message' : message }

    except Exception as e:
        return {'status': 'error', 'message': 'Something wrong happen'}
