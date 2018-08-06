![Superbly Great][logo]

[logo]: https://i.imgur.com/UvmBiv1.png "Superbly Great"

# superbly
## Superbly Great Private Messaging System (Core)

This is a private messaging Django app that gives users the ability to chat with
other users in a fast and secure way, giving the users 100% privacy by adding
features that deletes all messages in one-click!

You can signup by just adding a username and password, entering the captcha answer
and you can chat away for free. Using ONLY, a username and a password.

The app doesn't ask these information:
- Email addresses.
- First name or Last names.
- Home addresses.
- Or, any other personal info.

To install:
1. First, download this project and extract to your local computer.
2. Check for these app modules:
  - authentication (all views are located inside the 'views' folder, and all
  templates are located inside the 'templates' folder).
  - friends
  - menu
  - messaging
  - sgcommapp (which the models.py is located for the project).
  - SuperblyGreat (which includes settings, urls, etc).

Note: Don't forget to add '__init__.py' on every module and views or it will never work.

3. The database has its own captcha data samples. But, it's better to just copy
the captcha sample data to your newly created db.sqlite3 project using a database
browser or manager and exporting it as CSV, then reimporting it.

Note: If you don't have a database manager, you could download the free
DB Browser for SQLite online using Google Search.

4. Next, go to the folder where you extracted the zip file. Then, install these Python requirements by using 'pip install'
on the command prompt:
  - django (2.0.2 or later)
  - reportlab

Note: You will need Python 3+, or the latest Python version.

5. After installing the required modules, go to the command prompt and type: $python manage.py runserver.
It will tell to open your web browser and type: '127.0.0.1:8000' in the address bar and load it.
You will see the Superbly Great logo, signup and login.

Hooray!

I hope you would consider trying out the app and feel free to modify it and add
more features that will suit your needs. By opening the source code, I hope that it
will spark your creativity and bring life to a flourishing community.

So, let your imagination fly!

Thank You!

Sincerely,
Fernando

