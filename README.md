# Django-Example

<h1>this project contains some implementation of django concept</h1>
<b>1.) token based login and signup using rest_framework of django</b><br>
      -->used inbuilt User model with 'rest_framework' to generate and validate token to identify user<br>
      -->both login & signup are API '/api/auth/login' & '/api/auth/signup' gives JsonObject Response<br>
      -->calling login api --> curl -X POST http://127.0.0.1:8000/api/auth/login --data 'username=yourusername&password=yourpassword'<br>
      -->calling signup api --> curl -X POST http://127.0.0.1:8000/api/auth/signup --data 'username=yourusername&password=yourpassword&email=your_email'<br>
      <br><br>
<b>2.) 'posts' app </b><br>
      -->this app shows posts in sorted order according to their publishing date<br>
      -->to publish a post user must set Token(recieved after login) in header usnder 'Authorization' , it should be like this 'Token yourtoken'<br>
      -->calling add post api -->curl -X POST http://127.0.0.1:8000/api/post/add --data 'title=yourtitle&data=yourdata' --header 'Authorization:Token yourtoken'<br>
      
      

