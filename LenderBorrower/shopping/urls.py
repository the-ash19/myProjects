from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
   path('home/',views.home),
   path('booking/',views.booking,name='booking'),
   path('booking/deal_done/<int:pk>/',views.deal_done,name='deal_done'),
   path('log_in_as_borrower/',views.log_in_as_borrower,name='log_in_as_borrower'),
   path('/create_pdf/<int:pk>/$',views.create_pdf,name='create_pdf'),
   path('log_in_as_lender/',views.log_in_as_lender,name='log_in_as_lender'),
   path('log_in_as_lender/borrower_detail/<int:pk>',views.borrower_detail,name='borrower_detail'),
   path('log_in_as_lender/borrower_sort/<int:pk>',views.borrower_sort,name='borrower_sort'),
   path('log_in_as_lender/display_detail/<int:pk>',views.display_detail,name='display_detail'),
   path('donation/',views.donation,name='donation')

]
