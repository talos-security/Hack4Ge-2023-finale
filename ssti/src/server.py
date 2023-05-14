from flask import Flask
from jinja2Template import jinja2Template
from jinja2Template2 import jinja2Template2
from makoTemplate import mako_template
from notVulnerable import non_vulnerable
from ssti_template import ssti_template
from ssti_template_2 import ssti_template_2


app = Flask(__name__)
app.register_blueprint(jinja2Template2, url_prefix='/jinja2')
app.register_blueprint(jinja2Template, url_prefix='/jinja2_2')
app.register_blueprint(mako_template, url_prefix='/mako')
app.register_blueprint(ssti_template_2, url_prefix='/ssti2')
app.register_blueprint(ssti_template, url_prefix='/ssti')

app.register_blueprint(non_vulnerable, url_prefix='/nonVulnerable')


@app.route('/', methods=['GET','POST'])
def index():
	return """
	<!DOCTYPE html><html><body>

<a href="jinja2/">jinja2</a><br>
<a href="jinja2_2/">jinja2-test1</a><br>
<a href="jinja2_2/test1">jinja2-test2</a><br>
<a href="jinja2_2/test2header">jinja2-test2</a><br>
<a href="mako/">jinja2-test2</a><br>
<a href="ssti/">ssti-2-template-multi-method</a><br>

<a href="ssti2/">ssti-2-template-multi-method</a><br>
<a href="nonVulnerable/">nonVulnerable</a><br>

</body></html>
	""" 

if __name__=="__main__":
	  app.run("0.0.0.0",port = 6003,debug=False)