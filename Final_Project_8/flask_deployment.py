# Adding the variables headings and Data from the notebook

headings = ["Employee_ID","First_name","Last_name","Hire_Date","Job_ID","Salary","Manager_ID","Department_ID"]

data = [(198, 'Donald', 'OConnell', '21-JUN-07', 'SH_CLERK', 2600, 124, 50),
 (199, 'Douglas', 'Grant', '13-JAN-08', 'SH_CLERK', 2600, 124, 50),
 (200, 'Jennifer', 'Whalen', '17-SEP-03', 'AD_ASST', 4400, 101, 10),
 (201, 'Michael', 'Hartstein', '17-FEB-04', 'MK_MAN', 13000, 100, 20),
 (202, 'Pat', 'Fay', '17-AUG-05', 'MK_REP', 6000, 201, 20),
 (203, 'Susan', 'Mavris', '07-JUN-02', 'HR_REP', 6500, 101, 40),
 (204, 'Hermann', 'Baer', '07-JUN-02', 'PR_REP', 10000, 101, 70)]

# Importing flask
from flask import Flask, render_template

# Creating an instance
app = Flask(__name__)

# Using decorator for the flask instance and creating function with render_templates
@app.route("/about/")
def about():
	return render_template("about.html")

@app.route("/data_table/")
def data_table():
	return render_template("data_table.html",headings = headings, data = data)

@app.route("/")
def index_links():
	return render_template("home.html")

# Running the instance using run method
if __name__ == "__main__":
	app.run()
