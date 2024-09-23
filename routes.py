from flask import render_template, Flask, request, redirect, url_for
from data_base import select_random_records, select_game_name_for_url, select_all_games, filter_games_by_price
from models import PaymentForm

app = Flask(__name__)
app.secret_key = '1234567890'


@app.route('/')
def home():
    games_random = select_random_records()
    return render_template('home.html', games=games_random)


@app.route('/about_us/')
def about_us():
    return render_template('about_us.html')


@app.route("/buy_game/<string:game_name>/")
def buy_game(game_name):
    game = select_game_name_for_url(game_name)
    print(game)
    return render_template('buy_game.html', game=game)


@app.route('/all_games/', methods=['GET'])
def all_games():
    sort_by = request.args.get('sort_by', default='', type=str)
    games = select_all_games()
    sorted_games = filter_games_by_price(games, sort_by)

    return render_template('all_games.html', games=sorted_games)


@app.route('/payment/', methods=['GET', 'POST'])
def payment_page():
    form = PaymentForm()
    if form.validate_on_submit():
        # Here you would process the payment details.
        return redirect(url_for('payment_success'))

    return render_template('payment.html', form=form)


@app.route('/process_payment/', methods=['POST'])
def process_payment():
    name = request.form.get('name')
    card_number = request.form.get('card_number')
    expiry_date = request.form.get('expiry_date')
    cvv = request.form.get('cvv')

    return redirect(url_for('payment_success'))


@app.route('/payment_success/', methods=['GET'])
def payment_success():
    return render_template('payment_success.html')
