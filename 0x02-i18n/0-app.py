#!/usr/bin/env python3
"""Basic Flask application"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    """Renders the hello_world template"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port=8000)
