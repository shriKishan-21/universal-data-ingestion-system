from flask import Flask, render_template, request
from loader import load_data
from cleaner import clean_data
from db_handler import store_to_database, read_from_database
import os

import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)




UPLOAD_FOLDER = "Data"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    result = None

    if request.method == "POST":

        # FILE UPLOAD
        if "file" in request.files:
            file = request.files["file"]
            table_name = request.form["table"]

            if file.filename != "":
                path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
                file.save(path)

                df = load_data(path)
                df = clean_data(df)
                store_to_database(df, table_name)

                message = f"Data stored successfully in table '{table_name}'"

        # SQL QUERY
        if "query" in request.form:
            query = request.form["query"]
            result = read_from_database(query)

    return render_template("index.html", message=message, result=result)


if __name__ == "__main__":
    app.run(debug=True)
