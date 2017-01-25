from flask import Flask
import logging
from logging.handlers import RotatingFileHandler
from flask import render_template
from web_questionnaire import config
from web_questionnaire.logger.logger import get_logger

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/index')
def test():
    logger = get_logger('my_logger')
    logger.info('my message', extra={'var': 1})
    try:
        x = 1 / 0
    except:
        logger.exception('this is an exception')
    return render_template('test.html')


if __name__ == '__main__':
    app.run('127.0.0.1', 20000, True)
