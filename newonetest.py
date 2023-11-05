import jwt
# from django.conf import settings
JWT_SECRET = 'AAF5w3VjvG_enCevxteSSQL3e_RUNg6ZppE'

disct = {
    'pk':'hello_world',
}

data = jwt.encode({'pk':'hello_world'},key=JWT_SECRET,algorithm='HS256')
print(data)


# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk5MTgwNDAyLCJpYXQiOjE2OTkwOTQwMDIsImp0aSI6ImRiYzI2Y2I0YjY4ZTQ5OTFhZDc1YzVjNjJjNTI5MjJmIiwidXNlcl9p" \
#         "ZCI6InBhcmFzaHVyYW1rYWxha3V0YWdpOUBnbWFpbC5jb20ifQ.ov8EOt7kDXS9574_mOkXxTPUbRWdCxwvsCEpGaTHiPM"\
#          "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwayI6NDV9.wxv2uKmIcbgM9NwBHCgXRK3nb1SHB9Jw7KzWS2A67LY"

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InBhcmFzaHVyYW1rYWxha3V0YWdpOUBnbWFpbC5jb20ifQ.bFtqPwKRNF0-INWRapGFwglwLjtc7NzO9KJAiq2P2jM'
decode = jwt.decode(token,key=JWT_SECRET,algorithms='HS256')
print(decode)