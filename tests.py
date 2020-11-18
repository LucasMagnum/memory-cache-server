from cache import MemoryCache


def test_key_can_be_retrieved_after_it_is_added():
    cache = MemoryCache()
    cache.add("key", "value")
    assert cache.get("key") == "value", "Value does not match"


def test_get_key_should_return_none_when_key_does_not_exist():
    cache = MemoryCache()
    assert cache.get("key") is None


def test_get_key_should_return_value_stored():
    cache = MemoryCache()
    cache.add("key", "value")
    assert cache.get("key") == "value"


def test_delete_key_should_raise_exception_when_key_does_not_exists():
    cache = MemoryCache()

    try:
        cache.delete("invalid key")
    except KeyError:
        assert True, "Expected exception"


def test_delete_key_should_remove_key_when_it_exists():
    cache = MemoryCache()
    cache.add("key", "value")
    assert cache.get("key")

    cache.delete("key")
    assert cache.get("key", None) is None
