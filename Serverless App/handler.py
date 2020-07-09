import json
import pymysql
import sys
import logging

#Configuration Values
endpoint = 'blackswan-employee.cdua2sddrvov.us-east-1.rds.amazonaws.com'
username = 'root'
password = 'rootroot'
database_name = 'blackswanEmployee'

# Create DB Connection to the App
try:
    conn = pymysql.connect(endpoint, user=username, passwd=password, db=database_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

def getEmployeeList(event, context):
    item_count = 0
    data = {}
    results = []

    try:
        with conn.cursor() as cur:
            cur.execute("select * from Employee")
            data = cur.fetchall()
            for row in data:
                dt = {
                   'id' :  data[item_count][0],
                   'name' : data[item_count][1],
                   'email' : data[item_count][2]
                }
                item_count += 1
                results.append(dt)
        conn.commit()
        body = {
            "success": True,
            "message": "get employee list successful!",
            "data": results,
        }
        response = {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True,
            },
            "body": json.dumps(body)
        }
        return response
    except Exception as e:
        print("Database connection failed due to {}".format(e))
        body = {
            "success": False,
            "message": "get employee list failed!",
            "request data": [],
        }
        response = {
            "statusCode": 500,
            "headers":{
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True,
            },
            "body": json.dumps(body)
        }
        return response

def createEmployee(event, context):
    employeeName = (json.loads(event['body'])).get("name", "")
    employeeEmail = (json.loads(event['body'])).get("email", "")
    item_count = 0

    try:
        with conn.cursor() as cur:
            cur.execute("create table if not exists Employee ( EmpID int NOT NULL AUTO_INCREMENT, Name varchar(255) NOT NULL,Email varchar(255) NOT NULL, PRIMARY KEY (EmpID))")
            cur.execute('insert into Employee (Name, Email) values(%s, %s)', (employeeName, employeeEmail))
            conn.commit()
            cur.execute("select * from Employee")
            for row in cur:
                item_count += 1
        conn.commit()

        body = {
            "success": True,
            "message": "employee created successfully!",
            "employee": {
                "id": row[0],
                "name": row[1],
                "email": row[2]
            },
            "employeeCount" : item_count
        }

        response = {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True,
            },
            "body": json.dumps(body)
        }

        return response
    except Exception as e:
        print("Database connection failed due to {}".format(e))
        body = {
            "success": False,
            "message": "employee creation failed!",
            "employees": {}
        }
        response = {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True,
            },
            "body": json.dumps(body)
        }
        return response

def updateEmployee(event, context):
    employeeId = (json.loads(event['body'])).get("id", "")
    employeeName = (json.loads(event['body'])).get("name", "")
    employeeEmail = (json.loads(event['body'])).get("email", "")
    item_count = 0

    try:
        with conn.cursor() as cur:
            cur.execute('update Employee set `Name` = %s where (`EmpID` = %s)', (employeeName, employeeId))
            conn.commit()
            cur.execute('update Employee set `Email` = %s where (`EmpID` = %s)', (employeeEmail, employeeId))
        conn.commit()

        body = {
            "success": True,
            "message": "employee updated successfully!",
            "employee": {
                "id": employeeId,
                "name": employeeName,
                "email": employeeEmail
            }
        }

        response = {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True,
            },
            "body": json.dumps(body)
        }

        return response
    except Exception as e:
        print("Database connection failed due to {}".format(e))
        body = {
            "success": False,
            "message": "employee updating failed!",
        }
        response = {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True,
            },
            "body": json.dumps(body)
        }
        return response

def deleteEmployee(event, context):
    item_count = 0;
    employeeId = (json.loads(event['body'])).get("id", "")
    print('employeeId', employeeId)
    try:
        with conn.cursor() as cur:
            cur.execute('delete from Employee where (`EmpID` = %s)', (employeeId))
        conn.commit()

        body = {
            "success": True,
            "message": "employee deleted successfully!",
        }

        response = {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True,
            },
            "body": json.dumps(body)
        }

        return response
    except Exception as e:
        print("Database connection failed due to {}".format(e))
        body = {
            "success": False,
            "message": "employee deletion failed!",
        }
        response = {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True,
            },
            "body": json.dumps(body)
        }
        return response
