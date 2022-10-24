from pydoc import render_doc
from flask import Flask,render_template, request
app = Flask(__name__)

@app.route('/')##, methods=["POST", "GET"])
def index():
    ##if request.method == "POST":
        ##total_income = request.form['income']
        ##total_children=request.form['children']
        
        
    return render_template("index.html")
    

if __name__ == "__main__":
    app.run(debug=True)
