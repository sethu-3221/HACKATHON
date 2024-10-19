from flask import Flask, render_template, request, redirect, session, url_for, flash
from models import Student  # Assuming you have a Student model defined
from database.db_connection import db_session  # Setup your database connection here

app = Flask(__name__)
app.secret_key = 'super_secret_key'  # Required for session management

# Dummy admin credentials for example purposes
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password123"

# Home route
@app.route('/')
def home():
    return render_template('index.html')  # Main HTML page

# Admin login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Authenticate admin credentials
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['logged_in'] = True
            flash('Login successful!')
            return redirect(url_for('add_student_form'))
        else:
            flash('Invalid credentials, try again.')
            return redirect(url_for('login'))
    
    return render_template('login.html')

# Admin logout route
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Logged out successfully.')
    return redirect(url_for('home'))

# Form for adding student results (only accessible if logged in as admin)
@app.route('/add_student', methods=['GET', 'POST'])
def add_student_form():
    if 'logged_in' in session:
        if request.method == 'POST':
            # Extract data from the form
            student_id = request.form['student_id']
            gpa = request.form['gpa']
            consistency = request.form['consistency']
            core_gpa = request.form['core_gpa']
            local_hackathons = request.form['local_hackathons']
            national_hackathons = request.form['national_hackathons']
            paper_presentations = request.form['paper_presentations']
            peer_assistance = request.form['peer_assistance']
            
            # Add student data to the database (simplified example)
            new_student = Student(
                student_id=student_id,
                gpa=gpa,
                consistency=consistency,
                core_gpa=core_gpa,
                local_hackathons=local_hackathons,
                national_hackathons=national_hackathons,
                paper_presentations=paper_presentations,
                peer_assistance=peer_assistance
            )
            db_session.add(new_student)
            db_session.commit()

            flash('Student added successfully!')
            return redirect(url_for('add_student_form'))

        return render_template('add_student.html')
    else:
        flash('You need to log in as an administrator to access this page.')
        return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
