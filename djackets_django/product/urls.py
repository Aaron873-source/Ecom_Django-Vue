from django.urls import path, include

from product import views


urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view()),
    #MAPPING URL PATH FOR PRODUCT DETAILS TO USE NEWLY MADE class based view ProductDetails as view 
    path('products/<slug:category_slug>/<slug:product_slug>/',views.ProductDetail.as_view())
]


