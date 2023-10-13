from flask import Blueprint , render_template , redirect
from .forms import MyForm
from .task_execution import db_add

# initialize the blueprint for add_user fucntionality
add_user_bp = Blueprint( "add_user" , __name__ , 
                        template_folder= "templates" )

#define basic route
@add_user_bp.route("/")
def index():
    return "This is add_user function"

@add_user_bp.route("/form" , methods=['GET','POST']  )
def submit():
    form = MyForm()
    #validate data
    if form.validate_on_submit():
        print("Form Data :", form.data)
        #call the db execution using celery background processes
        task_id = db_add.delay(form.data)
        return render_template('cancel.html', task=task_id)

    return render_template('form.html',form = form)

@add_user_bp.route("/cancel/<task_id>")
def cancel_task(task_id):
    task = db_add.AsyncResult(task_id)
    task.abort()
    return 'Task Execusion Canceled ..'
