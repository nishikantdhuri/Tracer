from flask import Blueprint,render_template,request,url_for,redirect
trace_bp = Blueprint('trace_bp',__name__, template_folder='templates', url_prefix='/trace')

@trace_bp.route('/')
def healthcheck():
    return render_template('tracer.html')