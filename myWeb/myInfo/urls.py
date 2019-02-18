from django.urls import path,re_path
from . import views
urlpatterns = [#固定
    re_path('^index/$',views.index),
    re_path('^uploadFile/$',views.upload_file),
    re_path('^list/$',views.filelist),
    re_path('download/',views.download),
    re_path('^exam(\d+)/$',views.exam),

]