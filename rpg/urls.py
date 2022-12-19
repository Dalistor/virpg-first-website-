"""rpg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from virRPG.views import entrance, register, store_register, log, store_login, characters, character_edit, campaigns, campaign_del, log_out, c_password, store_c_password, token, skills, character_del, register_attack, edit_attack, del_attack, campaign_edit

urlpatterns = [
    path('admin/',                                          admin.site.urls     ),
    path('',                                                entrance            ),
    path('register/',                                       register            ),
    path('store_register/',                                 store_register      ),
    path('login/',                                          log                 ),
    path('store_login/',                                    store_login         ),
    path('campaigns/',                                      campaigns           ),
    path('campaigns/<int:cid>/delete',                      campaign_del        ),
    path('campaigns/<int:cid>/edit',                        campaign_edit       ),
    path('campaigns/<int:cid>/characters/',                 characters          ),
    path('campaigns/<int:cid>/characters/delete/<int:id>',  character_del       ),
    path('campaigns/<int:cid>/characters/edit/<int:id>',    character_edit      ),
    path('logout/',                                         log_out             ),
    path('change_password/',                                c_password          ),
    path('store_change_password/',                          store_c_password    ),
    path('token/<int:id>',                                  token               ),
    path('token/<int:id>/skills',                           skills              ),
    path('token/<int:id>/register_attack/',                 register_attack     ),
    path('token/<int:id>/edit_attack/<int:aid>',            edit_attack         ),
    path('token/<int:id>/del_attack/<int:did>',             del_attack          ),
]
