import json
import aiohttp
import asyncio

__VERSION__ = "1.0.4"

class Client:
    def __init__(self, session=None, loop=None, port=3030, host="localhost", password=None, is_async=True):
        """
        Params:
            session: (aiohttp.Session) Session to perform requests with.
            loop: (asyncio.Loop) Asyncio loop to use when creating the session.
            port: (int) Port to the API server.
            host: (str) Host of ths API server.
            password: (str) Password if set.

        Loop is only used if session is None as it will be used to create the session.
        If you provide your own session then loop is not needed.
        Password is only required when requesting with a host that is not localhost and one is set in the server.
        """
        self.is_async = is_async
        self.host = host
        self.session = session
        self.port = port
        self.password = password


    async def _get(self, endpoint, params=None):
        headers = None

        if self.password:
            headers = { "Authorization": self.password }

        response = await self.session.get(url=f"http://{self.host}:{self.port}{endpoint}", params=params, headers=headers)

        if response.status != 200:
            if "application/json" in response.headers.get("content-type", ""):
                raise Exception((await response.json())["message"])
            else:
                raise Exception(f"API returned status: {res.status}")

        if "application/json" in res.headers.get("content-type", ""):
            return await response.json()

        return await response.read()

    def ping(self):
        """
        Returns (dict):
            { message: "Pong!" }
        """
        return self._get("/ping")

    def stats(self, stats=True):
        """
        Params:
            stats: (bool) (default: true) Wether to request memory statistics (stats field).
        Returns (dict):
            { version: "version" uptime: 0, stats: { ... } }
        """
        return self._get("/stats", { "noStats": not stats })

    def religion(self, avatar):
        """
        Params:
            avatar: (str)
        """
        return self._get("/religion", { "avatar": avatar })

    def beautiful(self, avatar):
        """
        Params:
            avatar: (str)
        """
        return self._get("/beautiful", { "avatar": avatar })

    def fear(self, avatar):
        """
        Params:
            avatar: (str)
        """
        return self._get("/fear", { "avatar": avatar })

    def sacred(self, avatar):
        """
        Params:
            avatar: (str)
        """
        return self._get("/sacred", { "avatar": avatar })

    def painting(self, avatar):
        """
        Params:
            avatar: (str)
        """
        return self._get("/painting", { "avatar": avatar })

    def color(self, color):
        """
        Params:
            color: (str) Color hex like '#FFFFFF' (# optional) or a name like 'blue'
        """
        return self._get("/color", { "color": color })

    def delete(self, avatar):
        """
        Params:
            avatar: (str)
        """
        return self._get("/delete", { "avatar": avatar })

    def garbage(self, avatar):
        """
        Params:
            avatar: (str)
        """
        return self._get("/garbage", { "avatar": avatar })

    def tom(self, avatar):
        """
        Params:
            avatar: (str)
        """
        return self._get("/tom", { "avatar": avatar })

    def bed(self, avatar, target):
        """
        Params:
            avatar: (str)
            target: (str)
        """
        return self._get("/bed", { "avatar": avatar, "target": target })

    def crush(self, avatar, target):
        """
        Params:
            avatar: (str)
            target: (str)
        """
        return self._get("/crush", { "avatar": avatar, "target": target })

    def patrick(self, avatar):
        """
        Params:
            avatar: (str)
        """
        return self._get("/patrick", { "avatar": avatar })

    def dipshit(self, text):
        """
        Params:
            text: (str) max 33 characters
        """
        return self._get("/dipshit", { "text": text })

    def picture(self, avatar):
        """
        Params:
            avatar: (str)
        """
        return self._get("/picture", { "avatar": avatar })

    def tweet(self, text):
        """
        Params:
            text: (str) max 165 chars
        """
        return self._get("/tweet", { "text": text })

    def truth(self, avatar):
        """
        Params:
            avatar: (str)
        """
        return self._get("/truth", { "avatar": avatar })

    def bobross(self, avatar):
        """
        Params:
            avatar: (str)
        """
        return self._get("/bobross", { "avatar": avatar })

    def mask(self, avatar):
        """
        Params:
            avatar: (str)
        """
        return self._get("/mask", { "avatar": avatar })

    def father(self, avatar, text):
        """
        Params:
            avatar: (str)
            text: (str) max 41 chars
        """
        return self._get("/father", { "avatar": avatar, "text": text })

    def achievement(self, avatar, text):
        """
        Params:
            avatar: (str)
            text: (str) max 21 chars
        """
        return self._get("/achievement", { "avatar": avatar, "text": text })
