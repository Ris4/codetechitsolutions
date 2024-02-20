import random

# Define the questions and answers
questions = {
    "General Knowledge": [
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "answer": "Paris"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"],
            "answer": "Leonardo da Vinci"
        }
    ],
    "Science": [
        {
            "question": "What is the chemical symbol for water?",
            "options": ["W", "H2", "O", "H2O"],
            "answer": "H2O"
        },
        {
            "question": "What is the powerhouse of the cell?",
            "options": ["Nucleus", "Mitochondria", "Ribosome", "Endoplasmic reticulum"],
            "answer": "Mitochondria"
        }
    ]
}

def display_question(question, options):
    print(question)
    for idx, option in enumerate(options, start=1):
        print(f"{idx}. {option}")

def quiz():
    score = 0
    for category, questions_list in questions.items():
        print(f"\n{category}:\n")
        for q in questions_list:
            display_question(q['question'], q['options'])
            user_answer = input("Your answer (enter the number): ")
            correct_answer = q['options'].index(q['answer']) + 1
            if int(user_answer) == correct_answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {correct_answer}.")
    print(f"\nYour final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    quiz()
