from flask import Flask
from flask import render_template
from flask import request
from flask import session, redirect, url_for

app = Flask(__name__)
app.secret_key="12345123451234512345"


@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pw = request.form['pw']
        if email == "marius.wang@sunzinet.com" and pw == "Test123!":
            print(session)
            session['user'] = email
            return redirect(url_for('shop'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


@app.route('/shop')
def shop():
    if 'user' in session:
        return render_template('shop_member.html', member="Kunden")
    else:
        return render_template('shop_member.html', member="Nichtkunden")


if __name__ == '__main__':
    app.run(port=4000, debug=True)

