import asyncio
import os


async def kiemtrab4DTCHO(page, record):
    await page.get_by_label("Log Out").click()
    await page.get_by_placeholder("Username").fill(record["user_buoc4"])
    await page.get_by_placeholder("Password").fill(record["pass_buoc4"])
    await page.get_by_placeholder("Password").press("Enter")
    extracted_data = os.getenv("EXTRACTED_DATA")
    #extracted_data = "1000.BC.TSNN.151124.00002"
    await page.get_by_label("INWARD - CÔNG VIỆC CỦA TÔI", exact=True).click(timeout=100000)
    await page.get_by_placeholder("Enter search text...").fill(f"{extracted_data}")
    await page.get_by_role("button", name="Search").click(timeout = 100000)
    await asyncio.sleep(2)
    await page.get_by_label("task row action-menu button").click()
    await page.get_by_role("link", name="Launch task completion.").click()
    page4 = page.frame_locator("iframe[title=\"Kiểm tra thông tin xử lý\"]").frame_locator("iframe[title=\"HO BC\"]")
    await page4.get_by_role("link", name="Trao đổi thông tin").click()
    await page4.get_by_placeholder("Nhập nội dung trao đổi").fill("checker DVKD nhập nội dung")
    await page4.get_by_role("button", name=" Gửi").click(timeout=10000)
    await page4.get_by_role("link", name="Danh mục hồ sơ").click()
    file_input = page4.locator("div[id='div_136'] >> input[type='file'][aria-label='File Uploader']")
    await file_input.set_input_files("D:\WORK\AutoInward\Inward-Auto\File.txt", timeout=100000)
    await asyncio.sleep(1)
    await page4.get_by_role("button", name=" Phê duyệt").click()
    await asyncio.sleep(1)
    await page4.locator("[id='singleselect-TEMPLATE1:ApprovePopup:Approve_Modal_Child_4:NXLTT']").click(timeout = 100000)
    await page4.get_by_role("option", name="Lê Vũ Kim Tuyền").click()
    await page4.get_by_role("button", name=" Xác nhận").click(timeout=100000)
