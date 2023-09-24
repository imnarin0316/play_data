import json
import random
from django.shortcuts import render, redirect

from .models import Question

def start_game(request):
    # JSON 파일에서 데이터를 읽어옵니다.
    with open('quest.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 모든 문제를 가져옵니다.
    all_questions = data['questions']

    # 10개의 문제를 무작위로 추출합니다.
    random_questions = random.sample(all_questions, 10)
    
    # 각 문제에 순서를 부여합니다.
    for index, question in enumerate(random_questions, start=1):
        question['su'] = index

    # 추출된 문제를 세션에 저장합니다.
    request.session['questions'] = random_questions
    request.session['current_question_index'] = 0
    request.session['correct_answers'] = 0

    return render(request, 'quiz/start_game.html', {'question': random_questions[0], })

def answer_question(request):
    if 'questions' not in request.session or 'current_question_index' not in request.session:
        return render(request, 'quiz/quiz_result.html')

    questions = request.session['questions']
    current_question_index = request.session['current_question_index']
    correct_answers = request.session.get('correct_answers', 0)
    print(f"current_question_index: {current_question_index}") 
    
    if request.method == 'POST':
        user_answer = request.POST.get('answer')
        if user_answer is not None:
            # 사용자가 제출한 답을 확인합니다.
            correct_answer = questions[current_question_index]['answer']
            if user_answer == str(correct_answer):
                correct_answers += 1
                request.session['correct_answers'] = correct_answers

            # 현재 문제의 사용자 답을 세션에 저장합니다.
            question = questions[current_question_index]
            question['user_answer'] = user_answer
            request.session[f'user_answer_{question["id"]}'] = user_answer

        current_question_index += 1
        request.session['current_question_index'] = current_question_index

        if current_question_index < len(questions):
            return render(request, 'quiz/question.html', {'question': questions[current_question_index]})
        else:
            return redirect('quiz_result')  # 모든 문제를 다 풀었을 때, 결과 화면으로 이동합니다.

    return render(request, 'quiz/question.html', {'question': questions[current_question_index], 'current_question_index': 1})


def view_quiz_result(request):
    rank_range = list(range(1, 6))
    
    if 'questions' in request.session and 'correct_answers' in request.session:
        correct_answers = request.session['correct_answers'] * 1000
        questions = request.session['questions']

        # 각 문제에 사용자의 답과 정답을 추가합니다.
        for question in questions:
            question['user_answer'] = request.session.get(f'user_answer_{question["id"]}', 'N/A')
            question['correct_answer'] = '1' if question['answer'] else '0'

        return render(request, 'quiz/quiz_result.html', {'correct_answers': correct_answers, 'questions': questions, 'rank_range': rank_range})
    
    # 세션에 문제와 정답 개수가 없는 경우, 다시 질문 화면으로 이동합니다.
    return render(request, 'quiz/quiz_result.html', {'correct_answers': 0, 'questions': [], 'rank_range': rank_range})
