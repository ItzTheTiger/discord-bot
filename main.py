import discord
from discord.ext import commands
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Custom replies
trigger_response_map = {
    "hello": "Hello there! 👋",
    "bye": "Goodbye! 👋",
    "how are you": "I'm doing great, thanks for asking! 🤖",
}

# Replace with your Discord user ID (enable Developer Mode and right-click your profile → Copy User ID)
BOT_OWNER_ID = 880402221978771466  # <-- Replace this with your own user ID


@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Handle DMs
    if isinstance(message.channel, discord.DMChannel):
        user_message = message.content.lower()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Send reply to the user
        if user_message in trigger_response_map:
            reply = trigger_response_map[user_message]
            await message.channel.send(reply)
        else:
            await message.channel.send(
                "❓ I don't understand. Try 'hello', 'bye', or 'how are you'"
            )

        # DM the owner with log info
        try:
            owner = await bot.fetch_user(BOT_OWNER_ID)
            await owner.send(
                f"🔔 New DM to the bot!\n"
                f"👤 From: {message.author} (ID: {message.author.id})\n"
                f"💬 Message: {message.content}\n"
                f"🕒 Time: {current_time}"
            )
        except discord.HTTPException as e:
            print(f"❌ Could not send DM to owner: {e}")

    await bot.process_commands(message)


bot.run("MTM5ODU2ODMxMDM3ODk4NzUzMQ.GIBt1u._4dxr6usoUBgE36aPJ0ze5mybbNtPl2za90YmI")
