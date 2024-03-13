import sqlite3
import json
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
cors = CORS()

app = Flask(__name__)

cors.init_app(app)

def database_tasks(query):
    # Connecting to sqlite 
    try:
        print(query)
        conn = sqlite3.connect('sql.db') 
        cursor = conn.cursor() 
        data = cursor.execute(query) 
        if data:
            return [
                i for i in data
            ] 
    except Exception as exc:
        raise exc
    finally:
        conn.commit() 
        conn.close()
    

# Get patient medical records
@app.route('/records', methods=['GET'])
def get_records():
    ssn = request.args.get('ssn')
    firstname = request.args.get('firstname')
    lastname = request.args.get('lastname')
    query = f'''SELECT * FROM Patients  where id ={ssn} and firstname = '{firstname}' and lastname='{lastname}' '''
    records = database_tasks(query)
    print(records)
    if not records:
        response = make_response({'status': 'ok', **{'data':'Patient not found'}}, 404)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    response = make_response({'status': 'ok', **{'data':records}}, 200)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# Create a new patient
@app.route('/create-patient', methods=['POST'])
def create_patient():
    data = json.loads(request.get_data())
    firstname = data['firstname']
    lastname = data['lastname']
    phone = data['phone']
    record = data['record']
    create_query  = f'''INSERT INTO Patients VALUES (NULL, '{firstname}', '{lastname}', '{phone}','{record}')'''
    database_tasks(create_query)
    query = f'''Select * from Patients where firstname='{firstname}' and lastname='{lastname}' and phone='{phone}' '''
    data= database_tasks(query)[0]
    print(data)
    response = make_response({'status': 'ok', **{'data':f'Patient added successfully. Your ssn id is {data[0]}'}}, 200)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# Update existing patient phone number
@app.route('/update-patient', methods=['PUT'])
def update_patient():
    data = json.loads(request.get_data())
    print(data)
    ssn=data['ssn']
    firstname = data['firstname']
    lastname = data['lastname']
    phone = data['phone']
    record = data['record']
    query = f'''SELECT * FROM Patients  where id ={ssn} and firstname = '{firstname}' and lastname='{lastname}' '''
    records = database_tasks(query)
    if not records:
        response = make_response({'status': 'ok', **{'data':'Patient not found'}}, 404)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    query = f'''UPDATE patients SET record = '{record}', phone='{phone}' WHERE id='{ssn}' '''
    database_tasks(query)
    response = make_response({'status': 'ok', **{'data':'Patient Update successfully.'}}, 200)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Delete patient records
@app.route('/delete-patient', methods=['DELETE'])
def delete_patient():
    data = json.loads(request.get_data())
    ssn=data['ssn']
    firstname = data['firstname']
    lastname = data['lastname']
    query = f'''SELECT * FROM Patients  where id ={ssn} and firstname = '{firstname}' and lastname='{lastname}' '''
    records = database_tasks(query)
    if not records:
        response = make_response({'status': 'ok', **{'data':'Patient not found'}}, 404)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    query =f''' delete from Patients where id = {ssn} '''
    database_tasks(query)
    response = make_response({'status': 'ok', **{'data':'Patient Deleted successfully.'}}, 200)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True)
