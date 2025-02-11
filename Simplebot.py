import csv
import os

knowledge_file = "ChatbotKnowledge.csv"

if not os.path.exists(knowledge_file):
    with open(knowledge_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Question", "Answer"])

def load_knowledge():
    knowledge = {}
    with open(knowledge_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            knowledge[row["Question"]] = row["Answer"]
    return knowledge

def save_knowledge(question, answer):
    with open(knowledge_file, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([question, answer])
# Find_best_match ist sehr vereinfacht
def find_best_match(user_input, knowledge):
    user_words = set(user_input.lower().split())
    best_match = None
    best_score = 0

    for question in knowledge.keys():
        question_words = set(question.lower().split())
        score = len(user_words.intersection(question_words))

        if score > best_score:
            best_score = score
            best_match = question

    return best_match if best_score > 0 else None

def start_simplebot():
    knowledge = load_knowledge()

    print("Chatbot: Hallo! Ich bin dein lernfähiger Chatbot. Wie kann ich dir helfen?")

    while True:
        user_input = input("Du: ")

        # Beende den Chat, wenn der Benutzer "bye" eingibt
        if user_input.lower() == "bye":
            print("Chatbot: Tschüss! Bis zum nächsten Mal.")
            break

        # Finde die beste Übereinstimmung
        best_match = find_best_match(user_input, knowledge)

        if best_match:
            print(f"Chatbot: {knowledge[best_match]}")
        else:
            print("Chatbot: Ich kenne die Antwort auf diese Frage noch nicht. Kannst du mir die Antwort sagen?")
            answer = input("Antwort: ")
            save_knowledge(user_input, answer)
            knowledge[user_input] = answer
            print("Chatbot: Danke, ich habe gelernt!")

if __name__ == "__main__":
    start_simplebot()
