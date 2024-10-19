from flask import Blueprint, render_template, request, redirect, flash
from models import Student, db

student_bp = Blueprint('student_bp', __name__)

@student_bp.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        student_id = request.form['student_id']
        gpa = request.form['gpa']
        consistency = request.form['consistency']
        core_gpa = request.form['core_gpa']
        local_hackathons = request.form['local_hackathons']
        national_hackathons = request.form['national_hackathons']
        paper_presentations = request.form['paper_presentations']
        peer_assistance = request.form['peer_assistance']

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
        db.session.add(new_student)
        db.session.commit()
        flash('Student added successfully!')
        return redirect('/')

    return render_template('add_student.html')
