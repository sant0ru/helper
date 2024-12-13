# At the top of the file.
import disnake
from disnake.ext import commands
from disnake.interactions.modal import ModalInteraction
from disnake.ui.action_row import Components, ModalUIComponent
from disnake.utils import MISSING
from disnake import TextInputStyle

intents = disnake.Intents.all()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None, test_guilds=[1317157279543464027])

@bot.event
async def on_ready():
   print(f'Logged in as {bot.user}')

class modal(disnake.ui.Modal):
    def __init__(self):
        # The details of the modal, and its components
        components = [disnake.ui.TextInput(
                label="Никнейм | Статик",
                placeholder="Пример: Ivan Pupkin | 101010",
                custom_id="nickname",
                max_length=30,
                ),
             disnake.ui.TextInput(
                label="Имя",
                placeholder="Реальное имя",
                custom_id="name",
                max_length=15
                ),
            disnake.ui.TextInput(
                label="Возраст",
                placeholder="Ваш возраст",
                custom_id="age",
                max_length=3
                ),
            disnake.ui.TextInput(
                label="Опыт игры на рп проектах",
                placeholder="Сколько времени и где играли, ваши лидерки(если были) и т.п.",
                custom_id="exp",
                max_length=100
                ),
            disnake.ui.TextInput(
                label="Онлайн",
                placeholder="Ваш онлайн в день",
                custom_id="online",
                max_length=15
                ),
            disnake.ui.TextInput(
                label="Потребности",
                placeholder="Опишите, что вы ожидаете от семьи",
                custom_id="wait",
                max_length=100 ),
        ]

        super().__init__(title="Заявка в семью", components=components)
            
    # The callback received when the user input is completed.
        async def callback(self, inter: disnake.ModalInteraction):
            embed = disnake.Embed(title="Ticket")
            for key, value in inter.text_values.items():
             embed.add_field(
                name=key.capitalize(),
                value=value[:1024],
                inline=False,
            )
             
            await inter.response.send_message(embed=embed)

@bot.slash_command(name="app")
async def create_application(inter: disnake.AppCmdInter):
    modal = Application()
    await inter.response.send_modal(modal=modal)

bot.run("MTMxNzE1NzMzMDE5Nzk0MjM1NQ.GP8gsF.v2_G5L8AYfe0MiorNiinmMW62hKV5nAs1FBPVs")