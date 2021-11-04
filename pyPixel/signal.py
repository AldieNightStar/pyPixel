import asyncio


class Signal:
    def __init__(self):
        self.funcs = []

    def connect(self, func):
        self.funcs.append(func)
        return func

    def emit(self, *data):
        for f in self.funcs:
            f(*data)

    def disconnect(self, func):
        self.funcs.remove(func)

    async def wait(self):
        f = asyncio.Future()

        def cb(data):
            f.set_result(data)
            self.disconnect(cb)
        self.connect(cb)
        return await f
