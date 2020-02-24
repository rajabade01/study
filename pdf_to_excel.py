import pandas as pd
#import tabula
import tabula
import camelot
from camelot import read_pdf
file = "arabic.pdf"
#camelot.read_pdf(file)
#df = wrapper.read_pdf(file)
tables = read_pdf(file, pages='1-end')
path = 'enter your directory path here'  + file
df = tabula.read_pdf(file, pages = '1', multiple_tables = True)
tabula.convert_into(file, "output.csv", output_format="csv")
df[1].values

print(df)
