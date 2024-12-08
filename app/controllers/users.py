from flask import Blueprint, render_template
from flask_login import login_required, current_user

user_bp = Blueprint('users', __name__, url_prefix='/users')


@user_bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.is_admin():
        return render_template('dashboard.html', admin=True)
    return render_template('dashboard.html', admin=False)
