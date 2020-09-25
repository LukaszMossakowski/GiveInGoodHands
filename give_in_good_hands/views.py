from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.db.models import Sum, Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from give_in_good_hands.models import Donation, Institutions, Category, MyUser


class LandingPageView(View):
    def get(self, request):
        result1 = Donation.objects.aggregate(sum_pop=Sum('quantity'))
        lista = Institutions.objects.annotate(num_donations=Count('donation'))
        result2 = len(list(filter(lambda x: x.num_donations > 0, lista)))
        foundation = Institutions.objects.filter(type="fundacja").order_by("id")
        non_governmental = Institutions.objects.filter(type="organizacja_pozarządowa")
        local = Institutions.objects.filter(type="zbiórka_lokalna")

        paginator = Paginator(foundation, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        paginator2 = Paginator(non_governmental, 5)
        page_number2 = request.GET.get('page')
        page_obj2 = paginator2.get_page(page_number2)

        paginator3 = Paginator(local, 5)
        page_number3 = request.GET.get('page')
        page_obj3 = paginator3.get_page(page_number3)

        return render(request, "index.html", {'result1': result1['sum_pop'], "result2": result2,
                                              "foundations": foundation,
                                              "page_obj": page_obj,
                                              "non_governmentals": non_governmental,
                                              "page_obj2": page_obj2,
                                              "locals": local,
                                              "page_obj3": page_obj3})


@login_required
def add_donation_view(request):
    # if request.is_ajax():
    #     if form.is_valid:
    # try:
    #     quantity = request.POST.get("bags")
    #     categories_id = request.POST.getlis("categories")
    #     institution_id = request.POST.get("organization")
    #     address = request.POST.get("address")
    #     phone = request.POST.get("phone")
    #     city = request.POST.get("city")
    #     zip_code = request.POST.get("postcode")
    #     pick_up_date = request.POST.get("date")
    #     pick_up_time = request.POST.get("time")
    #     pick_up_comment = request.POST.get("more_info")
    #     donation = Donation.objects.create(quantity=quantity, address=address, phone_number=phone, city=city,
    #                                        zip_code=zip_code, pick_up_date=pick_up_date, pick_up_time=pick_up_time,
    #                                        pick_up_comment=pick_up_comment, user=request.user)
    #     donation.categories.set(categories_id)
    #     donation.institution.set(institution_id)
    #     return JsonResponse({})
    # except:
    #     if request.method == "GET":
    #         categories = Category.objects.all()
    #         institutions = Institutions.objects.all()
    #         return render(request, "form.html", {"categories": categories, "institutions": institutions})
    # return HttpResponse("failed")


    if request.method == "GET":
        categories = Category.objects.all()
        institutions = Institutions.objects.all()
        return render(request, "form.html", {"categories": categories, "institutions": institutions})

    if request.is_ajax():
        if request.method == "POST":
            quantity = request.POST.get("bags")
            categories_id = request.POST.getlist("categories")
            institution_id = request.POST.get("organization")
            institution=Institutions.objects.get(pk=institution_id)
            address = request.POST.get("address")
            phone = request.POST.get("phone")
            city = request.POST.get("city")
            zip_code = request.POST.get("postcode")
            pick_up_date = request.POST.get("date")
            pick_up_time = request.POST.get("time")
            pick_up_comment = request.POST.get("more_info")
            user=MyUser.objects.get(id=request.user.id)
            donation = Donation.objects.create(quantity=quantity, address=address, phone_number=phone, city=city,
                                               zip_code=zip_code, pick_up_date=pick_up_date, pick_up_time=pick_up_time,
                                               pick_up_comment=pick_up_comment, institution=institution,user=user)
            donation.categories.set(categories_id)
            # donation.institution.set(institution_id)
            # donation.user.set()
            return JsonResponse({})


class ContactView(View):
    def post(self, request):
        first_name = request.POST.get("name")
        last_name = request.POST.get("surname")
        message = request.POST.get("message")

        superuser = list(MyUser.objects.filter(is_admin=True))
        for user in superuser:
            send_mail(
                f"email from give in good hands contact form send by: {first_name} {last_name}",
                message,
                'mossakowskilukasz@gmail.com',  # email from
                (user.email,),  # email to,
                fail_silently=False
            )
        return redirect("landing_page")


class ThankYouView(View):
    def get(self, request):
        return render(request, "form-confirmation.html")