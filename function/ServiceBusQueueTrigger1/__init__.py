# This folder will contains the Azure function code.

# Note:

# - Before deploying, be sure to update your requirements.txt file by running `pip freeze > requirements.txt`
# - Known issue, the python package `psycopg2` does not work directly in Azure; install `psycopg2-binary` instead to use the `psycopg2` library in Azure

# The skelton of the `__init__.py` file will consist of the following logic:


import os
import logging
import azure.functions as func
import psycopg2
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail



def main(msg: func.ServiceBusMessage):
    
    try:

        notification_id = int(msg.get_body().decode('utf-8'))
        logging.info(
            'Python ServiceBus queue trigger processed message: %s', notification_id)

        # TODO: Get connection to database
        db_conn = psycopg2.connect(host="", database="techconfdb", user="azuredbuser", password="george")

        # Open a cursor to perform database operations
        with db_conn.cursor() as cur:

            # TODO: Get notification message and subject from database using the notification_id
            notification = cur.execute(
                "SELECT message, subject FROM public.notification WHERE id = %s", (notification_id,))

            # TODO: Get attendees email and name
            cur.execute(
                "SELECT email, first_name, last_name FROM public.attendee")
            row = cur.fetchall()
            # TODO: Loop through each attendee and send an email with a personalized subject
            # for attendee in attendees:
            #     subject = '{}: {}'.format(
            #         attendee.first_name, notification.subject)
            #     send_mail(attendee.email, subject, notification.message)

            # TODO: Update the notification table by setting the completed date and updating the status with the total number of attendees notified
            c_date = datetime.today()
            count_attendees =len(row)
            cur.execute("UPDATE public.notification SET completed_date = %s, status = %s WHERE id = %s", (c_date, 'Notified {} attendees'.format(count_attendees), notification_id,))
            # Commit the databases changes
            db_conn.commit()        

    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(f"message error {error}")
    finally:
        # TODO: Close connection       
        db_conn.close()
        logging.info("Closed ...")


def send_email(email, subject, body):
    if not app.config.get('SENDGRID_API_KEY'):
        message = Mail(
            from_email=app.config.get('ADMIN_EMAIL_ADDRESS'),
            to_emails=email,
            subject=subject,
            plain_text_content=body)

        sg = SendGridAPIClient(app.config.get('SENDGRID_API_KEY'))
        sg.send(message)
