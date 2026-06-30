import os
from typing import List

from mcdreforged.api.utils.serializer import Serializable


class Config(Serializable):
	server_path: str = './server'
	world_folder: str = 'world'
	save_world_on_query: bool = False
	save_world_on_rank: bool = False
	save_world_on_scoreboard: bool = True
	# Names matching any of these (re.fullmatch, case-insensitive) are treated
	# as bots and excluded from ranks/scoreboards unless -bot is passed.
	# Covers both bot-name conventions: a "bot" prefix and a "_bot" suffix
	# (e.g. load_bot, Slime_BOT, bot_alice).
	player_name_blacklist: List[str] = [
		'^bot.*', 'bot_.*', '.*_bot', 'Steve', 'Alex'
	]

	def get_world_path(self) -> str:
		return os.path.join(self.server_path, self.world_folder)

	__instance: 'Config' = None

	@classmethod
	def set_instance(cls, inst: 'Config'):
		cls.__instance = inst

	@classmethod
	def get_instance(cls) -> 'Config':
		return cls.__instance
