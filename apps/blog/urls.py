from loveshare.router import router
from .rest import PostViewSet

router.register(r'blog', PostViewSet)
urlpatterns = [
]