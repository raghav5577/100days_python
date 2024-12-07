question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

class Question:
    def __init__(self,text,answer):
        self.text=text
        self.answer=answer

class QuizBrain:
    def __init__(self,question_list):
        self.score=0
        self.question_number=0
        self.question_list=question_list

    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        user_answer=input(f"Q.{self.question_number}: {current_question.text}. (True/False)").lower()
        self.check_answer(user_answer,current_question.answer)
    
    def question_remain(self):
        if self.question_number<len(self.question_list):
            return True
        else:
            False
        
    
    def check_answer(self,user,correct):
        if user.lower()==correct.lower():
            self.score+=1
            print("You got it right")
        else:
            print("That's wrong")
        print(f"The correct answer was {correct}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

question_bank=[]
for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    new_q=Question(question_text,question_answer)
    question_bank.append(new_q)

quiz=QuizBrain(question_bank)

while quiz.question_remain():
    quiz.next_question()

print("You've completed the quiz...")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")