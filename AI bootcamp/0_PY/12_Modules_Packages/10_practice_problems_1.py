# Practice Problems - Part 1

print("=== PRACTICE PROBLEMS - PART 1 ===\n")

print("Problem 1: Create a configuration module")


class Config:
    DEBUG = True
    DATABASE_URL = "sqlite:///app.db"
    SECRET_KEY = "my-secret-key"
    MAX_CONNECTIONS = 100

    @classmethod
    def get_database_url(cls):
        return cls.DATABASE_URL

    @classmethod
    def is_debug(cls):
        return cls.DEBUG

    @classmethod
    def get_max_connections(cls):
        return cls.MAX_CONNECTIONS

    @classmethod
    def set_debug(cls, value):
        cls.DEBUG = value

    @classmethod
    def get_all_config(cls):
        return {
            "debug": cls.DEBUG,
            "database_url": cls.DATABASE_URL,
            "secret_key": cls.SECRET_KEY,
            "max_connections": cls.MAX_CONNECTIONS,
        }


print(f"Database URL: {Config.get_database_url()}")
print(f"Debug mode: {Config.is_debug()}")
print(f"Max connections: {Config.get_max_connections()}")

Config.set_debug(False)
print(f"Debug mode after change: {Config.is_debug()}")

print(f"All config: {Config.get_all_config()}")

print("\nProblem 2: Create a singleton logger")

import datetime


class Logger:
    _instance = None
    logs = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logs = []
        return cls._instance

    def log(self, message, level="INFO"):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {level}: {message}"
        self.logs.append(log_entry)
        print(log_entry)

    def get_logs(self):
        return self.logs.copy()

    def clear_logs(self):
        self.logs.clear()

    def get_logs_by_level(self, level):
        return [log for log in self.logs if f"{level}:" in log]

    def get_log_count(self):
        return len(self.logs)


# Test singleton logger
logger1 = Logger()
logger2 = Logger()
print(f"Same logger instance: {logger1 is logger2}")

logger1.log("Application started")
logger2.log("User logged in", "INFO")
logger1.log("Error occurred", "ERROR")
logger2.log("Database connection established", "INFO")

print(f"All logs: {logger1.get_logs()}")
print(f"Error logs: {logger1.get_logs_by_level('ERROR')}")
print(f"Total log count: {logger1.get_log_count()}")

print("\nProblem 3: Create a factory for different data formats")

import json


class DataFormatter:
    def format_data(self, data):
        pass

    def get_format_name(self):
        return "base"


class JSONFormatter(DataFormatter):
    def format_data(self, data):
        return json.dumps(data, indent=2)

    def get_format_name(self):
        return "json"


class XMLFormatter(DataFormatter):
    def format_data(self, data):
        # Simplified XML formatting
        xml = "<data>\n"
        for key, value in data.items():
            xml += f"  <{key}>{value}</{key}>\n"
        xml += "</data>"
        return xml

    def get_format_name(self):
        return "xml"


class CSVFormatter(DataFormatter):
    def format_data(self, data):
        if not data:
            return ""
        headers = list(data[0].keys())
        csv = ",".join(headers) + "\n"
        for row in data:
            csv += ",".join(str(row[header]) for header in headers) + "\n"
        return csv

    def get_format_name(self):
        return "csv"


class YAMLFormatter(DataFormatter):
    def format_data(self, data):
        # Simplified YAML formatting
        yaml = ""
        for key, value in data.items():
            yaml += f"{key}: {value}\n"
        return yaml

    def get_format_name(self):
        return "yaml"


def create_formatter(format_type):
    formatters = {
        "json": JSONFormatter,
        "xml": XMLFormatter,
        "csv": CSVFormatter,
        "yaml": YAMLFormatter,
    }

    if format_type in formatters:
        return formatters[format_type]()
    else:
        raise ValueError(f"Unknown format: {format_type}")


# Test formatters
test_data = {"name": "Alice", "age": 25, "city": "New York"}
test_list_data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]

print("Testing different formatters:")
for format_type in ["json", "xml", "csv", "yaml"]:
    try:
        formatter = create_formatter(format_type)
        if format_type == "csv":
            result = formatter.format_data(test_list_data)
        else:
            result = formatter.format_data(test_data)
        print(f"{format_type.upper()} format:")
        print(result)
        print()
    except Exception as e:
        print(f"Error with {format_type}: {e}")

print("\nProblem 4: Create a plugin system")


class Plugin:
    def execute(self, data):
        pass

    def get_name(self):
        return "base_plugin"


class UppercasePlugin(Plugin):
    def execute(self, data):
        if isinstance(data, str):
            return data.upper()
        return data

    def get_name(self):
        return "uppercase"


class ReversePlugin(Plugin):
    def execute(self, data):
        if isinstance(data, str):
            return data[::-1]
        return data

    def get_name(self):
        return "reverse"


class NumberPlugin(Plugin):
    def execute(self, data):
        if isinstance(data, (int, float)):
            return data * 2
        return data

    def get_name(self):
        return "number"


class LengthPlugin(Plugin):
    def execute(self, data):
        if hasattr(data, "__len__"):
            return len(data)
        return 0

    def get_name(self):
        return "length"


class PluginManager:
    def __init__(self):
        self.plugins = {}

    def register_plugin(self, name, plugin):
        self.plugins[name] = plugin
        print(f"Registered plugin: {name}")

    def execute_plugin(self, name, data):
        if name in self.plugins:
            return self.plugins[name].execute(data)
        else:
            raise ValueError(f"Plugin '{name}' not found")

    def list_plugins(self):
        return list(self.plugins.keys())

    def remove_plugin(self, name):
        if name in self.plugins:
            del self.plugins[name]
            print(f"Removed plugin: {name}")

    def get_plugin_info(self):
        return {name: plugin.get_name() for name, plugin in self.plugins.items()}


# Test plugin system
manager = PluginManager()
manager.register_plugin("uppercase", UppercasePlugin())
manager.register_plugin("reverse", ReversePlugin())
manager.register_plugin("number", NumberPlugin())
manager.register_plugin("length", LengthPlugin())

test_string = "hello world"
test_number = 42
test_list = [1, 2, 3, 4, 5]

print(f"Original string: {test_string}")
print(f"Uppercase: {manager.execute_plugin('uppercase', test_string)}")
print(f"Reverse: {manager.execute_plugin('reverse', test_string)}")
print(f"Length: {manager.execute_plugin('length', test_string)}")

print(f"Original number: {test_number}")
print(f"Doubled: {manager.execute_plugin('number', test_number)}")

print(f"Original list: {test_list}")
print(f"List length: {manager.execute_plugin('length', test_list)}")

print(f"Available plugins: {manager.list_plugins()}")
print(f"Plugin info: {manager.get_plugin_info()}")

print("\n=== END OF PRACTICE PROBLEMS - PART 1 ===")
