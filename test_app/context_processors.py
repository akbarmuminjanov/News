from test_app.models import Category

def category(request):
    categories = Category.objects.all()
    return {"kategoriyalar": categories}