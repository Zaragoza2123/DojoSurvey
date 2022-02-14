from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['locations'] = request.form['locations']
    session['languages'] = request.form['languages']
    session['comments'] = request.form['comments']
    return render_template("formresult.html", name =session['name'], locations=session['locations'],languages=session['languages'],comments=session['comments'] )

if __name__=="__main__":
    app.run(debug=True)