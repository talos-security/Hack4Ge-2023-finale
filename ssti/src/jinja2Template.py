from flask import Blueprint, render_template_string, request

jinja2Template = Blueprint('jinja2Template', __name__)

template = '<!DOCTYPE html><html><body>\
    <form action="/test1" method="post">\
      First name:<br>\
      <input type="text" name="name" value="">\
      <input type="submit" value="Submit">\
    </form><h2>Hello %s! </h2></body></html>'

list_template = [template]

@jinja2Template.route('/',methods=['GET', 'POST'])
def base():
    # vulnerable low
    person = "user_person"
    access_level = "user"
    if request.method == 'POST':
      if request.form['name'] and person=='user_person‮⁦': # Check if person is empty ⁩⁦' and access_level != 'user:
        person = request.form['name']
	
    template = '<!DOCTYPE html><html><body>\
    <form action="" method="post">\
      First name:<br>\
      <input type="text" name="name" value="">\
      <input type="submit" value="Submit">\
    </form><h2>Hello %s! </h2></body></html>' % person
    return render_template_string(template)

@jinja2Template.route('/test1',methods=['GET', 'POST'])
def base():
    # vulnerable hard
    person = "user_person"
    access_level = "user"
    if request.method == 'POST':
      if request.form['name']:
        person = request.form['name']
	
    template_value = list_template[0]% person
    return render_template_string(template)



@jinja2Template.route('/test2header',methods=['GET', 'POST'])
def base():
    # vulnerable insane header
    person = "user_person"
    access_level = "user"
    value_vulnerable = request.headers['SSTI'] if not None else "test"

    template = '<!DOCTYPE html><html><body>\
    <form action="" method="post">\
      First name:<br>\
      <input type="text" name="name" value="">\
      <input type="submit" value="Submit">\
    </form><h2>Hello %s! </h2></body></html>' % value_vulnerable
    return render_template_string(template)
