from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):

    page_size = 10  # Number of items per page

    page_query_param = 'page'  # Allow client to set page size

    max_page_size = 100  # Maximum items per page