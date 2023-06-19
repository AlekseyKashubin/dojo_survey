from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash




class Survey:
    DB = 'dojo_survey_schema'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']






    @staticmethod
    def validate_survey(survey):
        is_valid = True
        if len(survey['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if (survey['location']) == '0':
            flash("a Location must be chosen.")
            is_valid = False
        if (survey['language']) == '0':
            flash("a Language must be chosen.")
            is_valid = False
        if len(survey['comment']) < 1:
            flash("You must add a comment.")
            is_valid = False

        
        return is_valid

