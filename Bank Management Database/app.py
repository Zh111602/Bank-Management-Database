import MySQLdb
import flask
from flask import Flask, render_template, request, redirect
import mysql.connector
from flask_mysqldb import MySQL
from datetime import datetime
from flask import url_for



app = Flask(__name__)

# Configure db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '2811652'
app.config['MYSQL_DB'] = 'bank_management'

mysql = MySQL(app)



loggedInID = "arwhite6"
loggedInType = 0
# 1: Manager 2: Admin 3: Customer

# Screen 24: Customer Navigation
@app.route('/customer_menu', methods=['GET', 'POST'])
def customer_menu():
    global loggedInID
    global loggedInType
    print(loggedInID)
    print(str(loggedInType))
    if request.method == 'POST':
        # fetch form data
        if request.form['submit_button'] == '1':
            return redirect(url_for('manage_account_customer'))
        elif request.form['submit_button'] == '2':
            return redirect(url_for('make_deposit'))
        elif request.form['submit_button'] == '5':
            return redirect(url_for('make_withdrawal'))
        elif request.form['submit_button'] == '3':
            return redirect(url_for('start_stop_overdraft_customer'))
        elif request.form['submit_button'] == '4':
            return redirect(url_for('make_accountTransfer'))
        elif request.form['submit_button'] == 'Back':
            loggedInID = None
            loggedInType = None
            return redirect(url_for('InitialPage'))

    return render_template('customer_menu.html')


# Screen 23: Manager Menu
@app.route('/manager_menu', methods=['GET', 'POST'])
def manager_menu():
    global loggedInID
    global loggedInType
    print(loggedInID)
    print(str(loggedInType))
    if request.method == 'POST':
        # fetch form data
        if request.form['submit_button'] == '1':
            return redirect(url_for('pay_employee'))
        elif request.form['submit_button'] == '2':
            return redirect(url_for('hire_worker'))
        elif request.form['submit_button'] == 'Back':
            loggedInID = None
            loggedInType = None
            return redirect(url_for('InitialPage'))

    return render_template('manager_menu.html')


# Screen 20: Admin Menu
@app.route('/admin_menu', methods=['GET', 'POST'])
def admin_menu():
    global loggedInID
    global loggedInType
    print(loggedInID)
    print(str(loggedInType))
    if request.method == 'POST':
        # fetch form data
        if request.form['submit_button'] == '1':
            return redirect(url_for('view_stats'))
        elif request.form['submit_button'] == '2':
            return redirect(url_for('create_corporation'))
        elif request.form['submit_button'] == '3':
            return redirect(url_for('create_fee'))
        elif request.form['submit_button'] == '4':
            return redirect(url_for('manage_users'))
        elif request.form['submit_button'] == '5':
            return redirect(url_for('start_stop_overdraft_customer'))
        elif request.form['submit_button'] == '6':
            return redirect(url_for('hire_worker'))
        elif request.form['submit_button'] == '7':
            return redirect(url_for('pay_employee'))
        elif request.form['submit_button'] == '8':
            return redirect(url_for('replace_manager'))
        elif request.form['submit_button'] == '9':
            return redirect(url_for('manage_accountAdmin'))
        elif request.form['submit_button'] == '10':
            return redirect(url_for('create_bank'))
        elif request.form['submit_button'] == 'Back':
            loggedInID = None
            loggedInType = None
            return redirect(url_for('InitialPage'))

    return render_template('admin_menu.html')


# Screen 21: Manage Users
@app.route('/manage_users', methods=['GET', 'POST'])
def manage_users():
    global loggedInID
    global loggedInType
    if request.method == 'POST':
        # fetch form data
        if request.form['submit_button'] == '1':
            return redirect(url_for('create_employeeRole'))
        elif request.form['submit_button'] == '2':
            return redirect(url_for('create_customerRole'))
        elif request.form['submit_button'] == '3':
            return redirect(url_for('stop_employeeRole'))
        elif request.form['submit_button'] == '4':
            return redirect(url_for('stop_customerRole'))
        elif request.form['submit_button'] == 'Back':
            return redirect(url_for('admin_menu'))

    return render_template('manage_users.html')

# Screen 22: View Stats
@app.route('/view_stats', methods=['GET', 'POST'])
def view_stats():
    global loggedInID
    global loggedInType
    if request.method == 'POST':
        # fetch form data
        if request.form['submit_button'] == '1':
            return redirect(url_for('display_account_stats'))
        elif request.form['submit_button'] == '2':
            return redirect(url_for('display_corporation_stats'))
        elif request.form['submit_button'] == '3':
            return redirect(url_for('display_bank_stats'))
        elif request.form['submit_button'] == '4':
            return redirect(url_for('display_customer_stats'))
        elif request.form['submit_button'] == '5':
            return redirect(url_for('display_employee_stats'))
        elif request.form['submit_button'] == 'Back':
            return redirect(url_for('admin_menu'))

    return render_template('view_stats.html')


# Screen 18 Query 24
@app.route('/display_employee_stats', methods=['GET', 'POST'])
def display_employee_stats():
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        res_ = cur.execute("select * from display_employee_stats;")
        if res_ > 0:
            res = cur.fetchall()
        else:
            res = []
        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'bankAsc':
                query = "select * from display_employee_stats order by person_identifier asc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'bankDesc':
                query = "select * from display_employee_stats order by person_identifier desc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'corAsc':
                query = "select * from display_employee_stats order by tax_identifier asc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'corDesc':
                query = "select * from display_employee_stats order by tax_identifier desc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'bkNameAsc':
                query = "select * from display_employee_stats order by employee_name asc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'bkNameDesc':
                query = "select * from display_employee_stats order by employee_name desc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'streetAsc':
                query = "select * from display_employee_stats order by date_of_birth asc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'streetDesc':
                query = "select * from display_employee_stats order by date_of_birth desc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'cityAsc':
                query = "select * from display_employee_stats order by joined_system asc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'cityDesc':
                query = "select * from display_employee_stats order by joined_system desc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'stateAsc':
                query = "select * from display_employee_stats order by street asc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'stateDesc':
                query = "select * from display_employee_stats order by street desc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'zipAsc':
                query = "select * from display_employee_stats order by city asc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'zipDesc':
                query = "select * from display_employee_stats order by city desc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'numAccAsc':
                query = "select * from display_employee_stats order by state asc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'numAccDesc':
                query = "select * from display_employee_stats order by state desc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'bkAssetsAsc':
                query = "select * from display_employee_stats order by zip asc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'bkAssetsDesc':
                query = "select * from display_employee_stats order by zip desc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'totalAssetsAsc':
                query = "select * from display_employee_stats order by number_of_banks asc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'totalAssetsDesc':
                query = "select * from display_employee_stats order by number_of_banks desc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'cusAssetsAsc':
                query = "select * from display_employee_stats order by bank_assets asc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'cusAssetsDesc':
                query = "select * from display_employee_stats order by bank_assets desc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'Back':
                # back to admin page
                return redirect(url_for('view_stats'))

            cur.close()
    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('display_employee_stats.html', res=res)


@app.route('/display_employee_stats2/<query>', methods=['GET', 'POST'])
def display_employee_stats2(query):
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        res_ = cur.execute(query)
        if res_ > 0:
            res = cur.fetchall()
        else:
            res = []
        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'bankAsc':
                query = "select * from display_employee_stats order by person_identifier asc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'bankDesc':
                query = "select * from display_employee_stats order by person_identifier desc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'corAsc':
                query = "select * from display_employee_stats order by tax_identifier asc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'corDesc':
                query = "select * from display_employee_stats order by tax_identifier desc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'bkNameAsc':
                query = "select * from display_employee_stats order by employee_name asc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'bkNameDesc':
                query = "select * from display_employee_stats order by employee_name desc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'streetAsc':
                query = "select * from display_employee_stats order by date_of_birth asc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'streetDesc':
                query = "select * from display_employee_stats order by date_of_birth desc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'cityAsc':
                query = "select * from display_employee_stats order by joined_system asc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'cityDesc':
                query = "select * from display_employee_stats order by joined_system desc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'stateAsc':
                query = "select * from display_employee_stats order by street asc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'stateDesc':
                query = "select * from display_employee_stats order by street desc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'zipAsc':
                query = "select * from display_employee_stats order by city asc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'zipDesc':
                query = "select * from display_employee_stats order by city desc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'numAccAsc':
                query = "select * from display_employee_stats order by state asc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'numAccDesc':
                query = "select * from display_employee_stats order by state desc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'bkAssetsAsc':
                query = "select * from display_employee_stats order by zip asc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'bkAssetsDesc':
                query = "select * from display_employee_stats order by zip desc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'totalAssetsAsc':
                query = "select * from display_employee_stats order by number_of_banks asc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'totalAssetsDesc':
                query = "select * from display_employee_stats order by number_of_banks desc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'cusAssetsAsc':
                query = "select * from display_employee_stats order by bank_assets asc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'cusAssetsDesc':
                query = "select * from display_employee_stats order by bank_assets desc;"
                return redirect(url_for('display_employee_stats2', query=query))
            elif request.form['submit_button'] == 'Back':
                # bakc to admin page
                return redirect(url_for('view_stats'))

            cur.close()
    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('display_employee_stats.html', res=res, query=query)


# Screen 17 Query 23
@app.route('/display_customer_stats', methods=['GET', 'POST'])
def display_customer_stats():
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        res_ = cur.execute("select * from display_customer_stats;")
        if res_ > 0:
            res = cur.fetchall()
        else:
            res = []
        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'bankAsc':
                query = "select * from display_customer_stats order by person_identifier asc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'bankDesc':
                query = "select * from display_customer_stats order by person_identifier desc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'corAsc':
                query = "select * from display_customer_stats order by tax_identifier asc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'corDesc':
                query = "select * from display_customer_stats order by tax_identifier desc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'bkNameAsc':
                query = "select * from display_customer_stats order by customer_name asc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'bkNameDesc':
                query = "select * from display_customer_stats order by customer_name desc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'streetAsc':
                query = "select * from display_customer_stats order by date_of_birth asc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'streetDesc':
                query = "select * from display_customer_stats order by date_of_birth desc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'cityAsc':
                query = "select * from display_customer_stats order by joined_system asc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'cityDesc':
                query = "select * from display_customer_stats order by joined_system desc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'stateAsc':
                query = "select * from display_customer_stats order by street asc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'stateDesc':
                query = "select * from display_customer_stats order by street desc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'zipAsc':
                query = "select * from display_customer_stats order by city asc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'zipDesc':
                query = "select * from display_customer_stats order by city desc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'numAccAsc':
                query = "select * from display_customer_stats order by state asc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'numAccDesc':
                query = "select * from display_customer_stats order by state desc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'bkAssetsAsc':
                query = "select * from display_customer_stats order by zip asc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'bkAssetsDesc':
                query = "select * from display_customer_stats order by zip desc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'totalAssetsAsc':
                query = "select * from display_customer_stats order by number_of_accounts asc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'totalAssetsDesc':
                query = "select * from display_customer_stats order by number_of_accounts desc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'cusAssetsAsc':
                query = "select * from display_customer_stats order by customer_assets asc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'cusAssetsDesc':
                query = "select * from display_customer_stats order by customer_assets desc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'Back':
                # bakc to admin page
                return redirect(url_for('view_stats'))

            cur.close()
    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('display_customer_stats.html', res=res)


@app.route('/display_customer_stats2/<query>', methods=['GET', 'POST'])
def display_customer_stats2(query):
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        res_ = cur.execute(query)
        if res_ > 0:
            res = cur.fetchall()
        else:
            res = []
        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'bankAsc':
                query = "select * from display_customer_stats order by person_identifier asc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'bankDesc':
                query = "select * from display_customer_stats order by person_identifier desc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'corAsc':
                query = "select * from display_customer_stats order by tax_identifier asc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'corDesc':
                query = "select * from display_customer_stats order by tax_identifier desc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'bkNameAsc':
                query = "select * from display_customer_stats order by customer_name asc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'bkNameDesc':
                query = "select * from display_customer_stats order by customer_name desc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'streetAsc':
                query = "select * from display_customer_stats order by date_of_birth asc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'streetDesc':
                query = "select * from display_customer_stats order by date_of_birth desc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'cityAsc':
                query = "select * from display_customer_stats order by joined_system asc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'cityDesc':
                query = "select * from display_customer_stats order by joined_system desc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'stateAsc':
                query = "select * from display_customer_stats order by street asc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'stateDesc':
                query = "select * from display_customer_stats order by street desc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'zipAsc':
                query = "select * from display_customer_stats order by city asc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'zipDesc':
                query = "select * from display_customer_stats order by city desc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'numAccAsc':
                query = "select * from display_customer_stats order by state asc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'numAccDesc':
                query = "select * from display_customer_stats order by state desc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'bkAssetsAsc':
                query = "select * from display_customer_stats order by zip asc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'bkAssetsDesc':
                query = "select * from display_customer_stats order by zip desc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'totalAssetsAsc':
                query = "select * from display_customer_stats order by number_of_accounts asc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'totalAssetsDesc':
                query = "select * from display_customer_stats order by number_of_accounts desc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'cusAssetsAsc':
                query = "select * from display_customer_stats order by customer_assets asc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'cusAssetsDesc':
                query = "select * from display_customer_stats order by customer_assets desc;"
                return redirect(url_for('display_customer_stats2', query=query))
            elif request.form['submit_button'] == 'Back':
                # bakc to admin page
                return redirect(url_for('view_stats'))

            cur.close()
    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('display_customer_stats.html', res=res, query=query)


#Screen 16 Query 22
@app.route('/display_corporation_stats', methods=['GET', 'POST'])
def display_corporation_stats():
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        res_ = cur.execute("select * from display_corporation_stats;")
        if res_ > 0:
            res = cur.fetchall()
        else:
            res = []
        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'idAsc':
                query = "select * from display_corporation_stats order by corporation_identifier asc;"
                return redirect(url_for('display_corporation_stats2', query=query))
            elif request.form['submit_button'] == 'idDesc':
                query = "select * from display_corporation_stats order by corporation_identifier desc;"
                return redirect(url_for('display_corporation_stats2', query=query))
            elif request.form['submit_button'] == 'shortAsc':
                query = "select * from display_corporation_stats order by short_name asc;"
                return redirect(url_for('display_corporation_stats2', query=query))
            elif request.form['submit_button'] == 'shortDesc':
                query = "select * from display_corporation_stats order by short_name desc;"
                return redirect(url_for('display_corporation_stats2', query=query))
            elif request.form['submit_button'] == 'formalAsc':
                query = "select * from display_corporation_stats order by formal_name asc;"
                return redirect(url_for('display_corporation_stats2', query=query))
            elif request.form['submit_button'] == 'formalDesc':
                query = "select * from display_corporation_stats order by formal_name desc;"
                return redirect(url_for('display_corporation_stats2', query=query))
            elif request.form['submit_button'] == 'numAsc':
                query = "select * from display_corporation_stats order by number_of_banks asc;"
                return redirect(url_for('display_corporation_stats2', query=query))
            elif request.form['submit_button'] == 'numDsc':
                query = "select * from display_corporation_stats order by number_of_banks desc;"
                return redirect(url_for('display_corporation_stats2', query=query))
            elif request.form['submit_button'] == 'corpAssetsAsc':
                query = "select * from display_corporation_stats order by corporation_assets asc;"
                return redirect(url_for('display_corporation_stats2', query=query))
            elif request.form['submit_button'] == 'corpAssetsDesc':
                query = "select * from display_corporation_stats order by corporation_assets desc;"
                return redirect(url_for('display_corporation_stats2', query=query))
            elif request.form['submit_button'] == 'totalAsc':
                query = "select * from display_corporation_stats order by total_assets asc;"
                return redirect(url_for('display_corporation_stats2', query=query))
            elif request.form['submit_button'] == 'totalDesc':
                query = "select * from display_corporation_stats order by total_assets desc;"
                return redirect(url_for('display_corporation_stats2', query=query))
            elif request.form['submit_button'] == 'Back':
                #bakc to admin page
                return redirect(url_for('view_stats'))

            cur.close()
    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('display_corporation_stats.html', res=res)


@app.route('/display_corporation_stats2/<query>', methods=['GET', 'POST'])
def display_corporation_stats2(query):
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        res_ = cur.execute(query)
        if res_ > 0:
            res = cur.fetchall()
        else:
            res = []
        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'idAsc':
                query = "select * from display_corporation_stats order by corporation_identifier asc;"
                return redirect(url_for('display_corporation_stats2', query=query))
            elif request.form['submit_button'] == 'idDesc':
                query = "select * from display_corporation_stats order by corporation_identifier desc;"
                return redirect(url_for('display_corporation_stats2', query=query))
            elif request.form['submit_button'] == 'shortAsc':
                query = "select * from display_corporation_stats order by short_name asc;"
                return redirect(url_for('display_corporation_stats2', query=query))
            elif request.form['submit_button'] == 'shortDesc':
                query = "select * from display_corporation_stats order by short_name desc;"
                return redirect(url_for('display_corporation_stats2', query=query))
            elif request.form['submit_button'] == 'formalAsc':
                query = "select * from display_corporation_stats order by formal_name asc;"
                return redirect(url_for('display_corporation_stats2', query=query))
            elif request.form['submit_button'] == 'formalDesc':
                query = "select * from display_corporation_stats order by formal_name desc;"
                return redirect(url_for('display_corporation_stats2', query=query))
            elif request.form['submit_button'] == 'numAsc':
                query = "select * from display_corporation_stats order by number_of_banks asc;"
                return redirect(url_for('display_corporation_stats2', query=query))
            elif request.form['submit_button'] == 'numDsc':
                query = "select * from display_corporation_stats order by number_of_banks desc;"
                return redirect(url_for('display_corporation_stats2', query=query))
            elif request.form['submit_button'] == 'corpAssetsAsc':
                query = "select * from display_corporation_stats order by corporation_assets asc;"
                return redirect(url_for('display_corporation_stats2', query=query))
            elif request.form['submit_button'] == 'corpAssetsDesc':
                query = "select * from display_corporation_stats order by corporation_assets desc;"
                return redirect(url_for('display_corporation_stats2', query=query))
            elif request.form['submit_button'] == 'totalAsc':
                query = "select * from display_corporation_stats order by total_assets asc;"
                return redirect(url_for('display_corporation_stats2', query=query))
            elif request.form['submit_button'] == 'totalDesc':
                query = "select * from display_corporation_stats order by total_assets desc;"
                return redirect(url_for('display_corporation_stats2', query=query))
            elif request.form['submit_button'] == 'Back':
                return redirect(url_for('view_stats'))

            cur.close()
    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('display_corporation_stats.html', res=res, query=query)


#Screen 15 Query 21
@app.route('/display_bank_stats', methods=['GET', 'POST'])
def display_bank_stats():
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        res_ = cur.execute("select * from display_bank_stats;")
        if res_ > 0:
            res = cur.fetchall()
        else:
            res = []
        if request.method == 'POST':
            # fetch form data

            if request.form['submit_button'] == 'bankAsc':
                query = "select * from display_bank_stats order by bank_identifier asc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'bankDesc':
                query = "select * from display_bank_stats order by bank_identifier desc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'corAsc':
                query = "select * from display_bank_stats order by name_of_corporation asc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'corDesc':
                query = "select * from display_bank_stats order by name_of_corporation desc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'bkNameAsc':
                query = "select * from display_bank_stats order by name_of_bank asc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'bkNameDesc':
                query = "select * from display_bank_stats order by name_of_bank desc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'streetAsc':
                query = "select * from display_bank_stats order by street asc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'streetDesc':
                query = "select * from display_bank_stats order by street desc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'cityAsc':
                query = "select * from display_bank_stats order by city asc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'cityDesc':
                query = "select * from display_bank_stats order by city desc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'stateAsc':
                query = "select * from display_bank_stats order by state asc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'stateDesc':
                query = "select * from display_bank_stats order by state desc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'zipAsc':
                query = "select * from display_bank_stats order by zip asc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'zipDesc':
                query = "select * from display_bank_stats order by zip desc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'numAccAsc':
                query = "select * from display_bank_stats order by number_of_accounts asc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'numAccDesc':
                query = "select * from display_bank_stats order by number_of_accounts desc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'bkAssetsAsc':
                query = "select * from display_bank_stats order by bank_assets asc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'bkAssetsDesc':
                query = "select * from display_bank_stats order by bank_assets desc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'totalAssetsAsc':
                query = "select * from display_bank_stats order by total_assets asc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'totalAssetsDesc':
                query = "select * from display_bank_stats order by total_assets desc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'Back':
                # bakc to admin page
                return redirect(url_for('view_stats'))

            cur.close()
    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('display_bank_stats.html', res=res)


@app.route('/display_bank_stats2/<query>', methods=['GET', 'POST'])
def display_bank_stats2(query):
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        res_ = cur.execute(query)
        if res_ > 0:
            res = cur.fetchall()
        else:
            res = []
        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'bankAsc':
                query = "select * from display_bank_stats order by bank_identifier asc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'bankDesc':
                query = "select * from display_bank_stats order by bank_identifier desc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'corAsc':
                query = "select * from display_bank_stats order by name_of_corporation asc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'corDesc':
                query = "select * from display_bank_stats order by name_of_corporation desc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'bkNameAsc':
                query = "select * from display_bank_stats order by name_of_bank asc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'bkNameDesc':
                query = "select * from display_bank_stats order by name_of_bank desc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'streetAsc':
                query = "select * from display_bank_stats order by street asc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'streetDesc':
                query = "select * from display_bank_stats order by street desc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'cityAsc':
                query = "select * from display_bank_stats order by city asc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'cityDesc':
                query = "select * from display_bank_stats order by city desc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'stateAsc':
                query = "select * from display_bank_stats order by state asc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'stateDesc':
                query = "select * from display_bank_stats order by state desc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'zipAsc':
                query = "select * from display_bank_stats order by zip asc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'zipDesc':
                query = "select * from display_bank_stats order by zip desc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'numAccAsc':
                query = "select * from display_bank_stats order by number_of_accounts asc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'numAccDesc':
                query = "select * from display_bank_stats order by number_of_accounts desc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'bkAssetsAsc':
                query = "select * from display_bank_stats order by bank_assets asc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'bkAssetsDesc':
                query = "select * from display_bank_stats order by bank_assets desc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'totalAssetsAsc':
                query = "select * from display_bank_stats order by total_assets asc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'totalAssetsDesc':
                query = "select * from display_bank_stats order by total_assets desc;"
                return redirect(url_for('display_bank_stats2', query=query))
            elif request.form['submit_button'] == 'Back':
                # bakc to admin page
                return redirect(url_for('view_stats'))

            cur.close()
    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('display_bank_stats.html', res=res, query=query)


# Screen 14 Query 20
@app.route('/display_account_stats', methods=['GET', 'POST'])
def display_account_stats():
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        res_ = cur.execute("select * from display_account_stats;")
        if res_ > 0:
            res = cur.fetchall()
        else:
            res = []
        if request.method == 'POST':
            # fetch form data

            if request.form['submit_button'] == 'bankAsc':
                query = "select * from display_account_stats order by name_of_bank asc;"
                return redirect(url_for('display_account_stats2', query=query))
            elif request.form['submit_button'] == 'bankDesc':
                query = "select * from display_account_stats order by name_of_bank desc;"
                return redirect(url_for('display_account_stats2', query=query))
            elif request.form['submit_button'] == 'idAsc':
                query = "select * from display_account_stats order by account_identifier asc;"
                return redirect(url_for('display_account_stats2', query=query))
            elif request.form['submit_button'] == 'idDesc':
                query = "select * from display_account_stats order by account_identifier desc;"
                return redirect(url_for('display_account_stats2', query=query))
            elif request.form['submit_button'] == 'balAsc':
                query = "select * from display_account_stats order by account_assets asc;"
                return redirect(url_for('display_account_stats2', query=query))
            elif request.form['submit_button'] == 'balDesc':
                query = "select * from display_account_stats order by account_assets desc;"
                return redirect(url_for('display_account_stats2', query=query))
            elif request.form['submit_button'] == 'ownerAsc':
                query = "select * from display_account_stats order by number_of_owners asc;"
                return redirect(url_for('display_account_stats2', query=query))
            elif request.form['submit_button'] == 'ownerDesc':
                query = "select * from display_account_stats order by number_of_owners desc;"
                return redirect(url_for('display_account_stats2', query=query))
            elif request.form['submit_button'] == 'Back':
                #bakc to admin page
                return redirect(url_for('view_stats'))

            cur.close()
    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('display_account_stats.html', res=res)


@app.route('/display_account_stats2/<query>', methods=['GET', 'POST'])
def display_account_stats2(query):
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        res_ = cur.execute(query)
        if res_ > 0:
            res = cur.fetchall()
        else:
            res = []
        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'bankAsc':
                query = "select * from display_account_stats order by name_of_bank asc;"
                return redirect(url_for('display_account_stats2', query=query))
            elif request.form['submit_button'] == 'bankDesc':
                query = "select * from display_account_stats order by name_of_bank desc;"
                return redirect(url_for('display_account_stats2', query=query))
            elif request.form['submit_button'] == 'idAsc':
                query = "select * from display_account_stats order by account_identifier asc;"
                return redirect(url_for('display_account_stats2', query=query))
            elif request.form['submit_button'] == 'idDesc':
                query = "select * from display_account_stats order by account_identifier desc;"
                return redirect(url_for('display_account_stats2', query=query))
            elif request.form['submit_button'] == 'balAsc':
                query = "select * from display_account_stats order by account_assets asc;"
                return redirect(url_for('display_account_stats2', query=query))
            elif request.form['submit_button'] == 'balDesc':
                query = "select * from display_account_stats order by account_assets desc;"
                return redirect(url_for('display_account_stats2', query=query))
            elif request.form['submit_button'] == 'ownerAsc':
                query = "select * from display_account_stats order by number_of_owners asc;"
                return redirect(url_for('display_account_stats2', query=query))
            elif request.form['submit_button'] == 'ownerDesc':
                query = "select * from display_account_stats order by number_of_owners desc;"
                return redirect(url_for('display_account_stats2', query=query))
            elif request.form['submit_button'] == 'Back':
                # bakc to admin page
                return redirect(url_for('view_stats'))

            cur.close()
    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('display_account_stats.html', res=res, query=query)


# Screen 13 Query 17
@app.route('/pay_employee', methods=['GET', 'POST'])
def pay_employee():
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'pay':
                cur.execute('call pay_employees;')
                mysql.connection.commit()
                return "Success"
            elif request.form['submit_button'] == 'Back':
                if loggedInType == 1:
                    return redirect(url_for('manager_menu'))
                elif loggedInType == 2:
                    return redirect(url_for('admin_menu'))
            cur.close()
    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('pay_employee.html')


# Screen 12 Query 16
@app.route('/make_accountTransfer', methods=['GET', 'POST'])
def make_accountTransfer():
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        # getting perID
        bkRes = cur.execute(
            "select bankID from bank;")
        if bkRes > 0:
            bk = cur.fetchall()
        else:
            bk = []
        if request.method == 'POST':
            # fetch form data
            cur.close()
            if request.form['submit_button'] == 'Next':
                userDetails = request.form
                bank = userDetails['bank']
                bank2 = userDetails['bank2']
                return redirect(url_for('make_accountTransfer2', bankID=bank, bankID2=bank2))
            if request.form['submit_button'] == 'Cancel':
                return redirect(url_for('customer_menu'))

    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('make_accountTransfer.html', bk=bk)


@app.route('/make_accountTransfer2/<bankID>/<bankID2>', methods=['GET', 'POST'])
def make_accountTransfer2(bankID, bankID2):
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        # getting perID
        bkRes = cur.execute(
            "select accountID from access where bankID = '" + bankID + "' and perID = '" + loggedInID + "';")
        if bkRes > 0:
            bk = cur.fetchall()
        else:
            bk = []
            return "NO account from the bank"

        bkRes2 = cur.execute(
            "select accountID from access where bankID = '" + bankID2 + "' and perID = '" + loggedInID + "';")
        if bkRes2 > 0:
            bk2 = cur.fetchall()
        else:
            bk2 = []
            return "NO account from the bank"
        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'Confirm':
                userDetails = request.form
                acc = userDetails['acc']
                amount = userDetails['amount']
                acc2 = userDetails['acc2']
                date = datetime.today().strftime('%Y-%m-%d')
                dateStr = "'" + date + "'"
                cur.execute("call account_transfer('" + loggedInID + "', "
                            + amount + ", '" + bankID + "', '" + acc + "', '" + bankID2 + "', '" + acc2 + "', "
                            + dateStr + ");")
                mysql.connection.commit()
                cur.close()
                return "Success"
            if request.form['submit_button'] == 'B':
                return redirect(url_for('make_accountTransfer'))

    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('make_accountTransfer2.html', bk=bk, bk2=bk2, bank=bankID, bank2=bankID2)


# Screen 11 Query 15
@app.route('/make_withdrawal', methods=['GET', 'POST'])
def make_withdrawal():
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        # getting perID
        bkRes = cur.execute(
            "select bankID from bank;")
        if bkRes > 0:
            bk = cur.fetchall()
        else:
            bk = []
        if request.method == 'POST':
            # fetch form data
            cur.close()
            if request.form['submit_button'] == 'Next':
                userDetails = request.form
                bank = userDetails['bank']
                return redirect(url_for('make_withdrawal2', bankID=bank))
            if request.form['submit_button'] == 'Cancel':
                return redirect(url_for('customer_menu'))

    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('make_withdrawal.html', bk=bk)


@app.route('/make_withdrawal2/<bankID>', methods=['GET', 'POST'])
def make_withdrawal2(bankID):
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        # getting perID
        bkRes = cur.execute(
            "select accountID from access where bankID = '" + bankID + "' and perID = '" + loggedInID + "';")
        if bkRes > 0:
            bk = cur.fetchall()
        else:
            bk = []
        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'Confirm':
                userDetails = request.form
                if not bk:
                    return "No values selected"
                acc = userDetails['acc']
                amount = userDetails['amount']
                date = datetime.today().strftime('%Y-%m-%d')
                dateStr = "'" + date + "'"
                print("call account_withdrawal('" + loggedInID + "', "
                            + amount + ", '" + bankID + "', '" + acc + "'," + dateStr + ");")
                cur.execute("call account_withdrawal('" + loggedInID + "', "
                            + amount + ", '" + bankID + "', '" + acc + "'," + dateStr + ");")
                mysql.connection.commit()
                cur.close()
                return "Success"
            if request.form['submit_button'] == 'B':
                return redirect(url_for('make_withdrawal'))

    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('make_withdrawal2.html', bk=bk, bank=bankID)


# Screen 11 Query 14
@app.route('/make_deposit', methods=['GET', 'POST'])
def make_deposit():
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        # getting perID
        bkRes = cur.execute(
            "select bankID from bank;")
        if bkRes > 0:
            bk = cur.fetchall()
        else:
            bk = []
        if request.method == 'POST':
            # fetch form data
            cur.close()
            if request.form['submit_button'] == 'Next':
                userDetails = request.form
                bank = userDetails['bank']
                return redirect(url_for('make_deposit2', bankID=bank))
            if request.form['submit_button'] == 'Cancel':
                return redirect(url_for('customer_menu'))

    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('make_deposit.html', bk=bk)


@app.route('/make_deposit2/<bankID>', methods=['GET', 'POST'])
def make_deposit2(bankID):
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        # getting perID
        bkRes = cur.execute(
            "select accountID from access where bankID = '" + bankID + "' and perID = '" + loggedInID + "';")
        if bkRes > 0:
            bk = cur.fetchall()
        else:
            bk = []
        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'Confirm':
                userDetails = request.form
                if not bk:
                    return "No values selected"
                acc = userDetails['acc']
                amount = userDetails['amount']
                date = datetime.today().strftime('%Y-%m-%d')
                dateStr = "'" + date +"'"
                cur.execute("call account_deposit('" + loggedInID + "', "
                            + amount + ", '" + bankID + "', '" + acc + "'," + dateStr + ");")
                mysql.connection.commit()
                cur.close()
                return "Success"
            if request.form['submit_button'] == 'B':
                return redirect(url_for('make_deposit'))

    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('make_deposit2.html', bk=bk, bank=bankID)


@app.route('/create_corporation', methods=['GET', 'POST'])
def create_corporation():
    global loggedInID
    global loggedInType
    try:
        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'Create':
                userDetails = request.form
                corpID = userDetails['corpID']
                longName = userDetails['longName']
                shortName = userDetails['shortName']
                resAssets = userDetails['resAssets']
                cur = mysql.connection.cursor()
                cur.execute("call create_corporation(%s, %s, %s, %b);", (corpID, longName, shortName, resAssets))
                mysql.connection.commit()
                cur.close()
                return 'success'
            if request.form['submit_button'] == 'Back':
                return redirect(url_for('admin_menu'))
    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('create_corporation.html')


@app.route('/create_bank', methods=['GET', 'POST'])
def create_bank():
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        # getting corpID
        corpID_result = cur.execute("SELECT corpID FROM corporation;")
        if corpID_result > 0:
            corpID = cur.fetchall()
        else:
            corpId = []
        # getting managerID
        manager_result = cur.execute("select perID from employee where perID not in (SELECT manager from bank) "
                                     "and perID not in (select perID from workFor);")
        if manager_result > 0:
            manager = cur.fetchall()
        else:
            manager = []
        # getting employee
        employee_result = cur.execute("select perID from employee where perID not in(select manager from bank);")
        #employee_result = cur.execute("SELECT perID from person natural join bank_user where perID not in (SELECT"
        #                              " perID from employee) and perID not in (SELECT perID from system_admin); ")
        if employee_result > 0:
            employee = cur.fetchall()
        else:
            employee = []
        cur.close()
        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'Create':
                userDetails = request.form
                bankID = userDetails['bankID']
                name = userDetails['name']
                street = userDetails['street']
                city = userDetails['city']
                state = userDetails['state']
                zipcode = userDetails['zip']
                resAssets = userDetails['resAssets']
                corp_ID = userDetails['corp_ID']
                manager_ = userDetails['manager']
                employee_ = userDetails['employee']
                cur = mysql.connection.cursor()

                cur.execute("call create_bank('" + bankID + "', '" + name
                            + "', '" + street + "', '" + city + "', '" + state + "', '" + zipcode + "', "
                            + resAssets + ",'" + corp_ID + "', '" + manager_ + "', '" + employee_ + "');")
                mysql.connection.commit()
                cur.close()
                return "Success"
            if request.form['submit_button'] == 'Back':
                return redirect(url_for('admin_menu'))

    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('create_bank.html',
                           corpID=corpID, managerList=manager, employeeList=employee)


@app.route('/create_employeeRole', methods=['GET', 'POST'])
def create_employeeRole():
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        # getting person
        person_result = cur.execute("select perID from person where perID not in (SELECT perID from employee) "
                                    "and perID not in (SELECT perID from system_admin);")
        if person_result > 0:
            person = cur.fetchall()
        else:
            person = []
        cur.close()
        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'Create':
                userDetails = request.form
                person_ = userDetails['person']
                salary = userDetails['salary']
                paymentNum = userDetails['num']
                total = userDetails['accumulated']
                cur = mysql.connection.cursor()
                res_ = cur.execute(
                    "select taxID, firstName, lastName, birthdate, street, city, state, zip, dtJoined, pwd "
                    "from person join (select bank_user.perID, bank_user.taxID, bank_user.firstName, bank_user.lastName, "
                    "bank_user.birthdate, bank_user.street, bank_user.city, bank_user.state, bank_user.zip, "
                    "bank_user.dtJoined, employee.salary, employee.payments, employee.earned from employee "
                    "join bank_user on bank_user.perID = employee.perID) as temp1 on person.perID = temp1.perID "
                    "where person.perID = 'pbeesly17';")

                res = cur.fetchall()

                if res[0][0] == None:
                    a = ""
                else:
                    a = (res[0][0])
                if res[0][1] == None:
                    b = ""
                else:
                    b = (res[0][1])
                if res[0][2] == None:
                    c = ""
                else:
                    c = (res[0][2])
                if res[0][3] == None:
                    d = "NULL"
                else:
                    d = "'" + str(res[0][3]) + "'"
                if res[0][4] == None:
                    e = ""
                else:
                    e = (res[0][4])
                if res[0][5] == None:
                    f = ""
                else:
                    f = (res[0][5])
                if res[0][6] == None:
                    g = ""
                else:
                    g = (res[0][6])
                if res[0][7] == None:
                    h = ""
                else:
                    h = (res[0][7])
                if res[0][8] == None:
                    i = "NULL"
                else:
                    i = "'" + str(res[0][8]) + "'"
                if res[0][9] == None:
                    j = ""
                else:
                    j = (res[0][9])

                cur.execute(
                    "call start_employee_role('" + person_ + "', '" + a + "', '" + b + "', '" + c + "', " + d + ", '" + e + "', '" + f + "', '" + g + "', '" + h + "', " + i + ", " + salary + ", " + paymentNum + ", " + total + ", '" + j + "');")

                mysql.connection.commit()
                cur.close()
                return 'success'
            if request.form['submit_button'] == 'Back':
                return redirect(url_for('manage_users'))

    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('create_employeeRole.html', person=person)


@app.route('/create_customerRole', methods=['GET', 'POST'])
def create_customerRole():
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        # getting perID
        personRes = cur.execute(
            "SELECT perID from person natural join bank_user where perID not in (SELECT perID from customer) and perID not in (SELECT perID from system_admin);")
        if personRes > 0:
            per = cur.fetchall()
        else:
            per = []
        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'Create':
                userDetails = request.form
                perID = userDetails['perID']
                res_ = cur.execute("SELECT person.perID, taxID, firstName, lastName, birthdate, street, city, state,"
                                   " zip, dtJoined, pwd from bank_user join person on bank_user.perID = person.perID where "
                                   "person.perID = '" + perID + "';")
                res = cur.fetchall()
                if res[0][0] == None:
                    a = ""
                else:
                    a = (res[0][0])
                if res[0][1] == None:
                    b = ""
                else:
                    b = (res[0][1])
                if res[0][2] == None:
                    c = ""
                else:
                    c = (res[0][2])
                if res[0][3] == None:
                    d = ""
                else:
                    d = (res[0][3])
                if res[0][4] == None:
                    e = "NULL"
                else:
                    e = "'" + str(res[0][4]) + "'"
                if res[0][5] == None:
                    f = ""
                else:
                    f = (res[0][5])
                if res[0][6] == None:
                    g = ""
                else:
                    g = (res[0][6])
                if res[0][7] == None:
                    h = ""
                else:
                    h = (res[0][7])
                if res[0][8] == None:
                    i = ""
                else:
                    i = (res[0][8])
                if res[0][9] == None:
                    j = "NULL"
                else:
                    j = "'" + str(res[0][4]) + "'"
                if res[0][10] == None:
                    k = ""
                else:
                    k = (res[0][10])
                cur.execute("call start_customer_role('" + a + "', '" + b + "', '" + c + "', '"
                            + d + "', " + e + ", '" + f + "', '" + g + "', '"
                            + h + "', '" + i + "', " + j + ", '" + k + "');")
                mysql.connection.commit()
                cur.close()
                return "Success"
            if request.form['submit_button'] == 'Back':
                return redirect(url_for('manage_users'))

    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('create_customerRole.html',
                           per=per)


@app.route('/stop_employeeRole', methods=['GET', 'POST'])
def stop_employeeRole():
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        # getting perID
        personRes = cur.execute(
            "select perID from employee where perID not in(select manager from bank) "
            "and perID not in (SELECT distinct perID from workfor group by bankID having count(perID) = 1);")
        if personRes > 0:
            per = cur.fetchall()
        else:
            per = []
        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'Create':
                userDetails = request.form
                perID = userDetails['perID']
                cur.execute("call stop_employee_role('" + perID + "');")
                mysql.connection.commit()
                cur.close()
                return "Success"
            if request.form['submit_button'] == 'Back':
                return redirect(url_for('manage_users'))

    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('stop_employeeRole.html', per=per)


@app.route('/stop_customerRole', methods=['GET', 'POST'])
def stop_customerRole():
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        # getting perID
        personRes = cur.execute(
            "select perID from customer where perID not in (SELECT distinct perID from access join (SELECT access.bankID, access.accountID from access group by accountID, bankID having count(distinct perID) = 1) as temp "
            "on access.accountID = temp.accountID);")
        if personRes > 0:
            per = cur.fetchall()
        else:
            per = []
        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'Create':
                userDetails = request.form
                perID = userDetails['perID']
                res_ = cur.execute("call stop_customer_role('" + perID + "');")
                mysql.connection.commit()
                cur.close()
                return "Success"
            if request.form['submit_button'] == 'Back':
                return redirect(url_for('manage_users'))

    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('stop_customerRole.html', per=per)


@app.route('/hire_worker', methods=['GET', 'POST'])
def hire_worker():
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        # getting bank
        bankRes = cur.execute(
            "SELECT bankID from bank;")
        if bankRes > 0:
            bk = cur.fetchall()
        else:
            bk = []
        # getting perID
        personRes = cur.execute(
            "SELECT perID from employee where perID not in (SELECT manager from bank);")
        if personRes > 0:
            per = cur.fetchall()
        else:
            per = []
        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'Create':
                userDetails = request.form
                emp = userDetails['employee']
                bank = userDetails['bank']
                cur.execute("SELECT salary from workFor join employee on workFor.perID = employee.perID "
                            "where employee.perID = '" + emp + "';")
                res = cur.fetchall()
                if res[0][0] == None:
                    a = 0
                else:
                    a = str(res[0][0])
                cur.execute("call hire_worker('" + emp + "', '" + bank + "', " + str(a) + ");")
                mysql.connection.commit()
                cur.close()
                return "Success"
            if request.form['submit_button'] == 'Back':
                if loggedInType == 1:
                    return redirect(url_for('manager_menu'))
                elif loggedInType == 2:
                    return redirect(url_for('admin_menu'))

    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('hire_worker.html', per=per, bk=bk)


@app.route('/replace_manager', methods=['GET', 'POST'])
def replace_manager():
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        # getting bank
        bankRes = cur.execute(
            "SELECT bankID from bank;")
        if bankRes > 0:
            bk = cur.fetchall()
        else:
            bk = []
        # getting perID
        personRes = cur.execute(
            "SELECT perID from employee where perID not in (SELECT perID from workFor) and perID "
            "not in (SELECT manager from bank) and perID not in (select perID from system_admin); ")
        if personRes > 0:
            per = cur.fetchall()
        else:
            per = []
        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'Create':
                userDetails = request.form
                emp = userDetails['employee']
                bank = userDetails['bank']
                salary = userDetails['salary']

                cur.execute("call replace_manager('" + emp + "', '" + bank + "', " + str(salary) + ");")
                mysql.connection.commit()
                cur.close()
                return "Success"
            if request.form['submit_button'] == 'Back':
                return redirect(url_for('admin_menu'))

    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('replace_manager.html', per=per, bk=bk)

# Screen 8
# Admin goes to this screen
# manage_accountAdmin
@app.route('/manage_accountAdmin', methods=['GET', 'POST'])
def manage_accountAdmin():
    global loggedInID
    global loggedInType
    if request.method == 'POST':
        # fetch form data
        if request.form['submit_button'] == 'existing':
            return redirect(url_for('manage_account_customer'))
        elif request.form['submit_button'] == 'create':
            return redirect(url_for('create_account_admin'))
        elif request.form['submit_button'] == 'Back':
            return redirect(url_for('admin_menu'))

    return render_template('manageAccountAdmin.html')

@app.route('/create_account_admin', methods=['GET', 'POST'])
def create_account_admin():
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        # get customer
        cus_ = cur.execute("select perID from customer;")
        if cus_ > 0:
            c = cur.fetchall()
        else:
            c = []

        # get bankID
        bnk = cur.execute("select bankID from bank;")
        if bnk > 0:
            bk = cur.fetchall()
        else:
            bk = []

        # get accID
        accRes2 = cur.execute("SELECT accountID from bank_account;")
        if accRes2 > 0:
            acc2 = cur.fetchall()
        else:
            acc2 = []
        # account options
        accOpt = []
        accOpt.append("savings")
        accOpt.append("checking")
        accOpt.append("market")
        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'Create':
                userDetails = request.form
                requester = loggedInID
                customer = userDetails['owner']
                bankID = userDetails['bank']
                accountID = userDetails['accountID']
                accountType = userDetails['accountType']
                initialBalance = userDetails['initialBalance']
                rate = userDetails['interestRate']
                minBalance = userDetails['minBalance']
                maxWith = userDetails['maxWithdrawals']
                numWithdrawals = 0
                date = datetime.today().strftime('%Y-%m-%d')
                dateStr = "'" + date + "'"
                if not initialBalance:
                    initialBalance = 0
                if not rate:
                    rate = 0
                if not minBalance:
                    minBalance = 0
                if not maxWith:
                    maxWith = 0
                cur.execute("call add_account_access('" + requester + "', '" + customer + "', '" + accountType + "', '" + bankID + "', '" + accountID + "', " + str(initialBalance) + ", " + str(rate) + ", " + dateStr + ", " + str(minBalance) + ", " + str(numWithdrawals) + ", " + str(maxWith) + ", " + dateStr + ");")
                mysql.connection.commit()
                cur.close()
                return "Success"
            if request.form['submit_button'] == 'Back':
                return flask.redirect("/manage_accountAdmin")

    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('manage_account_admin.html', bk=bk, acc2=acc2, accOpt=accOpt, owner=c)





# Customer goes to this screen
@app.route('/manage_account', methods=['GET', 'POST'])
def manage_account_customer():
    global loggedInID
    global loggedInType
    try:
        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'Next':
                userDetails = request.form
                if request.form.get('check'):
                    return redirect(url_for('add_owner'))
                else:
                    return redirect(url_for('remove_owner'))
            if request.form['submit_button'] == 'Back':
                if loggedInType == 3:
                    return redirect(url_for('customer_menu'))
                elif loggedInType == 2:
                    return redirect(url_for('manage_accountAdmin'))

    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('add_remove_owner.html')


@app.route('/remove_owner', methods=['GET', 'POST'])
def remove_owner():
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        #getting accessible account
        if loggedInType == 2:
            access = cur.execute(
                "SELECT bankID, accountID from access;")
            if access > 0:
                accessRes = cur.fetchall()
            else:
                accessRes = []
        else:
            access = cur.execute(
                "SELECT bankID, accountID from access where perID = '" + loggedInID + "';")
            if access > 0:
                accessRes = cur.fetchall()
            else:
                accessRes = []
        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'Next':
                userDetails = request.form
                acc = userDetails['acc']
                return redirect(url_for('removeOwner2', acc=acc))

            if request.form['submit_button'] == 'Cancel':
                return redirect(url_for('manage_account_customer'))

    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('remove_owner.html', acc=accessRes)

@app.route('/removeOwner2/<acc>', methods=['GET', 'POST'])
def removeOwner2(acc):
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        s = acc.split(':', 1)
        bankID = s[0]
        accID = s[1]
        # getting perID
        perRes = cur.execute(
            "SELECT perID from customer where perID in "
            "(SELECT perID from access where accountID = '" + s[1] + "' and bankID = '" + s[0] + "');")
        if perRes > 0:
            per = cur.fetchall()
        else:
            per = []
        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'Confirm':
                userDetails = request.form
                sharer = userDetails['per']
                cur.execute("call remove_account_access('" + loggedInID + "', '"
                            + sharer + "', '" + bankID + "', '" + accID + "');")
                mysql.connection.commit()
                cur.close()
                return "Success"
            if request.form['submit_button'] == 'Back':
                return flask.redirect("/remove_owner")

    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('remove_owner2.html', per=per)


@app.route('/add_owner', methods=['GET', 'POST'])
def add_owner():
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        #getting accessible account
        if loggedInType == 2:
            access = cur.execute(
                "SELECT bankID, accountID from access;")
            if access > 0:
                accessRes = cur.fetchall()
            else:
                accessRes = []
        else:
            access = cur.execute(
                "SELECT bankID, accountID from access where perID = '" + loggedInID + "';")
            if access > 0:
                accessRes = cur.fetchall()
            else:
                accessRes = []
        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'Next':
                userDetails = request.form
                acc = userDetails['acc']
                return redirect(url_for('addOwner2', acc=acc))

            if request.form['submit_button'] == 'Cancel':
                return flask.redirect("/manage_account")

    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('add_owner1.html', acc=accessRes)

@app.route('/addOwner2/<acc>', methods=['GET', 'POST'])
def addOwner2(acc):
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        s = acc.split(':', 1)
        bankID = s[0]
        accID = s[1]

        # getting perID
        perRes = cur.execute(
            "SELECT perID from customer where perID not in "
            "(SELECT perID from access where accountID = '" + s[1] + "' and bankID = '" + s[0] + "');")
        if perRes > 0:
            per = cur.fetchall()
        else:
            per = []
        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'Confirm':
                userDetails = request.form
                per = userDetails['per']
                date = datetime.today().strftime('%Y-%m-%d')
                dateStr = "'" + date + "'"
                cur.execute("call add_account_access('" + loggedInID + "', '" + per + "', 'NULL', '" + bankID + "', '" + accID + "', 0, 0, null, 0, 0, 0," + dateStr + ");")
                mysql.connection.commit()
                cur.close()
                return "Success"
            if request.form['submit_button'] == 'Back':
                return flask.redirect("/add_owner")

    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('add_owner2.html', per=per)


@app.route('/create_fee', methods=['GET', 'POST'])
def create_fee():
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        # getting bank
        bankRes = cur.execute(
            "SELECT bankID from bank;")
        if bankRes > 0:
            bk = cur.fetchall()
        else:
            bk = []
        # to select account from dropdown
        accID = cur.execute(
            "SELECT accountID from bank_account; ")
        if accID > 0:
            acc = cur.fetchall()
        else:
            acc = []
        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'Create':
                userDetails = request.form
                bank = userDetails['bank']
                account = userDetails['account']
                feeType = userDetails['feeType']
                cur.execute("call create_fee('" + bank + "', '" + account + "', '" + feeType + "');")
                mysql.connection.commit()
                cur.close()
                return "Success"
            if request.form['submit_button'] == 'Back':
                return redirect(url_for('admin_menu'))

    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('create_fee.html', acc=acc, bk=bk)


@app.route('/start_stop_overdraft', methods=['GET', 'POST'])
def start_stop_overdraft_customer():
    global loggedInID
    global loggedInType
    try:
        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'Next':
                userDetails = request.form
                if request.form.get('check'):
                    num = 1
                    return redirect(url_for('overdraft2'))
                else:
                    num = 2
                    return redirect(url_for('removeOverdraft'))

            if request.form['submit_button'] == 'Back':
                if loggedInType == 2:
                    return redirect(url_for('admin_menu'))
                elif loggedInType == 3:
                    return redirect(url_for('customer_menu'))

    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('start_stop_overdraft_customer.html')


@app.route('/removeOverdraft', methods=['GET', 'POST'])
def removeOverdraft():
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        # getting savings account
        checking = cur.execute(
            "SELECT A.accountID, A.bankID from (SELECT bankID, accountID from checking where protectionbank is not null "
            "and protectionaccount is not null) as A join access where A.bankID = access.bankID and A.accountID = "
            "access.accountID and perID = '" + loggedInID + "';")
        if checking > 0:
            ck = cur.fetchall()
        else:
            ck = []

        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'Confirm':
                userDetails = request.form
                checking = userDetails['checking']
                bk = cur.execute("select bankID from access where perID = '" + loggedInID + "' and accountID = '" + checking
                                 + "'and accountID in (select accountID from checking where protectionbank is not null and protectionaccount is not null);")
                if bk > 0:
                    bank = cur.fetchall()
                s = checking.split(':',1)
                bankID = s[1]
                check = s[0]
                print(bankID)
                print(check)
                cur.execute("call stop_overdraft('" + loggedInID + "', '" + bankID + "', '" + check + "');")
                mysql.connection.commit()
                cur.close()
                return 'success'
            if request.form['submit_button'] == 'Back':
                return flask.redirect("/start_stop_overdraft")

    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('stop_overdraft.html', ck=ck)

@app.route('/overdraft2', methods=['GET', 'POST'])
def overdraft2():
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        # getting checking account
        checking = cur.execute("SELECT A.bankID, A.accountID from (SELECT bankID, accountID from checking where "
                               "protectionbank is null and protectionaccount is null) as A join access where A.bankID = "
                               "access.bankID and A.accountID = access.accountID and perID = '" + loggedInID + "';")
        if checking > 0:
            ck = cur.fetchall()
        else:
            ck = []

        # getting saving account
        saving = cur.execute("SELECT Distinct B.bankID, B.accountID from (SELECT perID from access join checking on "
                             "access.bankID = checking.bankID and access.accountID = checking.accountID where "
                             "protectionbank is null and protectionaccount is null) as A right outer join (SELECT "
                             "access.perID, access.bankID, access.accountID from access join savings on access.bankID = "
                             "savings.bankID and access.accountID = savings.accountID) as B on A.perID = B.perID where"
                             " B.perID = '" + loggedInID + "';")
        if saving > 0:
            sav = cur.fetchall()
        else:
            sav = []

        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'Confirm':
                userDetails = request.form
                checking = userDetails['checking']
                s = checking.split(':', 1)
                ckID = s[0]
                bkID = s[1]
                saving = userDetails['saving']
                s = saving.split(':', 1)
                savID = s[0]
                savBkID = s[1]

                cur.execute("call start_overdraft('" + loggedInID + "', '" + bkID + "', '" + ckID
                            + "', '" + savBkID + "', '" + savID + "');")

                mysql.connection.commit()
                cur.close()
                return 'success'
            if request.form['submit_button'] == 'Back':
                return flask.redirect("/start_stop_overdraft")

    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('start_overdraft.html', ck=ck, sav=sav)


@app.route('/loginM', methods=['GET', 'POST'])
def loginM():
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'Login':
                userDetails = request.form
                loginID = userDetails['loginid']
                pw = userDetails['pw']
                res = cur.execute("select * from person where perID = '" + loginID + "' and pwd = '" + pw + "';")
                if res > 0:
                    mngr = cur.execute("select * from bank where manager = '" + loginID + "';")
                    if mngr > 0:
                        loggedInID = loginID
                        loggedInType = 1
                        cur.close()
                        return redirect(url_for('manager_menu'))
                    else :
                        return "User Not Found! Please Login Again!"
                else:
                    return "Wrong ID or Password! Please Login Again!"
            elif request.form['submit_button'] == 'Back':
                return redirect(url_for('InitialPage'))


    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('login.html')


@app.route('/loginA', methods=['GET', 'POST'])
def loginA():
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'Login':
                userDetails = request.form
                loginID = userDetails['loginid']
                pw = userDetails['pw']
                res = cur.execute("select * from person where perID = '" + loginID + "' and pwd = '" + pw + "';")
                if res > 0:
                    admin = cur.execute("select * from system_admin where perID = '" + loginID + "';")
                    if admin > 0:
                        loggedInID = loginID
                        cur.close()
                        return redirect(url_for('admin_menu'))
                    else :
                        return "User Not Found! Please Login Again!"
                else:
                    return "Wrong ID or Password! Please Login Again!"
            elif request.form['submit_button'] == 'Back':
                return redirect(url_for('InitialPage'))

    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('login.html')


@app.route('/loginC', methods=['GET', 'POST'])
def loginC():
    global loggedInID
    global loggedInType
    try:
        cur = mysql.connection.cursor()
        if request.method == 'POST':
            # fetch form data
            if request.form['submit_button'] == 'Login':
                userDetails = request.form
                loginID = userDetails['loginid']
                pw = userDetails['pw']
                res = cur.execute("select * from person where perID = '" + loginID + "' and pwd = '" + pw + "';")
                if res > 0:
                    customer = cur.execute("select * from customer where perID = '" + loginID + "';")
                    if customer > 0:
                        loggedInID = loginID
                        cur.close()
                        return redirect(url_for('customer_menu'))
                    else :
                        return "User Not Found! Please Login Again!"
                else:
                    return "Wrong ID or Password! Please Login Again!"
            elif request.form['submit_button'] == 'Back':
                return redirect(url_for('InitialPage'))

    except MySQLdb.Error as error:
        return "Failed to create due to this error: " + repr(error)

    return render_template('login.html')


@app.route('/', methods=['GET', 'POST'])
def InitialPage():
    global loggedInID
    global loggedInType
    if request.method == 'POST':
        # fetch form data
        if request.form['submit_button'] == 'LoginM':
            loggedInType = 1
            return redirect(url_for('loginM'))
        elif request.form['submit_button'] == 'LoginA':
            loggedInType = 2
            return redirect(url_for('loginA'))
        elif request.form['submit_button'] == 'LoginC':
            loggedInType = 3
            return redirect(url_for('loginC'))

    return render_template('Initial_Page.html')


@app.route('/users', methods=['GET', 'POST'])
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM corporation")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html', userDetails=userDetails)


if __name__ == '__main__':
    app.run(debug=True)
