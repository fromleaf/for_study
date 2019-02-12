#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

from flavors.models import Flavor

from .serializers import FlavorSerializer


class FlavorCreateReadView(ListCreateAPIView):
    queryset = Flavor.objects.all()
    serializer_class = FlavorSerializer
    lookup_field = 'slug'


class FlavorReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Flavor.objects.all()
    serializer_class = FlavorSerializer
    lookup_field = 'slug'
