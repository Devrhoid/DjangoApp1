======
Polls
=====

Polls is a simple Django app to conduct Web-based polls. For each question, visitors can choose between a fixed number of answers. 

DEtailed documentationis in the docs directory.

Quick start
_____________

1. Add "polls" to your INSTALLED_APPS setting in the setting.py file of your project like this:

INSTALLED_APPS = (
...
'polls',
)

2. Include the polls URLconf in your project urls.py like this::

    url(r'^polls/',include('polls.urls')),

3. Run 'python manage.py syncdb' to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
to create a polls (you'll need the admin app enabled)

5. Visit http://127.0.0.1:8000/polls/ to participate in the poll
