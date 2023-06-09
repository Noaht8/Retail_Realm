from flask import redirect, render_template, url_for, flash, request
from shop import db, app
from .models import Brand, Category
from .forms import AddProducts
import secrets

@app.route('/addbrand', methods=['GET','POST'])
def addbrand():
    if request.method == "POST":
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        db.session.commit()
        flash(f'The Brand {getbrand} has been added to your database', 'success')
        return redirect(url_for('addbrand'))

    return render_template('products/addbrand.html', brands='brands')


@app.route('/addcat', methods=['GET','POST'])
def addcat():
    if request.method == "POST":
        getcat = request.form.get('category')
        cat = Category(name=getcat)
        db.session.add(cat)
        db.session.commit()
        flash(f'The Category {getcat} has been added to your database', 'success')
        return redirect(url_for('addcat'))

    return render_template('products/addbrand.html')


""" @app.route('/updatecat/<int:id>', methods=['GET','POST'])
def updatecat(id):
    if 'email' not in session:
        flash(f'Please login first', 'danger')
    updatecat = Category.query.get_or_404(id)
    category = request.form.get('category')
    if request.method == "POST":
        updatecat.name = category
        flash(f'Your category has been updated', 'success')
        db.session.commit()
        return redirect(url_for('category'))
    return render_template('products/updatebrand.html', title='Update Category Page', updatecat=updatecat) """


@app.route('/addproduct', methods=['POST','GET'])
def addproduct():
    brands = Brand.query.all()
    categories = Category.query.all()
    form = AddProducts(request.form)
    return render_template('products/addproduct.html', form=form, title="Add product", brands=brands, categories=categories)