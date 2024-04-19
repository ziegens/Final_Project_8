## GROUP PROJECT 8

**DESCRIPTION OF THE PROJECT**

In this project we created a python application that collects data from a csv file, stores it in SQlite database. After that we created a website and a small sample of the data was presented through the website using flask.


**IMPORTING LIBRARIES**

sqlite3- For this project we imported sqlite3 which was used to connect to and query the SQLite database.

csv- we also imported csv which was used to read data from a CSV file and insert it into the database. 

Flask- This package was used to create the web application and handle HTTP requests.

**CODE FUNCTIONS**

First, we create a connection to the "employees.db" SQLite database. This database will be storing the employee data we work with for this project.

Next, we created a cursor object (con.cursor()) which was linked with the connection 'con' to execute SQL commands to fetch data results which was our tool for running commands and getting data out of the database.
We can now define the structure of our database since the connection and cursor have been established. To accomplish this, we run the SQL statement CREATE TABLE. In essence, this command instructs the database to establish a brand-new "employee" table with particular columns and data kinds. With our database structure established, we open the "employees.csv" file, which holds the employee data we wish to keep in our database. 

Finally, we begin adding the CSV file's data to our database table. We run an INSERT INTO SQL query for each row of data in the CSV file. This command creates a new entry in the "employee" database by using the values from the relevant CSV file row.

**DATA CLEANING**

For this project using the sqlite3 module in Python, SQL queries were run on the SQLite database to do data cleansing and column dropping. More specifically, undesired columns were eliminated using the ALTER TABLE SQL statement.


**WEBSITE CREATING**

To begin with, we initialise our Flask application by using app = Flask(__name__). This basically starts the entire Flask web application development process. Now, we use @app.route("/"), @app.route("/about"), and @app.route("/data_table") to specify the various routes of our website. Consider these pathways as the various URLs or paths that users can take while on our website.

Flask is programmed to run the function linked to the route "/" when a user navigates to our website's home page. Using render_template("home.html"), this function retrieves the contents of the "home.html" template.
Similar to this, Flask runs a separate function that returns the contents of the "about.html" template when a user accesses the about page (the route "/about"). Information about our project or website is provided in this template.

When a user accesses the data page (the route "/data_table"), Flask runs a function that sends some data more precisely, the student data—to the "data_table.html" template in addition to returning the contents of that template. This enables us to dynamically display data on the website from our database.

Once these routes and templates are set up, Flask handles presenting the relevant content to the user in response to their request. It functions similarly to a tour guide, guiding users to various parts of our website so they may enjoy a smooth and seamless experience.

**INSTALLATION**

clone the project repository from GitHub. 

Use pip to obtain and configure required Python packages listed in requirements.txt.


**HOW TO USE**

Ensure Python and SQLite are installed on your computer.

 Get the project files by cloning the Github repository to your local machine.

 Install the necessary Python packages listed in requirements.txt using pip.

 Execute the Python script to import employee data from a CSV file into a SQLite database.

 Start the Flask application to launch the website locally by executing app.run() within your app.py file
 
 Access the website through your web browser to explore the different pages and interact with the data presented.

Enjoy exploring the project and discovering its capabilities!



