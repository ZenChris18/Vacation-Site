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

pip install Flask==2.3.2 Flask-Login==0.6.2 Werkzeug==2.3.6 requests beautifulsoup4 numpy pandas matplotlib scikit-learn


This hides the csrf token which took me a long time to figure out.