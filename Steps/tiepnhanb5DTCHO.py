import asyncio
import os


async def tiepnhanb5DTCHO(page, record):
    await page.get_by_label("Log Out").click()
    await page.get_by_placeholder("Username").fill(record["user_buoc5"])
    await page.get_by_placeholder("Password").fill(record["pass_buoc5"])
    await page.get_by_placeholder("Password").press("Enter")
    extracted_data = os.getenv("EXTRACTED_DATA")
    #extracted_data = "1000.BC.XN.121124.00003"
    await page.get_by_label("INWARD - CÔNG VIỆC CỦA TÔI", exact=True).click(timeout=100000)
    await asyncio.sleep(1)
    await page.get_by_placeholder("Enter search text...").fill(f"{extracted_data}")
    await page.get_by_role("button", name="Search").click(timeout = 100000)
    await asyncio.sleep(4)
    await page.get_by_label("task row action-menu button").click()
    await page.get_by_role("link", name="Launch task completion.").click()
    if(record["chon_gddn"]=="BC"):
        if(record["ketthucb5"] == "1"):
            await page5.get_by_role("button", name=" Kết thúc").click()
            await page5.get_by_role("textbox", name="Nội dung:").fill("Xác nhận kết thúc giao dịch")
            await page5.get_by_role("button", name=" Xác nhận").click(timeout=100000)
            return
        page5 = page.frame_locator("iframe[title=\"Tiếp nhận và kiểm tra thông tin xử lý\"]").frame_locator("iframe[title=\"S5_S6_HO \\=\\= BC\"]")
        await page5.get_by_role("button", name=" Xác nhận xử lý").click(timeout =100000)
        await page5.get_by_role("link", name="Xử lý tại HO").click()
        #Có tick Tra soát/Hoàn trả/Cả Tra soát và Hoàn trả
        if (record["tick_TSHT"] == "1"):
            await page5.get_by_label("Tra soát", exact=True).check()
            await page5.get_by_label("Tra soát thuộc trường hợp").select_option("TS04")
            await page5.get_by_label("Thông tin tra soát").get_by_label("Loại điện - MT").select_option("MT196")
            await page5.get_by_label("Thông tin tra soát").get_by_label("Loại điện - IN/OUT").select_option("INWARD")
            await page5.get_by_label("Hoàn trả", exact=True).check()
            await page5.get_by_label("Hoàn trả thuộc trường hợp").select_option("HT02")
            await page5.get_by_role("link", name="Thông tin hoàn trả").click()
            await page5.get_by_label("Thông tin hoàn trả").get_by_label("Loại điện - MT").select_option("MT999")
            await page5.get_by_label("Thông tin hoàn trả").get_by_label("Loại điện - IN/OUT").select_option("OUTWARD")
        await page5.get_by_role("link", name="Trao đổi thông tin").click()
        await page5.get_by_placeholder("Nhập nội dung trao đổi").fill("maker HO bước 5 nhập nội dung")
        await page5.get_by_role("button", name=" Gửi").click(timeout=10000)
        await page5.get_by_role("link", name="Danh mục hồ sơ").click()
        file_input = page5.locator("div[id='div_162'] >> input[type='file'][aria-label='File Uploader']")
        await file_input.set_input_files("D:\WORK\AutoInward\Inward-Auto\File.txt", timeout=100000)
        await asyncio.sleep(1)
        if (record["tick_TSHT"] == "1"):
            await page5.get_by_role("button", name=" Chuyển phê duyệt").click()
            await asyncio.sleep(1)
            await page5.locator("[id='singleselect-TEMPLATE1:ApprovePopup:Approve_Modal_Child_5:NXLTT']").click(timeout = 100000)
            await page5.get_by_role("option", name="Trần Thị Xuân Luân").click()
            await page5.get_by_role("button", name=" Xác nhận").click(timeout=100000)
        else: 
            if (record["tick_TSHT"] == "0"):
                await page5.get_by_role("button", name=" Chuyển phê duyệt").click()
                await page5.get_by_role("button", name=" Xác nhận").click(timeout=100000)
    
    if(record["chon_gddn"] != "BC"):
        page51= page.frame_locator("iframe[title=\"Tiếp nhận và kiểm tra thông tin xử lý\"]").frame_locator("iframe[title=\"S5_S6_HO \\!\\= BC\"]")
        if(record["ketthucb5"] == "1"):
            await page51.get_by_role("button", name=" Kết thúc").click()
            await page51.get_by_role("textbox", name="Nội dung:").fill("Xác nhận kết thúc giao dịch")
            await page51.get_by_role("button", name=" Xác nhận").click(timeout=100000)
            return
        await page51.get_by_role("link", name="Trao đổi thông tin").click()
        await page51.get_by_placeholder("Nhập nội dung trao đổi").fill("maker HO bước 5 nhập nội dung")
        await page51.get_by_role("button", name=" Gửi").click(timeout=10000)
        await page51.get_by_role("link", name="Danh mục hồ sơ").click()
        file_input = page51.locator("div[id='div_127'] >> input[type='file'][aria-label='File Uploader']")
        await file_input.set_input_files("D:\WORK\AutoInward\Inward-Auto\File.txt", timeout=100000)
        await page51.get_by_role("button", name=" Chuyển phê duyệt").click()
        await page51.get_by_role("button", name=" Xác nhận").click(timeout=100000)

        

