---
layout: plugin

id: TwitchTerminalCommands
title: OctoPrint-TwitchTerminalCommands
description: Sends gcode based on twitch commands
author: BenKnight135
license: AGPLv3

date: 2017-12-31

homepage: https://github.com/benknight135/OctoPrint-TwitchTerminalCommands
source: https://github.com/benknight135/OctoPrint-TwitchTerminalCommands
archive: https://github.com/benknight135/OctoPrint-TwitchTerminalCommands/archive/master.zip

tags:
- terminal
- command
- commands
- gcode
- ui

screenshots:
- url: /assets/img/plugins/TwitchTerminalCommands/terminal_tab.png
  alt: Terminal tab with command buttons
- url: /assets/img/plugins/TwitchTerminalCommands/terminal_commands_settings.png
  alt: Terminal Commands settings

featuredimage: /assets/img/plugins/TwitchTerminalCommands/terminal_tab.png

compatibility:

  octoprint:
  - 1.2.0

  os:
  - linux
  - windows
  - macos
  - freebsd

---

Buttons are inserted between the terminal command input and the terminal filters. Currenty only supports G-code commands that you can send through the terminal.

Multiple commands can be bound to one button by separating them with a semicolon (;) e.g. `M114; M503` (spaces before or after the semicolon are fine)
