from django.shortcuts import render,get_object_or_404,redirect
from .models import Meal, Order
from .forms import MealForm, OrderForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DeleteView

# Create your views here.
def admin_home(request):
    posts_meal = Meal.objects.all()
    context={
        'posts_meal':posts_meal,
    }
    return render(request, 'order_list/index.html', context)

def home(request):
    posts_meal = Meal.objects.all()
    context={
        'posts_meal':posts_meal,
    }
    return render(request, 'order_list/index_users.html', context)


def meal_detail(request, meal_id):
    details = get_object_or_404(Meal, pk=meal_id)
    context={
        'details':details,
    }
    return render(request, 'order_list/detail.html',context)

def add_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, ' تم إضافة الوجبة الجديدة  بنجاح.')
            return  redirect('/')
    else:
        form = MealForm()
    context = {
        'form': form
    }
    return render(request, 'order_list/meal_add.html', context)

def update_meal(request, meal_id):
    posts_meal = get_object_or_404(Meal, pk=meal_id)
    if request.method == 'POST':
            form = MealForm(request.POST, instance = posts_meal)
            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.user = request.user
                new_form.save()
                messages.success(request, ' تم التعديل بنجاح.')
                return  redirect('/')
    else:
        form = MealForm(instance = posts_meal)
    context = {
        'form': form,
        'posts_meal':posts_meal,
            
        }
    return render(request, 'order_list/edit.html', context)

def order_form(request, meal_id):
    orders = Order.objects.filter()
    meal_data = get_object_or_404(Meal,pk=meal_id)
    if request.method == 'POST':
        form = OrderForm(request.POST,)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
             
            return  redirect('/success-order')
    else:
        form = OrderForm( initial = {'order': meal_id} )
    context = {
        'form': form,
        'orders':orders,
        'meal_data':meal_data,
    }
    return render(request, 'order_list/orderForm.html', context)
 

def list_order(request):
    order_lists = Order.objects.filter()
   
    context={
        'order_lists':order_lists,
    }
    return render(request, 'order_list/list_order_admin.html', context)

def success_order(request):
    return render(request, 'order_list/success.html')

class BlogDeleteView(DeleteView):
    model = Order
    template_name = 'order_list/deleted.html'
    success_url = reverse_lazy('list_order')
    

