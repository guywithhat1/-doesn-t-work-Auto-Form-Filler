from flask import Flask, render_template, request, session, redirect, url_for
import form_inputs

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def main():
    if request.method == "POST":
        form_inputs.inputs['email'] = request.form["email"]


    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
