from pydoc import render_doc
from flask import Flask,render_template, request
app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def index():
    ##
    if request.method == "POST":
        ##
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
       ## print(total_income,total_children,total_family,years_experience,months_balance,income_type,education_type,Family_Status,Housing_Type,Job_Title,car,realty)
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
    return render_template("index.html")
    

if __name__ == "__main__":
    app.run(debug=True)
