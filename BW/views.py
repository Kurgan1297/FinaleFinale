
from django.shortcuts import render, redirect
from django.views.generic import View

from django.core import paginator

from BW.models import Bikes
from BW.forms import FilterForm
from BW.crud import add_review, create_Order, add_item_to_order

class HomeView(View):
    def get(self, request):
        return render(request, 'greetings.html')
    
    def post(self, request):
        return render(request, "greetings.html")

class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')
    
    def post(self, request):
        return render(request, "about.html")

class ShopView(View):
    def get(self, request):

        form = FilterForm()

        bike_type = self.request.GET.get("bike_type", None)

        if bike_type is None:
            all_bikes = Bikes.objects.all()
        else:
            all_bikes = Bikes.objects.filter(bike_type=bike_type)

        bikes_p = paginator.Paginator(all_bikes, 6)
        page_now = request.GET.get("page")
        page_bikes = bikes_p.get_page(page_now)

        return render(request, 'store.html', context={
            "all_bikes": page_bikes,
            "filter_form": form
        })

    def post(self, request):
        return render(request, 'store.html')

    

class DescitptionView(View):
    def get(self, request, bikeid):

        bike_info = Bikes.objects.get(id=bikeid)    
        # add_review(request.user, review_description)

        return render(request, "bike_page.html", context={"bike_info":bike_info})

    def post(self, request, bikeid):
        raspakovka = request.POST.get("pridumal")
        request.session["velik"] = raspakovka

        return redirect("cart_page")
    
class OrderView(View):
    def get(self, request):
        raspakovka = Bikes.objects.get(id=request.session["velik"])

        return render(request, "order.html", context={"cart": raspakovka})

    def post(self, request):
        phone_number = request.POST.get("phone")
        card_number = request.POST.get("card")
        email = request.POST.get("email")
        User_Agreement = bool(request.POST.get("agreement"))

        if not User_Agreement:
            return redirect("main_store_page")
        
        return redirect("order_end_page")

class OrderEndView(View):   
    def get(self, request):
        return render(request, 'order_end.html')
    
    def post(self, request):
        pass
    

class CartView(View):
    def get(self, request):
        return render(request, "cart.html", context={"cart": request.session['cart']})

    def post(self, request, create_Order, add_item_to_order):
        order = create_Order(request.user)
        for item in request.session['cart']:
            product = Bikes.objects.get(id=item["Bikes.id"])
            add_item_to_order(order, product, item["count"])

        request.session['cart'] = []
        request.session['cart'].append({'product': Bikes.id, 'count': Bikes.bike_amount})
        
        return redirect("cart_page")

class MakeReviewView(View):
    def get(self, request, bikeid):
        return render(request, "make_review.html")

    def post(self, request, bikeid):
        rating = int(request.POST.get("rating")) 
        review_text = request.POST.get("review_text")
        user=request.user

        if user.is_authenticated == False:
            add_review(
                author=user,
                review_description=review_text,
                mark=rating,
                product_review=Bikes.objects.get(id=bikeid)
            )


        return redirect("bike_page", bikeid=bikeid)