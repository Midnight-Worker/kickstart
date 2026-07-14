import asyncio
from playwright.async_api import async_playwright


async def start_browser(
    url="https://quotes.toscrape.com/",
    headless=False,
):
    pw = await async_playwright().start()

    browser = await pw.chromium.launch(
        headless=headless,
    )

    page = await browser.new_page()
    await page.goto(url)

    return pw, browser, page


async def stop_browser(pw, browser):
    if browser.is_connected():
        await browser.close()

    await pw.stop()

async def main():
    pw, browser, page = await start_browser()

asyncio.run(main())
