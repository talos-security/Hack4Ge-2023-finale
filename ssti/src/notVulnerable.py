from flask import Blueprint, request
from mako.template import Template

non_vulnerable = Blueprint('non_vulnerable', __name__)

@non_vulnerable.route('/',methods=['GET', 'POST'])
def base():
    # not vulnerable
    person = ""
    
    if request.method == 'POST':
      if request.form['name']:
        person = request.form['name']
    if request.method == "GET":
        person = request.args.get('name') if request.args.get('password') is not None else "pippo"
    
    template = '<!DOCTYPE html><html><body>\
    <h1>THIS IS NOT VULNERABLE TO SSTI</h1>\
    <br>\
    <form action="" method="post">\
      First name:<br>\
      <input type="text" name="name" value="">\
      <input type="submit" value="Submit">\
    </form><h2>Hello ${name} </h2></body></html>'
    return Template(template).render(name = person)
