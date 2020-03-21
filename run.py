from flask import Flask
from flask_socketio import SocketIO
application=Flask(__name__,template_folder='app/templates')
socketio = SocketIO(application)
from flask import render_template,request

@application.route('/')
def healthcheck():
    return render_template('/tracer.html')

@application.route('/soc',methods=['POST'])
def update():
    input_json = request.get_json(force=True)
    socketio.emit('event',{'data': input_json},namespace='/test')
    return render_template('demo.html')

if __name__ == '__main__':
    socketio.run(application)
