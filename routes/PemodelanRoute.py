import json
import os
from flask import Blueprint, request, Response,flash, jsonify,redirect, render_template, url_for,send_from_directory
from controllers import PemodelanController

bp = Blueprint('PemodelanRoutes', __name__)

pemodelanRoutes = PemodelanController()

@bp.route('/pemodelan', methods=['GET'])
def pemodelan():
        return render_template('pemodelan.html')
