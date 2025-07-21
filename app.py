from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database connection configuration
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        database='apartment'
    )

@app.route('/')
def index():
    return render_template('index.html')

# Tenants Routes
@app.route('/tenants')
def tenants():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tenants")
    tenants_data = cursor.fetchall()
    connection.close()
    return render_template('tenants.html', tenants=tenants_data)

@app.route('/add_tenant', methods=['POST'])
def add_tenant():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO tenants (tenant_id, Fname, Lname, contact_info, email) VALUES (%s, %s, %s, %s, %s)",
        (request.form['tenant_id'], request.form['fname'], request.form['lname'], request.form['contact_info'], request.form['email'])
    )
    connection.commit()
    connection.close()
    return redirect('/tenants')

@app.route('/delete_tenant/<int:tenant_id>', methods=['POST'])
def delete_tenant(tenant_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM tenants WHERE tenant_id = %s", (tenant_id,))
    connection.commit()
    connection.close()
    return redirect('/tenants')

# Apartments Routes
@app.route('/apartments')
def apartments():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM apartments")
    apartments_data = cursor.fetchall()
    connection.close()
    return render_template('apartments.html', apartments=apartments_data)

@app.route('/add_apartment', methods=['POST'])
def add_apartment():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO apartments (apartment_id, monthly_rent, apartment_number, floor_number, type) VALUES (%s, %s, %s, %s, %s)",
        (request.form['apartment_id'], request.form['monthly_rent'], request.form['apartment_number'], request.form['floor_number'], request.form['type'])
    )
    connection.commit()
    connection.close()
    return redirect('/apartments')

@app.route('/delete_apartment/<int:apartment_id>', methods=['POST'])
def delete_apartment(apartment_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM apartments WHERE apartment_id = %s", (apartment_id,))
    connection.commit()
    connection.close()
    return redirect('/apartments')

# Leases Routes
@app.route('/leases')
def leases():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM leases")
    leases_data = cursor.fetchall()
    connection.close()
    return render_template('leases.html', leases=leases_data)

@app.route('/add_lease', methods=['POST'])
def add_lease():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO leases (lease_id, apartment_id, tenant_id, lease_start_date, lease_end_date) VALUES (%s, %s, %s, %s, %s)",
        (request.form['lease_id'], request.form['apartment_id'], request.form['tenant_id'], request.form['lease_start_date'], request.form['lease_end_date'])
    )
    connection.commit()
    connection.close()
    return redirect('/leases')

@app.route('/delete_lease/<int:lease_id>', methods=['POST'])
def delete_lease(lease_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM leases WHERE lease_id = %s", (lease_id,))
    connection.commit()
    connection.close()
    return redirect('/leases')

# Payments Routes
@app.route('/payments')
def payments():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM payments")
    payments_data = cursor.fetchall()
    connection.close()
    return render_template('payments.html', payments=payments_data)

@app.route('/add_payment', methods=['POST'])
def add_payment():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO payments (payment_id, lease_id, payment_date, amount, payment_method) VALUES (%s, %s, %s, %s, %s)",
        (request.form['payment_id'], request.form['lease_id'], request.form['payment_date'], request.form['amount'], request.form['payment_method'])
    )
    connection.commit()
    connection.close()
    return redirect('/payments')

@app.route('/delete_payment/<int:payment_id>', methods=['POST'])
def delete_payment(payment_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM payments WHERE payment_id = %s", (payment_id,))
    connection.commit()
    connection.close()
    return redirect('/payments')

# Maintenance Requests Routes
@app.route('/maintenance_requests')
def maintenance_requests():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM maintenance_requests")
    maintenance_data = cursor.fetchall()
    connection.close()
    return render_template('maintenance_requests.html', maintenance_requests=maintenance_data)

@app.route('/add_maintenance_requests', methods=['POST'])
def add_maintenance_requests():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO maintenance_requests (request_id, apartment_id, tenant_id, status, description) VALUES (%s, %s, %s, %s, %s)",
        (request.form['request_id'],request.form['apartment_id'], request.form['tenant_id'], request.form['status'], request.form['description'])
    )
    connection.commit()
    connection.close()
    return redirect('/maintenance_requests')

@app.route('/delete_maintenance_requests/<int:request_id>', methods=['POST'])
def delete_maintenance_requests(request_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM maintenance_requests WHERE request_id = %s", (request_id,))
    connection.commit()
    connection.close()
    return redirect('/maintenance_requests')

# Parking Routes
@app.route('/parking')
def parking():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM parking")
    parking_data = cursor.fetchall()
    connection.close()
    return render_template('parking.html', parking=parking_data)

@app.route('/add_parking', methods=['POST'])
def add_parking():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO parking (parking_id, tenant_id, space_number, parking_type,availability_status) VALUES (%s, %s, %s, %s, %s)",
        (request.form['parking_id'], request.form['tenant_id'], request.form['space_number'], request.form['parking_type'], request.form['availability_status'])
    )
    connection.commit()
    connection.close()
    return redirect('/parking')

@app.route('/delete_parking/<int:parking_id>', methods=['POST'])
def delete_parking(parking_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM parking WHERE parking_id = %s", (parking_id,))
    connection.commit()
    connection.close()
    return redirect('/parking')

# Staff Routes
@app.route('/staff')
def staff():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM staff")
    staff_data = cursor.fetchall()
    connection.close()
    return render_template('staff.html', staff=staff_data)

@app.route('/add_staff', methods=['POST'])
def add_staff():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO staff (staff_id, Fname, Lname, role, contact_info) VALUES (%s, %s, %s, %s, %s)",
        (request.form['staff_id'], request.form['Fname'], request.form['Lname'], request.form['role'], request.form['contact_info'])
    )
    connection.commit()
    connection.close()
    return redirect('/staff')

@app.route('/delete_staff/<int:staff_id>', methods=['POST'])
def delete_staff(staff_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM staff WHERE staff_id = %s", (staff_id,))
    connection.commit()
    connection.close()
    return redirect('/staff')

if __name__ == '__main__':
    app.run(debug=True)
