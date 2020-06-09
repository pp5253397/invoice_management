from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import AgentDetails, InvoiceDetails, ItemDetails
from .forms import InvoiceDetailsForm , ItemDetailsForm
from datetime import datetime
import smtplib 
import schedule 
import time 
from datetime import date 
from datetime import timedelta 

def index(request):

    if request.session.has_key('agent-name'):
        agent_name = request.session['agent-name']
        if request.method == "POST" and request.FILES['pdf-file']:
            form = InvoiceDetailsForm(request.POST, request.FILES)
            if form.is_valid():
                model = InvoiceDetails()
                model.pdf = request.FILES['pdf-file']
                model.agent_name = agent_name
                model.save()
                return redirect('invoice-form')
              
        
        return render(request,'user/index.html',{'agent_name':agent_name})
    else:
        return redirect('login')

def invoicedata(request):
    model = InvoiceDetails.objects.filter(agent_name = request.session['agent-name'])
    return render(request,'user/invoicedata.html',{'model':model})

def detailed_invoice(request,id):
    if request.session.has_key('agent-name'):
        agent_name = request.session['agent-name']
        model = InvoiceDetails.objects.get(id=id)
        items_get = ItemDetails.objects.filter(invoice_number = model.invoice_number)
        total = 0
        for i in items_get:
            total += i.item_rate

        return render(request,'user/detailed-invoice.html',{'model':model,'items':items_get,'total':total,'agent_name':agent_name})
    else:
        return redirect('login')
def invoiceformview(request):
    if request.session.has_key('agent-name'):
        agent_name = request.session['agent-name']
        item_model_all = None
        item_model = ItemDetails()
        model = InvoiceDetails.objects.latest('id')
        formset = ItemDetailsForm(request.POST, instance=model)
        pdf = model.pdf
        if request.method == "POST":
            item_model_all = ItemDetails.objects.filter(agent_name = request.session['agent-name']).filter(invoice_number = request.POST['invoice_number'])
            item_model.agent_name = request.session['agent-name']
            item_model.invoice_number = request.POST['invoice_number']
            item_model.item_description = request.POST['item_description']
            item_model.item_quantity = request.POST['item_quantity']
            item_model.item_rate = request.POST['item_rate']
            item_model.save()

            model.agent_name = request.session['agent-name']
            model.invoice_number = request.POST['invoice_number']
            model.vender_name = request.POST['vender_name']
            model.invoice_date = request.POST['invoice_date']
            model.upload_time = datetime.now()
            model.save()
        
        
            print(model.upload_time)
        return render(request,'user/invoice-form.html',{'pdf':pdf,'formset':formset,'model':model,'item':item_model_all,'agent_name':agent_name})
    else:
        return redirect('login')

def loginview(request):
    if request.method == 'POST':
        try:
            agent_data = AgentDetails.objects.get(email = request.POST['email'])
            if agent_data.password == request.POST['password']:
                request.session['agent-name'] = agent_data.full_name
                return redirect('index')
            else:
                return HttpResponse('<h3><a href = ''>Password Is Incorrect</a></h3>')
        except:
            return HttpResponse('<h3><a href = ''>Email not Found</a></h3>')

    return render(request,'user/login.html')

def logout(request):
    if request.session.has_key('agent-name'):
        del request.session['agent-name']
        return redirect('login')
    else:
        return redirect('login')

def delete_item(request,id):
    obj = ItemDetails.objects.get(id=id)
    obj.delete()
    return redirect('invoice-form')

def invoice_email(request):
    if request.session.has_key('agent-name'):
        model = InvoiceDetails.objects.latest('id')
        agent_name = request.session['agent-name']
       
        invoice = model.invoice_number
        time = model.upload_time
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login("YOUR EMAIL", "YOUR PASSWORD")
        message = f'''
        A New Invoice has been created\n
        Invoice Id: { invoice }\n
        Agent Name: { agent_name }\n
        Time: { time }
        '''
        s.sendmail("YOUR EMAIL", "RECEIVER EMAIL", message) 
        s.quit() 
        return redirect('index')
    else:
        return redirect('login')


    # # Get today's date 
    # today = date.today() 
    # print("Today is: ", today) 
    
    # # Yesterday date 
    # yesterday = today - timedelta(days = 1) 
    # model = InvoiceDetails.objects.filter(invoice_date = yesterday)
    
    # total_invoice = 0
    # total_invoice = InvoiceDetails.objects.filter(invoice_date = yesterday).count()
    # tota_amount = 0
    # for i in model:
    #     item = ItemDetails.objects.get(invoice_number = i.invoice_date)
    #     total_amount += i.item_rate
    # print(total_amount , total_invoice)

