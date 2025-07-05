from flask import Flask, render_template, request, redirect, session
from extractTextFromFile import extractTextFromFile
from feedback import feedbackFromAi
from FormatFeedback import FormatFeedback
from ai_chat import ai_chat
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ResumePro.db'
db = SQLAlchemy(app)

class Users(db.Model): 
    serial_no = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(500), nullable = False)
    password = db.Column(db.String(200), nullable = False)

@app.route("/", methods = ["GET", "POST"])
def login_signup():
    return render_template("log_in_sign_up.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        if( not username.strip() or not password.strip()):
            return render_template("login.html", error="The username or password cannot be empty")
        
        username_exists = Users.query.filter_by(username = username).first()

        if username_exists and username_exists.password == password:
            return redirect("/home")
        elif not(username_exists):
            error = f"Username {username} is invalid"
            return render_template("login.html", error = error)
        elif username_exists and username_exists.password != password:
            error = "Invalid Password"
            return render_template("login.html", error = error)
    return render_template("login.html")

@app.route("/signup", methods = ["GET", "POST"])
def signup():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if( not username.strip() or not password.strip()):
            return render_template("login.html", error="The username or password cannot be empty")
        
        username_exists = Users.query.filter_by(username = username).first()

        if username_exists:
            error = f"User with username {username} already exists"
            return render_template("signup.html", error = error)
        else:
            user = Users(username = username, password = password)
            db.session.add(user)
            username = Users.query.filter_by(username = username).first()
            db.session.commit()
            return redirect("/home")
    return render_template("signup.html")


@app.route("/home")
def home():
    return render_template("index.html", page="home")

@app.route("/analyze", methods = ["GET", "POST"])
def analyze():
    if request.method == "POST":
        input_file = request.files.get("input_file")
        # print(f"File received: {input_file.filename if input_file else 'None'}") for debugging file input
        if input_file:
            # print("Uploaded")
            if input_file.filename.endswith('.pdf') and len(input_file.read()) <= 5*1024*1024:
                input_file.seek(0)
                content = extractTextFromFile(input_file) 
                session['resume_content'] = content
                print("Resume stored in session.")
                
                # print(content) for debugging content extraction
                ai_feedback = feedbackFromAi(content)
                ai_feedback_formatted = FormatFeedback(ai_feedback)
                # print(f"Ai Feedback: {ai_feedback}") for debugging ai feedback
                return render_template("analyze.html", feedback = ai_feedback_formatted)
            else:
                return render_template("analyze.html", error = "File size greater than 5mb")
        else:
            return render_template("analyze.html", error = "Enter a valid pdf file")

    return render_template("analyze.html")

@app.route("/information")
def about():
    return render_template("information.html")

@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

@app.route("/contact")
def resources():
    return render_template("contact.html")

@app.route('/chat', methods = ["GET", "POST"])
def chat():
    if request.method == "POST":
        question = request.form.get("user-text")
        content = session.get("resume_content", "")

        print(question)
        if not content.strip():
            return render_template("chat.html", answer="Please upload your resume first on the Analyze page.")
        
        answer = ai_chat(content, question)
        answer_formatted = FormatFeedback(answer)
        return render_template("chat.html", answer=answer_formatted, question=question)
    
    return render_template("chat.html")

@app.before_request
def create_tables():
    db.create_all()
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
