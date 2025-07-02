import csv
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        gender = request.form["gender"]
        emergency = request.form["emergency"]
        payment = request.form["payment"]
        Age= request.form.get("Age")
        # Save the submitted data to a CSV file
        with open("applicants.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([name, phone, gender, emergency, payment,Age])
        return "Form submitted!"
    return '''
        <h2>University of Chittagong</h2>
        <h3>Department of chemistry</h3>
        <h4>Are you ready to register?</h4>
        
        <form method="post">
            Name: <input name="name"><br>
            Phone: <input name="phone"><br>
            Gender: <input name="gender"><br>
            Emergency Contact: <input name="emergency"><br>
            Payment Mood: <input name="payment"><br>
            Age: <input name="Age"><br>
            <input type="submit">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)


