from django.shortcuts import render,redirect, get_object_or_404
from .models import Lender,Slot,Borrower
from django.http import HttpResponse
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa
from django.views.generic import View

# Create your views here.

def home(request):
	return render(request,'home.html')

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def create_pdf(request,pk):
	borrower = Borrower.objects.get(pk=pk)
	template = get_template('bill.html')
	html = template.render({'borrower': borrower})
	pdf = render_to_pdf('bill.html',{'borrower': borrower})
	return HttpResponse(pdf,content_type='application/pdf')


def booking(request):
	if request.method == "POST":
		date = request.POST['date']
		time = request.POST['time']
		if date and time:
			slots = Slot.objects.filter(date=date,time=time,count__gte=1)
			if slots:
				return render(request,'booking.html',{'ok_message':"Yes Specified Slot Is Available",'slots':slots})
			else:
				slots = Slot.objects.filter(count__gte=1)
				if slots:
					return render(request,'booking.html',{'no_slot_of_time_date':"No Any Free Slot For That Date and Time",'appology': "Sorry For Inconvience.",'checking_other_slot':"You Can Check These Slots If You Want.",'slots':slots})
				else:
					return render(request,'booking.html',{'not_any_slot': "No Slot Is Available For Our Shop.",'appology': "Sorry For Inconvience."})
		else:
			return render(request,'booking.html')
	else:
		return render(request,'booking.html')




def log_in_as_borrower(request):
	if request.method == "POST":
		email = request.POST['email']
		roll_no = request.POST['roll_no']
		if email and roll_no:
			borrower = Borrower.objects.filter(email=email,roll_no=roll_no).first()
			if borrower:
				return render(request,'borrower_home.html',{'borrower':borrower})
			else:
				return render(request,'log_in_as_borrower.html',{'error': "Invalid Email or Roll No."})
		else:
			return render(request,'log_in_as_borrower.html')
	else:
		return render(request,'log_in_as_borrower.html')

def deal_done(request,pk):
	if request.method == 'POST':
		slot = Slot.objects.get(pk=pk)
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		date = slot.date
		time = slot.time
		roll_no = request.POST['roll_no']
		mobile = request.POST['mobile']
		stationary = request.POST['stationary']
		musical = request.POST['musical']
		book = request.POST['book']
		if first_name and last_name and email and mobile :
			borrower = Borrower(roll_no=roll_no,first_name=first_name,last_name=last_name,slot=slot,email=email,date=date,time=time,
									mobile=mobile,stationary=stationary,musical=musical,book=book)
		else:
			return render(request,'deal_done.html',{'pk':pk})
		borrower.save()
		if slot.count == 1:
			slot.c1 = borrower.pk
		elif slot.count == 2:
			slot.c2 = borrower.pk
		else:
			slot.c3 = borrower.pk
		slot.count = slot.count-1
		slot.save()
		return render(request,'deal_status.html',{'borrower':borrower })
	else:
		return render(request,'deal_done.html',{'pk':pk})

def borrower_sort(request,pk):
	lender = Lender.objects.get(pk=pk)
	date = request.POST["date"]
	time = request.POST.get('time', False)
	if request.method == 'POST':
		if date:
			borrower = Borrower.objects.filter(date=date)
			if time:
				borrower = borrower.filter(time=time)
			if borrower:
				return render(request,'lender.html',{'lender': lender,'borrower': borrower,'messagess':"Your Borrowing are ",'datee':date})
			else:
				return render(request,'lender.html',{'lender':lender,'messagess':"No Borrowers For Your Specified Slot"})
		else:
			return render(request,'lender.html',{'lender':lender})
	else:
		return render(request,'lender.html',{'lender':lender})

# try:
#     user = UniversityDetails.objects.get(email=email)
# except UniversityDetails.DoesNotExist:
#     user = None

def display_detail(request,pk):
	borrower = Borrower.objects.get(pk=pk)
	return render(request,'borrower_home.html',{'borrower': borrower})

def borrower_detail(request,pk):
	lender = Lender.objects.get(pk=pk)
	if request.method == "POST":
		roll_no = request.POST['roll_no']
		if roll_no:
			borrower = Borrower.objects.filter(roll_no=roll_no).first()
			if borrower:
				return render(request,'lender.html',{'lender':lender,'borrower':borrower,'found':"Yes"})
			else:
				return render(request, "lender.html", {'lender': lender, 'not_found' : "True"})
		else:
			return render(request,'lender.html',{'lender': lender })
	else:
		return render(request,'lender.html',{'lender': lender })

def log_in_as_lender(request):
	if request.method == "POST":
		email = request.POST["email"]
		password = request.POST["password"]
		if email and password:
			lender = Lender.objects.filter(password=password,email=email).first()
			if lender:
				return render(request,'lender.html',{'lender' : lender })
			else:
				return render(request,'log_in_as_lender.html',{'error_message': "Invalid User Id Or Password"})
		else:
			return render(request,'log_in_as_lender.html')
	else:
		return render(request,'log_in_as_lender.html')

def donation(request):
	return render(request,'donate.html')
