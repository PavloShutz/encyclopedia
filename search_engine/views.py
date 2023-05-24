from django.shortcuts import render

from .parser import render_article
from .db_services import save_article


def index(request):
    """Render main page."""
    if request.method == "POST":
        word: str = request.POST.get("swrd")
        article = render_article(word)
        if word.strip() != '':
            save_article(word, article)
        return render(request, "index.html", context={"article": article})
    return render(
        request,
        "index.html",
        context={
            "article": "Тут будуть з'являтися слова, які тобі потрібно"
        }
    )
