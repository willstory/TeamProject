from django.shortcuts import render
from django.db.models import Sum, Count
from datetime import datetime
from .models import Membership, Payment

def dashboard(request):
    # 1) 회원 현황 (월별 가입자 수)
    # 예시로 11월, 12월 회원 수를 구한다 가정
    # 실제로는 쿼리셋을 더 세부적으로 작성할 수 있음
    this_year = datetime.now().year
    month11 = Membership.objects.filter(join_date__year=this_year, join_date__month=11).count()
    month12 = Membership.objects.filter(join_date__year=this_year, join_date__month=12).count()

    # 2) 당월 수납 (월별 수납 금액, 수납 건수)
    # 11월, 12월 결제 총합
    pay11 = Payment.objects.filter(pay_date__year=this_year, pay_date__month=11)
    pay12 = Payment.objects.filter(pay_date__year=this_year, pay_date__month=12)
    
    total11 = pay11.aggregate(total=Sum('amount'))['total'] or 0
    total12 = pay12.aggregate(total=Sum('amount'))['total'] or 0

    count11 = pay11.count()
    count12 = pay12.count()

    context = {
        # 회원 현황
        'month11_member_count': month11,
        'month12_member_count': month12,

        # 당월 수납
        'month11_payment_count': count11,
        'month12_payment_count': count12,
        'month11_payment_total': total11,
        'month12_payment_total': total12,
    }
    return render(request, 'acad/dashboard.html', context)