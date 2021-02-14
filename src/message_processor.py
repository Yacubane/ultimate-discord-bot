from src.command_db import context_free_command_db, start_with_command_db, async_command_db


class MessageProcessor:
    async def parse(self, message_object, client):
        message = message_object.content.lower()
        is_response, response_message = False, ""
        cmd = message.split(" ")[0]

        if message in context_free_command_db.keys():
            is_response = True
            response_message = context_free_command_db[message](message_object, client)
            return is_response, response_message

        if cmd in async_command_db.keys():
            await async_command_db[cmd](message_object, client)

        for cmd_name in start_with_command_db:
            if message.startswith(cmd_name):
                is_response, response_message = True, start_with_command_db[cmd_name](message_object)
                break

        return is_response, response_message
