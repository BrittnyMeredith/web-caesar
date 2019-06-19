from flask import Flask, request
from ceasar import rotate_string

app = Flask(__name__)

app.config['DEBUG'] = True

rotation_form="""
<!doctype html>
<html>
    <head>
    <body>
    <style>
    form {{
        background-color: #eee;
        padding: 20px;
        margin: 0 auto;
        width: 540px;
        font: 16px sans-serif;
        border-radius: 10px;
         }}
        textarea {{
            margin: 10px 0;
            width: 540px;
            height: 120px;
        }}
     </style>
    <form method="post">
     <label for="rotate by"> Rotate By:</label>
    <input id="rotate by" type="number" name="rot" value="0" />
    <textarea name="text">{0}</textarea>
    <input type="submit" name="submit_button" Value="Submit"/>
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    text=request.form['text']
    rot=int(request.form['rot'])
    cool_message=rotate_string(text,rot)
    return rotation_form.format(cool_message)
    
@app.route("/")   
def index():
    return rotation_form.format("")

app.run()