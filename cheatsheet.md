# Browser
browser = playwright.chromium.launch(headless=False)
page = browser.new_page()
browser.close()

# Navigation
page.goto(url)
page.reload()
page.go_back()
page.go_forward()

# Informationen
page.title()
page.url
page.content()

# Speichern
page.screenshot(path="bild.png", full_page=True)

# Elemente finden
page.locator(".klasse")
page.locator("#id")
page.get_by_text("Text")
page.get_by_role("button", name="Speichern")
page.get_by_label("E-Mail")
page.get_by_placeholder("Suchbegriff")

# Interaktion
locator.click()
locator.fill("Text")
locator.press("Enter")
locator.check()
locator.uncheck()
locator.select_option("DE")

# Daten lesen
locator.inner_text()
locator.text_content()
locator.get_attribute("href")
locator.input_value()

# Listen
locator.count()
locator.first
locator.last
locator.nth(0)
locator.all_inner_texts()
