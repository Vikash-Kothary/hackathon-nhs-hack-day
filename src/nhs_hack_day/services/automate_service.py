from jinja2 import Environment, FileSystemLoader

def __render_email(template_name: str, data: dict) -> str:
    # Set up the Jinja2 environment to load templates from the current directory
    env = Environment(loader=FileSystemLoader('src/nhs_hack_day/services/templates'))
    
    # Load the specified template
    template = env.get_template(template_name)
    
    # Render the template with the provided data
    return template.render(data)

def automate_outpatient_booking_appointment():
    # email_content = 
    # send_email
    pass

def automate_blood_tests():
    pass

def automate_inpatient_speciality_referral():
    pass
