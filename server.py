from flask import Flask, render_template, url_for, request, redirect #render allows to send html file, send_from_directory - sending images
app = Flask(__name__)
import csv
@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database_csv:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database_csv,delimiter=','    , quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\nfrom:{email}, subject:'{subject}', MESSAGE: {message}")

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()#get data from "form"
            #write_to_file(data)
            write_to_csv(data)
            return redirect('thankU.html')
        except:
            return 'WARNING! Error occured while saving to database'
    else:
        return "Something went wrong. Probably request.method isn't 'POST'"