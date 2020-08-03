import os
from flask import * 
import faceExtractor as ex 
app = Flask(__name__)  
 
@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)  
        path = "C:/faces"
        try:
        	os.mkdir(path)
        except:
        	print("My bad")
        ex.func(f.filename,path)
        return render_template("success.html", name = f.filename)


if __name__ == '__main__':
      app.run(host='127.0.0.1', port=50)
