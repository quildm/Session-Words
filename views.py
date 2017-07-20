from django.shortcuts import render,redirect, HttpResponse
from time import gmtime, strftime

def index(request):
	try:
		request.session["words"]
	except:
		request.session["words"] = []
	
	return render(request,'session_words/index.html')

def process(request):
	if request.POST.get("font") == "font":
		fontsize = "big"
	else:
		fontsize = "regular"

	context = {
	"word": request.POST.get("word"),
	'color': request.POST.get('color'),
	"font": fontsize,
	"time": strftime("%I:%M:%S %p, %B %d %Y ", gmtime())
	}

	request.session["words"].append(context)
	request.session.modified = True  #allows to append information 
	print request.session['words']
	return redirect(request,'session_words/')

def clear(request):
	request.session.clear()
	return redirect(request,'session_words/')



