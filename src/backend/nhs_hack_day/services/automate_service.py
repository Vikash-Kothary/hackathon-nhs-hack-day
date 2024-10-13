from jinja2 import Environment, FileSystemLoader

from nhs_hack_day.services import send_email


def __render_email(template_name: str, data: dict) -> str:
    # Set up the Jinja2 environment to load templates from the current directory
    env = Environment(loader=FileSystemLoader('src/nhs_hack_day/services/templates'))
    
    # Load the specified template
    template = env.get_template(template_name)
    
    # Render the template with the provided data
    return template.render(data)

def __automate_task(task, context):
    sender = "cp2423@gmail.com"
    recipient = "chris.pitcher@nhs.net"
    subject = task['description']
    #template = "email_template.html"
    template = f"{task['task_type']}.md"
    #context = {'name': 'Chris Pitcher', 'message': 'This is a test email'}
    
    service = send_email.create_gmail_service()
    send_email.send_email(service, sender, recipient, subject, template, context)

def automate_outpatient_booking_appointment(task):
    # email_content = 
    # send_email
    __automate_task(task, context = {
        'test': 'Full blood count',
        'name': 'Patient X',
        'hospital_number': '123456',
        'email_signature': 'Dr Jones'
    })
   

def automate_blood_tests(task):
    __automate_task(task, context = {
        'test': 'Blood Test',
        'name': 'Patient X',
        'hospital_number': '123456',
        'email_signature': 'Dr Jones'
    })

def automate_inpatient_speciality_referral(task):
    __automate_task(task, context = {
        'test': 'Inpatient Speciality',
        'name': 'Patient X',
        'hospital_number': '123456',
        'email_signature': 'Dr Jones'
    })
