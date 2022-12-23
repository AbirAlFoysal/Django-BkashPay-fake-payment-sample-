from django.shortcuts import render

# Create your views here.

def bkashHome(request):
    if request.method == 'POST':
        amount = request.POST['amount']
        return render(request, 'bkash_number.html', {'amount': amount})
    return render(request, 'bkashHome.html')

def bkashNumber(request):
    return render(request, 'bkash_number.html')

def bkashPIN(request):
    return render(request, 'bkash_pin.html')

def bkashSuccess(request):
    return render(request, 'bkash_success.html')