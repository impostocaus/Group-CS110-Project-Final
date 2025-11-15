# Final project for CS 110
# Worked on by Max M., Thai D., Kailey R.


quiz = [
    {
        "question": "1. The Teacher Evaluation Model (VAM) is considered a WMD for which of the following reasons?",
        "choices": ["A) It shows the quality of teaching",
                    "B) It lacks transparency and can be misjudged",
                    "C) It shows the school’s teachers’ opinions",
                    "D) It increases the school’s reputation"],
        "answer": "B"
    },
    {
        "question": "2. Which of the following is an example of a WMD used in recruiting?",
        "choices": ["A) Asking candidates about their preferences",
                    "B) Using an assessment algorithm score, and hiring based on personality",
                    "C) Only face-to-face interviews",
                    "D) Testing direct job performance"],
        "answer": "B"
    },
    {
        "question": "3. According to WMD, what types of online advertising are considered predatory?",
        "choices": ["A) Ads for games you follow",
                    "B) Ads that use personal data for targeting",
                    "C) Ads that promote free services",
                    "D) Social media advertising"],
        "answer": "B"
    },
    {
        "question": "4. What is one way social media exacerbates political divisions?",
        "choices": ["A) It shares information transparently, and has multiple perspectives on issues",
                    "B) It displays relevant content, and reinforces users’ own views on political issues",
                    "C) It removes political advertising",
                    "D) It encourages open debate"],
        "answer": "B"
    },
    {
        "question": "5. What are some examples of weapons of mass destruction (WMD) used in insurance?",
        "choices": ["A) Based on credit score, and age to calculate different insurance rates.",
                    "B) Fair insurance rates for everyone",
                    "C) Require a preferred insurance rate",
                    "D) Allow customers to negotiate insurance rates"],
        "answer": "A"
    }
]

score = 0

for q in quiz:
    print("\n" + q["question"])
    for choice in q["choices"]:
        print(choice)

    user_answer = input("Enter your answer: ").upper()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {q['answer']}.")

print("\nQuiz finished!")
print(f"Your score: {score} out of {len(quiz)}")
