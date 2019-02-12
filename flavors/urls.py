#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import path

from .views import *

app_name = 'flavors'

# View URLs
urlpatterns = [
    path(r'shopping-cart/', ShoppingCartView.as_view(), name='shopping_cart'),
]
