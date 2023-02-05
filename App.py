from flask import Flask,render_template,Response, request
import web_utils



app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST']) 
def login():
    if request.method == 'POST':
        print('Login POST')
        return render_template('index.html')

    if request.method == 'GET':
        return render_template('index.html')

    return render_template('login.html')
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        print('register post')
        return render_template('register.html')

    return render_template('register.html')

@app.route('/index')
def index():
    return render_template('index.html')  

@app.route('/video')
def video():
    return render_template('video.html')  

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')  

@app.route('/logs')
def logs():
    return render_template('logs.html')  

@app.route('/error404')
def error404():
    return render_template('error-404.html')  

@app.route('/video-stream')
def video_stream():
    return Response(web_utils.generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)
