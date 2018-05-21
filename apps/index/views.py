from django.shortcuts import render

# Create your views here.
from django.views.generic import View

from index.models import Banner
from content.models import Article


class IndexView(View):
    def get(self, request):
        all_banner = Banner.objects.filter(is_banner=True).order_by('order')
        # image = Banner.objects.all()
        # author = Banner.objects.all()
        # title = Banner.objects.all()
        # text = Banner.objects.all()
        # time = Banner.objects.all()

        all_article = Article.objects.all()

        # article_author = Article.objects
        # article_category =
        # article_create_time =
        # article_title =
        # article_content =
        # article_image =
        # article_tag =
        return render(request, 'lw-index.html', {
            "all_banner": all_banner,
            "all_article": all_article,
        })
