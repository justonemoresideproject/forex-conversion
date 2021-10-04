from flask import Flask, request, render_template
from flask.helpers import get_flashed_messages, flash
from forex_python.converter import CurrencyRates

app = Flask(__name__)
app.secret_key = 'definitelynotasecretkey'

c = CurrencyRates()

@app.route('/getRates/<id>')
def front_demo(id):
    r = c.get_rates(id)
    return render_template('base.html', t=r)

@app.route('/')
def front_page():
    return render_template('base.html')

def getOutput(conversionTo, conversionFrom, amount):
    r = c.get_rates(conversionFrom)
    output = r[conversionTo] * float(amount)
    return output
    

@app.route('/get-currency')
def currencyReturn():
    try:
        to = request.args['to']
        comingFrom = request.args['from']
        amount = float(request.args['amount'])
        if(to == comingFrom):
            return render_template('base.html', comingFrom=comingFrom, to=to, amount=amount, output=amount)
        output = getOutput(to, comingFrom, amount)
        return render_template('base.html', comingFrom=comingFrom, to=to, amount=amount, output=output)
    except:
        flash('Not a valid amount')
        Error = True
        return render_template('base.html', Error=Error)
