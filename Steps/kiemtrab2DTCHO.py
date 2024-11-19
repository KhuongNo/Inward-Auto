import asyncio
import os


async def kiemtrab2DTCHO(page, record):
    await page.get_by_label("Log Out").click()
    await page.get_by_placeholder("Username").fill(record["user_buoc2"])
    await page.get_by_placeholder("Password").fill(record["pass_buoc2"])
    await page.get_by_placeholder("Password").press("Enter")
    extracted_data = os.getenv("EXTRACTED_DATA")
    #extracted_data = "1000.BC.XN.151124.00025"
    await page.get_by_label("INWARD - CÔNG VIỆC CỦA TÔI", exact=True).click(timeout=100000)
    await page.get_by_placeholder("Enter search text...").fill(f"{extracted_data}")
    await page.get_by_role("button", name="Search").click(timeout = 100000)
    await asyncio.sleep(2)
    await page.get_by_label("task row action-menu button").click()
    await page.get_by_role("link", name="Launch task completion.").click()
    page2 = page.frame_locator("iframe[title=\"Kiểm tra yêu cầu\"]").frame_locator("iframe[title=\"HO BC\"]")
    await page2.get_by_label("Chứng từ cần bổ sung").check()
    await page2.get_by_label("Gia hạn hạn phản hồi").check()
    await page2.get_by_role("link", name="Trao đổi thông tin").click()
    await page2.get_by_placeholder("Nhập nội dung trao đổi").fill("checker HO nhập nội dung")
    await page2.get_by_role("button", name=" Gửi").click(timeout=10000)
    await page2.get_by_role("link", name="Danh mục hồ sơ").click()
    file_input = page2.locator("div[id='div_136'] >> input[type='file'][aria-label='File Uploader']")
    await file_input.set_input_files("D:\WORK\AutoInward\Inward-Auto\File.txt", timeout=100000)
    await asyncio.sleep(1)
    await page2.get_by_role("button", name=" Phê duyệt").click()
    await asyncio.sleep(1)
    await page2.locator("[id='singleselect-TEMPLATE1:ApprovePopup:Approve_Modal_Child_2:NXLTT']").click(timeout = 100000)
    await page2.get_by_role("option", name="HUỲNH ĐOÀN DUY KHƯƠNG").click()
    await page2.get_by_role("button", name=" Xác nhận").click(timeout=100000)
