import asyncio
import os


async def pheduyetb6DTCHO(page, record):
    await page.get_by_label("Log Out").click()
    await page.get_by_placeholder("Username").fill(record["user_buoc6"])
    await page.get_by_placeholder("Password").fill(record["pass_buoc6"])
    await page.get_by_placeholder("Password").press("Enter")
    extracted_data = os.getenv("EXTRACTED_DATA")
    #extracted_data = "1000.BC.XN.191124.00002"
    await page.get_by_label("INWARD - CÔNG VIỆC CỦA TÔI", exact=True).click(timeout=100000)
    await page.get_by_placeholder("Enter search text...").fill(f"{extracted_data}")
    await page.get_by_role("button", name="Search").click(timeout = 100000)
    await asyncio.sleep(2)
    await page.get_by_label("task row action-menu button").click()
    await page.get_by_role("link", name="Launch task completion.").click()
    page6 = page.frame_locator("iframe[title=\"Phê duyệt yêu cầu\"]").frame_locator("iframe[title=\"S5_S6_HO \\=\\= BC\"]")
    await page6.get_by_role("link", name="Xử lý tại HO").click()
    await page6.get_by_role("button", name=" Tạo điện").click()
    await page6.get_by_role("link", name="Trao đổi thông tin").click()
    await page6.get_by_placeholder("Nhập nội dung trao đổi").fill("checker HO phê duyệt nhập nội dung")
    await page6.get_by_role("button", name=" Gửi").click(timeout=10000)
    await page6.get_by_role("link", name="Danh mục hồ sơ").click()
    file_input = page6.locator("div[id='div_162'] >> input[type='file'][aria-label='File Uploader']")
    await file_input.set_input_files("D:\WORK\AutoInward\Inward-Auto\File.txt", timeout=100000)
    await asyncio.sleep(1)
    await page6.get_by_role("button", name=" Phê duyệt").click()
    await page6.get_by_role("button", name=" Xác nhận").click(timeout=100000)
    if(record["ketthucb6"]=="1"):
        await page6.get_by_role("button", name=" Kết thúc").click()
        await page6.get_by_role("textbox", name="Nội dung:").fill("Xác nhận kết thúc giao dịch")
        await page6.get_by_role("button", name=" Xác nhận").click(timeout=100000)
