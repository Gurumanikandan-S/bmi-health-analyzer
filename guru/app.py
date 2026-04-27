from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        try:
            weight = float(request.form.get('weight'))
            height_cm = float(request.form.get('height'))
            
            if weight <= 0 or height_cm <= 0:
                return render_template('calculator.html', error="Weight and height must be positive numbers.")

            height_m = height_cm / 100
            bmi = round(weight / (height_m ** 2), 2)
            
            if bmi < 18.5:
                category = "Underweight"
                message = "You are underweight. It's important to eat a nutrient-rich diet to gain weight safely."
                calories = "Increase your daily intake by 300-500 calories focusing on proteins and healthy fats."
                color_class = "underweight"
                score = 30
            elif 18.5 <= bmi <= 24.9:
                category = "Normal"
                message = "Great job! You have a healthy body weight. Maintain your balanced diet and active lifestyle."
                calories = "Maintain your current daily calorie intake for weight maintenance."
                color_class = "normal"
                score = 90
            elif 25 <= bmi <= 29.9:
                category = "Overweight"
                message = "You are slightly overweight. Consider increasing physical activity and monitoring portion sizes."
                calories = "Reduce your daily intake by 300-500 calories for safe weight loss."
                color_class = "overweight"
                score = 60
            else:
                category = "Obese"
                message = "Your BMI falls into the obese category. It is highly recommended to consult a healthcare provider."
                calories = "Focus on a structured, low-calorie diet under professional guidance."
                color_class = "obese"
                score = 20
                
            return render_template('calculator.html', 
                                   bmi=bmi, 
                                   category=category, 
                                   message=message, 
                                   calories=calories,
                                   color_class=color_class,
                                   score=score,
                                   progress_attr=f'style="width: {score}%;"')
        except (TypeError, ValueError):
            error = "Please enter valid numbers for weight and height."
            return render_template('calculator.html', error=error)
            
    return render_template('calculator.html')

if __name__ == '__main__':
    app.run(debug=True)
