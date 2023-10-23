## APIs

### Start

The complete project is dockerized.

Run the below commands to run docker image and start the project on local machine

```
docker-compose build
docker-compose up
```
### .env
First create a .env file inside the project directory.
and add your secret key by using following lines of code:
```
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```
This will generate a secret_key.
<br>
Or else add following in the .env file:
```
SECRET_KEY=2ns&e7w-89&=7^^v(mnzfqqx=i(^ytw20_327l3&^v*w1_^sju
```

**To access all the endpoints you can create your own user or use already exsisting user with admin access**
</br>
```
username: admin
password: admin
```


## Available endpoints to hit
**All the APIs are documented at https://localhost:8000/**
</br>
**To view this documentation, first you need to login using https://localhost:8000/admin/ and the admin credentials available above.**

- <code><span class="text-uppercase">POST</span> /api/login/</code>  -> Takes a set of user credentials and returns an access and refresh JSON web
token pair to prove the authentication of those credentials.
JSON body:
    ```
    {
        "username":"admin",
        "password":"admin"
    }
    ```
    This returns new refersh and access token.

- <code><span class="text-uppercase">POST</span> /api/auth/refresh-token/</code>  -> Takes a refresh type JSON web token and returns an access type JSON web
token if the refresh token is valid. JSON body:
    ```
    {
    "refresh": "old refresh_token"
    }
    ```
    This returns new refersh and access token.

- <code><span class="text-uppercase">POST</span> /api/auth/verify-token/</code>  -> Takes a token and indicates if it is valid. This view provides no information about a token's fitness for a particular use. JSON body:
    ```
    {
    "token": "token"
    }
    ```
**All the APIs below can only be accessible using JWT token.**
**To use them use the /api/auth/generate-token/ endpoint.**
**And while calling these APIs use Header Authorization: JWT {{access_token}}**
- <code><span class="text-uppercase">GET</span> /api/companies/</code>  -> To fetch all the available companies. Can only work if the user is admin. It returns list of company objects. This endpoint requires admin permissions.

- <code><span class="text-uppercase">POST</span> /api/company/</code>  -> To create a new company. This endpoint requires admin permissions. JSON body:
    ```
    {
        "company_name": "DoctousTech",
        "company_ceo": "Founder",
        "company_address": "India",
        "inception_Date": "2020-06-03"
    }
    ```


- <code><span class="text-uppercase">GET</span> /api/company/{id}/</code>  -> To retrieve a single company using its unique company id. This returns a complete object of the company with the company id.


- <code><span class="text-uppercase">PUT</span> /api/company/{id}/</code>  -> To completely update the company object with the given id. JSON body:
    ```
    {
        "company_name": "Google",
        "company_ceo": "Sundar Pichai",
        "company_address": "USA",
        "inception_Date": "2002-06-03"
    }
    ```

- <code><span class="text-uppercase">PATCH</span> /api/company/{id}/</code>  -> To partially update the company object with given comapny id.

- <code><span class="text-uppercase">DELETE</span> /api/delete-company/{id}/</code>  -> To delete the company object with the given company id. This endpoint requires admin permissions.
