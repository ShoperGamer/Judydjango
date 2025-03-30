from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import person
from django.contrib import messages

def index(request):
    all_person = person.objects.all()
    return render(request, "index.html", {"all_person": all_person})

def about(request):
    return render(request, "about.html")

def form(request):
    if request.method == "POST":
        # รับข้อมูล
        name = request.POST["name"] 
        age = request.POST["age"]

        # ตรวจสอบข้อมูลที่จำเป็น
        if not name or not age:
            messages.error(request, "กรุณากรอกข้อมูลให้ครบถ้วน")
            return redirect("form")
            
        try:
            age = int(age)
            # ตรวจสอบช่วงอายุ
            if age < 1 or age > 200:
                messages.error(request, "อายุต้องอยู่ระหว่าง 1-200 ปี")
                return redirect("form")
                
        except ValueError:
            messages.error(request, "อายุต้องเป็นตัวเลขเท่านั้น")
            return redirect("form")

        # บันทึกข้อมูล
        new_person = person.objects.create(
            name=name,
            age=age,
        )
        new_person.save()
        messages.success(request,"บันทึกข้อมูลเรียบร้อย")
        # กลับหน้าแรก
        return redirect("index")  # ใช้ชื่อ URL pattern
    
    return render(request, "form.html")  # แก้ไข path



def edit(request, person_id):
    person_obj = get_object_or_404(person, id=person_id)
    
    if request.method == "POST":
        person_obj.name = request.POST["name"]
        person_obj.age = request.POST["age"]
        person_obj.save()
        messages.success(request, "อัปเดตข้อมูลเรียบร้อยแล้ว")
        return redirect("index")
    
    #ดึงข้อมูลประชากรเพื่อแก้ไข
    else:
        Person = person.objects.get(id=person_id)
        return render(request, "edit.html", {"person": Person})
    
#ลบข้อมูล
def delete(request, person_id):
    person_obj = get_object_or_404(person, id=person_id)
    person_obj.delete()
    messages.success(request, "ลบข้อมูลเรียบร้อยแล้ว")
    return redirect("index")
    
