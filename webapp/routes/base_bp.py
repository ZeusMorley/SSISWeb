from flask import Blueprint, render_template, flash

base_bp = Blueprint('base', __name__)

@base_bp.route('/')
def base_page():
    return render_template("base.html")