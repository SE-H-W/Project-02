from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
 
from search.helpers.autocomplete import GenericDBSearchAutoCompleteHelper
from search.helpers.photo import UnplashCityPhotoHelper
from search.utils.search import AmadeusCitySearch
from search.utils.url import URL
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import render
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
 
 
@login_required
@require_http_methods(["GET"])
def main_page(request):
    user_count = get_user_model().objects.all().count()
    return render(request, "search/search.html", context={"request": request, "userCount": user_count})
 
 
@require_http_methods(["GET"])
def city_suggestions(request):
    suggestions_data = GenericDBSearchAutoCompleteHelper(
        klass=AmadeusCitySearch, url=URL(**settings.AMADEUS_CONFIG)
    ).get_suggestions(city=request.GET.get("q"), max=10)
 
    return JsonResponse({"results": suggestions_data.get("data", [])})
 
 
@require_http_methods(["GET"])
def city_photo(request):
    photo_link = UnplashCityPhotoHelper().get_city_photo(
        city=request.GET.get("q")
    )
    return JsonResponse(
        {
            "path": photo_link,
        }
    )


def initialize_gemini_llm():
    api_key = 'AIzaSyCQuxhdViKd_-H1CQxEpFsgsHEolKLEN7w' 
    if not api_key:
        raise Exception("Gemini API Key not set. Please configure the key.")
    my_llm = ChatGoogleGenerativeAI(model='gemini-pro', api_key=api_key)
    return my_llm

def city_info(request, city_name):
    itinerary = None  # To store the generated itinerary
    if request.method == 'POST':
        
        days = request.POST.get('days')
        my_llm = initialize_gemini_llm()
        my_prompt = PromptTemplate.from_template('Create an itinerary for {placename} for {num} days')
        chain = LLMChain(llm=my_llm, prompt=my_prompt, verbose=False)
        inputs = {'placename': city_name, 'num': days}
        response = chain.invoke(input=inputs)
        itinerary = response
        return render(request, 'info/itinerary.html', {
            'city': city_name,
            'itinerary': itinerary
        })
