# Practice Problems 2

print("=== PRACTICE PROBLEMS 2 ===\n")


# Problem 5: Create a simple cache
class SimpleCache:
    def __init__(self, max_size=100):
        self.cache = {}
        self.max_size = max_size

    def get(self, key):
        return self.cache.get(key)

    def set(self, key, value):
        if len(self.cache) >= self.max_size:
            # Remove oldest item (simple FIFO)
            oldest_key = next(iter(self.cache))
            del self.cache[oldest_key]
        self.cache[key] = value

    def clear(self):
        self.cache.clear()

    def size(self):
        return len(self.cache)


# Test cache
cache = SimpleCache(max_size=3)
cache.set("user1", {"name": "Alice", "age": 25})
cache.set("user2", {"name": "Bob", "age": 30})
cache.set("user3", {"name": "Charlie", "age": 35})
cache.set("user4", {"name": "Diana", "age": 28})  # This will evict user1

print(f"Cache size: {cache.size()}")
print(f"User1: {cache.get('user1')}")  # None (evicted)
print(f"User2: {cache.get('user2')}")  # Still there


# Problem 6: Flatten nested dictionary
def flatten_dict(d, parent_key="", sep="_"):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


nested = {
    "user": {"name": "Alice", "address": {"city": "New York", "zip": "10001"}},
    "settings": {"theme": "dark"},
}

flattened = flatten_dict(nested)
print(f"Nested: {nested}")
print(f"Flattened: {flattened}")


# Problem 7: Dictionary-based configuration
class Config:
    def __init__(self, config_dict):
        self._config = config_dict

    def get(self, key, default=None):
        keys = key.split(".")
        value = self._config

        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default

        return value

    def set(self, key, value):
        keys = key.split(".")
        config = self._config

        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]

        config[keys[-1]] = value


# Test configuration
config_dict = {"database": {"host": "localhost", "port": 5432}, "api": {"timeout": 30}}

config = Config(config_dict)
print(f"Database host: {config.get('database.host')}")
print(f"API timeout: {config.get('api.timeout')}")
print(f"Non-existent: {config.get('database.password', 'default')}")

config.set("database.password", "secret123")
print(f"After setting password: {config.get('database.password')}")

print("\n=== END ===")
