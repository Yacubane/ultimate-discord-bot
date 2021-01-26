import asyncio


class Voice:
    async def run(self, context, client, discord):
        user = context.author
        voice_channel = user.voice.channel
        channel = None
        # only play music if user is in a voice channel
        if voice_channel != None:
            # grab user's voice channel
            channel = voice_channel.name
            await context.channel.send('User is in channel: ' + channel)
            # create StreamPlayer
            voice_client = await voice_channel.connect()
            audio_source  = discord.FFmpegPCMAudio(executable="./bin/ffmpeg.exe", source='./src/asset/voice/kolezanko_przepraszam.mp3')
            if not voice_client.is_playing():
                voice_client.play(audio_source, after=None)
            # disconnect after the player has finished
            # await voice_client.disconnect()
        else:
            await context.channel.send('User is not in a channel.')