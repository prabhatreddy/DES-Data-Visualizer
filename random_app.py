import csv
from flask import Flask
from flask import render_template
from flask import request
from flask import json

app = Flask(__name__)

#Gets data and converts it to a list of objects
def getData():
    #Todo: Fetch data from db rather than a static csv
    path_to_data = './static/data.csv'
    data_file = open(path_to_data, 'rb')
    data_obj = csv.DictReader(data_file)
    obj_list = list(data_obj)
    filtered_list = filterData(obj_list)
    return filtered_list

def filterData(objects):
    filtered_list = []
    for obj in objects:
        if float(obj['RA']) < 322.5:
            filtered_list.append(obj)
    return filtered_list

def isVisible(obj):
    if obj.RA < 322.5:
        return True
    return False

@app.route("/")
def main():
    object_list = getData()
    return render_template('random_map.html', object_list = object_list)

if __name__ == "__main__":
    app.run()
