from .extensions import db
from .database_schema import User
import time 
from celery import shared_task
from celery.contrib.abortable  import AbortableTask

#perform user add into the database
@shared_task(bind=True , base=AbortableTask)
def db_add(self, form_data):

    # add user
    db.session.add( User(name=form_data['name']) )
    # commit the db
    db.session.commit()

    # create expensive operation
    for i in range(10):
        print("Run Stage : {}",i)
        time.sleep(1)
        if self.is_aborted():
            return 'Task Stopped ...'
    
    return "DB Updated ..."