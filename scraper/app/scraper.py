from playwright.async_api import async_playwright


async def scrape_url(url: str) -> dict:
    """
    Minimal scraping logic.
    Extend later for LinkedIn/company portals.
    """
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        try:
            await page.goto(url, timeout=30000)
            await page.wait_for_load_state("networkidle")

            title = await page.title()
            html = await page.content()

            return {
                "title": title,
                "html_preview": html[:5000]   # avoid massive payloads
            }

        except Exception as e:
            return {"error": str(e)}

        finally:
            await browser.close()
