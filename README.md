# Hexocean task

Django REST API that allows any user to upload an image in
PNG or JPG format.

## Build and run api
Using docker-compose run api
```
docker-compose up -d
```
After that api will open on adress `http://0.0.0.0:8000/`
## Add new user
To add a new user go to adress http://0.0.0.0:8000/admin and log in `user:admin` and `password:admin` and in the `user` field add a user and assign him a tier
## Upload images
At http://0.0.0.0:8000/upload_image/ you can upload a photo in png or jpg format. For this you need the login and password of the user you created earlier
Also you can do this with curl:
```bash
curl -i -X POST -F 'image=@test.jpg' -u username:userpassword http://127.0.0.1:8000/upload_image/
```
## View image link
At http://0.0.0.0:8000/list_image/ app shows link to photo depents on tier
```bash
curl -i -X -u username:userpassword GET http://0.0.0.0:8000/list_image/
```
## Tier
You can also add and modify tiers from the admin level in the `Tier` field