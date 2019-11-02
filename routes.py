from flask import render_template, redirect
from app import app
from forms import playGame, Game




@app.route('/', methods=['GET', 'POST'])
def start_page():
    form = playGame()

    if form.validate_on_submit():
        return redirect('/game_page')
    return render_template('start_page.html', title='my web page', form=form)


# usersAnswer = form.answer.data


@app.route('/game_page', methods=['GET', 'POST'])
def game():
    form = Game()

    if form.validate_on_submit():
        if form.answer.data == 'Delhi':
            return redirect('/congo')
        else:
            return redirect('/loser')


    return render_template('game_page.html', title='gaming heaven', form=form)


@app.route('/congo')
def congo():
    return render_template('correct_answer.html', title='winner winner chicken dinner')

@app.route('/loser')
def loser():
    return render_template('loser.html', title='Don cry')




@app.route('/login')
def login():
    return 'Please log in to save progress'
