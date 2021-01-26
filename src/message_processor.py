from src.command_db import context_free_command_db, start_with_command_db, async_command_db


class MessageProcessor:
    async def parse(self, message_object, client, discord):
        message = message_object.content.lower()
        is_response = False
        response_message = ""

        if message in context_free_command_db.keys():
            is_response = True
            response_message = context_free_command_db[message](message_object, client)
            return is_response, response_message

        if message in async_command_db.keys():
            await async_command_db[message](message_object, client, discord)

        for cmd_name in start_with_command_db:
            if message.startswith(cmd_name):
                is_response = True
                response_message = start_with_command_db[cmd_name](message_object)
                return is_response, response_message

        return is_response, response_message
