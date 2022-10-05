from flasgger import Schema, SwaggerView, fields  # type: ignore


class SignUp(Schema):
    email = fields.Str()
    password = fields.Str()


class Login(Schema):
    email = fields.Str()
    password = fields.Str()


class RefreshToken(Schema):
    refresh_token = fields.Str()


class ChangeCreds(Schema):
    email = fields.Str()
    password = fields.Str()
    access_token = fields.Str()


class SignUpView(SwaggerView):
    tags = ['SignUp']
    parameters = [
        {
            'name': 'email',
            'in': 'body',
            'type': 'string',
            'required': True,
        },
        {
            'name': 'password',
            'in': 'body',
            'type': 'string',
            'required': True,
        }
    ]
    responses = {
        200: {
            'description': 'User sign up',
            'schema': SignUp
        }
    }


class LoginView(SwaggerView):
    tags = ['Login']
    parameters = [
        {
            'name': 'email',
            'in': 'body',
            'type': 'string',
            'required': True,
        },
        {
            'name': 'password',
            'in': 'body',
            'type': 'string',
            'required': True,
        }
    ]
    responses = {
        200: {
            'description': 'User login',
            'schema': Login
        }
    }


class RefreshView(SwaggerView):
    tags = ['Refresh token']
    parameters = [
        {
            'name': 'refresh_token',
            'in': 'headers',
            'type': 'string',
            'required': True,
        }
    ]
    responses = {
        200: {
            'description': 'Refresh tokens',
            'schema': RefreshToken
        }
    }


class ChangeCredsView(SwaggerView):
    tags = ['Creds change']
    parameters = [
        {
            'name': 'email',
            'in': 'body',
            'type': 'string',
            'required': True,
        },
        {
            'name': 'password',
            'in': 'body',
            'type': 'string',
            'required': True,
        },
        {
            'name': 'access_token',
            'in': 'headers',
            'type': 'string',
            'required': True,
        }
    ]
    responses = {
        200: {
            'description': 'Password change',
            'schema': ChangeCreds
        }
    }
