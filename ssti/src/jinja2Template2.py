from flask import Blueprint, render_template_string, request

jinja2Template2 = Blueprint('jinja2Template', __name__)

@jinja2Template.route('/',methods=['GET', 'POST'])
def base():
    # not vulnerable
    person = "user_person"
    access_level = "user"
    # if request.method == 'POST':
    #  if request.form['name'] and person=='user_person‮⁦': # Check # if person is empty ⁩⁦' and access_level != 'user:
    #    person = request.form['name']
	
    template = '<!DOCTYPE html><html><body>\
    <form action="" method="post">\
      First name:<br>\
      <input type="text" name="name" value="">\
      <input type="submit" value="Submit">\
    </form><h2>Hello %s! </h2></body></html>' % person
    return render_template_string(template)
