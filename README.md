![Superbly Great][logo]

[logo]: https://i.imgur.com/UvmBiv1.png "Superbly Great"

# superbly
## Superbly Great Private Messaging System
Website: [Superbly Great](https://www.superblygreat.com "Superbly Great")

Note: Not all features reflected on the live website. Source code here on Github is much feature rich and updated.

Other Website: [Superbly Great Info](http://www.superblygreat.info "Superbly Great Info") Information on how you can benefit from this.

This is a private messaging Django app that gives users the ability to chat with
other users in a fast and secure way, giving the users 100% privacy by adding
features that deletes all messages in one-click!

Other special use cases:
- Corporate or SMB internal communique. More secure than email.
- Technical support chat system. For businesses that communicate directly at customers.
- Your own messaging website. You can just upload this to your server or free hosting site and have your own FB.
- As developers, you can extend and add features like photo sharing, video sharing, and more!
- This is also ideal for kids for they don't need to get an email address and they don't have to put in their names, home addresses, or phone numbers.

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

Well Done!

Important Note: If you are going to use superbly for production, please refer to this Django link: [Django Deployment Checklist](https://docs.djangoproject.com/en/2.1/howto/deployment/checklist "Django Deployment Checklist") 

An Open Letter

You know nowadays there is no more privacy. Big companies know everything about you, but you don't
know anything about them. Can they be trusted? Maybe not since we read the news that these employees 
go out-of-bounds and use your data for nefarious purposes and stalking women online and it's scary.
We cannot control social media from those powers beyond ourselves, that is why we need and our duty
to stand up against intrusions into our lives and protect our freedom. We need to build a social
network based on the foundation of these freedoms, promote privacy and enjoy our lives connecting
to our dearest friends and families, holding ourselves accountable for their freedom, for we are
a society built on trust.

"I have planted a seed, you must do your part and make it grow."

-Fernando
