# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 15:35:53 2021

@author: dinah
"""

import os
from pathlib import Path
from flask import Flask,request
import json

# Path with student json files
students_path = "../../wis-advanced-python-2021-2022/students/"
# students_path = r"\\data.wexac.weizmann.ac.il\sorek\dinah\2022_pythoncourse\wis-advanced-python-2021-2022\students"
# student_list = sorted([student for student in os.listdir(students_path) if student.endswith(".json")])

print(os.listdir(students_path))


# with open(students_path) as f:
#     for line in f:
#         print(line)
# #
app = Flask(__name__)
app.config["DEBUG"] = True



@app.route("/")
def main():
    return '''
    <form method="POST" action="/search">
    <input name="pattern">
    <input type="submit" value="Search">
    </form>
    '''

# @app.route("/search", methods=['POST'] )
# def student_list_pattern():
    










