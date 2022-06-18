## RESTful API
An API is a convenient way to provide users access to data from our application

#### django-rest-framework
We use the **django-rest-framework** to enable us to build a restful api.<br/> 
We will begin by creating a very basic structure that can handle GET requests then move on to adding authentication and handling POST request.
To install `pip install djangorestframework`

project/settings.py
```bash
INSTALLED_APPS = [
.......
    'rest_framework',
]
```
#### Serializers
A serializer is a component that will convert Django models to JSON objects and vice-versa.
news/serializer.py
```bash
from rest_framework import serializers
from .models import MoringaMerch

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoringaMerch
        fields = ('name', 'description', 'price')  OR  __all__
```
* Then create urls for api in project/urls.py
* We configure our API to also allow us to add data to our database in views.py

#### POST request
To retrieve data from our database we want to configure our API to also allow us to add data to our database

## Authentication
To allow the Admin to add new Items/data.
project/settings.py
```bash
INSTALLED_APPS = [
    'rest_framework.authtoken'
]
.....
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}
```
* Remember to do migrations
* Add authentication app url in the urlpatterns
project/urls.py
```bash
from rest_framework.authtoken.views import obtain_auth_token
.......
urlpatterns = [
.......
    path('api-token-auth/', obtain_auth_token)
]
```

* We create a new POST request and pass in the username and password in our app
app/permissions.py
```bash 
from rest_framework.permissions import SAFE_METHODS, BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff
```

* We then add the permissions to the API view class.
news/views.py
```bash
from .permissions import IsAdminOrReadOnly
 ........
class MerchList(APIView):
 .........
    permission_classes = (IsAdminOrReadOnly,)
```    