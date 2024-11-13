import asyncio
import os

async def khoitaoDTCHO(page, record):
    await page.get_by_placeholder("Username").fill(record["user_buoc1"])
    await page.get_by_placeholder("Password").fill(record["pass_buoc1"])
    await page.get_by_placeholder("Password").press("Enter")