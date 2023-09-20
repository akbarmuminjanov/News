from django.urls import path
from .views import main_page, batafsil_page, category_page, add_news_page, add_category, admin_page, del_news, news_holati


urlpatterns = [
    path('',main_page, name="home-page"),
    path('category/<int:cat_id>',category_page, name="category-page"),
    path('batafsil/<int:id>', batafsil_page, name="batafsil-page"),
    path('addnews/', add_news_page, name="add-news-page"),
    path('addcate/', add_category, name="add-category-page"),
    path('adminpage/', admin_page, name="admin-page"),
    path('adminpage/delete/<int:news_id>', del_news, name="del-page"),
    path('adminpage/change/<int:news_id>', news_holati, name="change-page"),
]


