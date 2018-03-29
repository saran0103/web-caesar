from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form_header = """
<!DOCTYPE html>
<html>
    <head>
        
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
    </head>
    <body>
        <div class="container">
                <form class="encrypt" action ="/" method="POST">
                    <label for "rot">Rotate by : </label>
                    <input type="text" id="rot" name="rot">
                    <textarea name="text" placeholder="Write something..." style="height:200px">{0}</textarea>
                    <input type="submit" value="Submit Query">
                </form>
        </div>
        """
form_footer = """
    </body>
</html>
"""

@app.route("/")
def index():
    return form_header.format("") + form_footer

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    rot_text = str(request.form['text'])
    encrypt_text = rotate_string(rot_text, rot)
    return form_header.format(encrypt_text) + form_footer

app.run()