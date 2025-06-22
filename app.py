from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    bmi = None
    category = None
    suggestion = None
    name = age = ""

    if request.method == "POST":
        try:
            name = request.form["name"]
            age = request.form["age"]
            weight = float(request.form["weight"])
            height = float(request.form["height"])  # in feet

            if weight <= 0 or height <= 0:
                return render_template("index.html", error="Enter positive values!")

            height_m = height * 0.3048
            bmi = weight / (height_m ** 2)

            if bmi < 18.5:
                category = "Underweight"
                suggestion = "Eat nutrient-rich foods and consult a doctor for guidance."
            elif bmi <= 24.9:
                category = "Normal weight"
                suggestion = "Maintain your healthy habits!"
            elif bmi <= 29.9:
                category = "Overweight"
                suggestion = "Consider a healthy diet and more physical activity."
            elif bmi <= 35.9:
                category = "Obese"
                suggestion = "Seek a professional plan for weight management."
            elif bmi <= 39:
                category = "Severely Obese"
                suggestion = "Your health may be at risk. Get medical help soon."
            else:
                category = "Morbidly Obese"
                suggestion = "Immediate medical support is highly recommended."

        except ValueError:
            return render_template("index.html", error="Invalid input. Please enter numbers only.")

    return render_template("index.html", bmi=bmi, category=category, suggestion=suggestion, name=name, age=age)

if __name__ == "__main__":
    app.run(debug=True)
