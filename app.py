# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 01:50:37 2019

@author: Rashika
"""

import FetchData

from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def result():
    
      re=FetchData.data()
      
      return render_template("result.html",tables= [re.to_html()])
  
if __name__ == '__main__':
    app.run(port=5000, debug=True)
    