import json
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse , HttpResponseNotAllowed ,JsonResponse
from django.shortcuts import render
from home.models import Account , Profit
from django.utils.dateparse import parse_date

@csrf_exempt
def charge(request , account_id :int):
    if request.method == 'POST' :
        data = json.loads(request.body)
        account = get_object_or_404(Account, id = account_id)
        account.amount+= data.get("amount")
        account.save()
        
        return HttpResponse(f"your account charged with {data.get('amount')} ")
@csrf_exempt
def show_balance(request , account_id :int ):
    account = get_object_or_404(Account, id=account_id)
    return HttpResponse(f"you have {account.amount} in your account")


@csrf_exempt
def list_profit(request , account_id):
    
    PROFIT_CONFIG = {
    'monthly': {'percentage': 10, 'duration': 30},
    'annually': {'percentage': 20, 'duration': 365},
    }
    account = get_object_or_404(Account, id=account_id)
    if request.method == 'GET' :
        profits = Profit.objects.select_related('account').all()
        results =[]
        for profit in profits :
            config = PROFIT_CONFIG.get(profit.profit_type, {'percentage': 0, 'duration': 0})
            amount = (profit.account.balance * config['percentage'] * config['duration']) / (100 * 365)
            results.append({
                'account_id': profit.account.id,
                'account_name':Profit.account.name,
                'date': profit.date.strftime('%Y-%m-%d'),
                'profit_type': profit.get_profit_type_display(),
                'amount': round(amount, 2)
            })
        return JsonResponse({'profits': results}, status=200)
    
@csrf_exempt
def post_profit(request, account_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        profit_type = data.get('profit_type')
        date = parse_date(data.get('date'))

        account = get_object_or_404(Account, id=account_id)

        Profit.objects.create(
            account=account,
            profit_type=profit_type,
            date=date
        )

        return HttpResponse("profit record created", status=201)
            
        
    #if request.method == 'GET':
    #    profits = Profit.objects.filter(account_id = account_id)
    #    return HttpResponse('\n'.join(
    #        f"{p.date}: - {p.amount} ({p.duration} days)"
    #        for p in profits
    #    ))
    #elif  request.method == 'POST':
    #    Profit.objects.create(
    #        account_id = account_id,
    #        title = request.POST.get('title'),
    #        duration = request.POST.get('duartion')
    #    )
    #    return HttpResponse("proft reccord created",status = 201 )
    #
    #return HttpResponseNotAllowed(['GET', 'POST'])


        


    
