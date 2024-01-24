from django.shortcuts import render,redirect
from time import strftime
from . models import Scarp_Material
import random
import string
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.sessions.models import Session

# Create your views here.


Material=Scarp_Material.objects.all()


def index(request):
    us=request.user.username
    Material=Scarp_Material.objects.all()
    n:int =0
    n1:int =0
    if us == '' :
        for mat in Material:
            if mat.pending_with == "Manufacturing" :
                n1=n1+1
        return render(request,'index.html',{'Material':Material,'numbers':n1})
   
    us=request.user.username
    
    for mat in Material:
        if mat.pending_with == us :
            n=n+1
    return render(request,'index.html',{'Material':Material,'numbers':n})


def man_submit(request):
    Scarp=Scarp_Material.objects.all()

    if request.method == "POST":
        date=strftime("%Y-%m-%d")
        da=random.randint(0,1000)
        date_q=strftime("%y%m%d")
        doc_no= date_q+str(da)
        doc_no=int(doc_no)
        if Scarp_Material.objects.filter(doc_no = doc_no).exists():
            messages.info(request,'Document no taken')
            return redirect('submit')
           
        else:
            department= request.POST['department']
            category=request.POST['category']
            location=request.POST['location']
            identified_by=request.POST['identified_by']
            item_warehouse=request.POST['item_warehouse']
            item_code=request.POST['item_code']
            quantity=request.POST['quantity']
            unit=request.POST['unit']
            reason=request.POST['reason']
            man_img=request.FILES['man_img']
            superviser_name=request.POST['superviser_name']
            approved_by=request.POST['approved_by']
            pending_with='Planning'
            if quantity.isdigit():
                if department != 'Select' and category != 'Select':

                        
                    Man_Data= Scarp_Material(date=date,doc_no=doc_no,department=department,category=category,location=location,
                                        identified_by=identified_by,item_warehouse=item_warehouse,item_code=item_code,
                                        quantity=quantity,unit=unit,reason=reason,man_img=man_img,superviser_name=superviser_name,
                                        approved_by=approved_by,pending_with=pending_with)
                    Man_Data.save();
                    
                    messages.info(request,doc_no)
                    return redirect('submit')
                    

                else:
                    messages.info(request,'Please select department or category')
                    return redirect('submit')

            
            else:
                messages.info(request,'Enter a valid quantity')
                return redirect('submit')

    else:
        return render(request,'submit.html')





def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.SESSION_KEY
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/',{'user':user})

        else:
            messages.info(request,'invelid crendential')
            return redirect('login')

    else:
        return render(request,'login.html')



def logout(request):
    auth.logout(request)
    return redirect('/')




def action(request):
    doc_no=int(request.GET['doc_no'])
    Material=Scarp_Material.objects.all()
    return render(request,'action.html',{'Material':Material,'doc_no':doc_no})



def p_approve(request):
    if request.user.first_name('Planning'):
        doc_no=int(request.GET['doc_no'])
        return render(request,'p_approve.html',{'doc_no': doc_no })

def p_submit(request):
    if request.method == 'POST':
        doc_no=request.POST['doc_no']
        planner_name=request.POST['planner_name']
        order_no=request.POST['order_no']
        pos_no=request.POST['pos_no']
        u=Scarp_Material.objects.get(doc_no=doc_no)
        u.planner_name=planner_name
        u.order_no=order_no
        u.planner_name=planner_name
        u.pos_no=pos_no
        u.pending_with='Store1'
        u.save()
        return redirect('/')


    else:
        return render(request,'p_approve.html')


def q_approve(request):
    doc_no=int(request.GET['doc_no'])
    return render(request,'q_approve.html',{'doc_no': doc_no })

def q_submit(request):
    if request.method == 'POST':
        doc_no=request.POST['doc_no']
        qa_disposition=request.POST['qa_disposition']
        qa_classification=request.POST['qa_classification']
        qa_name=request.POST['qa_name']
        qa_engineer=request.POST['qa_engineer']
        qa_remark=request.POST['qa_remark']
        if qa_classification=='Select' or qa_disposition=='Select':
            messages.info(request,'select classification or disposition')
            return render(request,'q_approve.html',{'doc_no':doc_no})

        else:
            u=Scarp_Material.objects.get(doc_no=doc_no)
            u.qa_classification=qa_classification
            u.qa_diposition=qa_disposition
            u.qa_name=qa_name
            u.qa_engineer=qa_engineer
            u.qa_remark=qa_remark
            u.pending_with='Store2'
            u.save()
            return redirect('/')

        return redirect('/')

    else:
        return render(request,'q_approve.html')

def s1_approve(request):
    doc_no=int(request.GET['doc_no'])
    return render(request,'s1_approve.html',{'doc_no': doc_no })

def s1_submit(request):
    if request.method == 'POST':
        doc_no=request.POST['doc_no']
        store1_name=request.POST['store1_name']
        material_received=request.POST['material_received']
        erp_person=request.POST['erp_person']
        store1_img=request.FILES['store1_img']
        if material_received == 'Select':
            messages.info(request,'select material received or not')
            return render(request,'s1_approve.html',{'doc_no':doc_no})

        else:
            u=Scarp_Material.objects.get(doc_no=doc_no)
            u.store1_name=store1_name
            u.material_received=material_received
            u.erp_person=erp_person
            u.store1_img=store1_img
            u.pending_with='Quality'
            u.save()
            return redirect('/')

    else:
        return render(request,'s1_approve.html')

def s2_approve(request):
    doc_no=int(request.GET['doc_no'])
    return render(request,'s2_approve.html',{'doc_no': doc_no })

def s2_submit(request):
    if request.method == 'POST':
        doc_no=request.POST['doc_no']
        store2_disposition=request.POST['store2_disposition']
        store2_name=request.POST['store2_name']
        store2_orderno=request.POST['store2_orderno']
        store2_ordernumber=request.POST['store2_ordernumber']
        supplier_name=request.POST['supplier_name']
        if store2_disposition == 'Select':
            messages.info(request,'select disposition')
            return render(request,'s2_approve.html',{'doc_no':doc_no})


        else:
            u=Scarp_Material.objects.get(doc_no=doc_no)
            u.store2_disposition=store2_disposition
            u.store2_name=store2_name
            u.store2_orderno=store2_orderno
            u.store2_ordernumber=store2_ordernumber
            u.supplier_name=supplier_name
            u.pending_with='Complete'
            u.save()
            return redirect('/')

    else:
        return render(request,'s2_approve.html')

def rejection(request):
    doc_no=int(request.GET['doc_no'])
    return render(request,'rejection.html',{'doc_no': doc_no })



def rejection_update(request):
    if request.method == "POST":
        doc_no=request.POST['doc_no']
        rejection_name=request.POST['rejection_name']
        rejection_reason=request.POST['rejection_reason']
        
            
        u=Scarp_Material.objects.get(doc_no=doc_no)
        u.rejection_name=rejection_name
        u.rejection_reason=rejection_reason
        u.pending_with='Manufacturing'
        
        u.save()
        return redirect('/')

    else:
        return render(request,'rejection.html')

def man_update(request):
    doc_no=int(request.GET['doc_no'])
    Material=Scarp_Material.objects.all()
    return render(request,'man_update.html',{'Material':Material,'doc_no': doc_no })


def man_update_submit(request):
    if request.method == "POST":
        doc_no=request.POST['doc_no']
        department= request.POST['department']
        category=request.POST['category']
        location=request.POST['location']
        identified_by=request.POST['identified_by']
        item_warehouse=request.POST['item_warehouse']
        item_code=request.POST['item_code']
        quantity=request.POST['quantity']
        unit=request.POST['unit']
        reason=request.POST['reason']
        
        superviser_name=request.POST['superviser_name']
        approved_by=request.POST['approved_by']
        pending_with='Planning'
        if quantity.isdigit():
            u=Scarp_Material.objects.get(doc_no=doc_no)
            u.department=department
            u.category=category
            u.location=location
            u.identified_by=identified_by
            u.item_warehouse=item_warehouse
            u.item_code=item_code
            u.quantity=quantity
            u.unit=unit
            u.reason=reason
            if len(request.FILES) != 0:
                man_img=request.FILES['man_img']
                u.man_img=man_img
            u.superviser_name=superviser_name
            u.approved_by=approved_by
            u.pending_with=pending_with
            u.save()
            return redirect('/')




        else:
            messages.info(request,'Enter a valid quantity')
            return render(request,'man_update.html')

    else:
        return render(request,"man_update.html")