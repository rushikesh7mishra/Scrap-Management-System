from django.urls import path
from . import views


urlpatterns=[

    path('',views.index,name='Manufacturing'),
    path('index',views.index,name='Manufacturing'),
    path('submit',views.man_submit,name='submit'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('action',views.action,name='action'),
    path('p_approve',views.p_approve,name='p_approve'),
    path('q_approve',views.q_approve,name='q_approve'),
    path('s1_approve',views.s1_approve,name='s1_approve'),
    path('s2_approve',views.s2_approve,name='s2_approve'),
    path('p_submit',views.p_submit,name='p_submit'),
    path('q_submit',views.q_submit,name='q_submit'),
    path('s1_submit',views.s1_submit,name='s1_submit'),
    path('s2_submit',views.s2_submit,name='s2_submit'),
    path('rejection',views.rejection,name='rejection'),
    path('rejection_update',views.rejection_update,name='rejection_update'),
    path('man_update',views.man_update,name='man_update'),
    path('man_update_submit',views.man_update_submit,name='man_update_submit'),
    
  
]