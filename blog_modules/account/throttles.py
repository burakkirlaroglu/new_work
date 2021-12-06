from rest_framework.throttling import SimpleRateThrottle, AnonRateThrottle, \
    UserRateThrottle

# class RegisterThtottle(SimpleRateThrottle):
#     scope = 'registerthrottle'
#
#     def get_cache_key(self, request, view):
#         if request.user.is_authenticated or request.method == 'GET':
#             return None
#
#         return self.cache_format % {
#             'scope': self.scope,
#             'ident': self.get_ident(request)
#         }
#
#     def parse_rate(self, rate):
#         if rate is None:
#             return (None, None)
#         num, period = rate.split('/')
#         num_requests = int(num)
#         duration = {'s': 1, 'm': 60, 'h': 7200, 'd': 100000}[period[0]]
#         return (num_requests, duration)


# class RegisterThtottle(AnonRateThrottle):
#     """Yukarıda olan yerine sadece bu şekilde de kullanılabilinir
#     Yukarı taraf daha fazla configure edilebilir durumdadır."""
#     scope = 'registerthrottle'


class RegisterThtottle(UserRateThrottle):
    """Kullanıcının user id si ile bakar giriş yapıldığı için
    ama logout olup tekrar denenirse bu sefer max değere geldiğinde
    IP adresine göre kilitler"""
    scope = 'registerthrottle'


"""
Scope Throttle ile süreç şu şekilde;

* Settings e default ayar eklenir
* daha sonra istenilen bir view için throttle_scope değeri girilir
* DEFAULT_THROTTLE_RATES içine de o değer girilerek kısıtlama süresi ve miktarı yazılır
"""
