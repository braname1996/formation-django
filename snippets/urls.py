from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', snippet_list),
    path('snippets/<int:id>/', snippet_detail),

    path('products/', product_list),
    path('products/<int:pk>/', product_detail),

    ##### '''  url des views base sur les classes ''' #####
    path("produits/", list_produit.as_view()),
    path("produits/<int:pk>/", update_product.as_view()),

    ####### url des vue generic base sur les class #########

    path("snippetsList/", snippetList.as_view(), name="snippetsList"),
    path("snippetsList/<int:pk>", snippetDetail.as_view(), name="snippetsDetail"),
    



]

urlpatterns = format_suffix_patterns(urlpatterns)