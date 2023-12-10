import openai

# Set your OpenAI GPT-3 API key here
openai.api_key = ''

def generate_exam_question(topic, difficulty):
    prompt = f"Generate an exam question on the topic '{topic}' with difficulty '{difficulty}'."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def generate_exam_answer(question):
    prompt = f"Provide the answer to the following question: '{question}'"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def generate_explanation(question, correct_answer):
    prompt = f"Why is the answer to the question '{question}' '{correct_answer}'?"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def main():
    print("Welcome to the Exam Prep Chatbot!")

    while True:
        topic = input("Enter the topic for the exam question (e.g., Math, Science, History): ")
        difficulty = input("Select the difficulty level (easy, medium, hard): ")

        # Generate exam question
        exam_question = generate_exam_question(topic, difficulty)
        print(f"\nGenerated Exam Question: {exam_question}")

        # Allow the user to answer the question
        user_answer = input("\nProvide your answer to the question: ")

        # Generate the answer to the question
        correct_answer = generate_exam_answer(exam_question)

        # Generate an explanation for the correct answer
        explanation = generate_explanation(exam_question, correct_answer)
        print(f"\nExplanation: {explanation}")

        # Compare the user's answer with the correct answer
        if user_answer.strip().lower() == correct_answer.lower():
            print("Correct! Well done!")
        else:
            print(f"Sorry, that's incorrect. The correct answer is: {correct_answer}")

        # Ask if the user wants to continue
        another_question = input("\nDo you want another question? (yes/no): ")
        if another_question.lower() != 'yes':
            print("Thank you for using the Exam Prep Chatbot. Good luck with your studies!")
            break

if __name__ == "__main__":
    main()
    
    print("hello")
    print("Setup...")
    print("Logic...")