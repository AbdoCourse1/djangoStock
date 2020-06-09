from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages

# pk_fabc1e9a460b4b399f7ac8a7a672cf04 
# Create your views here.
def home(request):
	import requests
	import json

	if(request.method == 'POST'):
		
		ticker = request.POST['tickerSymbol']
		api_request = requests.get("https://cloud-sse.iexapis.com/stable/stock/"+ ticker +"/quote?token=pk_fabc1e9a460b4b399f7ac8a7a672cf04")
		try:
			api=json.loads(api_request.content)

		except Exception as e:
			api = "Error ..."
		context ={"api":api}
		return render(request, 'home.html',context)

	else:
		context ={"ticker":"Enter a ticker above"}
		return render(request, 'home.html',context)
		
	

def about(request):
	return render(request,'about.html', {})
	
def addStock(request):
	import requests
	import json

	if request.method == 'POST':
		form = StockForm(request.POST or None)
		
		if form.is_valid():
			form.save()
			#all_items = Stock.objects.all()
			messages.success(request,'item has been added to list!')
			#context={'ticker':all_items}
			#return render(request,'addStock.html',context)

	

	ticker = Stock.objects.all()
	output = []
	for tickerItem in ticker:
		api_request = requests.get("https://cloud-sse.iexapis.com/stable/stock/"+ str(tickerItem) +"/quote?token=pk_fabc1e9a460b4b399f7ac8a7a672cf04")
		try:
			api=json.loads(api_request.content)
			output.append(api)

		except Exception as e:
			api = "Error"
			output.append(api)
	
	#context={'ticker':ticker,'output':output}
	context={'ticker':zip(ticker,output)}
	return render(request,'addStock.html',context)

def delete(request, stockId):
	item = Stock.objects.get(pk=stockId)
	item.delete()
	messages.success(request,("Stock has been deleted"))
	return redirect(addStock)

def deleteStock(request):

	ticker = Stock.objects.all()
	context={'ticker':ticker}
	return render(request,'deleteStock.html',context)

def delete1(request, stockId):
	item = Stock.objects.get(pk=stockId)
	item.delete()
	messages.success(request,("Stock has been deleted"))
	return redirect(deleteStock)