from __future__ import absolute_import

from django.views.generic import TemplateView

from flavors.models import Flavor


class SiteMapView(TemplateView):
    template_name = 'core/sitemap.xml'

    def flavors(self):
        return Flavor.objects.all()
