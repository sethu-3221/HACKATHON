from flask import Blueprint, render_template, request, redirect, session, flash, url_for
from models import Admin, db
from werkzeug.security import check_password_hash

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        admin = Admin.query.filter_by(username=username).first()

        if admin and check_password_hash(admin.password_hash, password):
            session['admin_logged_in'] = True
            flash('Login successful!')
            return redirect(url_for('student_bp.add_student'))
        else:
            flash('Invalid credentials')
            return redirect(url_for('admin_bp.login'))
    
    return render_template('login.html')

@admin_bp.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    flash('Logged out successfully!')
    return redirect(url_for('admin_bp.login'))
