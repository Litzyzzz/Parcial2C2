
from bokeh.plotting import figure, show, output_file



"""output_file("graficoB.html")#se indica el archivo que se abrirá en la web

nombres = ["Litzy", "Yohana","Blanca", "Katia"]# datos a graficar
edad = [17, 18, 19, 20]

grafico = figure(title="Gráfico de barras", 
                 x_axis_label="Nombres", 
                 y_axis_label="Edades", 
                 x_range=nombres)# Crea la figura (el lienzo donde se dibujará el grafico)

grafico.vbar(x=nombres, top=edad,width=0.4, 
             color=["purple","pink","fuchsia","lavender"])# Dibuja las barras usando los datos

show(grafico)#muestra el grafico en el navegador


"""
output_file("graficoDisp.html")

#datos
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(title="Gráfico de Dispersión", x_axis_label='X', y_axis_label='Y')# Crea figura

p.scatter(x, y, size=10, color="red")#añade los puntos

show(p)# muestra el gráfico"""
