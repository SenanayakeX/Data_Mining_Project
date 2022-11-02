from fileinput import filename
from pydoc import render_doc
from flask import Flask,render_template, request
import pickle
import model as md
import function as util

app = Flask(__name__)
ruless = pickle.load(open('rules.pkl', 'rb'))

# @app.route('/', methods=["POST", "GET"])
# def welcome():
#     return render_template("home.html")

@app.route('/association')
def association_start():
    return render_template('association.html')

@app.route('/classification')
def classification_start():
    return render_template('index.html')

app = Flask(__name__)

def prediction(list):
    filename='model/predictor.pickle'
    with open(filename,'rb') as file:
        model= pickle.load(file)
    pred_value=model.predict([list])
    return pred_value

@app.route('/predict', methods=["POST", "GET"])
def index():

    pred = -1
    if request.method == "POST":
        ##take inputs from the frontend to variables
        total_income = request.form['income']
        total_children=request.form['children']     
        total_family = request.form['family']
        age=request.form['age']
        years_experience=request.form['experience']
        months_balance=request.form['months_balance']
        income_type=request.form['income_type']
        education_type=request.form['education_type']
        Family_Status=request.form['Family_Status']
        Housing_Type=request.form['Housing_Type']
        Job_Title=request.form['Job_Title']
        car=request.form.getlist('car')
        realty=request.form.getlist('realty')
        ##print(total_income,total_children,total_family,years_experience,months_balance,income_type,education_type,Family_Status,Housing_Type,Job_Title,car,realty)
        ## append values to array
        feature_list =[]
        feature_list.append(len(car))
        feature_list.append(len(realty))
        feature_list.append(int(total_children))
        feature_list.append(int(total_income))
        feature_list.append(int(total_family))
        feature_list.append(int(age))
        feature_list.append(int(years_experience))
        feature_list.append(int(months_balance))
        ##make a list of options in the drop downs to check which option is selected
        income_type_list=['Commercial associate','Pensioner','State servant','Student','Working']
        education_type_list=['Academic degree','Higher education','Incomplete higher','Lower secondary','Secondary / secondary special']
        Family_Status_list=['Civil marriage','Married','Separated','Single / not married','Widow']
        Housing_Type_list=['Co-op apartment','House / apartment','Municipal apartment','Office apartment','Rented apartment','With parents']
        Job_Title_list=['Accountants','Core staff','Dining staff','Drivers','High skill tech staff','Laborers','Low-skill Laborers','Managers','Medicine staff','Office staff','Sales staff']
        
        def traverse(list,value):
            for item in list:
                if item==value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)
        traverse(income_type_list,income_type)
        traverse(education_type_list,education_type)
        traverse(Family_Status_list,Family_Status)
        traverse(Housing_Type_list,Housing_Type)
        traverse(Job_Title_list,Job_Title)
        ##call prediction method and store result in pred variable(predicted answer)
        pred=prediction(feature_list)
        print("prediction", pred)

        """if pred == 0:
            result = 'Customer Is Not Eligible For Credit Card.'
        elif pred == 1:
            result = 'Customer Is Eligible For Credit Card'"""

    
    return render_template("index.html", pred = pred)

@app.route("/rule", methods=["GET", "POST"])
def pattern_analysis():
    listed = ""
    items_selected = []
    item_list = []
    if request.method == "POST":
        item_select1 = request.form.get('item_select1')
        item_select2 = request.form.get('item_select2')
        item_select3 = request.form.get('item_select3')

        if item_select1 != "0":
            items_selected.append(item_select1+ "    ")
            item_list.append(item_select1)
        if item_select2 != "0":
            items_selected.append(item_select2)
            item_list.append(item_select2)
        if item_select3 != "0":
            items_selected.append(item_select3)
            item_list.append(item_select3)

        item_selected = " , ".join([str(item) for item in items_selected])
        listed = util.recommend_product(item_list)
        #util.networkPlotRule(item_list)

    return render_template('association.html', pattern1=listed,items=" , ".join([str(item) for item in items_selected]))


@app.route("/", methods=["GET", "POST"])
def analysis():

    return render_template('home.html')
    

if __name__ == "__main__":
    app.run(debug=True)