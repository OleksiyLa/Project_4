# Planner App (Task Manager)
The Planner App serves as an extensive task manager, facilitating goal setting, planning, task assignment, and calendar-based scheduling. It empowers users to set goals, strategize essential steps, allocate tasks, and effectively schedule these tasks for goal achievement. Users have the ability to track progress visually by adjusting the status of scheduled tasks, tasks, and goals, enabling a transparent overview of their journey. Additionally, a convenient Kanban board for goals, comprising sections like 'To Do,' 'In Progress,' 'On Hold,' and 'Done,' enhances organizational efficiency and progress visualization.

  - GitHub Repository: https://github.com/OleksiyLa/Project_4
  - Live Project: https://task-manager-planner-app-ca416dc67970.herokuapp.com/

![Goals Board page](./README/images/goals_board.png)

## Planning & Development

### Target audience
  - Students: The Planner App is ideal for students of all ages looking to manage their academic goals, such as completing assignments, preparing for exams, or achieving personal development milestones.

  - Professionals: Career-focused individuals can benefit from the app by setting and tracking career-related objectives, managing projects, and enhancing their time management skills.

  - Entrepreneurs: Entrepreneurs and small business owners can use the app to organize and prioritize their business goals, create action plans, and measure their progress toward success.

  - Goal-Oriented Individuals: Anyone with personal aspirations, whether related to fitness, hobbies, or self-improvement, can harness the Planner App to plan, execute, and monitor their goals effectively.

  - Time Management Enthusiasts: Those interested in improving their time management skills can use the app to schedule tasks, set deadlines, and optimize their daily routines.

  - Productivity Seekers: Individuals seeking to boost their productivity and accomplish more in less time can find value in the app's task management and progress tracking features.

### App Objectives
  - Empower Goal Achievement:
    - Enable users to set and achieve their personal and professional goals effectively. Provide a platform that promotes action and progress toward meaningful objectives.

  - Enhance Time Management:
      - Help users improve their time management skills by scheduling tasks and allocating time for goal-related activities. Foster efficient use of time to maximize productivity and goal accomplishment.

  - Improve Accountability:
    - Encourage users to take ownership of their goals by breaking them down into actionable tasks and to-do lists. Facilitate tracking and monitoring of progress, creating a sense of responsibility for goal outcomes.

  - Foster Versatility:
    - Cater to a diverse user base, including students, professionals, entrepreneurs, and goal-oriented individuals. Offer a user-friendly and intuitive web-based platform accessible from various devices.

  - Encourage Consistency:
    - Cultivate the habit of consistent goal setting and achievement, helping users build a lifelong practice of pursuing their aspirations.

  - Support Self-Improvement:
    - Enable users to not only achieve specific goals but also enhance their personal development, productivity, and time management skills.

  - Deliver Convenience:
    - Provide a convenient and accessible tool for goal planning and tracking that fits seamlessly into users' daily routines.

### Features to be implemented
  - Goal Board: Create your goals in one place.
  - Tasks Cards: Break down your goals into actionable tasks.
  - Task Scheduling: Schedule specific activities and allocate time to achieve your goals effectively.
  - The Calendar dashboard showcases days with scheduled tasks, visually highlighting these specific dates. Users can select a day from the calendar interface to view all tasks scheduled for that particular day, providing a detailed overview of the day's assigned tasks.

### Wireframes

<details><summary>Authentication wireframes</summary>

  ![Mobile wireframe](./README/wireframes/mobile/sign_in.png) ![Mobile wireframe](./README/wireframes/mobile/sign_up.png)
  ![Ipad wireframe](./README/wireframes/tablet/sign_in.png) ![Ipad wireframe](./README/wireframes/tablet/sign_up.png)
  ![Desktop wireframe](./README/wireframes/desktop/sign_in.png) ![Desktop wireframe](./README/wireframes/desktop/sign_up.png)

</details>

<details><summary>Goals Board wireframes</summary>

  ![Mobile wireframe](./README/wireframes/mobile/board.png)
  ![Ipad wireframe](./README/wireframes/tablet/board.png)
  ![Desktop wireframe](./README/wireframes/desktop/board.png)

</details>

<details><summary>Tasks wireframes</summary>

  ![Mobile wireframe](./README/wireframes/mobile/tasks.png)
  ![Ipad wireframe](./README/wireframes/tablet/tasks.png)
  ![Desktop wireframe](./README/wireframes/desktop/tasks.png)

</details>

<details><summary>Calendar wireframes</summary>

  ![Mobile wireframe](./README/wireframes/mobile/calendar.png)
  ![Ipad wireframe](./README/wireframes/tablet/calendar.png)
  ![Desktop wireframe](./README/wireframes/desktop/calendar.png)

</details>

<details><summary>Account wireframes</summary>

  ![Mobile wireframe](./README/wireframes/mobile/account.png)
  ![Ipad wireframe](./README/wireframes/tablet/account.png)
  ![Desktop wireframe](./README/wireframes/desktop/account.png)

</details>

### Models
  - A PostgreSQL SQL database is utilized. Three Django database models have been established, each containing a user field serving as a foreign key connected to the default Django User model.
  - The 'Goal' and 'Task' models maintain a one-to-many relationship, with the 'Task' model possessing a 'goal' field acting as a foreign key referencing the 'Goal' table. Additionally, the 'Task' and 'Scheduled Tasks' tables exhibit a one-to-many relationship, where the 'task' field in the 'ScheduledTask' table is a foreign key associated with the 'Task' model.
  - The 'Goal' model contains the following fields:
    - user: foreign key referencing the default Django User model with cascade deletion
    - title: character field with a maximum length of 50 characters
    - slug: slug field with a maximum length of 200 characters
    - description: text field with a maximum length of 2500 characters
    - status: choice field with the following options: 'ToDo', 'In Progress', 'On Hold' and 'Completed'
    - created_at: date field with a default value of the current date
    - updated_at: date field with a default value of the current date
    - expected_deadline: date field
  - The 'Task' model contains the following fields:
    - user: foreign key referencing the default Django User model with cascade deletion
    - goal: foreign key referencing the 'Goal' model with cascade deletion
    - title: character field with a maximum length of 50 characters
    - slug: slug field with a maximum length of 200 characters
    - description: text field with a maximum length of 2500 characters
    - completed: boolean field with a default value of 'False'
    - created_at: date field with a default value of the current date
  - The 'ScheduledTask' model contains the following fields:
    - user: foreign key referencing the default Django User model with cascade deletion
    - task: foreign key referencing the 'Task' model with cascade deletion
    - slug: slug field with a maximum length of 200 characters
    - date: date field
    - start_time: time field
    - end_time: time field
    - completed: boolean field with a default value of 'False'

![Visual depiction presenting the relational connections among database models, displaying their fields and respective data types](./README/images/task_app_model.png)

### Colors

The chosen color palette represents a deliberate and meticulous selection aimed at fostering an environment of simplicity and comfort for all users. Each color was thoughtfully chosen to maintain a minimalist and visually unobtrusive interface, prioritizing ease of comprehension and user focus within the application.

  - The application utilized the following color palette:
    - #023685: Used as the link color.
    - #000000: Predominantly employed as the text color due to its high contrast.
    - #025702: Designated for marking completed tasks in the calendar.
    - #8B0000: Reserved for tasks yet to be done in the calendar.
    - #eeeeee: Applied to denote today's date in the calendar and when hovering over dates.
    - #DAA520: Designated for highlighting the selected day in the calendar.
    - #ffffff: Utilized for the logo, text panel, and social links.
    - #fafafa: Chosen as the overall background color.
    - #500e86: Allocated for the edit icon.
    - #b10b0b: Designated as the delete icon color.

![Color Pallete](./README/images/color_pallete_1.png)
![Color Pallete](./README/images/color_pallete_2.png)

### Fonts
The project's font selection comprises 'Playfair Display' and 'Roboto'. 'Playfair Display' is designated for the main headings, footer and the navigation menu to evoke a sense of seriousness and visual elegance. 'Roboto' has been incorporated specifically to enhance legibility.

This choice is intended to establish a formal tone and improve readability. The deliberate juxtaposition of 'Playfair Display' and 'Roboto' serves a dual purpose: creating visual distinction and ensuring content clarity within the project's framework.

  - Playfair Display
  - Roboto

### Technologies
  - Framework
    - Django

  - Languages:
    - Python
    - HTML
    - CSS
    - JavaScript
  
  - Databases:
    - PostgreSQL
  
  - Libraries:
    - Bootstrap 5

  - Packages:
    - asgiref - ASGI framework specifications.
    - Beautiful Soup 4 - A Python library for pulling data out of HTML and XML files.
    - certifi - Certificates for Python.
    - cffi - Foreign Function Interface for Python calling C code.
    - charset-normalizer - Python implementation of the WHATWG Encoding standard.
    - crispy-bootstrap5 - Integration of Django Crispy Forms with Bootstrap 5.
    - cryptography - A package designed to expose cryptographic primitives and recipes to Python developers.
    - defusedxml - XML bomb protection for Python stdlib modules.
    - dj-database-url - Django database URL configuration parser.
    - django-allauth - Integrated set of Django applications addressing authentication, registration, account management, as well as 3rd party (social) account authentication.
    - django-bootstrap-v5 - Bootstrap 5 for Django projects.
    - django-crispy-forms - A Django app that lets you easily build, customize, and reuse forms using Bootstrap.
    - gunicorn - A Python WSGI HTTP server for UNIX.
    - idna - Internationalized Domain Names in Applications (IDNA) library.
    - oauthlib - A generic, spec-compliant, thorough implementation of the OAuth request-signing logic.
    - packaging - Core utilities for Python packages.
    - psycopg2 - PostgreSQL adapter for Python.
    - pycparser - C parser in Python.
    - PyJWT - JSON Web Token implementation in Python.
    - python3-openid - Python OpenID library.
    - requests - An elegant and simple HTTP library for Python.
    - requests-oauthlib - OAuthlib authentication support for Requests.
    - soupsieve - A CSS selector library for Python.
    - sqlparse - A non-validating SQL parser for Python.
    - tzdata - Timezone database and utilities.
    - urllib3 - A powerful, user-friendly HTTP client for Python.
    - whitenoise - Simplify serving of static files.

### User Stories
  - User-Friendly Navigation: As a user, I anticipate the app to provide intuitive navigation for effortless movement between its various pages and features.
  - Intuitive Interaction: As a user, I expect the app to provide intuitive interaction, enabling me to effortlessly create, edit, or delete goals and tasks, and seamlessly schedule tasks for efficient management.
  - Goals: As a user I can easily view, create, edit, and track my personal and professional goals on a well-designed dashboard so that I can efficiently monitor my progress, stay motivated, and achieve my desired outcomes.
  - Tasks: As a user I can be able to create tasks related to my goals, access detailed information about each task through task cards or a dedicated details page, and have the ability to delete or edit tasks as needed.
  - Scheduled Tasks: As a user I can schedule tasks and have a visual representation of my scheduled tasks on a calendar, where these tasks are clearly highlighted. I should be able to select a specific day to view the tasks scheduled for that day, and I need the ability to delete or modify these tasks directly from the calendar.
  - Notification of significant actions and errors: As a user I will receive clear and contextual messages, both confirming significant actions and highlighting errors, to ensure that I am aware of the system's status and any potential issues.
  - Authorization and Authentication: As a user, I expect the capability to securely create an account, log in and out as needed, and have exclusive, secure access to view and manage my personal data within the application, without concern about unauthorized access by other users.

### Agile Methotology

In developing my Task Manager App using Django, the implementation of Agile methodology was both a challenge and a guiding framework. As a solo developer navigating a new technology landscape, the Agile principles of adaptability and iterative progress became my cornerstone.

  - Agile Adaptation and Solo Development Challenges:
    - Agile methodologies, inherently designed for team collaboration, presented unique challenges in a solo development environment. Estimating tasks accurately within this framework was intricate, especially while acquainting myself with Django's complexities. The Agile structure demanded constant adaptation, a process complicated by the solitary nature of my work and the nuances of a new technology stack.

  - Transitioning to Sprints with Django's Novelty:
    - Embracing Agile principles initially led me to adopt sprints, yet navigating Django's unfamiliar terrain made estimating task durations a challenge within my limited timeframe. Recognizing the uncertainty, I pivoted towards an adaptable approach. Understanding the unpredictability of future sprints, I chose to prioritize adaptability over rigid planning. This shift allowed me to focus on completing as many tasks as possible within the given time frame, mitigating the uncertainties that came with mastering a new technology like Django.

  - Embracing Iterative Learning in Agile Efficiency:
    -As I delved deeper into Django, my proficiency in estimating tasks and user stories gradually strengthened. This ongoing learning curve notably boosted my ability to forecast and plan effectively. Transitioning away from mere task completion, I honed the skill of precise estimations, steering development toward a more refined and controlled path.

  - Refinement in Agile Sprint Planning:
    - Transitioning from rigid sprint structures, I embraced Agile flexibility, emphasizing task completion over predefined timeframes. This strategic shift allowed me to navigate uncertainties more effectively. Notably, in the project's final phase, my refined estimation process under the Agile umbrella ensured efficient allocation of time, culminating in the successful completion of the Task Manager App.

  - Future Iterations and Agile Integration:
    - Armed with a comprehensive understanding of Django and refined Agile practices, I am poised to integrate Agile principles more seamlessly into future iterations. The adaptive journey within Agile, while initially marked by adjustments and unconventional tactics, has been instrumental in my learning trajectory. My newfound confidence in Django and a strengthened Agile foundation will undoubtedly shape more efficient and structured sprint planning processes in the future.

  - Kanban board: https://github.com/users/OleksiyLa/projects/2

## Features

### Authentication

  - Access to the app begins with a mandatory login or sign-up process. Upon successful authentication, users are redirected to access the app's functionalities, ensuring that only authenticated users can utilize the application.

![Login](./README/features/login.png)

### Goals Board

  - The application experience commences at the goals page, featuring a goal panel with a prominent 'Create Goal' button on the right side. Upon clicking, this button redirects users to a form. After successful form submission, the user is redirected to the goals page where a goal card is generated within the 'ToDo' column, displaying pertinent information from the form. In cases of lengthy text descriptions, the card provides a truncated view, with full content accessible upon clicking the 'Details' link on the card.

  - Clicking the 'Details' link redirects users to the goal details page, offering a comprehensive view of all goal-related data. Both the goal card and details page allow users to edit or delete the goal via respective icons. Additionally, the goal card's status can be altered by clicking appropriate buttons—'In Progress,' 'On Hold,' or 'Done'—clearly denoting the current status in the column header. Reverting the status back to 'ToDo' can be accomplished within the edit form.

  - The goal card or its detailed page features an 'Add Task' button, enabling users to create tasks associated with the respective goal. Upon clicking this button, users can seamlessly create tasks directly linked to the goal, facilitating a streamlined task management process.

![Goals Board](./README/features/goals_board.png)

### Tasks

  - After a user adds a task, a corresponding task panel is generated on the tasks page. Within this panel, positioned on the left side, lies a 'Create Task' button mirroring the functionality available on the goal panel, allowing users to create tasks associated with the goal. Directly beneath this panel is a collapsible 'Goal Title' section. When expanded, it reveals all tasks pertaining to the goal; when collapsed, it conceals the contents. This intuitive feature facilitates seamless navigation through the tasks associated with various goals.

  - The panel content comprises task cards featuring essential details such as the task's creation date, title, description, and a link to access further details. Additionally, each task card includes buttons allowing users to mark the task as complete or schedule it for a specific date.

  - Tasks scheduled for future dates are categorized and displayed within separate sections on the card: 'Scheduled Tasks,' 'Completed Scheduled Tasks,' 'Not Completed Scheduled Tasks,' and 'Failed Scheduled Tasks.' This classification aids users in efficiently tracking and managing scheduled tasks based on their statuses.

  - Within the task card, users can access specific information about 'Scheduled Tasks,' 'Completed Scheduled Tasks,' 'Not Completed Scheduled Tasks,' and 'Failed Scheduled Tasks.' These values dynamically adjust based on associated scheduled tasks, offering users insights into the current status and distribution of tasks directly on the task card.

  - Tasks can be edited or deleted by clicking on the respective icons available on the task card itself or within the details page. This convenient feature allows users to efficiently update or remove tasks as needed, either directly from the card or through the detailed task view.

![Tasks](./README/features/tasks.png)

### Calendar

  - If a task is scheduled, it will be visible and displayed within the calendar on the calendar page. This integration ensures that scheduled tasks are effectively reflected and accessible within the calendar interface. Tasks offer scheduling options to occur on a specific date or within selected weekdays in a defined range. This feature allows users the flexibility to schedule tasks with precision on a particular date or within specific weekdays across a range.

  - The calendar highlights days with scheduled tasks in red and shifts to green once all tasks for that day are completed. Users can select a specific day by clicking on it, causing the selected day to be highlighted in a yellowish shade. Adjacent to the calendar, tasks scheduled for the selected day are displayed in chronological order, offering users a clear view of the day's scheduled tasks.

  - The 'Next' and 'Previous' buttons adjacent to the calendar facilitate navigation to the next or previous month, respectively. Additionally, the 'Today' button conveniently redirects users to the current day, irrespective of the displayed calendar month, providing quick access to the present date.

  - Scheduled tasks can be completed, edited, or deleted. Unlike scheduling, where tasks can be allocated to future dates, scheduled tasks have the flexibility to be edited to past dates if needed. This feature allows users to adjust scheduled tasks as needed, even if the date has passed.

![Calendar](./README/features/calendar.png)

### Authorization

  - Users are authorized to view and modify their own data within the application. Access to data is restricted for other users, ensuring that they cannot obtain or modify information belonging to other users.

### Intuitive design (Good UX)

  - The application's remarkable intuitiveness negates the necessity for elaborate instructions to navigate its features. Its user-friendly interface encompasses a convenient navigation menu, intuitive edit and delete icons, a user-centric Kanban board, calendar integration, and a 'Back' icon within forms. Additionally, the app employs error messages for forms, along with success or warning messages for significant actions, all harmonizing to ensure a seamless user experience.

![Schedule_task_form](./README/features/schedule_task_form.png)

<br>

![Calendar](./README/features/calendar_ipad.png)

### Responsive design

  - The website is responsive and adeptly adjusts its layout across various devices. On smaller screens, a burger menu is featured for general navigation between pages. Additionally, within the goal page, another burger menu facilitates navigation between different columns, offering seamless movement from 'ToDo' to 'Done' sections. This feature ensures that users can easily navigate the goal page, even on smaller screens.

![Mobile](./README/features/goals_board_mobile.jpg)

## Future Features

  - For future enhancements, a statistics page could be incorporated to provide users with comprehensive insights into their overall progress. This feature could showcase trends, detailing achieved goals, failed goals, and other valuable metrics. By offering this data, users can gain valuable insights to enhance and improve their goal achievement.

  - In order to uphold user privacy, an account deletion feature that allows users to delete their accounts along with all associated data can be added. This ensures that users have the option to securely remove their personal information from the system.

  - Exploring the addition of internal logic within the project to automate behavior is recommended. For instance, upon task creation, an automatic transition of the associated goal status to 'in progress' could be initiated. Similarly, upon task completion, an automated removal of all relevant scheduled tasks from the calendar could occur. These automated functionalities aim to streamline user experience and optimize operational efficiency within the project.

  - Exploring the possibility of integrating an automated system to send reminder emails specifically on scheduled task days could be considered as a potential future feature. This strategic approach aims to prompt and encourage users on specific task days, potentially aiding in the timely completion of tasks aligned with their established goals.

  - To enhance user experience, the addition of a 'Forgot Password' link on the login page could be considered. This feature would allow users to reset their passwords by entering their email addresses and receiving a link to initiate the reset process.

  - To maintain dashboard clarity, an archiving mechanism to remove outdated data can be implemented. Archiving outdated data will facilitate a clearer and more concise dashboard interface, ensuring that only relevant information remains visible.

## Testing

### Manual Testing

- __Authentication__

  - Form validation is handled by Django. The following tests were conducted to ensure the authentication process is working as intended.
  - When accessing the website, it automatically redirects to the login page.
    
![Login Page](./README/tests/manual_testing/auth/initial_sign_in.png)
   
  - If incorrect data is submitted in any field, the system displays error messages to indicate the errors. Specifically, an error message highlighted in red appears under each erroneous input field and above the form, just under title, to highlight the mistake.

![Login Page (Password is required)](./README/tests/manual_testing/auth/sign_in_password_required.png)

  - If the user enters an incorrect username or password, the system displays an error message to indicate the error. Specifically, an error message highlighted in red appears above the form, just under title, to highlight the mistake. The system intentionally displays an error message solely below the 'Sign In' title, deliberately omitting specific field-related error messages. This design choice aims to avoid indicating which data entry—username or password—was incorrect.

![Login Page (Password is required)](./README/tests/manual_testing/auth/sign_in_error.png)
    
  - If the user enters the correct username and password, the system redirects to the 'Goals Board' page with the notification message just under the navigation menu.

![Goals Board Logged in](./README/tests/manual_testing/auth/goals_board_signed_in.png)
    
  - If the user clicks the 'Sign Up' link, the system redirects to the 'Sign Up' page.

![Sign Up Form](./README/tests/manual_testing/auth/sign_up_form.png)

  - If the user types incorrect data in any field, the system displays error messages to indicate the errors. Specifically, an error message highlighted in red appears under each erroneous input field and above the form, just under title, to highlight the mistake.

![Sign Up Form](./README/tests/manual_testing/auth/sign_up_error.png)

  - Upon successful registration, the system redirects to the 'Goals Board' page with the notification message just under the navigation menu.

![Goals Board (signed up)](./README/tests/manual_testing/auth/goals_board_signed_up.png)

  - If the user clicks logout at the rigth top corner, the system redirects to the 'Sign Out' page to confirm logout.

![Goals Board (signed up)](./README/tests/manual_testing/auth/sign_out.png)

  - Upon confirmation of logout, the system redirects to the 'Sign In' page with the notification message just under the navigation menu.

![Sign in page after logout](./README/tests/manual_testing/auth/sign_in_after_sign_out.png)

<br>

__Goals Board__
    
  - When the user is signed in, they get to use the Goals Board!

![Goals Board](./README/tests/manual_testing/goals_board/goals_board.png)

  - Let's try it out by creating a goal. Just click the 'Create Goal' button on the goal panel.

![Kanban goal panel](./README/tests/manual_testing/goals_board/goals_board-panel.png)

  - It'll take you to a form where you can set up a new goal.

![Create goal](./README/tests/manual_testing/goals_board/create_goal_datepicker_empty.png)

  - When the user clicks on the datepicker, a calendar will appear, and past dates will be disabled or unavailable for selection.

![Create goal datepicker open](./README/tests/manual_testing/goals_board/create_goal_datepicker_past_dates_unavailable.png)

  - When attempting to submit empty fields, error messages will appear to prompt the user to fill in the required information.

![Empty fields submission create goal](./README/tests/manual_testing/goals_board/create_goal_submit_empty_fields.png)

  - In the event that a user tries to circumvent front-end validation by altering it using the inspector tool and selects a past date in the datepicker, the form will reload, displaying error messages indicating the issue. Additionally, if the content in the textarea is fewer than 20 words, an error will be triggered as well.

![Circumvented front-end validation for past dates and textarea create goal](./README/tests/manual_testing/goals_board/invalid_past_dates_textarea.png)

  - In case a user attempts to bypass front-end validation by adding an unlimited number of words for the title or in the textarea field, error messages will be triggered to prompt adherence to the specified limitations.

![Unlimited title and textarea create goal](./README/tests/manual_testing/goals_board/invalid_create_goal_more_than_required.png)

  - If the user add correct data in all fields, the system redirects to the 'Goals Board' page with the notification message just under the navigation menu and the goal card in ToDo colomn.

![Valid input for create goal](./README/tests/manual_testing/goals_board/valid_create_goal.png)
![Goals Board created goal](./README/tests/manual_testing/goals_board/goal_card_created.png)

  - If the user clicks the "In Progress" button on the goal card, the system redirects to the 'Goals Board' page with the notification message just under the navigation menu and the goal card in In Progress colomn.

![Goal In Progress](./README/tests/manual_testing/goals_board/goal_card_in_progress.png)

  - If the user clicks the "On Hold" button on the goal card, the system redirects to the 'Goals Board' page with the notification message just under the navigation menu and the goal card in On Hold colomn.

![Goal On Hold](./README/tests/manual_testing/goals_board/goal_card_on_hold.png)
    
  - If the user clicks the "Done" button on the goal card, the system redirects to the 'Goals Board' page with the notification message just under the navigation menu and the goal card in Done colomn.

![Goal Done](./README/tests/manual_testing/goals_board/goal_card_done.png)

  - If the user clicks the 'Edit' icon on the goal card, the system redirects to the 'Edit Goal' page.

![Edit goal](./README/tests/manual_testing/goals_board/edit_goal.png)

  - Edit goal form is pre-populated with the goal data and it has the same validation as the create goal form apart from the status field. The status field is a choice field and it has the same value as the status of the goal card.

![Edit goal status](./README/tests/manual_testing/goals_board/edit_goal_status.png)

  - If the user circumvent front end validation by altering it using the inspector tool and modifies the value of the status field that does not exist and submits the form, the system will reload the form and display an error message indicating the issue.

![Edit goal status done](./README/tests/manual_testing/goals_board/edit_goal_status_done.png)
![Edit goal status error](./README/tests/manual_testing/goals_board/edit_goal_status_error.png)

  - If the user edit the goal and add correct data in all fields, the system redirects to the 'Goals Board' page with the notification message just under the navigation menu and the goal card with updated data.

![Updated goal card](./README/tests/manual_testing/goals_board/updated_goal_card.png)

  - If the user clicks the Details link on the goal card, the system redirects to the 'Goal Details' page.

![Goal details](./README/tests/manual_testing/goals_board/goal_details.png)

  - If the user clicks the 'Edit' icon on the goal details page, the system redirects to the 'Edit Goal' page.

  - If the user clicks the 'Delete' icon on the goal details page, the confirmation modal will appear.

![Delete modal from details](./README/tests/manual_testing/goals_board/delete_from_details_modal.png)

  - If the user clicks the 'Cancel' button on the confirmation modal, the system redirects to the 'Goal Details' page.
  - If the user clicks the 'Confirm' button on the confirmation modal, the system redirects to the 'Goals Board' page with the notification message just under the navigation menu and the goal card is deleted.

![Deleted card from details](./README/tests/manual_testing/goals_board/delete_from_details_modal.png)

  - If the user clicks the 'Delete' icon on the goal card, the confirmation modal will appear.

![Delete modal from Goals Board](./README/tests/manual_testing/goals_board/delete_from_goals_board_modal.png)

  - If the user clicks the 'Confirm' button on the confirmation modal, the system redirects to the 'Goals Board' page with the notification message just under the navigation menu and the goal card is deleted.

![Deleted from Goals Board](./README/tests/manual_testing/goals_board/deleted_from_goals_board.png)

<br>

- __Tasks__

  - If the user clicks the 'Tasks' link on the navigation menu, the system redirects to the 'Tasks' page.

  ![No tasks](./README/tests/manual_testing/tasks/tasks_no_tasks.png)

  - The user can create a task by clicking the 'Add Task' button on the goal card on the 'Goals' page.

  ![Goals page, add task](./README/tests/manual_testing/tasks/add_task_goal_board.png)

  - When the user clicks the 'Add Task' button, the system redirects to the 'Add Task' form.

  ![Add task form](./README/tests/manual_testing/tasks/add_task_form.png)

  - If the user submits the form with empty fields, the system displays error messages to indicate the errors. Specifically, an error message highlighted in red appears under each erroneous input field and above the form, just under title, to highlight the mistake.

  !['Add Task' form, empty field validation image](./README/tests/manual_testing/tasks/add_task_form_empty_fields.png)

  - If the user circumvent front end validation by altering it using the inspector tool and removes maximum input validation the user will be able to add unlimited amount of text.

  !['Add Task' form, max validation image](./README/tests/manual_testing/tasks/add_task_form_max_input_validation.png)

  - If the user circumvent front end validation by altering it using the inspector tool and removes minimum input validation and add less text than required.

  !['Add Task' form, min validation image](./README/tests/manual_testing/tasks/add_task_form_min_input_validation.png)

  - When the user submits the correct data, they will be redirected to the Tasks page. Here, a task panel corresponding to the entered goal will be generated, displaying a task card beneath the panel.

![Created task](./README/tests/manual_testing/tasks/tasks_created.png)

  - If the user clicks the 'Edit' icon on the task card, the system redirects to the 'Edit Task' page with the pre-populated form. The form has the same validation as the create task form but an additional field "complete".

![Created task](./README/tests/manual_testing/tasks/edit_task_card.png)

  - If the user updates values in the form and submits it, the system redirects to the 'Tasks' page with the notification message just under the navigation menu and the task card is updated.

![Updated task](./README/tests/manual_testing/tasks/edit_task_updated.png)
![Updated task](./README/tests/manual_testing/tasks/edited_task.png)

  - If the user clicks the 'Details' link on the task card, the system redirects to the 'Task Details' page.

![Task details](./README/tests/manual_testing/tasks/task_details.png)

  - If the user clicks the 'Complete' button on the task card or details page, the system redirects to the 'Tasks' page with the notification message just under the navigation menu and the task card is completed and changed color to green.

![Task complete](./README/tests/manual_testing/tasks/task_completed.png)

  - In details page the user can click the 'Uncomplete' button which redirects the user  to the 'Tasks' page with the notification message just under the navigation menu and the task card is not completed and changed color to the original one.

![Task uncomplete](./README/tests/manual_testing/tasks/task_uncomplete.png)
![Task uncompleted](./README/tests/manual_testing/tasks/task_uncompleted.png)

  - When the user clicks on the goal title under the task panel, it will toggle the task card container. If the cards were open, they will hide; if hidden, they will display. Additionally, the toggle icon will change to its opposite state. This functionality proves convenient for users managing numerous tasks, enabling them to focus on one goal at a time or easily locate specific tasks by closing irrelevant ones.

![Task panels closed and open](./README/tests/manual_testing/tasks/task_closed_open.png)

  - If the user clicks the 'Delete' icon on the task card, the confirmation modal will appear.

![Delete modal](./README/tests/manual_testing/tasks/task_delete_modal.png)


  - If the user confirms the deletion, the system redirects to the 'Tasks' page with the notification message just under the navigation menu and the task card is deleted.

![Task deleted](./README/tests/manual_testing/tasks/task_deleted.png)

<br>

- __Calendar__
  - If the user clicks the 'Calendar' link on the navigation menu, the system redirects to the 'Calendar' page where the user can see the calendar with the current month, year and current day higlighted.
  
![Calendar page](./README/tests/manual_testing/calendar/calendar_no_tasks.png)

  - To schedule a task the user needs to click schedule button on the task card on the 'Tasks' page or on the 'Details' page. The system will redirect to the 'Schedule Task' page.
  
![Schedule task](./README/tests/manual_testing/calendar/schedule_task_form.png)

  - If the user submits fields with empty values, the system will display error messages to indicate the errors. Specifically, an error message highlighted in red appears under each erroneous input field and above the form, just under title, to highlight the mistake.

![Schedule task empty fields](./README/tests/manual_testing/calendar/schedule_task_empty.png)

  - If the user add end time is earlier than start time, the system will display error messages to indicate the errors. Specifically, an error message appears above the form, just under title, to highlight the mistake.

![Schedule task end time earlier than start time](./README/tests/manual_testing/calendar/schedule_task_time_error.png)

  - if the user add end date is earlier than start date, the system will display error messages to indicate the errors. Specifically, an error message highlighted in red appears under each erroneous input field and above the form, just under title, to highlight the mistake.

![Schedule task end date earlier than start date](./README/tests/manual_testing/calendar/schedule_task_end_date.png)

  - In the event that a user attempts to schedule tasks beyond the range limit, set at 365 days, error messages will be prominently displayed under the title section and below the end date field, notifying the user of the limit violation.

![Schedule task beyond range](./README/tests/manual_testing/calendar/schedule_above_range_limit.png)

  - If the user add correct data including optional end date but forgets to check at least one weekday, an error message will appear.

![Schedule task no weekdays](./README/tests/manual_testing/calendar/schedule_task_weekday.png) 
  
  - If the user add correct data including optional end date and check at least one weekday, the system will redirect to the 'Calendar' page with the notification message just under the navigation menu and the tasks are scheduled within the date range and weekdays selected. If scheduled tasks are over deadline, the warning will appear to notify the user how many tasks are over deadline.

![Schedule tasks over deadline](./README/tests/manual_testing/calendar/calendar_tasks_over_deadline.png)

  - To see the scheduled task for the next month, the user needs to click the 'Next' button on the calendar. The 'Calendar' switch to the next month.

![Schedule tasks next month](./README/tests/manual_testing/calendar/scheduled_tasks_next_month.png)

  - If the user will not select end date, the system will schedule the task for the exact date only.

![Schedule task form, no end date](./README/tests/manual_testing/calendar/schedule_task.png)
![Schedule tas in calend](./README/tests/manual_testing/calendar/scheduled_task.png)

  - If the user clicks the specific date in the caledandar, the date will be selected, higlighted and the tasks scheduled for that date will be displayed next to the calendar.
  - If the user clicks the complete button in the calendar, the scheduled task will be marked as completed and the color of the text will change to green and delete icon will dissapear.

![Selected date and completed task](./README/tests/manual_testing/calendar/completed_task.png)

  - All completed scheduled tasks will be displayed in the calendar with the green color.

![Completed scheduled tasks](./README/tests/manual_testing/calendar/completed_task_green.png)

  - To edit scheduled task the user needs to click the 'Edit' icon on the scheduled task card. The system will redirect to the 'Edit Scheduled Task' form.

![Edit scheduled task form](./README/tests/manual_testing/calendar/edit_scheduled_task.png)

  - The edit scheduled task form adheres to the same validation rules as the 'Schedule Task' form, with the exception of allowing modifications to past dates. If the user adjusts the date and time in a manner resulting in task overlap with existing ones, an error message will promptly notify the user about the conflict.

![Edit scheduled task form, conflicting tasks](./README/tests/manual_testing/calendar/edit_task_overlaps.png)
![Schedule task form overlaps](./README/tests/manual_testing/calendar/schedule_tasks_ovelaps.png)

  - The calendar will be visible only when the user's data is successfully fetched. In the absence of fetched data due to a network error, a loader will be displayed instead of the calendar.

![Calendar data fetched](./README/tests/manual_testing/calendar/data_fetched.png)
![Calendar data not fetched](./README/tests/manual_testing/calendar/data_not_fetched.png)

  - If the user clicks the 'Delete' icon on the scheduled task card, the confirmation modal will appear. If the user clicks the 'Confirm' button on the confirmation modal, the system redirects to the 'Calendar' page with the notification message just under the navigation menu and the scheduled task is deleted.

![Delete scheduled task modal](./README/tests/manual_testing/calendar/delete_scheduled_task_modal.png)
![Delete scheduled task](./README/tests/manual_testing/calendar/deleted_scheduled_task.png)

  - Multiple scheduled tasks can occur on the same day if they do not conflict with each other. These tasks will be showcased in the calendar in chronological order.

![Several scheduled tasks](./README/tests/manual_testing/calendar/scheduled_tasks_in_order.png)

  - Deleting the 'Go to The Gym' task will result in the deletion of all scheduled tasks associated with that specific goal. However, tasks such as 'Run' and others unrelated to the deleted goal will remain unaffected

![Cascade delete task](./README/tests/manual_testing/calendar/deleted_task_removes_scheduled.png)
![Cascade scheduled task deleted](./README/tests/manual_testing/calendar/shceduled_tasks_deleted_task_deleted.png)

  - When a user deletes a goal, all associated tasks, including scheduled tasks, will be deleted as part of this action.

![Cascade delete goal](./README/tests/manual_testing/calendar/deleted_goal.png)
![Cascade delete goal](./README/tests/manual_testing/calendar/empty_task_goal_deletion.png)

<br>

- __Authorization__

  - To assess authorization, attempts were made to access the app's goals, tasks, calendar, and edit page without logging in. When unauthenticated, users are automatically redirected to the login page.

![Unauthorized access](./README/tests/manual_testing/authorization/sign_in.png)

  - Upon creating two distinct accounts, users observe that data associated with one account remains inaccessible to the other.

![Unauthorized access](./README/tests/manual_testing/authorization/one_account.png)
![Unauthorized access](./README/tests/manual_testing/authorization/another_account.png)

  - Furthermore, any attempt by a user to access the edit or detail page of an account from another account results in a redirection to the 'Not Found' page.

![Unauthorized access](./README/tests/manual_testing/authorization/edit_goal_one_account.png)
![Unauthorized access](./README/tests/manual_testing/authorization/redirect_edit_of_another_account.png)

  - Similarly, if a user attempts to access the edit or detail page of a goal or task that does not exist, the system redirects to the 'Not Found' page.

<br>

- __Data displayed correctly__

  - When a user creates a goal, the initial values displayed on the goal card for 'Tasks' and 'Tasks to Complete' will be zero. Upon adding two tasks, these numbers will be updated accordingly on the goal card. As tasks are completed, the user will observe the count change, indicating the total tasks and those remaining to complete.

![Data displayed correctly](./README/tests/manual_testing/correct_data/details.png)
![Data displayed correctly](./README/tests/manual_testing/correct_data/tasks.png)
![Data displayed correctly](./README/tests/manual_testing/correct_data/goal_card_two_tasks.png)
![Data displayed correctly](./README/tests/manual_testing/correct_data/tasks_one_completed.png)
![Data displayed correctly](./README/tests/manual_testing/correct_data/goal_details_task_completed.png)


  - When all tasks associated with a goal are completed, the user can view specific details showcasing the number of tasks and their completion status. Additionally, the goal card and details section undergo a color change, turning green to signify successful goal achievement.

![Data displayed correctly](./README/tests/manual_testing/correct_data/goal_card_all_tasks_completed.png)

  - When a user schedules 40 tasks for 'Go to the gym' goal, editing one task to be in the past while marking it incomplete, and completing six others, the task card will reflect the following values: Total tasks - 40, Completed tasks - 6, and Failed tasks - 1.

![Data displayed correctly](./README/tests/manual_testing/correct_data/scheduled_6_completed.png)
![Data displayed correctly](./README/tests/manual_testing/correct_data/tasks_6_completed.png)

<br>

- __Responsiveness__

  - The burger menu for the goal panel is designed to activate when the width reaches 1199 pixels, while the navigation burger menu activates at 575 pixels. Both burger menus function as intended, displaying the necessary navigation content.

![Responsiveness](./README/tests/manual_testing/rensponsiveness/goal_panel_burger.png)
![Responsiveness](./README/tests/manual_testing/rensponsiveness/nav_burger.png)

  - The navigation links within the burger menu function correctly, seamlessly directing users to the selected pages. In the goal panel, the links appropriately scroll users to the relevant goal categories.

<br>

- __404 page__

  - When a user attempts to access a page that does not exist, the system redirects to the 'Not Found' page.

- __Navigation__

  - The navigation menu is visible on all pages, allowing users to seamlessly navigate between pages. The navigation menu is responsive, featuring a burger menu on smaller screens. The burger menu functions as intended, displaying the necessary navigation content.

- __Footer__

  - When a user clicks the social links in the footer, the system opens a new tab to the respective social media pages.

### Testing User Stories

- User-Friendly Navigation: As a user, I anticipate the app to provide intuitive navigation for effortless movement between its various pages and features.
  - The navigation menu is visible on all pages, allowing users to seamlessly navigate between pages. The navigation menu is responsive, featuring a burger menu on smaller screens. The burger menu functions as intended, displaying the necessary navigation content.

- Intuitive Interaction: As a user, I expect the app to provide intuitive interaction, enabling me to effortlessly create, edit, or delete goals and tasks, and seamlessly schedule tasks for efficient management.
  - The application's remarkable intuitiveness negates the necessity for elaborate instructions to navigate its features. Its user-friendly interface encompasses a convenient navigation menu, intuitive edit and delete icons, a user-centric Kanban board, calendar integration, and a 'Back' icon within forms. Additionally, the app employs error messages for forms, along with success or warning messages for significant actions, all harmonizing to ensure a seamless user experience.

- Goals: As a user I can easily view, create, edit, and track my personal and professional goals on a well-designed dashboard so that I can efficiently monitor my progress, stay motivated, and achieve my desired outcomes.
  - The application experience commences at the goals page, featuring a goal panel with a prominent 'Create Goal' button on the right side. Upon clicking, this button redirects users to a form. After successful form submission, the user is redirected to the goals page where a goal card is generated within the 'ToDo' column, displaying pertinent information from the form. In cases of lengthy text descriptions, the card provides a truncated view, with full content accessible upon clicking the 'Details' link on the card. The goal card also features an edit and delete icon, allowing users to seamlessly edit or delete goals as needed. Additionally, the goal card's status can be altered by clicking appropriate buttons—'In Progress,' 'On Hold,' or 'Done'—clearly denoting the current status in the column header. Reverting the status back to 'ToDo' can be accomplished within the edit form.

- Tasks: As a user I can be able to create tasks related to my goals, access detailed information about each task through task cards or a dedicated details page, and have the ability to delete or edit tasks as needed.
  - After a user adds a task, a corresponding task panel is generated on the tasks page. Within this panel, positioned on the left side, lies a 'Create Task' button mirroring the functionality available on the goal panel, allowing users to create tasks associated with the goal. Directly beneath this panel is a collapsible 'Goal Title' section. When expanded, it reveals all tasks pertaining to the goal; when collapsed, it conceals the contents. This intuitive feature facilitates seamless navigation through the tasks associated with various goals. The panel content comprises task cards featuring essential details such as the task's creation date, title, description, and a link to access further details. Additionally, each task card includes buttons allowing users to mark the task as complete or schedule it for a specific date. Tasks scheduled for future dates are categorized and displayed within separate sections on the card: 'Scheduled Tasks,' 'Completed Scheduled Tasks,' 'Not Completed Scheduled Tasks,' and 'Failed Scheduled Tasks.' This classification aids users in efficiently tracking and managing scheduled tasks based on their statuses. Within the task card, users can access specific information about 'Scheduled Tasks,' 'Completed Scheduled Tasks,' 'Not Completed Scheduled Tasks,' and 'Failed Scheduled Tasks.' These values dynamically adjust based on associated scheduled tasks, offering users insights into the current status and distribution of tasks directly on the task card. Tasks can be edited or deleted by clicking on the respective icons available on the task card itself or within the details page. This convenient feature allows users to efficiently update or remove tasks as needed, either directly from the card or through the detailed task view.

- Scheduled Tasks: As a user I can schedule tasks and have a visual representation of my scheduled tasks on a calendar, where these tasks are clearly highlighted. I should be able to select a specific day to view the tasks scheduled for that day, and I need the ability to delete or modify these tasks directly from the calendar.
  - If a task is scheduled, it will be visible and displayed within the calendar on the calendar page. This integration ensures that scheduled tasks are effectively reflected and accessible within the calendar interface. Tasks offer scheduling options to occur on a specific date or within selected weekdays in a defined range. This feature allows users the flexibility to schedule tasks with precision on a particular date or within specific weekdays across a range. The calendar highlights days with scheduled tasks in red and shifts to green once all tasks for that day are completed. Users can select a specific day by clicking on it, causing the selected day to be highlighted in a yellowish shade. Adjacent to the calendar, tasks scheduled for the selected day are displayed in chronological order, offering users a clear view of the day's scheduled tasks. The 'Next' and 'Previous' buttons adjacent to the calendar facilitate navigation to the next or previous month, respectively. Additionally, the 'Today' button conveniently redirects users to the current day, irrespective of the displayed calendar month, providing quick access to the present date. Scheduled tasks can be completed, edited, or deleted. Unlike scheduling, where tasks can be allocated to future dates, scheduled tasks have the flexibility to be edited to past dates if needed. This feature allows users to adjust scheduled tasks as needed, even if the date has passed.

- Notification of significant actions and errors: As a user I will receive clear and contextual messages, both confirming significant actions and highlighting errors, to ensure that I am aware of the system's status and any potential issues.
  - The application ensures a seamless user experience through error messages for form submissions and success or warning messages for significant actions. It prompts users to fill required fields, detects and flags issues such as past dates in date pickers or insufficient words in text areas, and enforces input limitations. Error notifications prominently appear for empty fields, input errors, date/time mismatches, or when task scheduling limits are exceeded. Successful submissions redirect users to relevant pages, such as the 'Goals Board' or 'Calendar,' accompanied by a success message informing the user. Form validations include error notifications for conflicts, while confirmation modals redirect users to the respective pages for task or goal deletion.

- Authorization and Authentication: As a user, I expect the capability to securely create an account, log in and out as needed, and have exclusive, secure access to view and manage my personal data within the application, without concern about unauthorized access by other users.
  - To assess authorization, attempts were made to access the app's goals, tasks, calendar, and edit page without logging in. When unauthenticated, users are automatically redirected to the login page. Upon creating two distinct accounts, users observe that data associated with one account remains inaccessible to the other. Furthermore, any attempt by a user to access the edit or detail page of an account from another account results in a redirection to the 'Not Found' page. Similarly, if a user attempts to access the edit or detail page of a goal or task that does not exist, the system redirects to the 'Not Found' page.

### LightHouse Testing
  
  - The following LightHouse tests were conducted to ensure the application's performance, accessibility, best practices, and SEO are optimized. The tests were conducted on the deployed application. Each result is at least 90% or higher.

<details><summary>Login</summary>

  ![Login Ligthouse](./README/tests/lighthouse/login.png)

</details>

<details><summary>Goals (mobile and desktop)</summary>

  ![Goals Ligthouse mobile](./README/tests/lighthouse/goals.png)
  ![Goals Ligthouse](./README/tests/lighthouse/goals_desktop.png)

</details>

<details><summary>Tasks (mobile and desktop)</summary>

  ![Tasks Ligthouse mobile](./README/tests/lighthouse/tasks.png)
  ![Tasks Ligthouse](./README/tests/lighthouse/tasks_desktop.png)

</details>

<details><summary>Calendar (mobile and desktop)</summary>

  ![Calendar Ligthouse mobile](./README/tests/lighthouse/calendar.png)
  ![Calendar Ligthouse](./README/tests/lighthouse/calendar_desktop.png)

</details>

### Python PEP8 Validation

  - The Python PEP8 validation tests were performed to assess the adherence of the application's Python code to the PEP8 style guide. These tests were executed on the deployed application, and no errors were detected.

<details><summary>Views validation</summary>

  ![PEP8 Views](./README/tests/pep8/views.png)

</details>

<details><summary>Models validation</summary>

  ![PEP8 Models](./README/tests/pep8/models.png)

</details>

<details><summary>Forms validation</summary>

  ![PEP8 Forms](./README/tests/pep8/forms.png)

</details>

<details><summary>Urls validation</summary>

  ![PEP8 Urls](./README/tests/pep8/urls.png)

</details>

### HTML Validation
  
  - All HTML files have been validated using the W3C HTML Validator, with no errors or warnings found.

<details><summary>Login, Sign Up, Logout</summary>

  ![W3C HTML Validation](./README/tests/html/login.png)
  ![W3C HTML Validation](./README/tests/html/logout.png)
  ![W3C HTML Validation](./README/tests/html/sign_up.png)

</details>

<details><summary>Goals, goal detail, create goal, edit goal</summary>

  ![W3C HTML Validation](./README/tests/html/goal_board.png)
  ![W3C HTML Validation](./README/tests/html/goal_detail.png)
  ![W3C HTML Validation](./README/tests/html/edit_goal.png)
  ![W3C HTML Validation](./README/tests/html/create_goal.png)

</details>


<details><summary>Tasks, task details, edit task, add task</summary>

  ![W3C HTML Validation](./README/tests/html/tasks.png)
  ![W3C HTML Validation](./README/tests/html/task_detail.png)
  ![W3C HTML Validation](./README/tests/html/edit_task.png)
  ![W3C HTML Validation](./README/tests/html/add_task.png)

</details>

<details><summary>Calendar, Schedule tasks, Edit Scheduled task</summary>

  ![W3C HTML Validation](./README/tests/html/calendar.png)
  ![W3C HTML Validation](./README/tests/html/schedule_form.png)
  ![W3C HTML Validation](./README/tests/html/edit_scheduled_task.png)

</details>

<details><summary>Page Not Found</summary>

  ![W3C HTML Validation](./README/tests/html/404.png)

</details>

### W3C CSS Validator (Jigsaw)
  
  - The CSS code has been validated using the W3C CSS Validator (Jigsaw), and no errors were found.

<details><summary>W3C CSS Validator (Jigsaw) results</summary>

  ![W3C CSS Validation](./README/tests/css/w3c_validated.png)

</details>

### JSHint JavaScript Validator

The JavaScript file has been validated using the JSHint JavaScript Validator, and no errors were detected but there was a warning "Functions declared within loops referencing an outer scoped variable may lead to confusing semantics. (index)."

  - The calendar.js file has been validated using the JSHint JavaScript Validator, and no errors were detected."

<details><summary>Validation for calendar.js</summary>

  ![JSHint JavaScript Validator](./README/tests/js/calendar.js.png)

</details>

  - The 'index.js' file underwent validation using the JSHint JavaScript Validator, resulting in no errors being detected. However, a warning regarding the 'undefined' variable 'bootstrap' was flagged, which pertains to a Bootstrap 5 variable utilized within the project's context. To verify, I logged the variable's value using the console.log function. Upon inspection in the inspector tool, it was evident that the variable holds the 'bootstrap' object.

<details><summary>Validation for index.js</summary>

  ![JSHint JavaScript Validator](./README/tests/js/index.js.png)
  ![JSHint JavaScript Validator](./README/tests/js/log_bootsrap.png)
  ![JSHint JavaScript Validator](./README/tests/js/log_results.png)

</details>

## Code Refactoring Opportunities

  - When considering future improvements, it's advantageous to refactor the view.py file by standardizing the implementation, opting for either class-based or function-based views. This intentional effort will significantly enhance the overall consistency of the codebase.

  - Future improvement involves a refactor of the schedule_task view to streamline its structure. Strategies aimed at modularizing the codebase, eliminating redundancies, and enhancing code readability could yield substantial enhancements.

![Schedule_task_view](./README/images/schedule_task_view.png)

## Bugs
  - On a mobile device, accessing the burger menu from the goal panel and selecting a specific category, such as 'In Progress,' smoothly navigates the user to the corresponding column. However, an issue arises where the selected column slightly obstructs the view of the first card, impacting the user experience a bit. This issue is not present on larger screens.

<details><summary>Goal Panel Navigation</summary>

  ![Goal Panel Navigation](./README/bugs/goal_panel_nav_progress_open.jpg)
  ![Goal Panel Navigation](./README/bugs/goal_panel_nav_progress_closed.jpg)

</details>

  - For enhanced user experience, displaying the complete column title would be beneficial to ensure users are aware that they've navigated to the correct column after selecting a category from the Goal Panel Navigation in the goal panel on a mobile device.

<details><summary>Goal Panel Navigation</summary>

![Goal Panel Navigation](./README/bugs/goal_panel_nav_progress.jpg)

</details>

## Deployment
  - The Task Manager App was deployed to Heroku using the following steps:
    - Create a virtual environment and install Django.
      - python -m venv myenv
      - myenv\Scripts\activate
      - Install Django using pip install Django
    - Create a project and app.
      - django-admin startproject project_name
      - cd project_name
      - python manage.py startapp app_name
    - Heroku setup
      - Log in to Heroku or create an account if required.
      - Click "Create new app".
      - Select the relevant region.
      - Enter a unique app name.
      - Click "Create app".
    - Update Django settings for Heroku.
      - Ensure DEBUG is set to False.
      - Update ALLOWED_HOSTS to include your Heroku app's domain.
      - Update the DATABASES configuration to use dj_database_url for the Heroku PostgreSQL database.
      - Add logic for Heroku-specific configurations, e.g., handling static files.
    - Install dependencies.
    - Prepare requirements file.
      - Use pip3 freeze > requirements.txt to generate a requirements.txt file listing the Python dependencies for your project.
    - Create a Procfile.
      - Create a Procfile to declare what commands are run by your app's dynos on the Heroku platform. For example, for a Django project, it might contain: web: gunicorn your_app_name.wsgi.
    - Push project to GitHub.
      - Push your project to a GitHub repository.
    - Configure environment variables.
      - Scroll down to the "Config Vars" section.
      - Click "Reveal Config Vars".
      - Add the following environment variables:
      - DATABASE_URL: Link to your PostgreSQL database.
      - PORT: Set the value to 8000.
      - SECRET_KEY: Set the Django secret key for your application.
    - Set buildpack.
      - Scroll down to the buildpacks section of the settings page.
      - Click "Add buildpack".
      -  Select "Python" and save changes.
    - Deployment configuration.
      - Navigate to the "Deploy" tab.
      -  Connect your Heroku app to the GitHub repository containing your project.
      -  Choose the branch to deploy.
    - Deploy to Heroku.
      - Trigger the deployment process in Heroku either manually or set up automatic deployments.
      -  Initiate the deployment process in Heroku.
      -  Monitor the build logs to ensure successful deployment
    - Access live application.
      - Once deployed, click "View" in Heroku to access your live application.

## Credits

### Content
- The Roboto and Playfair Display fonts were obtained from Google Fonts: https://fonts.google.com

### Media
- All SVG icons, including the favicon, were sourced from FontAwesome and Bootstrap icons: 
    - https://fontawesome.com
    - https://icons.getbootstrap.com/

### Frameworks and Libraries
- Django Docs: https://docs.djangoproject.com/en/4.2/
- Bootsrap5: https://getbootstrap.com/docs/5.3/getting-started/introduction/

### README
- The color palette images featured in the README was sourced from the website http://colormind.io/
- The text content in the README was composed with the assistance of ChatGPT: https://chat.openai.com
- The validation image for HTML were captured from: https://validator.w3.org/
- The validation image for CSS were captured from: https://jigsaw.w3.org/css-validator/
- The validation image for JS were captured from: https://jshint.com/
- The validation image for Python were captured from: https://pep8ci.herokuapp.com/#
- Database model image was created with the assistance of Draw Sql: https://drawsql.app/
