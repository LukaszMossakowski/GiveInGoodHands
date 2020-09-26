# Give in good hands - donation app

### Python web application prepared to maintain database with functionalities typical for logistic website

## Table of contents

* [General info](#general-info)
* [Technologies](#technologies)
* [Screenshots](#screenshots)
* [Status](#status)

## General info

The app was created as my second individual project prepared as part of Portfolio Lab at Coders Lab after 3 months Python Developer course in Coders Lab IT school. The main aim was to sum up and develope skills in Django, JavaScript and many others.

The Medicine Registration application allows:

* for administrator (superuser):
    * add, modify and delete specialisations available in the medical center with picture field (list of available specialisations is presented with loaded pictures 
        and descriptions in the website)
    * add, modify and delete medical staff available in the medical center with picture field (list of available medical staff with related specialisations is presented 
        with loaded pictures and descriptions in the website)
    * add, modify and delete groups of users - [view screenshot]
    * add and delete realtions between registered users, groups of users and medical specialisations (medical staff exists as related group of registered users)
    * add, modify and delete available terms of appointments for every doctor (with appropriate date and time of appointment) - the dedicated view also presents information 
         whether particular term is reserved and information about related user tied with the appointment in case the amdinistrator would like to modify or delete the term - the date and time fields are equiped with set of validations enabling the proper data as for example: beginning time can not occure after the ending time, the date 
         can not occure as previous in comparison with the present date, two appointments to the same doctor can not occure in the same date and time - [view screenshot 1] [view screenshot 2]
    * view list of opinions send by users/patients with information about related user, doctor and appointment - (pagination was applied)

* for user/patient:
   * create user profile
   * login/logout
   * make appointment with chosen doctor in desired term (current and future terms with status: unreserved are listed only) - [view screenshot](./img_readme/user_make_appointment_view.png) 
   * list all appointments made by the request user to particular doctor (with date and time) divided into previous and future appointments also with functionality to cancel the reserved terms - [view screenshot](./img_readme/user_my_appointments_view.png)
   * create opinion related with the appropriate appointment (appointments)


## Technologies

* Bootstrap 4
* Python 3.8.3
* Django
* JavaScript (AJAX, jQuery, JSON)
* pytest-django, psycopq2-binary, pytz, six, envfile
* postgres
* IDE (PyCharm)

The application bases on the database created in the postgres. The app was created in Django and JS with many different technics applied: AJAX, jQuery and JsonRequest in practice submit action via JavaScript to Django, contact form with emailing to users with admin status (SMTP method), custom user model and login by email not my username, activation user profile via personal unique link send by email to a new user (SMTP method), custom delete method preventing deletion of the last admin, set of functionalities as 'forgot your password', 'set new password' and following, aggregate and annotate methods in practice, creating forms, models and views (generic and straight classic views and generic forms with applied widgets), custom password unique validation methods.

## Screenshots

![sikorka](./img_readme/1_landing_page.png)
![admin_manage_term_view_screenshot](./img_readme/2_aggregate_annotate.png)
![admin_manage_term_view_screenshot]
![admin_delete_term_view_screenshot]
![user_main_view_screenshot]
![user_doctor_view_screenshot]
![user_specialisation_view_screenshot]
![user_make_appointment_view_screenshot]
![user_my_appointments_view_screenshot]


## Status

The project is _in progress_. The next step in planned development of the application is to develop JS functionality :)
