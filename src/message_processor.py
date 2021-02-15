from src.command_db import CommandDB


class MessageProcessor:
    command_db = None

    def __init__(self, client):
        self.command_db = CommandDB(client)

    async def parse(self, message_object, client) -> (bool, str):
        message = message_object.content.lower()
        is_response, response_message = False, ""
        cmd = message.split(" ")[0]

        if message in self.command_db.context_free_command_db.keys():
            is_response = True
            response_message = self.command_db.context_free_command_db[message](message_object, client)
            return is_response, response_message

        if cmd in self.command_db.async_command_db.keys():
            await self.command_db.async_command_db[cmd](message_object)

        for cmd_name in self.command_db.start_with_command_db:
            if message.startswith(cmd_name):
                is_response, response_message = True, self.command_db.start_with_command_db[cmd_name](message_object)
                break

        return is_response, response_message
