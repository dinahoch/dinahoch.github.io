import os
from pathlib import Path
from flask import Flask,request
import json

students_path = Path("../wis-advanced-python-2021-2022/students/") # path to directory with json files for students
student_list = sorted([student for student in os.listdir(students_path) if student.endswith(".json")]) # Collect all json files of students and sort by name

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/") # default route. returns a list of ALL students in an html format. Clicking on a students opens the info.
def main_page():
    return(html_list_of_students(student_list))+"""
    <form method="POST" action="/search">
    <input name="pattern">
    <input type="submit" value="Search">
    </form>
    """ # return list of all students plus option to search specific pattern in the json files

@app.route("/student/<json_file>")
def show_json(json_file):
    f = open(students_path / json_file)
    data = json.load(f)
    f.close()
    html = """
    <h1>Information: {}</h1>
    <p>
    {}
    </p>
    """.format(json_file.rstrip(".json"),"<br>".join(["{}: {}".format(key,value) for key,value in data.items() if value!=None]))
    return(html)

@app.route("/search", methods=['POST'] )
def list_students_with_pattern():
    pattern = request.form.get('pattern')
    filtered_list = []
    for student in student_list:
        f = open(students_path / student)
        txt = f.read()
        f.close()
        if pattern in txt:
            filtered_list.append(student)
    return(html_list_of_students(filtered_list)).replace("Students in the Course:","Students with pattern '{}'".format(pattern))
        


def html_list_of_students(json_files):
    """
    Parameters
    ----------
    json_files : TYPE list
        list of all students to be presented, json files in dir "students"
    Returns
    -------
    clickble html list of students in list
    """
    html = """
    <h1> Students in the Course:</h1>
    <ul>
    {}
    </ul>
    """.format("".join(["<li><a href=/student/"+student+">"+student.rstrip(".json")+"</a></li>" for student in json_files]))
    return(html)

app.run(port="8043",host="0.0.0.0")
