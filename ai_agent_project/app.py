import os
import pandas as pd
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Ensure the 'uploads' directory exists
if not os.path.exists('uploads'):
    os.makedirs('uploads')

# Route for displaying the dashboard
@app.route('/')
def home():
    return render_template('index.html', columns=[], file_path="")

# Route for handling file upload
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    # Save file to server
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)

    # Process the file and extract columns (assuming it's a CSV)
    try:
        df = pd.read_csv(file_path)
        columns = df.columns.tolist()  # Get the column names from the CSV
    except Exception as e:
        return f"Error processing file: {e}", 500

    # Pass columns and file path to template for the next form
    return render_template('index.html', columns=columns, file_path=file_path)

# Route for handling query submission
# Route for handling query submission
@app.route('/query', methods=['POST'])
def query():
    column_name = request.form['column_name']
    prompt_template = request.form['prompt_template']
    file_path = request.form['file_path']

    # Parse the search value from the prompt template
    # Example: If prompt_template is "Get me the email address of {company}"
    search_value = prompt_template.split("{")[-1].split("}")[0].strip().lower()

    # Read the file and search for the value in the specified column
    try:
        df = pd.read_csv(file_path)

        # Ensure all values in the column are lowercase and stripped of whitespace
        df[column_name] = df[column_name].astype(str).str.strip().str.lower()

        # Check if the search value exists in the specified column
        if df[column_name].str.contains(search_value, regex=False).any():
            message = f"The value '{search_value}' was found in the '{column_name}' column."
        else:
            message = f"The value '{search_value}' was not found in the '{column_name}' column."

        return jsonify({"message": message})
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500


if __name__ == "__main__":
    app.run(debug=True)