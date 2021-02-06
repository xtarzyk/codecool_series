from flask import Flask, render_template, url_for
from data import queries
import math
from dotenv import load_dotenv

ROWS_PER_PAGE = 15

load_dotenv()
app = Flask('codecool_series')

@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')



@app.route('/shows/most-rated')
@app.route('/shows/most-rated/<int:page_number>')
@app.route('/shows/order-by-<order_by>')
@app.route('/shows/order-by-<order_by>/<int:page_number>')
@app.route('/shows/order-by-<order_by>-<order_direction>')
@app.route('/shows/order-by-<order_by>-<order_direction>/<int:page_number>')
def shows(order_by='rating', order_direction='DESC', page_number=1):
    most_rated_shows = queries.display_shows(order_by=order_by, order_direction=order_direction, limit=ROWS_PER_PAGE, offset=ROWS_PER_PAGE*(page_number-1))
    return render_template('shows.html', shows=most_rated_shows)

def main():
    app.run(debug=False)


if __name__ == '__main__':
    main()
