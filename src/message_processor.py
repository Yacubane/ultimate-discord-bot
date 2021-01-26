from src.command_db import context_free_command_db, start_with_command_db


class MessageProcessor:
    def parse(self, message_object):
        message = message_object.content.lower()
        is_response = False
        response_message = ""

        if message in context_free_command_db.keys():
            is_response = True
            response_message = context_free_command_db[message](message_object)
            return is_response, response_message

        for cmd_name in start_with_command_db:
            if message.startswith(cmd_name):
                is_response = True
                response_message = start_with_command_db[cmd_name](message_object)
                return is_response, response_message

        return is_response, response_message
