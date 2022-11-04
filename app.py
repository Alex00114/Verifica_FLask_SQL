from flask import Flask, render_template, request, send_file, make_response, url_for, Response, redirect
app = Flask(__name__)
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import pymssql
conn = pymssql.connect(server = '213.140.22.237\SQLEXPRESS', user='tag.alessandro', password='xxx123##', database='tag.alessandro')


@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")


@app.route('/bestCustomers', methods=['GET'])
def bestCustomers():
    global dfMiglioriClienti

    query = 'select sales.customers.customer_id, sum(production.products.list_price) as soldi_spesi from sales.customers inner join sales.orders on sales.customers.customer_id = sales.orders.customer_id inner join sales.order_items on sales.orders.order_id = sales.order_items.order_id inner join production.products on sales.order_items.product_id = production.products.product_id group by sales.customers.customer_id order by soldi_spesi desc'
    dfMiglioriClienti = pd.read_sql(query, conn)
    dfMiglioriClienti = dfMiglioriClienti.head(10)
    return render_template('bestCustomers.html', nomiColonne = dfMiglioriClienti.columns.values, dati = list(dfMiglioriClienti.values.tolist()))


@app.route('/listaOrdini', methods=['GET'])
def listaOrdini():
    return render_template('listaOrdini.html')

















if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)