from django.urls import path
from sqldj.apiviews.export_whitelisted_data import FetchWhiteListedData , PostWhiteListedData
urlpatterns = [
	path('fetch',FetchWhiteListedData.as_view(),name='fetch data'),
	path('post',PostWhiteListedData().as_view(),name='post data'),
]