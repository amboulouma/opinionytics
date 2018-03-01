from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from features.summary.SummaryGenerator import *
from features.topicsInvolved.TopicClassifier import *
from features.positivity.PositivityAnalyzer import *
from features.subjectivity.SubjectivityAnalyzer import *
from features.popularity.PopularityAnalyzer import *

from pytrends.request import TrendReq 
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, ConceptsOptions
from aylienapiclient import textapi



APP_ID = "8ebd4c0e"
APP_KEY = "707f70d4fe70e4e22210bfd824949ba9"

client = textapi.Client(APP_ID, APP_KEY)

USERNAME='ea1c5c7c-c39e-4af6-bcd5-b9103dc229a2'
PASSWORD='Xl21Xq1EeDwW'
VERSION='2017-02-27'

natural_language_understanding = NaturalLanguageUnderstandingV1(
    username=USERNAME,
    password=PASSWORD,
    version=VERSION)

pytrends = TrendReq(hl='en-US', tz=360)

summaryGenerator = SummaryGenerator(client)
subjectivityAnalyzer = SubjectivityAnalyzer(client)
positivityAnalyzer = PositivityAnalyzer(client)
topicsClassifier = TopicClassifier(client)
popularityAnalyzer = PopularityAnalyzer(pytrends, natural_language_understanding)

def index(request):
    return render(request, 'input.html')

def getText(request):
    result = ""
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('../../registration')
        text = request.POST.get('textfield', None)
        if len(text.split(" ")) > 50:
            result += str(subjectivityAnalyzer.getSubjectivity(text=text))
            result += str(positivityAnalyzer.getPositivity(text=text))
            result += str(topicsClassifier.getTopics(text=text))
            result += str(popularityAnalyzer.getPopularity(text=text))
            result += str(summaryGenerator.getSummary(text=text))
            return render(request, 'result.html', {'result': result})

        else:
            return HttpResponseRedirect("..")
