from flask import render_template
from app import app


@app.errorhandler(404)
def four_Ow_four(error):
    """
    Function to render 404 error page
    :param error:
    :return:
    """
    return render_template('error.html'), 404
