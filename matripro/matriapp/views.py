from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from matriapp.forms import Step1_Form,Step2_Form,Step3_Form,Step4_Form,Photo_form
from matriapp.models import Matrimonydata,Photos,Castee,Subcastee,Heightt,MotherTonguee,Weightt,Starr,Raasii,Countryy,Statee,Cityy,Agee,Ageto,Religionn,Profile,Preheightt
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request,'index.html')

def myprofile(request,slug):
    myp = Matrimonydata.objects.get(slug=slug)
    return render(request,'my profile.html',{'ss':myp})

def myhome(request):
    ak = Matrimonydata.objects.all()
    prop = Matrimonydata.objects.all()
    return render(request,'myhome.html',{'save':ak,'pro':prop})

@login_required
def selfprofile(request,slug):
    sp1 = Matrimonydata.objects.get(slug=slug)
    prop = Matrimonydata.objects.all()
    phot_data = Photos.objects.all()
    return render(request,'selfprofile.html',{'sp':sp1,'pro':prop,'pics':phot_data}) 

@login_required
def photos(request):
    phot_data = Photos.objects.all()
    if request.method == "POST":
        form = Photo_form(request.POST, request.FILES)
        if form.is_valid():
            photo_obj = form.save()
            photo_obj.user = request.user
            photo_obj.save()
            return redirect('photos')
        else:
            form = Photo_form()
            return render(request, 'photos.html', {'form': form})    
    else:
        form = Photo_form()
        return render(request,'photos.html', {'form': form,'pics':phot_data})

def delete_photo(request, id): 
    obj = Photos.objects.get(id = id)
    obj.delete() 
    return redirect(photos)


def profiles(request):
    return render(request,'profiles.html')

def search(request):
    return render(request,'search.html')
  


@login_required
def step1(request):
    if request.method == "POST":
        form = Step1_Form(request.POST or {})
        
        if form.is_valid():
            matri_obj = form.save()
            matri_obj.user = request.user
            matri_obj.save()
            return redirect('step2', matri_uuid=matri_obj.uuid)
        else:
            form = Step1_Form()
            return render(request, 'step1.html', {'form': form})    
    else:
        form = Step1_Form()
        return render(request,"step1.html",{'form':form,'viewtab':'step1','slug':None})

def step2(request,matri_uuid):
    matri_obj = get_object_or_404(Matrimonydata, uuid=matri_uuid)
    if request.method == "POST":
        form = Step2_Form (request.POST or {}, instance=matri_obj)
        if form.is_valid():
            matri_obj = form.save()
            return redirect('step3', matri_uuid=matri_obj.uuid)
        else:
            form = Step2_Form()
            return render(request, 'step2.html', {'form': form})    
    else:
        form = Step2_Form(instance=matri_obj)
    return render(request,"step2.html",{'form':form,'viewtab':'step2','slug':None,'matri_obj':matri_obj})


def step3(request,matri_uuid):
    matri_obj = get_object_or_404(Matrimonydata, uuid=matri_uuid)
    if request.method == "POST":
        form = Step3_Form (request.POST or {}, instance=matri_obj)
        if form.is_valid():
            matri_obj = form.save()
            return redirect('step4', matri_uuid=matri_obj.uuid)
        else:
            form = Step3_Form()
            return render(request, 'step3.html', {'form': form})    
    else:
        form = Step3_Form(instance=matri_obj)
    return render(request,"step3.html",{'form':form,'viewtab':'step3','slug':None,'matri_obj':matri_obj})


def step4(request,matri_uuid):
    matri_obj = get_object_or_404(Matrimonydata, uuid=matri_uuid)
    if request.method == "POST":
        form = Step4_Form (request.POST or {}, instance=matri_obj)
        if form.is_valid():
            matri_obj = form.save()
            return redirect('myhome')
        else:
            form = Step4_Form()
            return render(request, 'step4.html', {'form': form})    
    else:
        form = Step4_Form(instance=matri_obj)
    return render(request,"step4.html",{'form':form,'viewtab':'step4','slug':None,'matri_obj':matri_obj})    

def matridata_edit(request,matri_uuid):
    matri_obj = get_object_or_404(Matrimonydata, uuid=matri_uuid)
    if request.method == "POST":
        form = Step1_Form(request.POST, instance=matri_obj)
        if form.is_valid():
            matri_obj = form.save()
            return redirect('step2', matri_uuid=matri_obj.uuid)
    else:
        form = Step1_Form(instance=matri_obj)
        mothertonguee_objects = MotherTonguee.objects.all()
        castee_objects = Castee.objects.all()
        subcastee_objects = Subcastee.objects.all()
        heightt_objects = Heightt.objects.all()
        preheightt_objects = Preheightt.objects.all()
        weightt_objects = Weightt.objects.all()
        starr_objects = Starr.objects.all()
        raasii_objects = Raasii.objects.all()
        countryy_objects = Countryy.objects.all()
        statee_objects = Statee.objects.all()
        cityy_objects = Cityy.objects.all()
        agee_objects = Agee.objects.all()
        ageto_objects = Ageto.objects.all()
        religionn_objects = Religionn.objects.all()
        return render(request,"step1.html",{
        'form':form,'viewtab':'Basic Details','slug':None,'mothertonguee_objects':mothertonguee_objects,'castee_objects':castee_objects,
        'subcastee_objects':subcastee_objects,'heightt_objects':heightt_objects,'preheightt_objects':preheightt_objects,'weightt_objects':weightt_objects,
        'starr_objects':starr_objects,'raasii_objects':raasii_objects,'countryy_objects':countryy_objects,'statee_objects':statee_objects,'cityy_objects':cityy_objects,
        'agee_objects':agee_objects,'ageto_objects':ageto_objects,'religionn_objects':religionn_objects})





# def edit(request, id):
#     matri = Matridata.objects.get(id=id)
#     return render(request, "edit.html", {'matri': matri})

# def update(request, id):
#     matri = Matridata.objects.get(id=id):
#     form = MatriForm(request.POST, request.FILES, instance = matri)
#     if form.is_valid():
#         form.save()
#         return redirect(myprofile)
#     else:
#         return render(request, "edit.html", {'matri': matri})

# def delete(request, id):
#     matri = Matridata.objects.get(id=id):
#     matri.delete()
#     return redirect(myprofile)









#Login_Authetications

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        profilepic = request.FILES['profilepic']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirmpass']
        if password1 == password2:

            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists")
                return render(request, 'index.html')
            else:

                user=User.objects.create_user(username=email,first_name=firstname,last_name=lastname,email=email,password=password1)
                Profile.objects.create(user=user,pic=profilepic)
                user=authenticate(username=email,password=password1)
                auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                if user:
                    messages.success(request, "Registered successfully")
                    return redirect(step1)
        else:
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['password']
        user= auth.authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login successfull")
            return redirect(myhome)
        else:
            messages.error(request, "Invalid credentials")
            return render(request, 'index.html')
    else:
        return redirect(login)



def logout(request):
    auth_logout(request)
    return redirect('/')    





def photo_save(request,matri_uuid):
    matri_obj = get_object_or_404(Matrimonydata, uuid=matri_uuid)
    if request.method == "POST":
        form = Photo_form (request.POST or {}, instance=matri_obj)
        if form.is_valid():
            matri_obj = form.save()
            return redirect('photos')
        else:
            form = Photo_form()
            return render(request, 'photos.html', {'form': form})    
    else:
        form = Step3_Form(instance=matri_obj)
    return render(request,"photos.html",{'form':form,'viewtab':'photos','slug':None,'matri_obj':matri_obj})