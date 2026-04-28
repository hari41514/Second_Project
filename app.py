#Number Guessing Game (Second Project) 
from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "secret123"

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 50)
        session['score'] = 5
        session['message'] = "Guess a number between 1 to 50"

    if request.method == 'POST':
        guess = int(request.form['guess'])
        number = session['number']
        score = session['score']

        if score <= 0:
            session['message'] = "Game Over! You Lost"
        else:
            if guess > 50 or guess < 1:
                session['message'] = "Invalid! Lost 1 chance"
            elif guess == number:
                session['message'] = "🎉 Congratulations! You Won!"
            elif guess < number:
                session['message'] = "Too Low! Try higher"
            else:
                session['message'] = "Too High! Try lower"

            session['score'] = score - 1

    return render_template(
        'index.html',
        message=session.get('message'),
        score=session.get('score')
    )

@app.route('/reset')
def reset():
    session.clear()
    return "Game Reset! <a href='/'>Play Again</a>"

if __name__ == '__main__':
    app.run(debug=True)
