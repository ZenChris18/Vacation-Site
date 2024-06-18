# Vacation Spots Web App

#### Video Demo:  [URL HERE]

#### Description:
This project is a web application that showcases various vacation spots in the Philippines and also worldwide vacation spots but it isn't the main focus. It loads vacation spot data from a dataset i made and allows users to view details of each spot by clicking on the respective cards. The application has a feature that users can scroll infinitely to fetch more vacation spots as the user scrolls down the page.

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

- **index.html**: Contains the main HTML structure for displaying vacation spots. It includes placeholders for dynamically loaded vacation spot cards and a loading indicator.

- **styles.css**: Defines the styles for the vacation spot cards, layout, and loading indicator to ensure a visually appealing and responsive design.

- **script.js**: Implements the client-side JavaScript logic. It handles fetching vacation spot data from the server via AJAX (using `fetch` API), dynamically creating HTML elements for each spot, and linking each card to its respective details page.

### Design Choices:

- **Infinite Scrolling**: Implemented to enhance user experience by loading vacation spots gradually as the user scrolls, reducing initial load time and providing a seamless browsing experience.

- **Fallback Image**: Used a fallback image (`fallback.jpg`) in case the image URL of a vacation spot is invalid or not available, ensuring a consistent user experience even if spot images fail to load.

### Future Enhancements:

- Implementing a backend server to manage and serve vacation spot data more dynamically and securely.
- Adding user authentication and personalized features such as favorite spots and user reviews.

This project demonstrates the use of modern web development techniques such as asynchronous data loading, responsive design, and progressive enhancement. It aims to provide users with a visually engaging and efficient way to explore vacation spots in the Philippines and if they prefer also worldwide vacation spots.

For a video demonstration of the application, please visit [URL HERE].

### Problems while developing
1. <input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
- took me a long time to make the csrf token work. 
- This hides the csrf token which took me a long time to figure out.

2. Log in and Register
- how to save user data into a database using sqlite3
- took me a long time to implement this feature because there are a lot of things i didn't know at the start
