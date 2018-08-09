from flask import Flask
from flask import render_template, redirect, request
app = Flask(__name__)

class AskOtagoQuestion:
    question = ""
    answer = ""

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


def getQuestions():
    staticquestions = [
        AskOtagoQuestion(question="Who won the Battle of York?", answer="The Americans won a clear victory, however it did not have decisive strategic results as York was a less important objective in military terms than Kingston, where the British armed vessels on Lake Ontario were based."),
        AskOtagoQuestion(question="Who would win in a race if they were transformed into bats - the Archway building or the Burns building?", answer="Easy. Archway hands down. Burns is a box, Archway is far more aerodynamic and it almost already has wings. The asbestos also has the effect of slowing Burns down."),
        AskOtagoQuestion(question="How big should I expect my 50 bag to be?", answer="In Dunedin 2.5 grams isn’t that bad. A gram should be a 20 bag - it’s not normally, but in theory you want somewhere around there so at a minimum you should be paying that rate. You may get a bit of economies of scale due to the extra amount, but don’t expect it."),
        AskOtagoQuestion(question="What kind of grades do I need to get into Med?", answer="If you have to ask, you’re not getting in."),
        AskOtagoQuestion(question="Who is Charlene Chainz?", answer="Harlene Hayne’s rap persona"),
        AskOtagoQuestion(question="What is New Zealand’s oldest, bestest, and most technologically advanced student magazine?", answer="Not sure. The ODT?")
    ]
    return staticquestions


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    questionset = getQuestions()
    return render_template('index.html',  questionset=questionset)
