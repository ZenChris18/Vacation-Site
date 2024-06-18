# PHGetaway - Vacation Spots Management Web App

#### Video Demo:  [URL HERE]

#### Description:
This project is a web application that showcases various vacation spots in the Philippines and also worldwide vacation spots but it isn't the main focus. It loads vacation spot data from a dataset i made and allows users to view details of each spot by clicking on the respective cards. The application has a feature that users can scroll infinitely to fetch more vacation spots as the user scrolls down the page.


### Key Features

- **User Authentication**: Register, login, logout with password hashing.
- **Profile Management**: Update username, change passwords, delete accounts.
- **Spot Management**: Save, remove, view spots.
- **Spot Details**: Fetch descriptions from Wikipedia.
- **Searching**: Search by name or location.
- **Dynamic Loading**: AJAX for loading more spots.
- **Responsive Design**: Optimized for desktop and mobile.


### Libraries Used:
- **beautifulsoup4==4.12.3**
- **Flask==3.0.3**
- **Flask_Login==0.6.3**
- **flask_sqlalchemy==3.1.1**
- **flask_wtf==1.2.1**
- **pandas==2.2.2**
- **Requests==2.32.3**
- **Werkzeug==3.0.3**


### Project Structure:

- **app.py**: The main Flask application file. It contains routes for user authentication, spot management, and profile management. It is the entry point of the application.

- **database.py**: Handles the initialization of the SQLite database and includes functions for inserting users and managing data.

- **models.py**: Defines the SQLAlchemy models for User and SavedSpot, which represent the application's primary data structures.

- **scrape_utils.py**: Contains utility functions for scraping Wikipedia to fetch spot details.

- **templates/**: This directory contains HTML templates for different pages of the application, including index, login, register, profile, saved spots, and spot details.

- **static/**: Includes static files such as CSS and JavaScript used for styling and adding interactivity to the application.

#### javascript files
- **autocomplete.js**: Enhances the search functionality by providing autocomplete suggestions as the user types in the search bar, fetching suggestions based on the current dataset.

- **darkmode.js**: Provides a toggle for dark mode, allowing users to switch between light and dark themes, and remembers the user's preference using localStorage.

- **flash-messages.js**: Automatically removes flash messages from the DOM after a specified timeout to keep the interface clean.

- **phone-screen-layout.js**: Updates the text of navbar links based on the screen width to ensure optimal display on different devices.

- **phone-screen-ph.js**: Adjusts the title text for Philippine-specific pages based on the screen width to maintain clarity on smaller screens.

- **phone-screen.js**: Similar to phone-screen-ph.js, but for worldwide pages, updating the title text based on screen width.

- **scroll-world.js**: Implements infinite scrolling for the worldwide vacation spots, dynamically loading more spots as the user scrolls down.

- **scroll.js**: Implements infinite scrolling for the Philippine vacation spots, similar to scroll-world.js, loading more spots dynamically as the user scrolls down.
### Design Choices:

- **Infinite Scrolling**: Implemented to enhance user experience by loading vacation spots gradually as the user scrolls, reducing initial load time and providing a seamless browsing experience.

- **Fallback Image**: Used a fallback image (`fallback.jpg`) in case the image URL of a vacation spot is invalid or not available, ensuring a consistent user experience even if spot images fail to load.

### Future Enhancements:

- Implementing a backend server to manage and serve vacation spot data more dynamically and securely.
- Adding other people as friends and have chat system and reviews


For a video demonstration of the application, please visit [URL HERE].

### Problems while developing
1. <input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
- took me a long time to make the csrf token work. 
- This hides the csrf token which took me a long time to figure out.

2. Log in and Register
- how to save user data into a database using sqlite3
- took me a long time to implement this feature because there are a lot of things i didn't know at the start


