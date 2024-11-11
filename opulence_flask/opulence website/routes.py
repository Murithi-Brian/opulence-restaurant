from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from models import Reservation  # Import your Reservation model
from app import db  # Import your database instance
 
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/gallery')
def gallery():
    return render_template('gallery.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/menu')
def menu():
    return render_template('menu.html')

@main.route('/reservation', methods=['GET', 'POST'])
@login_required
def reservation():
    if request.method == 'POST':
        name = request.form.get('name')
        date = request.form.get('date')
        
        # Create a new reservation instance
        reservation = Reservation(name=name, date=date, user_id=current_user.id)
        
        # Add the reservation to the database
        db.session.add(reservation)
        db.session.commit()
        
        flash('Reservation submitted successfully!', 'success')
        return redirect(url_for('main.reservation'))
    
    return render_template('reservation.html')