from .models import Post

def categoria(unique):	
	return Post.objects.all().prefetch_related("categoria").filter(category=unique, status='published').order_by('-published')