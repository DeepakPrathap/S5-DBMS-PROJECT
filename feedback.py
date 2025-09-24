from tkinter import *
from tkinter import messagebox
from db_connect import project_db
import datetime

class FeedbackWindow:
    def __init__(self, player_email):
        self.player_email = player_email
        self.root = Tk()
        self.root.title("Quiz Feedback")
        self.root.geometry("500x350")
        self.root.config(bg="#E3F2FD")
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        Label(self.root, text="We value your feedback!", font=("Montserrat", 18, "bold"), bg="#E3F2FD").pack(pady=10)
        Label(self.root, text="Please share your thoughts about the quiz:", font=("Montserrat", 12), bg="#E3F2FD").pack(pady=5)
        self.feedback_text = Text(self.root, width=50, height=8, font=("Montserrat", 11), bg="#FFFFFF")
        self.feedback_text.pack(pady=10)
        Button(self.root, text="Submit Feedback", font=("Montserrat", 12), bg="#1976D2", fg="white", command=self.submit_feedback).pack(pady=10)

    def submit_feedback(self):
        feedback = self.feedback_text.get("1.0", END).strip()
        if not feedback:
            messagebox.showwarning("Empty Feedback", "Please enter your feedback before submitting.")
            return
        try:
            db = project_db()
            cursor = db.cursor()
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            query = "INSERT INTO FEEDBACK (PLAYER_EMAIL, FEEDBACK_TEXT, DATE_SUBMITTED) VALUES (%s, %s, %s)"
            cursor.execute(query, (self.player_email, feedback, now))
            db.commit()
            messagebox.showinfo("Thank You!", "Your feedback has been submitted.")
            self.root.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Could not submit feedback.\n{e}")

# Example usage:
# FeedbackWindow(player_email="AJAY@GMAIL.COM")
