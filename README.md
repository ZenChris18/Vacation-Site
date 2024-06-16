# Vacation-site
Libraries Used
1. Flask - pip install Flask
2. Flask-Login - pip install Flask-Login
3. SQLAlchemy - pip install SQLAlchemy
4. Flask-WTF - pip install Flask-WTF
5. Flask-WTF CSRFProtect - pip install Flask-WTF
6. requests
7. random
8. pip install requests beautifulsoup4


Added this line of code in the forms login.html and register.html:
<input type="hidden" name="csrf_token" value="{{ csrf_token() }}">

This hides the csrf token which took me a long time to figure out.