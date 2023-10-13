from project import create_app

app , celery = create_app()
# make the db changes inside application context(if not clery not be able to access the db)
app.app_context().push()