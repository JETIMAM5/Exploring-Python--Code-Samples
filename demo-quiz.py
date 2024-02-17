# Question

class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer= answer
    
    def checkAnswer(self,answer):
        return self.answer == answer


# Quiz

class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        if self.questionIndex < len(self.questions):
          return self.questions[self.questionIndex]
        else:
          self.questionIndex = 0
          return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Question {self.questionIndex+1} : {question.text}")

        for q in question.choices:
            print("-"+ q)

        answer = input("Answer: ")
        self.guess(answer)
        self.loadQuestion()

    def guess(self,answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1

        self.questionIndex += 1

        self.displayQuestion()

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print("----------------------------------------------------------------------------------------------------------")
        print("Score : " + self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion :
            print("Quiz is Over..")
        else:
            print(f"Question {self.questionIndex+1} of {totalQuestion}".center(100,'*'))



    
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
q1 = Question("What's the best programming language ? ",['C#','Python','Java','Flutter'],'Python')
q2 = Question("What's the most popular programming language ? ",['Java','Python','C#','Flutter'],'Python')
q3 = Question("Which is the most profitable programming language ? ",['C#','Java','Flutter','Python'],'Java')
q4 = Question("Which programming language is easier to learn? ? ",['C#','Java','Flutter','Python'],'Python')


questions = [q1,q2,q3,q4]

quiz = Quiz(questions)
quiz.loadQuestion() #