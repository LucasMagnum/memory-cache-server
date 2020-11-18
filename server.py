import asyncio
import functools
import os
from cache import MemoryCache


async def start_cache_server(cache, host, port):
    handle_cache_operations = functools.partial(handle_cache, cache)
    server = await asyncio.start_server(handle_cache_operations, host, port)

    addr = server.sockets[0].getsockname()
    print(f"Serving on {addr}")

    async with server:
        await server.serve_forever()

    print("Server closed")


async def handle_cache(cache, reader, writer):
    while True:
        try:
            data = await reader.read(100)
            command = data.decode()
        except Exception:
            continue

        try:
            result = execute_command(cache, command)
        except StopIteration:
            break

        addr = writer.get_extra_info("peername")
        print(f"Received {command!r} from {addr!r}")

        message = f"{result}\n"
        writer.write(message.encode())
        await writer.drain()

    print("Close the connection")
    writer.close()


def execute_command(cache, command):
    command, *args = command.strip().split(" ")

    if command == "SET":
        key, value = args
        cache.add(key, value)
        return "OK"

    elif command == "GET":
        return cache.get(args[0], "NOT_FOUND")

    elif command == "DELETE":
        try:
            cache.delete(args[0])
        except KeyError:
            return "NOT_FOUND"
        return "OK"

    elif command == "EXIT":
        raise StopIteration()

    else:
        return "Commands available: SET, GET, DELETE, EXIT"


if __name__ == "__main__":
    memory_cache = MemoryCache()
    asyncio.run(start_cache_server(memory_cache, "127.0.0.1", 5000))
