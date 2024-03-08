import json
import os
from flask import Blueprint, request, Response,flash, jsonify,redirect, render_template, url_for,send_from_directory
from controllers import VisualisasiController

bp = Blueprint('VisualisasiRoutes', __name__)

visualisasiRoutes = VisualisasiController()

@bp.route('/visualisasi', methods=['GET'])
def visualisasi():
        return render_template('visualisasi.html')
