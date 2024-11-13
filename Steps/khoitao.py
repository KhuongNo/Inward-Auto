import asyncio
import os

async def khoitao(page, record):
    await page.get_by_placeholder("Username").fill(record["user_buoc1"])
    await page.get_by_placeholder("Password").fill(record["pass_buoc1"])
    await page.get_by_placeholder("Password").press("Enter")
    await page.get_by_label("Chuyển tiền đến từ NNg - Điện tài chính", exact=True).click(timeout =100000)
    if (record["chon_gddn"] == "MT103"):
        await page.frame_locator("iframe[title=\"Coach\"]").get_by_label("Giao dịch đề nghị").select_option("MT103")
        await page.frame_locator("iframe[title=\"Coach\"]").get_by_label("Nghiệp vụ").select_option("TS")
    if (record["chon_gddn"] == "PHIDV"):
        await page.frame_locator("iframe[title=\"Coach\"]").get_by_label("Giao dịch đề nghị").select_option("PHIDV")
        await page.frame_locator("iframe[title=\"Coach\"]").get_by_label("Nghiệp vụ").select_option("TPK")
    if (record["chon_gddn"] == "PHIDV"):
        await page.frame_locator("iframe[title=\"Coach\"]").get_by_label("Giao dịch đề nghị").select_option("RP")
        await page.frame_locator("iframe[title=\"Coach\"]").get_by_label("Nghiệp vụ").select_option("RP")
    if (record["chon_gddn"] == "PHIDV"):
        await page.frame_locator("iframe[title=\"Coach\"]").get_by_label("Giao dịch đề nghị").select_option("FRAUD")
        await page.frame_locator("iframe[title=\"Coach\"]").get_by_label("Nghiệp vụ").select_option("FRAUD")
    if (record["chon_nghiepvu"] == "PHIDV"):
        await page.frame_locator("iframe[title=\"Coach\"]").get_by_label("Giao dịch đề nghị").select_option("XLK")
        await page.frame_locator("iframe[title=\"Coach\"]").get_by_label("Nghiệp vụ").select_option("XLK")
    await page.frame_locator("iframe[title=\"Coach\"]").get_by_role("button", name=" Khởi tạo").click()