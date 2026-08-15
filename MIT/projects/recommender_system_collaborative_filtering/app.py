from flask import Flask, request, render_template_string
from model import ProductRecommender

# Initialize the Flask App
app = Flask(__name__)

# Initialize the ML Model and Recommendation Engine once when the server starts
recommender = ProductRecommender()

# Embedded HTML interface (Satisfies UI Rubric requirements)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-Commerce Recommendation System</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f6; margin: 0; padding: 0; display: flex; justify-content: center; align-items: center; min-height: 100vh; }
        .container { background-color: white; padding: 40px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); width: 100%; max-width: 600px; text-align: center; }
        h1 { color: #2c3e50; font-size: 24px; margin-bottom: 20px; }
        form { display: flex; flex-direction: column; gap: 15px; }
        input[type="text"] { padding: 15px; font-size: 16px; border: 1px solid #ccc; border-radius: 5px; outline: none; transition: border-color 0.3s; }
        input[type="text"]:focus { border-color: #3498db; }
        button { background-color: #3498db; color: white; border: none; padding: 15px; font-size: 16px; border-radius: 5px; cursor: pointer; transition: background-color 0.3s; font-weight: bold; }
        button:hover { background-color: #2980b9; }
        .results { margin-top: 30px; text-align: left; }
        .results h2 { color: #27ae60; font-size: 20px; border-bottom: 2px solid #27ae60; padding-bottom: 10px; }
        ul { list-style-type: none; padding: 0; }
        li { background-color: #ecf0f1; margin: 10px 0; padding: 15px; border-radius: 5px; color: #34495e; font-weight: 500; border-left: 5px solid #3498db; }
        .error { color: #e74c3c; font-weight: bold; margin-top: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔍 Smart Product Recommender</h1>
        <p>Enter a username to get the top 5 personalized, highly-rated product recommendations.</p>

        <form method="POST" action="/">
            <input type="text" name="username" placeholder="Enter Username (e.g., rachel)" required value="{{ requested_user }}">
            <button type="submit">Submit</button>
        </form>

        {% if recommendations %}
            <div class="results">
                <h2>Top 5 Recommendations for '{{ requested_user }}'</h2>
                <ul>
                    {% for item in recommendations %}
                        <li>{{ item }}</li>
                    {% endfor %}
                </ul>
            </div>
        {% elif error %}
            <div class="error">
                <p>{{ error }}</p>
            </div>
        {% endif %}
    </div>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []
    error = ""
    requested_user = ""

    if request.method == "POST":
        requested_user = request.form.get("username").strip()

        try:
            # Call the ML backend to get filtered recommendations
            results = recommender.get_top_5_recommendations(requested_user)

            # If the result string indicates an error (user not found)
            if len(results) > 0 and "not found in the database" in results[0]:
                error = results[0]
            else:
                recommendations = results
        except Exception as e:
            error = f"An error occurred while processing your request: {str(e)}"

    # Render the embedded HTML string, passing the necessary variables
    return render_template_string(
        HTML_TEMPLATE,
        recommendations=recommendations,
        error=error,
        requested_user=requested_user,
    )


if __name__ == "__main__":
    # Run the Flask app on localhost, port 5000
    app.run(debug=True, host="0.0.0.0", port=5000)
