#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers

from flavors.models import Flavor


class FlavorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flavor
        fields = (
            'title',
            'slug',
            'scoops_remaining'
        )
