class CrossOriginOpenerPolicyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Set the Cross-Origin-Opener-Policy header
        response['Cross-Origin-Opener-Policy'] = 'same-origin'

        return response
