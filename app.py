from flask import Flask, render_template, request
from predict import predict_image
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET","POST"])
def index():
    prediction = ""

    if request.method == "POST":
        file = request.files['file']
        path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(path)
        prediction = predict_image(path)

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
