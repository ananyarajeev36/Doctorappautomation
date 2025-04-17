from playwright.sync_api import sync_playwright, Page, Browser,expect




def global_helper_function() -> tuple[Page, Browser, sync_playwright]:
    """Set up the browser and return a Page instance."""
    playwright = sync_playwright().start()
    # Launch Microsoft Edge
    browser = playwright.chromium.launch(channel="msedge", headless=False)  # Ensure to use the correct channel
    page = browser.new_page()
    return page, browser, playwright