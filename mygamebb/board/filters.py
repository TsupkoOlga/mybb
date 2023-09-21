from django_filters import FilterSet
from .models import *

class CommentFilter(FilterSet):
   class Meta:
       model = Comment
       fields = {
           'bulletin': ['exact'],
       }