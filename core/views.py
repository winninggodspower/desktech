from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def training(request):
    return render(request, 'training.html')

def services(request):
    services = [
        {
            'title': 'Social Media Management',
            'description': 'Managing brand presence across Facebook, Instagram, LinkedIn, X (Twitter), and TikTok with scheduled posts, analytics, and content strategies.',
            'icon_path': 'icons/social-media.svg'
        },
        {
            'title': 'Content Creation & Copywriting',
            'description': 'Boosting website visibility on Google and other search engines through on-page optimization, keyword strategy, and content enhancement.',
            'icon_path': 'icons/brand-strategy.svg'
        },
        {
            'title': 'Influencer Marketing',
            'description': 'Partnering with credible influencers to expand reach and build authentic brand connections.',
            'icon_path': 'icons/social-media.svg'
        },
        {
            'title': 'Analytics & Reporting',
            'description': 'Detailed monthly reports tracking growth, engagement, and campaign performance.',
            'icon_path': 'icons/brand-strategy.svg'
        },
        {
            'title': 'Search Engine Optimization (SEO)',
            'description': 'Boosting website visibility on Google and other search engines through on-page optimization, keyword strategy, and content enhancement.',
            'icon_path': 'icons/social-media.svg'
        },
        {
            'title': 'Pay-Per-Click Advertising (PPC)',
            'description': 'Running high-conversion campaigns on Google Ads, Meta Ads, and other digital ad platforms to reach targeted audiences.',
            'icon_path': 'icons/brand-strategy.svg'
        },
        {
            'title': 'Brand Strategy & Consultation',
            'description': 'Helping clients define their digital identity, tone, and long-term growth roadmap.',
            'icon_path': 'icons/brand-strategy.svg'
        },
        {
            'title': 'Email Marketing & Automation',
            'description': 'Building and managing mailing lists, designing newsletters, and automating email campaigns for consistent engagement.',
            'icon_path': 'icons/brand-strategy.svg'
        },
    ]
    return render(request, 'services.html', {'services': services})

def job(request):
    return render(request, 'jobs.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact_us.html')

def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')
