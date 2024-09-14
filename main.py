from flask import Flask
from flask import render_template
from flask import request
from flask import session, redirect, url_for

app = Flask(__name__)
app.secret_key="f5ds7dsadsf7dg68s7d5"

@app.route('/')
def index():
    if 'user' in session:
        return render_template('index.html', user=session['user'])
    return render_template('index.html')


@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pw = request.form['pw']
        if email == "saykin.developer@gmail.com" and pw == "Test1234!":
            print(session)
            session['user'] = email
            return redirect(url_for('index'))
            # return redirect(url_for('shop'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


@app.route('/shop')
def shop():
    print(session)
    context = {'member': 'Nicht-Kunden'}
    if 'user' in session:
        context['member'] = 'Kunden'
    return render_template('shop_member.html', **context)


if __name__ == '__main__':
    app.run(port=4000, debug=True)