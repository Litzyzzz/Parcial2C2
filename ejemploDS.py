import pandas as pd
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import DatetimeTickFormatter

datos = pd.read_csv("covid19.csv") #se importan los datos a graficar

output_file("lineasDS.html")#en que archivo queremos que se muestre
datos["Date"] = pd.to_datetime(datos["Date"])#se configura la fecha porque daba error

#se crea el lienzo mediante figure
g = figure(title="Aumento de muertes COVID19",
           x_axis_label="Fechas", y_axis_label="Muertes", x_axis_type="datetime")

# Configura el formato de fechas en el eje X, cuando se le hace zoom
g.xaxis.formatter = DatetimeTickFormatter(
  days="%d/%m/%Y",
  months="%d/%m/%Y", 
  years="%Y"    
)

g.line(datos["Date"].head(20), datos["Deaths"].head(20),
       line_width=2, color='brown')#crea el grafico de lineas

show(g)#muestra la grafica en la web