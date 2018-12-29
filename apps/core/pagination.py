from rest_framework import pagination
from rest_framework.response import Response
class PageNumberPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'pagebar':{
                'previous': self.get_previous_link(),
                'next': self.get_next_link(),
                'total': self.page.paginator.count,
                'pages': self.page.paginator.num_pages
            },
            'results': data
        })