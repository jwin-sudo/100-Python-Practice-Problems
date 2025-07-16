'''
create a program that asks the user to submit text through a web app
'''

from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        with open('submitted_text.txt', 'a') as file:
            file.write(text + '\n')
        return render_template_string('<h1>Text submitted successfully!</h1><a href="/">Go back</a>')
    return '''
        <form method="post">
            <textarea name="text" rows="4" cols="50"></textarea><br>
            <input type="submit" value="Submit">
        </form>
    ''' 
if __name__ == '__main__':
    app.run(debug=True)
'''
This code creates a simple Flask web application that allows users to submit text through a form. The submitted text is saved to a file named `submitted_text.txt`. The app runs in debug mode for development purposes.
'''

