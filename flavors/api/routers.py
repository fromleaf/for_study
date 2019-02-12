#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path, include

from .views import (
    FlavorCreateReadView, FlavorReadUpdateDeleteView
)

urlpatterns = [
    path(r'', FlavorCreateReadView.as_view(), name='flavor_rest_api'),
    path(r'<int:slug>/', FlavorReadUpdateDeleteView.as_view(), name='flavor_rest_api'),
]
