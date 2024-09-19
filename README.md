# Flowify

**Interactive web-based algorithm visualizer.**  
**Contributors**: Aryn and Aaditya

## Project Idea

Flowify is an interactive web-based algorithm visualizer that enables users to explore and understand various algorithms through dynamic visual representations. Developed using Python for the backend, React for the frontend, and MySQL for the database, this tool allows for real-time interaction with algorithms, providing an engaging learning experience.

## Objectives

1. **Develop a Visualizer for Multiple Algorithms**: Support various algorithms, including sorting algorithms (e.g., QuickSort, MergeSort) and graph algorithms (e.g., Dijkstra’s algorithm, A* search).
2. **Interactive User Interface**: Provide an intuitive and responsive interface for users to interact with algorithms, start and stop visualizations, and adjust parameters.
3. **Real-time Data Handling**: Handle algorithm execution on the backend and update the frontend in real-time to reflect the algorithm's progress.
4. **Database Management**: Use MySQL to store user preferences, visualization settings, and historical data related to algorithm execution.

## System Flow

- **Frontend**: React app communicating with Django through REST APIs and WebSockets for real-time updates.
- **Backend**: Django handling the logic, algorithm processing, and serving data from MySQL.
- **Database**: MySQL for user data storage and additional data storage.

## Main Features

1. **User Authentication**: Users can register and log in using a username and password.
2. **Dashboard**: Access to previous logs, account updates (change password, delete account), and algorithm visualizations.
3. **Algorithm Visualization**: Enter custom data, view the algorithm's code, and interact with the visual representation.
4. **Future Features**: Potential implementation of start, stop, previous, and speed control features once initial functionality is complete.

## Additional Features

1. **Dynamic Code View**: Users can view dynamic code for algorithms in C++ and Python, with changes reflecting user input.
2. **Activity Logs**: View previous activity logs, including values entered and algorithms used, stored in the database for easy retrieval.

## Getting Started

### Setting Up the Project

1. **Creating a Git Repository**
   - Initialize a Git repository for the project.

2. **Creating a Sample Django App**
   - Set up a new Django project within the backend folder.

3. **Setting Up a Sample React App**
   - Initialize a React app within the frontend folder.

4. **Connecting Django and React (Testing)**
   - Set up API endpoints in Django.
   - Use Axios or Fetch in React to make requests to Django.
   - Test data exchange between frontend and backend.

5. **Setting Up the Database**
   - Configure the database connection in Django’s settings.

6. **Creating Dashboard, Login, and Register Pages**
   - Develop login and registration pages in React.
   - Implement authentication logic in Django.
   - Create the dashboard to display user-specific content.

7. **Building the User Portal**
   - Create a portal for users to view logs, update account information, and access features.

8. **Gathering and Understanding Algorithms**
   - Research and prepare algorithms for visualization.
   - Design UI components for algorithm representation.

9. **Building the UI for Algorithm Visualization**
   - Develop React components for visualizing algorithms.
   - Implement interactive features for algorithm control.

10. **Adding Algorithms**
    - Start with the first algorithm visualizer.
    - Use it as a template for adding more algorithms.

## Technologies Used

- **Backend**:
  - Python
  - Django
  - Django REST Framework (DRF)

- **Frontend**:
  - React
  - React Router
  - Redux or Context API
  - D3.js, Three.js, or Plotly
  - Bootstrap or Material-UI

- **Database**:
  - MySQL

## Database Requirements

### User Table
- `user_id` (INT, PRIMARY KEY, AUTO_INCREMENT)
- `username` (VARCHAR, UNIQUE, NOT NULL)
- `password_hash` (VARCHAR, NOT NULL)
- `created_at` (DATETIME, NOT NULL, DEFAULT CURRENT_TIMESTAMP)
- `last_login` (DATETIME, NULLABLE)
- `account_deleted` (BOOLEAN, NOT NULL, DEFAULT FALSE)

### Logs Table
- `log_id` (INT, PRIMARY KEY, AUTO_INCREMENT)
- `user_id` (INT, FOREIGN KEY REFERENCES User(user_id))
- `log_name` (VARCHAR, NOT NULL)
- `algorithm_name` (VARCHAR, NULLABLE)
- `algorithm_data` (TEXT, NULLABLE)
- `created_at` (DATETIME, NOT NULL, DEFAULT CURRENT_TIMESTAMP)

## Design

### Basic Structure
- Implement a user-friendly interface for algorithm visualization.
- Ensure real-time updates and responsive design.

Feel free to explore, contribute, and enhance Flowify!
