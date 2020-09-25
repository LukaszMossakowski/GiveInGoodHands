from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import authenticate, login
from django.core.mail import EmailMessage
from django.db.models import Sum, Count, Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from accounts.forms import LoginForm, UserRegistrationForm, EditProfileForm
from give_in_good_hands.models import Donation, Institutions, MyUser
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_generator, generate_token


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "registration/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['email'], password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("landing_page")
                else:
                    return HttpResponse("Konto jest zablokowane")
            else:
                return redirect("register")
        else:
            return render(request, "registration/login.html", {"form": form})


class RegisterView(View):
    def get(self, request):
        user_form = UserRegistrationForm()
        return render(request, "registration/register.html", {"user_form": user_form})

    def post(self, request):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            domain = get_current_site(request).domain
            uidb64 = urlsafe_base64_encode(force_bytes(new_user.pk))
            link = reverse('activate', kwargs={'uidb64': uidb64, 'token': token_generator.make_token(new_user)})
            activate_url = 'http://' + domain + link

            email_subject = f"email rejestracyjny z witryny: Give in good hands: {new_user.first_name} {new_user.last_name}"
            email_body = f"Witaj {new_user.first_name} kliknij w poniższy link aby aktywować Twoje konto:\n" \
                         + activate_url
            email = EmailMessage(
                email_subject,
                email_body,
                'mossakowskilukasz@gmail.com',  # email from
                (new_user.email,),  # email to,
            )
            email.send(fail_silently=False)

            return redirect('login')
        return render(request, "registration/register.html", {"user_form": user_form})


class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = MyUser.objects.get(pk=uid)
            token = token
        except Exception as identifier:
            user = None

        if user is not None and token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('login')
        return redirect('register')


class ProfileView(View):
    def get(self, request):
        donations = Donation.objects.filter(user=request.user).order_by('is_taken', 'id')
        user_sum = Donation.objects.filter(user=request.user).aggregate(sum_pop=Sum('quantity'))
        lista = Institutions.objects.annotate(num_donations=Count('donation', filter=Q(donation__user=request.user)))
        result2 = len(list(filter(lambda x: x.num_donations > 0, lista)))
        return render(request, "profile.html", {"user": request.user, "user_sum": user_sum['sum_pop'],
                                                "given_institutions": result2, "donations": donations})

    def post(self, request):
        a = request.POST.get("change_status")
        donation = Donation.objects.get(pk=a)
        if donation.is_taken == "zabrane":
            donation.is_taken = "niezabrane"
        else:
            donation.is_taken = "zabrane"
        donation.save()
        return redirect("user_profile")


class EditProfileView(View):
    def get(self, request):
        form = EditProfileForm(instance=request.user)
        return render(request, "edit_profile.html", {"form": form})

    def post(self, request):
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("user_profile")
        return render(request, "edit_profile.html", {"form": form})
