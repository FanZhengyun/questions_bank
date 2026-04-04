from flask import Blueprint, render_template, redirect, url_for, flash, request
from app import db
from app.models import Question
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

bp = Blueprint('main', __name__)

class QuestionForm(FlaskForm):
    text = TextAreaField('题目内容', validators=[DataRequired(), Length(min=5)])
    answer = StringField('答案', validators=[DataRequired(), Length(max=200)])
    explanation = TextAreaField('解析', validators=[Length(max=500)])
    difficulty = SelectField('难度', choices=[('easy', '简单'), ('medium', '中等'), ('hard', '困难')], default='medium')
    submit = SubmitField('提交')

@bp.route('/')
def index():
    questions = Question.query.order_by(Question.created_at.desc()).all()
    return render_template('index.html', questions=questions)

@bp.route('/question/<int:id>')
def view_question(id):
    q = Question.query.get_or_404(id)
    return render_template('view_question.html', question=q)

@bp.route('/question/new', methods=['GET', 'POST'])
def new_question():
    form = QuestionForm()
    if form.validate_on_submit():
        q = Question(
            text=form.text.data,
            answer=form.answer.data,
            explanation=form.explanation.data,
            difficulty=form.difficulty.data
        )
        db.session.add(q)
        db.session.commit()
        flash('题目已添加', 'success')
        return redirect(url_for('main.index'))
    return render_template('question_form.html', form=form, title='添加题目')

@bp.route('/question/<int:id>/edit', methods=['GET', 'POST'])
def edit_question(id):
    q = Question.query.get_or_404(id)
    form = QuestionForm(obj=q)
    if form.validate_on_submit():
        q.text = form.text.data
        q.answer = form.answer.data
        q.explanation = form.explanation.data
        q.difficulty = form.difficulty.data
        db.session.commit()
        flash('题目已更新', 'success')
        return redirect(url_for('main.view_question', id=q.id))
    return render_template('question_form.html', form=form, title='编辑题目')

@bp.route('/question/<int:id>/delete', methods=['POST'])
def delete_question(id):
    q = Question.query.get_or_404(id)
    db.session.delete(q)
    db.session.commit()
    flash('题目已删除', 'success')
    return redirect(url_for('main.index'))