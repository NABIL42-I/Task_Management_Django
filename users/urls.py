from django.urls import path
from users.views import sign_up,sign_in,sign_out,activate_user,admin_dashboard,assign_role,create_group,group_list,CustomLoginView,ProfileView,ChangePassword
from users.views import CustomResetPassword,CustomPasswordResetConfirm
# from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView,PasswordChangeView,PasswordChangeDoneView


urlpatterns =[
    path("sign_up/",sign_up,name='sign_up'),
    # path("sign_in/",sign_in, name='sign_in'),
    path("sign_in/",CustomLoginView.as_view(template_name = 'registration/sign_in.html'), name='sign_in'),
    # path("sign_out/",sign_out,name='sign_out'),
    path("sign_out/",LogoutView.as_view(),name='sign_out'),
    path('activate/<int:user_id>/<str:token>/',activate_user),
    path('admin/dashboard/',admin_dashboard,name='admin_dashboard'),
    path('admin/<int:user_id>/assign_role/',assign_role,name="assign_role"),
    path('admin/create_group/',create_group,name="create_group"),
    path('admin/group_list/',group_list,name="group_list"),
    # path('accounts/profile/',TemplateView.as_view(template_name="accounts/profile.html"))
    path('accounts/profile/',ProfileView.as_view(),name="profile"),
    path('password_change/',ChangePassword.as_view(template_name="accounts/password_change.html"),name="password_change"),
    path('password_change/done',PasswordChangeDoneView.as_view(template_name="accounts/password_change_done.html"),name="password_change_done"),
    #must declare this password_change/done after using changepasswordView
    path('password_reset',CustomResetPassword.as_view(),name="password_reset"),
    path('password_reset/confirm/<uidb64>/<token>',CustomPasswordResetConfirm.as_view(),name="password_reset_confirm"),
    








]  