# Img API Python
This is an API wrapper for [my image manipulation API](https://github.com/pollen5/img-api) in Python.

## Install
```sh
$ pip install git+https://github.com/pollen5/imgapi
```
I'm too lazy to get this on PyPi so uh just use git for now.

## Usage
```py
import imgapi

# All options are optional.
# Port defaults to 3030
# Host defaults to localhost
# Password defaults to None.
# if session is available a session is used otherwise a new session is made.
# Loop is only used when a new session is made. If not provided defaults to asyncio.get_event_loop()
client = imgapi.Client(port=3030, host="localhost", password="password", loop=asyncio.get_event_loop(), session=aiohttp.Session())

# All functions are asynchronous.
async def main():
  img = await client.tom(avatar_url)
```
Send with discord.py using `(channel|ctx).send(file=discord.File(buffer, "image.png"))` where `buffer` is the image results of the functions.

> **Note:** The API only accepts `png` and `jpg` make sure your avatar urls are formatted accordingly, the default one uses `webp` which is not supported.

## Changelog

#### v1.0.0 (19/5/2020)
- Initial release

## License
[MIT License](LICENSE)
