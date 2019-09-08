# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class TwitchTerminalCommandsPlugin(octoprint.plugin.SettingsPlugin,
                             octoprint.plugin.AssetPlugin,
                             octoprint.plugin.TemplatePlugin):

	def get_settings_defaults(self):
		return dict(
			controls=[]
		)

	def get_assets(self):
		return dict(
			js=["js/TwitchTerminalCommands.js"],
			css=["css/TwitchTerminalCommands.css"]
		)

	def get_template_configs(self):
		return [
            dict(type="settings", custom_bindings=True)
        ]

	def get_update_information(self):
		return dict(
			TwitchTerminalCommands=dict(
				displayName="TwitchTerminalCommands Plugin",
				displayVersion=self._plugin_version,

				type="github_release",
				user="benknight135",
				repo="OctoPrint-TwitchTerminalCommands",
				current=self._plugin_version,

				pip="https://github.com/benknight135/OctoPrint-TwitchTerminalCommands/archive/{target_version}.zip"
			)
		)

__plugin_name__ = "Twitch Terminal Commands"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = TwitchTerminalCommandsPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}

