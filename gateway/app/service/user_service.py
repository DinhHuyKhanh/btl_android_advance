import httpx

class UserService():

    async def get_all_user(self, url):
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            return response.json()
