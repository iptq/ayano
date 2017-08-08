import imp
import os
import re
from utils import parse_args


class ConflictingModuleNameException(Exception):
    pass


class ConflictingCommandNameException(Exception):
    pass


async def help_function(client, message):
    await client.send_message(message.channel, "helo im not a bot")


ILLEGAL_COMMAND_NAME = re.compile("[^a-z]")


class CommandLibrary(object):
    def __init__(self):
        self.trigger = "//"
        self.commands = dict()
        self.register_command("help", help_function)

    def _filter_command_name(self, name):
        return ILLEGAL_COMMAND_NAME.sub("", name.lower())

    def unregister_command(self, name):
        filtered_name = self._filter_command_name(name)
        if filtered_name in self.commands:
            del self.commands[filtered_name]

    def register_command(self, name, handler):
        filtered_name = self._filter_command_name(name)
        if filtered_name in self.commands:
            raise ConflictingCommandNameException("There is already a command named '{}'.".format(filtered_name))
        self.commands[name] = handler

    async def on_message(self, client, message):
        if message.content.startswith(self.trigger):
            message_ = message.content[len(self.trigger):]
            parts = parse_args(message_)
            command = parts[0]
            if command in self.commands:
                await self.commands[command](client, message, parts)
                return


class ModuleLibrary(object):
    def _register_module(self, name, module):
        if name in self.modules:
            raise ConflictingModuleNameException("There is already a module named '{}'.".format(name))
        self.modules[name] = module
        if hasattr(module, "on_mention"):
            assert callable(module.on_mention)
            self.on_mention[name] = module.on_mention
        if hasattr(module, "commands"):
            assert type(module.commands) == dict
            for name, command in module.commands.items():
                self.command_library.register_command(name, command)

    def _load_modules(self):
        files = os.listdir(self.module_folder)
        for fname in files:
            fullpath = os.path.join(self.module_folder, fname)
            if os.path.isdir(fullpath):
                continue
            with open(fullpath) as f:
                mname = fname.replace(".py", "")
                contents = f.read()
                module = imp.load_source(mname, os.path.join(self.module_folder, fname))
                self._register_module(mname, module)

    def __init__(self, module_folder=None):
        self.modules = dict()
        self.on_mention = dict()
        self.command_library = CommandLibrary()
        if not module_folder:
            module_folder = os.path.join("lib", "modules")
        self.module_folder = os.path.abspath(module_folder)
        self._load_modules()

    def reload_modules(self):
        self._load_modules()

    async def on_message(self, client, message):
        await self.command_library.on_message(client, message)
        if message.content.startswith("<@{}>".format(client.user.id)):
            for module, handler in self.on_mention.items():
                await handler(client, message)
