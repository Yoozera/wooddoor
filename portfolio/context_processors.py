from .models import PortfolioTag, PortFolioCategory, Portfolio, InstagramGallery


def sidebar_data(request):
    return {
        'all_tags': PortfolioTag.objects.all(),
        'categories': PortFolioCategory.objects.all(),
        'recent_news': Portfolio.objects.filter(is_active=True).order_by('-created_at')[:5],
        'instagram_image': InstagramGallery.objects.all()[:6],
    }