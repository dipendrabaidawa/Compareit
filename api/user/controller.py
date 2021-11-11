from flask_restx import Resource, Namespace
import json

User = Namespace(name='Users', description="User API")


@User.route('')
class Users(Resource):
    def get(self):
        user_id = request.form.get('id')

        from api.user.models import User
        all_users = User.query.filter_by(email=user['email']).first()
        if all_users :
            return data, 200
        else:
            return {"message": "User Not Found"}, 404

    def post(self):
        return {}, 201