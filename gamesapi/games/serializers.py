from rest_framework import serializers
from games.models import Game

class GameSerializer(serializers.ModelSerializer):
	class Meta:
		model = Game
		fields = ('id', 'name', 'release_date', 'game_category')

	def is_empty(self, value):
		if value == '' or value is None:
			raise serializers.ValidationError("Can't be empty fields")
		return value

	def is_registered(self, value):
		if Game.objects.filter(name=value):
			raise serializers.ValidationError("This game was registered already!")

	def validate_name(self, name):
		self.is_registered(name)
		return self.is_empty(name)
		
	def validate_release_date(self, release_date):
		return self.is_empty(release_date)

	def validate_game_category(self, game_category):
		return self.is_empty(game_category)
