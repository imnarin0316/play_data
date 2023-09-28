import json
import random
from django.shortcuts import render, redirect

from .models import Question
from .models import Rank
from django.db.models import F
from django.http import HttpResponse


def start_game(request):
 
    # JSON 파일에서 데이터를 읽어옵니다.
    with open('quest.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 모든 문제를 가져옵니다.
    all_questions = data['questions']

    # 8개의 문제를 무작위로 추출합니다.
    random_questions = random.sample(all_questions, 8)
    
    # 각 문제에 순서를 부여합니다.
    for index, question in enumerate(random_questions, start=1):
        question['su'] = index

    # 3개의 문제를 추가로 무작위로 선택합니다.
    selected_questions = random.sample(random_questions, 3)
    global_selected_questions = random.sample(random_questions, 3)
    
    # 추출된 문제를 세션에 저장합니다.
    request.session['questions'] = random_questions
    request.session['current_question_index'] = 0
    request.session['correct_answers'] = 0
    request.session['quest3'] = global_selected_questions
    
    
    return render(request, 'quiz/start_game.html', {'question': random_questions[0], 'selected_questions':selected_questions })

    

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
    rank_range = list(range(1, 5))
    
    if 'questions' in request.session and 'correct_answers' in request.session:
        correct_answers = request.session['correct_answers'] * 1000
        questions = request.session['questions']

        # 각 문제에 사용자의 답과 정답을 추가합니다.
        for index, question in enumerate(questions, start=1):
            question['user_answer'] = request.session.get(f'user_answer_{question["id"]}', 'N/A')
            question['correct_answer'] = '1' if question['answer'] else '0'
            question['su'] = index * 1000
            question['idxx'] = index
        
        # POST 요청 처리
        if request.method == 'POST':
            nickname = request.POST.get('nickname')
            if nickname:
                # Rank 모델에 닉네임과 점수 저장
                Rank.objects.create(nickname=nickname, score=correct_answers)

        # 상위 랭킹 정보 가져오기
        user_rank = Rank.objects.filter(score=correct_answers).first()
        
        # 현재 사용자의 점수보다 높거나 같은 점수를 가진 사용자를 가져옴
        top_ranks = (
            Rank.objects
            .filter(score__gte=correct_answers)
            .order_by('-score', 'id')[:4]
        )

        # 현재 사용자의 랭킹 정보 추가
        if user_rank:
            user_rank.rank = Rank.objects.filter(score__gt=correct_answers).count() + 1

        
        # 각 랭킹에 순위 정보 추가
        for index, rank in enumerate(top_ranks, start=1):
            rank.rank = index

        return render(request, 'quiz/quiz_result.html', {'correct_answers': correct_answers, 'questions': questions, 'rank_range': rank_range, 'top_ranks': top_ranks})
    
    # 세션에 문제와 정답 개수가 없는 경우, 다시 질문 화면으로 이동합니다.
    return render(request, 'quiz/quiz_result.html', {'correct_answers': 0, 'questions': [], 'rank_range': rank_range})

