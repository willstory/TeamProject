from django.shortcuts import render

# Create your views here.
def academy_list(request):
    context = {
        "categories": [
            {"name": "모의고사", "checked": False},
            {"name": "EBS", "checked": True},
        ],
        "grades": [
            {"name": "1학년", "checked": False},
            {"name": "2학년", "checked": False},
            {"name": "3학년", "checked": False},
        ],
        "years": [
            {"name": "2019", "checked": False},
            {"name": "2020", "checked": True},
            {"name": "2021", "checked": True},
            {"name": "2022", "checked": True},
            {"name": "2023", "checked": True},
            {"name": "2024", "checked": True},
        ],
    }
    return render(request, "academy_list.html", context)

def academy_list_result(request):
    # 선택된 값 (예제에서는 기본값 설정)
    selected_year = "2019"
    selected_month = "3"
    selected_category = "모의고사"
    selected_grade = "고1"

    # 구분 데이터  
    # =================================================
    # 꼬옥 읽어 주세요........
    # "name": "목적", "count": 7 의 경우
    # count 옆에 있는 것은 total_count 입니다.
    # total_count = YearData.objects.aggregate(total_count=Sum('count'))['total_count'] or 0
    # 결과를 템플릿에 전달
    # context = {
    #  'years': [
    #       {"name": "2019", "count": total_count},  # 연도는 고정, count는 DB에서 가져온 값
    #   ]
    # }
    # 이렇게 하면 될 거 같은데 db 값 연동 해야 합니다. 
    # =================================================
    context = {
        "categories": [
            {"name": "목적", "count": 7},
            {"name": "어법", "count": 13},
            {"name": "어휘", "count": 6},
            {"name": "일치불일치", "count": 1},
            {"name": "무관한문장", "count": 2},
            {"name": "서술형", "count": 11},
            {"name": "지칭대상", "count": 3},
            {"name": "기타", "count": 20},
            {"name": "제목", "count": 27},
            {"name": "문장넣기", "count": 7},
            {"name": "순서", "count": 12, "class": "green"},
            {"name": "빈칸", "count": 5, "class": "green"},
            {"name": "요약문완성", "count": 9},
            {"name": "연결어", "count": 2},
            {"name": "요지", "count": 19},
            {"name": "주제", "count": 10},
            {"name": "주장", "count": 6},
            {"name": "밑줄의미", "count": 17},
            {"name": "심경분위기", "count": 1},
            {"name": "연결사", "count": 1},
            {"name": "도표", "count": 6},
            {"name": "장문", "count": 8},
        ],
        "grades": [
            {"name": "1학년", "checked": False},
            {"name": "2학년", "checked": False},
            {"name": "3학년", "checked": False},
        ],
        # 연도 데이터
        "years": [
            {"name": "2019", "count": 7},
            {"name": "2020", "count": 13},
            {"name": "2021", "count": 6},
            {"name": "2022", "count": 1},
            {"name": "2023", "count": 2},
            {"name": "2024", "count": 11},
            {"name": "2025", "count": 3},
        ]
    }

    return render(request, "academy_list_result.html", context)
