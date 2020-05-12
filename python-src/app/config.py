import os

dir_path = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = dir_path + "/upload/"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024 # 16 MB

UPLOAD_FORM = '''
    <!doctype html>
    <title>Project 3: Deep Learning</title>
    <h1>Upload new Picture</h1>
    <form method=post enctype=multipart/form-data>
        <input type=file name=file>
        <input type=submit value=Upload>
    </form>
'''
