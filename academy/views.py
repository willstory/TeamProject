from django.shortcuts import render
from django.db.models import Count
from .models import QuestionData



def academy_list(request):

    # GET 요청에서 필터링 값 가져오기
    selected_categories = request.GET.get("categories", "").split(",") if request.GET.get("categories") else []
    selected_grades = request.GET.get("grades", "").split(",") if request.GET.get("grades") else []
    selected_years = request.GET.get("years", "").split(",") if request.GET.get("years") else []

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
    selected_year = request.GET.get('year')
    selected_grade = request.GET.get('grade')
    selected_month = request.GET.get('month')
    selected_category = request.GET.get('category')

    # 필터링된 문제 가져오기
    if selected_year and selected_grade and selected_month:
        questions = QuestionData.objects.filter(연도=selected_year, 학년=selected_grade, 강=selected_month)
    else:
        questions = QuestionData.objects.none()  # 조건이 없을 경우 빈 쿼리셋 반환

    # 번호별 문제 수 계산
    number_counts = questions.values('번호').annotate(count=Count('번호')).order_by('번호')

    # 📌 (번호(개수)) 문자열 리스트 생성
    question_list = ', '.join(f"{num['번호']}({num['count']})" for num in number_counts)
    total_count = sum(num['count'] for num in number_counts)  # 총 문제 수 계산

    # 📌 학년별 문제 수 계산 및 리스트 변환
    grade_counts = QuestionData.objects.values('학년').annotate(count=Count('학년'))
    grades = [
        {
            "name": grade['학년'], 
            "count": grade['count'],
            "checked": selected_grade == grade['학년']
        }
        for grade in grade_counts
    ]

    # 📌 유형별 문제 수 계산 및 리스트 변환
    category_counts = QuestionData.objects.values('유형').annotate(count=Count('유형'))
    categories = [
        {
            "name": category['유형'], 
            "count": category['count'],
            "checked": selected_category == category['유형']
        }
        for category in category_counts
    ]

    # 📌 연도별 문제 수 계산 및 리스트 변환
    year_counts = QuestionData.objects.values('연도').annotate(count=Count('연도'))
    years = [
        {
            "name": year['연도'], 
            "count": year['count'],
            "checked": str(selected_year) == str(year['연도'])
        }
        for year in year_counts
    ]

    exams = [{
        'question_list': question_list,
        'question_counter': total_count,  # 총 문제 수
        #'link': ['색인']  # 필요에 따라 링크 설정
        'link': None
    }]

    category = '모의고사'
    context = {
        "exams": exams,
        "selected_year": selected_year,
        "selected_grade": selected_grade,
        "grades": grades,
        "years": years,
        "categories": categories,
        "selected_month" : selected_month,
    }

    return render(request, "academy_list_result.html", context)