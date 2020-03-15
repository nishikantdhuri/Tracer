from flask import Flask
import logging
application=Flask(__name__)
application.debug=False
from app.tracer_controller import trace_bp
application.register_blueprint(trace_bp)

if __name__ == '__main__':
    application.run(port=82)