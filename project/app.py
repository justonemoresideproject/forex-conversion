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
    currency = c.get_rates('USD')
    return render_template('base.html', currency = currency)

def getOutput(conversionTo, conversionFrom, amount):
    if conversionTo == conversionFrom:
        return round(amount, 2)
    r = c.get_rates(conversionFrom)
    output = r[conversionTo] * float(amount)
    return round(output, 2)
    

@app.route('/get-currency')
def currencyReturn():
    currency = c.get_rates('USD')
    try:
        to = request.args['to']
        comingFrom = request.args['from']
        amount = round(float(request.args['amount']), 2)

        # if(to == comingFrom):
        #     return render_template('base.html', comingFrom=comingFrom, to=to, amount=amount, output=amount)

        output = getOutput(to, comingFrom, amount)

        return render_template('base.html', comingFrom=comingFrom, to=to, amount=amount, output=output, currency=currency)
    except:
        flash('Not a valid amount')
        Error = True
        return render_template('base.html', Error=Error, currency=currency)
