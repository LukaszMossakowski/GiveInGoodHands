from django.urls import path, include
from give_in_good_hands import views

urlpatterns=[
    path('adddonation/', views.add_donation_view, name="add_donation"),
    path('thank_you/', views.ThankYouView.as_view(), name="thank_you"),
    path('contact/', views.ContactView.as_view(), name="contact_form")
]
