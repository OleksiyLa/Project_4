# Planner App (Task Manager)
The Planner App is a game-changer for anyone looking to set and achieve their goals. This web-based platform is designed to simplify the goal-setting process. It allows you to create, prioritize, and break down your goals into manageable tasks, while also providing the flexibility to schedule your activities. Plus, with in-depth goal statistics, you'll gain a clear view of your achievements and areas for improvement. Whether you're a student, professional, or goal-oriented individual, this app is your pathway to success.

![Am I responsive, login](./README/web_site_images/responsive_login.png)
![Goals Board page](./README/web_site_images/goals_board.png)

## Planning & Development
- __Target audience__
    - Students: The Planner App is ideal for students of all ages looking to manage their academic goals, such as completing assignments, preparing for exams, or achieving personal development milestones.

    - Professionals: Career-focused individuals can benefit from the app by setting and tracking career-related objectives, managing projects, and enhancing their time management skills.

    - Entrepreneurs: Entrepreneurs and small business owners can use the app to organize and prioritize their business goals, create action plans, and measure their progress toward success.

    - Goal-Oriented Individuals: Anyone with personal aspirations, whether related to fitness, hobbies, or self-improvement, can harness the Planner App to plan, execute, and monitor their goals effectively.

    - Time Management Enthusiasts: Those interested in improving their time management skills can use the app to schedule tasks, set deadlines, and optimize their daily routines.

    - Productivity Seekers: Individuals seeking to boost their productivity and accomplish more in less time can find value in the app's task management and progress tracking features.

- __App Objectives__
    - Empower Goal Achievement:
        - Enable users to set, prioritize, and achieve their personal and professional goals effectively. Provide a platform that promotes action and progress toward meaningful objectives.

    - Enhance Time Management:
        - Help users improve their time management skills by scheduling tasks and allocating time for goal-related activities. Foster efficient use of time to maximize productivity and goal accomplishment.

    - Improve Accountability:
        - Encourage users to take ownership of their goals by breaking them down into actionable tasks and to-do lists. Facilitate tracking and monitoring of progress, creating a sense of responsibility for goal outcomes.

    - Provide Valuable Insights:
        - Offer goal statistics and data-driven feedback to help users gain a realistic view of their achievements and areas for improvement. Enable users to make data-informed decisions about their goals and time allocation.

    - Foster Versatility:
        - Cater to a diverse user base, including students, professionals, entrepreneurs, and goal-oriented individuals. Offer a user-friendly and intuitive web-based platform accessible from various devices.

    - Encourage Consistency:
        - Cultivate the habit of consistent goal setting and achievement, helping users build a lifelong practice of pursuing their aspirations.

    - Support Self-Improvement:
        - Enable users to not only achieve specific goals but also enhance their personal development, productivity, and time management skills.

    - Deliver Convenience:
        - Provide a convenient and accessible tool for goal planning and tracking that fits seamlessly into users' daily routines.

- __User Stories__
  - Task Management
    - As a user, I want to break down my goals into actionable tasks and create to-do lists, allowing me to plan the steps needed to achieve my goals.
  - Progress Tracking
    - As a user, I want to track my progress on each goal, so I can stay motivated and ensure I'm making consistent strides toward achieving my objectives.
  - Time Management
    - As a user, I want to be able to schedule specific activities and allocate time to work on my goals, helping me manage my time effectively.
  - Goal Statistics
    - As a user, I want to see statistics on goals achieved and those that were not, giving me insights into my performance and areas for improvement.
  - Versatile User Base
    - As a user, I want the app to cater to different types of goals, whether they are academic, career-related, personal, or hobby-related.
  - Convenience and Accessibility
    - As a user, I want to be able to access the app from various devices through a web-based platform, ensuring convenience and flexibility in managing my goals.
  - Cultivating Consistency
    - As a user, I want the app to encourage consistency in my goal-setting and achievement, helping me establish a habit of pursuing my aspirations.
  - Personal Development
    - As a user, I want the app to not only help me achieve specific goals but also support my personal development, productivity, and time management skills.

- __Features to be implemented__
  - Goal Board: Create and prioritize your goals in one place.
  - Todo Lists: Break down your goals into actionable tasks and to-do lists.
  - Progress Tracking: Monitor your progress towards each goal.
  - Time Management: Schedule specific activities and allocate time to achieve your goals effectively.
  - Goal Statistics: Gain insights with statistics on achieved and missed goals.

- __Wireframes__

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

- __Models__
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

- __Colors__

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

- __Fonts__
The project's font selection comprises 'Playfair Display' and 'Roboto'. 'Playfair Display' is designated for the main headings, footer and the navigation menu to evoke a sense of seriousness and visual elegance. 'Roboto' has been incorporated specifically to enhance legibility.

This choice is intended to establish a formal tone and improve readability. The deliberate juxtaposition of 'Playfair Display' and 'Roboto' serves a dual purpose: creating visual distinction and ensuring content clarity within the project's framework.

  - Playfair Display
  - Roboto

- __Technologies__
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
    - Font Awesome
    - Google Fonts
    - Django Crispy Forms
    - Django Allauth
    - Django Extensions
    - Gunicorn
    - Psycopg2
    - Whitenoise

- __Agile Methotology__

In developing my Task Manager App using Django, the implementation of Agile methodology was both a challenge and a guiding framework. As a solo developer navigating a new technology landscape, the Agile principles of adaptability and iterative progress became my cornerstone.

  - Agile Adaptation and Solo Development Challenges:
    - Agile methodologies, inherently designed for team collaboration, presented unique challenges in a solo development environment. Estimating tasks accurately within this framework was intricate, especially while acquainting myself with Django's complexities. The Agile structure demanded constant adaptation, a process complicated by the solitary nature of my work and the nuances of a new technology stack.

  - Strategic Sprint Adjustments and Agile Principles:
    - To align Agile principles with my solo development needs, I adopted an adaptive approach. Initially, I found myself frequently refining the structure of sprints due to the novelty of Django. However, as I progressed, the need for caution and strategic planning became apparent. While traditional Agile discourages mid-sprint changes, I maximized efforts on high-priority tasks, deviating to manage uncertainties arising from a new technology landscape.

  - Iterative Learning and Agile Efficiency:
    - As my proficiency in Django improved, so did my grasp of task estimations. This iterative learning process allowed me to plan subsequent sprints with greater precision. Evolving beyond mere task completion, I ensured a more nuanced and controlled development process. Agile, as a guiding philosophy, encouraged adaptability in my approach, fostering continuous improvement and efficiency in task estimation and project planning.

  - Refinement in Agile Sprint Planning:
    - Transitioning from rigid sprint structures, I embraced Agile flexibility, emphasizing task completion over predefined timeframes. This strategic shift allowed me to navigate uncertainties more effectively. Notably, in the project's final phase, my refined estimation process under the Agile umbrella ensured efficient allocation of time, culminating in the successful completion of the Task Manager App.

  - Future Iterations and Agile Integration:
    - Armed with a comprehensive understanding of Django and refined Agile practices, I am poised to integrate Agile principles more seamlessly into future iterations. The adaptive journey within Agile, while initially marked by adjustments and unconventional tactics, has been instrumental in my learning trajectory. My newfound confidence in Django and a strengthened Agile foundation will undoubtedly shape more efficient and structured sprint planning processes in future iterations of the Task Manager App.

  - Kanban board: https://github.com/users/OleksiyLa/projects/2

## Features

## Future Features

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

  - When the user clicks on the goal tile under the task panel, it will toggle the task card container. If the cards were open, they will hide; if hidden, they will display. Additionally, the toggle icon will change to its opposite state. This functionality proves convenient for users managing numerous tasks, enabling them to focus on one goal at a time or easily locate specific tasks by closing irrelevant ones.

![Task panel closed](./README/tests/manual_testing/tasks/task_panel_closed.png)


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
![Data displayed correctly](./README/tests/manual_testing/correct_data/goal_details_task_completed.png)


  - When all tasks associated with a goal are completed, the user can view specific details showcasing the number of tasks and their completion status. Additionally, the goal card and details section undergo a color change, turning green to signify successful goal achievement.

![Data displayed correctly](./README/tests/manual_testing/correct_data/goal_card_all_tasks_completed.png)

  - When a user schedules 40 tasks, editing one task to be in the past while marking it incomplete, and completing six others, the task card will reflect the following values: Total tasks - 40, Completed tasks - 6, and Failed tasks - 1.

![Data displayed correctly](./README/tests/manual_testing/correct_data/scheduled_6_completed.png)
![Data displayed correctly](./README/tests/manual_testing/correct_data/tasks_6_completed.png)

<br>

- __Responsiveness__


<br>

## Bugs

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
