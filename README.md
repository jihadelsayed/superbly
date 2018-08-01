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
1. First, create a Django project.
2. Add these app modules:
  - authentication (all views are located inside the 'views' folder, and all
  templates are located inside the 'templates' folder).
  - friends
  - menu
  - messaging
  - sgcommapp (which the models.py is located for the project).
  Note: Don't forget to add '__init__.py' on every module and views.
3. The database has its own captcha data samples. But, it's better to just copy
the captcha sample data to your newly created db.sqlite3 project using a database
browser or manager and exporting it as CSV, then reimporting it.

Note: If you don't have a database manager, you could download the free
DB Browser for SQLite online using Google Search.

I hope you would consider trying out the app and feel free to modify it and add
more features that suit your needs. By opening the source code, I hope that it
will spark your creativity and bring life to a flourishing community.

So, let your imagination fly!

Thank You!

Sincerely,
Fernando

