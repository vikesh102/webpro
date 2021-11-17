from flask import Flask, url_for, render_template, request, redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
	render_template(page_name)

@app.route('/about.html')
def about():
	return render_template('about.html')


@app.route('/works.html')
def works():
	return render_template('works.html')

def write_to_csv(data):
	with open('database.csv', mode='a') as database2:
	 email = data['email']
	 subject = data["subject"]
	 message = data["message"]
	 csv_writer = csv.writer(database2, delimiter=',', quotechar = '"', newline='', quoting=csv.QUOTE_MINIMAL)
	 csv_writer.writerow([email,subject,message])


def write_to_file(data):
	with open('database.txt', mode='a') as database:
	 email = data['email']
	 subject = data["subject"]
	 message = data["message"]
	 file = database.write(f'\n{email},{subject},{message}')


@app.route('/contact.html')
def contact():
	return render_template('contact.html')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_csv(data)
		return 'Details Submitted'
	else:
		return 'something went wrong pleas try again'




    