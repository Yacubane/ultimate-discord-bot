from src.command_db import command_db


class MessageProcessor:
    def parse(self, message_object):
        message = message_object.content
        is_response = False
        response_message = ""
        if message in command_db.keys():
            is_response = True
            response_message = command_db[message](message_object)
        return is_response, response_message
