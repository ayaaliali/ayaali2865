import csv


def load_questions_from_csv_file(file_path):

    with open(file_path, 'r') as file:

        reader = csv.reader(file)
        questions = [row for row in reader]
        return questions

# The administer_quiz function remains the same as in the text file example


questions_file = "questions.csv"
user_name = input("Enter your name: ")
quiz_questions = load_questions_from_csv_file(questions_file)
user_score = administer_quiz(quiz_questions)

print(f"Dear {user_name}, your score is: {user_score}/20")

with open("user_results.csv", "a", newline="") as result_file:
    writer = csv.writer(result_file)
    writer.writerow([user_name, user_score])
