from __future__ import absolute_import

from django.views.generic import TemplateView


class ShoppingCartView(TemplateView):
    template_name = 'flavors/shopping_cart.html'
