import json
import csv
import sys
import MySQLdb

# Function to establish a connection with database
def dbconnect():
    
    try:
       db = MySQLdb.connect(   
           host = "127.0.0.1",  
           user = "username", (database username)  
           passwd = "password", (database password)
        )
    except Exception as e:
        sys.exit("Can't connect to Database")
    return db

# def createDB(db_name, table_name):
def DB_to_json(db_name,table,output_json,output_csv):
    try:
        db = dbconnect()
        cursor = db.cursor()
        # cursor.execute('''SELECT * FROM real estate.realestate''')
        cursor.execute('''SELECT * FROM {}.{}'''.format(db_name,table))
        headers = [x[0] for x in cursor.description]
        data = cursor.fetchall()
        json_result=[]

        for i in data:
            json_result.append(dict(zip(headers,i)))

        try:
            with open(output_json + '.json', 'w') as json_out:
                json.dump(json_result, json_out,indent=4)
        except Exception as e:
            print "Error in generating json file \n", e

        try:
            c=csv.writer(open(output_csv + '.csv', 'wb'))
            for i in data:
                c.writerow(headers)
                c.writerow(i)
        except Exception as e:
            print "Error in generating csv file \n", e

    except Exception as e:
        print e

#Call function define Database, Table and name of the Output json file.
#User input to select Json & CSV filename.

print "\n-------- Enter Json & CSV filename -------------\n"

while True:
    json_output_file = raw_input("Json File Name: ")
    csv_output_file = raw_input("CSV File Name: ")

    if json_output_file.isalpha() and csv_output_file.isalpha():
        break
    print "Enter correct file name"

DB_to_json(db_name="houseprice",table="realestate",output_json=json_output_file,output_csv=csv_output_file)

