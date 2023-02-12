from flask import Flask, render_template, request
import json,requests,csv
from csv import DictReader

app = Flask(__name__)

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
my_dict = data[0]
rates = my_dict['rates']

@app.route("/", methods=["GET", "POST"])
def convert():
    result = None
    if request.method == "POST":
        amount = request.form['amount']
        currency_code = request.form['currency_code']
        for rate in rates:
            if rate['code'] == currency_code:
                result = round(float((rate['ask']))* float(amount), 2)

        return render_template("home.html", amount = amount, currency_code = currency_code, result = result)
    
    else:
        
        return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)

