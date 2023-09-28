def selected_questions(request):
    # 여기에서 selected_questions 데이터를 가져오는 로직을 작성합니다.
    # 예: 세션에서 가져온다고 가정합니다.
    selected_questions = request.session.get('selected_questions', [])
    return {'selected_questions': selected_questions}
