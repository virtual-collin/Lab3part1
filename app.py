import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader.data as web
import datetime
from dateutil.relativedelta import relativedelta

start = datetime.datetime.today() - relativedelta(years=5)
end = datetime.datetime.today()

df = web.DataReader("GE", start=start, end=end, output_format="pandas")
print(df.head())