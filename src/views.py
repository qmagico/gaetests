#coding: utf-8
import sys
import os
from google.appengine.api.taskqueue.taskqueue import TaskRetryOptions
from util import write_template
import logging
from google.appengine.api import taskqueue
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))

import webapp2


NO_RETRY = TaskRetryOptions(task_retry_limit=0)


class MainPage(webapp2.RequestHandler):
    def get(self):
        data = {}
        write_template(self, 'index.html', data)


class EnqueueTaskDapau(webapp2.RequestHandler):
    def get(self):
        taskqueue.add(
            url='/task_dapau',
            queue_name='DEFAULT',
            retry_options=NO_RETRY
        )


class TaskDapau(webapp2.RequestHandler):
    def get(self):
        logging.warning('Vai dar pau')
        raise BaseException('Deu pau :-)')

    def post(self):
        return self.get()


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/enqueue_dapau', EnqueueTaskDapau),
    ('/task_dapau', TaskDapau),
], debug=True)