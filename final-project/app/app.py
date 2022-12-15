import pip 
pip.main(['install', 'pandas','numpy','flask','flask-sqlalchemy','click','pandas-datareader','matplotlib','pyarrow'])

import os
import sys

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy # database based on flask and sql
import click

import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import matplotlib.pyplot as plt
# import seaborn as sns
import numpy as np

import matplotlib
matplotlib.use('Agg')  # 
from io import BytesIO
import base64




WIN = sys.platform.startswith('win')
if WIN:  # if the system is windows
    prefix = 'sqlite:///'
else:  # if the system is not windows
    prefix = 'sqlite:////'

# initial the app
app = Flask(__name__)


# database
app.config['SQLALCHEMY_DATABASE_URI'] = \
    prefix + os.path.join(app.root_path, 'data.db') # the address of the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # close the track for the modification
db = SQLAlchemy(app)


@app.cli.command()  # register as command
@click.option('--drop', is_flag=True, help='Create after drop.')  # options
def initdb(drop):
    """Initialize the database."""
    if drop:  # whether get the info
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')  # output the reminder info




@app.route('/')
def index():
    return render_template('index.html', name="Digital Tools for Finance", data_column_headers = data_column_headers)

class User(db.Model):  # the name of the table will user
    id = db.Column(db.Integer, primary_key=True)  # main key
    name = db.Column(db.String(20))  # currency


class Movie(db.Model):  # the name of the table will 
    id = db.Column(db.Integer, primary_key=True)  # main key
    title = db.Column(db.String(60))  
    year = db.Column(db.String(4))  


# interactive part for the currency
data_normal = pd.read_parquet('data_small.parquet')

# Get the list of all column names from data
data_column_headers = list(data_normal.columns.values)
print("The Column Header :", data_column_headers)


# @app.route('/currency_visual/<currency_name>/')
def currency_visual(currency_name):
    
    currency_name1 = currency_name
    print(currency_name)
    currency_name = data_normal[f'{currency_name}'].plot.line(figsize=(20,6), grid = True, \
         title= f'{currency_name} movement 2018-2022')
    

    plt.savefig(f'static/results/{currency_name1}.png')

# plot generating
# for header in iter(data_column_headers):
#     currency_visual(header)
#     plt.close()


if __name__ == '__main__':
    app.run(debug=True)

