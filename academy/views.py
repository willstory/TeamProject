from django.shortcuts import render
from django.db.models import Count
from .models import QuestionData

def academy_list(request):
    # GET 요청에서 선택된 값 가져오기
    selected_years = request.GET.getlist("year", [])
    selected_grades = request.GET.getlist("grade", [])
    selected_categories = request.GET.getlist("category", [])

    # 모든 문제 가져오기 및 필터링
    questions = QuestionData.objects.all()
    if selected_years:
        questions = questions.filter(연도__in=selected_years)
    if selected_grades:
        questions = questions.filter(학년__in=selected_grades)
    if selected_categories:
        questions = questions.filter(유형__in=selected_categories)

    # 학년, 연도 및 유형 데이터베이스에서 가져오기
    grades = QuestionData.objects.values_list('학년', flat=True).distinct()
    years = QuestionData.objects.values_list('연도', flat=True).distinct()
    categories = QuestionData.objects.values_list('유형', flat=True).distinct()

    # 필요한 필드만 가져오기
    exams = questions.values('색인', '유형', '학년', '연도', '강')

    # 결과를 원하는 형식으로 변환
    formatted_exams = []
    seen_titles = set()
    for exam in exams:
        title = f"{exam['학년']} {exam['연도']}년 {exam['강']}월 모의고사"
        category = "모의고사"
        if title not in seen_titles:
            formatted_exam = {
                'category': category,
                'grade': exam['학년'], 
                'year': exam['연도'],
                'month': exam['강'],
                'title': title,
                'link': exam['색인'],
            }
            formatted_exams.append(formatted_exam)
            seen_titles.add(title)
    exams = formatted_exams

    context = {
        "exams": exams,
        "grades": [{"name": grade, "checked": grade in selected_grades} for grade in grades],
        "years": [{"name": year, "checked": str(year) in selected_years} for year in years],
        "categories": [{"name": category, "checked": category in selected_categories} for category in categories],
        "selected_years": selected_years,
        "selected_grades": selected_grades,
        "selected_categories": selected_categories,
    }

    return render(request, "academy_list.html", context)

def academy_list_result(request):
    # 선택된 값 가져오기
    selected_year = request.GET.get('year', '2019')
    selected_category = request.GET.get('category', '모의고사')
    selected_grade = request.GET.get('grade', '고1')

    # 데이터 카운트 계산
    years = QuestionData.objects.values('연도').annotate(count=Count('색인')).order_by('연도')
    grades = QuestionData.objects.values('학년').annotate(count=Count('색인')).order_by('학년')
    categories = QuestionData.objects.values('유형').annotate(count=Count('색인')).order_by('유형')

    context = {
        "categories": [{"name": category['유형'], "count": category['count']} for category in categories],
        "grades": [{"name": grade['학년'], "count": grade['count']} for grade in grades],
        "years": [{"name": year['연도'], "count": year['count']} for year in years],
        "selected_year": selected_year,
        "selected_category": selected_category,
        "selected_grade": selected_grade,
    }

    return render(request, "academy_list_result.html", context)