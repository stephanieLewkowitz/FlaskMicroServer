#https://github.com/alankbi/detecto/blob/master/docs/index.rst
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import requests
import requests_toolbelt

UPLOAD_FOLDER = 'serverUploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/ufo', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        # if 'file' not in request.files:
            # flash('No file part')
            # return redirect(request.url)
        print("post")
        print('request.data', request.data)
        print('request.json', request.json)
        print('request.form', request.form)
        print('request.files', request.files)
        print('request.headers', request.headers)
        file = request.files['file']
        name = request.form['name']
        print('name: ', name)
        
        # classifier = request.form['class']
        # nameID = request.form['name']
        # #request.files['image'].save('path/to/file.jpg')
        # # if user does not select file, browser also
        # # submit an empty part without filename
        # if file.filename == '':
            # flash('No selected file')
            # return redirect(request.url)
        # if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        print("filename", filename)
        #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        file.save(os.path.join(UPLOAD_FOLDER, filename))
       # return redirect(url_for('uploaded_file',
        #                        filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
if __name__ == '__main__':
    #app.run(debug=True)
    # start flask app
    app.run(host="0.0.0.0", port=5000)


# @app.route('/upload', methods=['POST'])
# def upload_files():
    # resp = flask.make_response()
    # if authenticate_user(request.form):
        # request.files['image'].save('path/to/file.jpg')
        # resp.status_code = 204
    # else:
        # resp.status_code = 411
    # return resp
    
    
#m = MultipartEncoder(fields=your_fields)
#r = requests.post('https://httpbin.org/post', data=m, headers={'Content-Type': m.content_type})
#print(r.json()['form'])

