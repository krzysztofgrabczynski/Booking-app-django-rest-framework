# <p align=center> <a name="top">Booking-app </a></p>  

## Description
The Booking app is used to browse hotels with hotel rooms, and allows to book rooms only for logged-in users. Additionally, certain permissions are required to add hotels or hotel rooms. To edit or delete a room, the user must be an administrator or owner of that particular hotel room. Only admin users can delete an entire hotel with all rooms. This app provides also user registration, and authorization through auth tokens.
This project is fully based on Django REST framework and API was tested using Postman application. 

Project has been dockerized and uses some linters and tools such as Black, Mypy, Flake8.

If you want to check out my other projects [click here.](https://github.com/krzysztofgrabczynski)


## The main features of the API include:
- [x] [hotel and room browsing - list/retrieve informations about hotel with rooms or specific room (no need to logged-in)](#browsing)
- [x] [CRUD operations for hotel/room - only for users with specific permissions/record owners](#crud)
- [x] [booking room - only for logged-in users](#booking)
- [x] [user registration - authorization through the auth tokens](#user-registration)
- [x] [retrive specific user profile with list of reserved rooms](#user-profile)


## Browsing hotels/rooms
All users (even not logged-in) can check the list of hotels or retrive detail for the speficic hotel. The same applies for hotel rooms.
<p align="center">
  <img src="https://github.com/krzysztofgrabczynski/Booking-app-django-rest-framework/assets/90046128/abde75f9-ac27-4dcd-b1ee-14a63b68b431.gif">
</p>

[Go to top](#top) 

## CRUD
To create a hotel or a new hotel room, a user must have certain permissions. Only admin user can delete/update a hotel. Only the admin user or user who created the hotel room record can delete/update that record.

[Go to top](#top) 

## Booking
Authenticated users can book a specific hotel room if 'is_available' is set to 'True'. Otherwise, the API will respond that the room is already booked. If the reservation action succeed, 'is_available' will change to 'False'.
<p align="center">
  <img src="https://github.com/krzysztofgrabczynski/Booking-app-django-rest-framework/assets/90046128/6bd34d85-5340-4d06-8ad6-ac96df61e80a.gif">
</p>

[Go to top](#top) 

## User registration
User can register as below (if username and email address are unique). An authentication token will be created automatically for this user.
<p align="center">
  <img src="https://github.com/krzysztofgrabczynski/Booking-app-django-rest-framework/assets/90046128/05acdb91-a0ed-4a20-adf4-f25718923e02.gif">
</p>

[Go to top](#top) 

## User profile
All users can check only their profiles for id, name and email address. They can also check all the reservations they have made.
<p align="center">
  <img src="https://github.com/krzysztofgrabczynski/Booking-app-django-rest-framework/assets/90046128/3ef79a12-b0d1-4931-9474-16d47969bd53.gif">
</p>

[Go to top](#top) 

