from flask import Flask, render_template, request, redirect, url_for
import sys
sys.path.append('./data')
app= Flask(__name__)
import data

@app.route("/",methods =['GET','POST'])
def home():
    ProductosRecomendados = []
    if request.method == 'POST':


        raiting =request.form['raiting']
        category =request.form['category']
        subcategory =request.form['sub_category']
        if(category=='Select the category:'):
            error="The category is required"
            return render_template('home.html',error = error)

 
        h=data.ReadData(int(category),int(subcategory),int(raiting))
        print(h.ProductosRecomendados)
        print(request.form)
        ProductosRecomendados = h.ProductosRecomendados

        return render_template('recommendations.html', Products=ProductosRecomendados)
    return render_template('home.html')


@app.route("/matchs")
def matchs():
    
    
    return render_template('recommendations.html', )
