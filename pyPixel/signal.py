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

    async def wait(self, loop):
        f = asyncio.Future()

        def cb(data):
            async def tsafe():
                f.set_result(data)
            asyncio.run_coroutine_threadsafe(tsafe(), loop)
            self.disconnect(cb)
        self.connect(cb)
        return await f
