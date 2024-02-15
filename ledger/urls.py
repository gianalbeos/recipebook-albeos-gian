from django.urls import path 
from .views import recipe_list, recipe_1, recipe_2

urlpatterns = [
    path('recipes/list/', recipe_list, name='recipes'),
    path('recipe/1/', recipe_1, name='recipe'),
    path('recipe/2/', recipe_2, name='recipe'),
]

app_name = 'ledger'