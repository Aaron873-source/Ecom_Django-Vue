# Ecom_Django-Vue


#STEPS DONE TO START THE PROJECT
- pip3 install django (INSTALLED DJANGO)
- pip3 install django-rest-framework (FOR MAKING APIS)
- pip3 install django-cors-headers(HELPS US WITH SECURITY SO EVERYTHING BETWEEN THE BACK END AND API WILL BE WORKING SECURELY)
- pip3 install djoser(HELP WITH AUTHENTICATION, ADDS MORE END POINTS TO THE API SO ITS EASIER TO LOGIN AND GET TOKEN FOR AUTHENTICATION)
- pip3 install pillow(HELP TO RESIZE IMAGES )
- pip3 install stripe (TO HANDLE PAYMENTS)


#Highlights
- When making serializers we also use 'class Meta' to referrence the model in question along with what properties of the model we want to convert into JSON to display
- The generated Serializers are used in the view functions (views.py) before returning the response where by the model in question is converted to JSON using the serializer then returned in the response of the view function 
- REGISTERING : When registering an app to the admin panel in the apps admin.py we register the Model we want to be seen