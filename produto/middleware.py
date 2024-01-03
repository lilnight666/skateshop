class SetDefaultCharsetMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.encoding = 'utf-8'
        response = self.get_response(request)
        return response
