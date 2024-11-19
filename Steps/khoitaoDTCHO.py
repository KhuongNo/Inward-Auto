import asyncio
import os
from datetime import datetime

async def khoitaoDTCHO(page, record):
    await page.get_by_placeholder("Username").fill(record["user_buoc1"])
    await page.get_by_placeholder("Password").fill(record["pass_buoc1"])
    await page.get_by_role("link", name="Log in").click(timeout=100000)
    await page.get_by_label("Chuyển tiền đến từ NNg - Điện tài chính", exact=True).click(timeout=100000)
    today_date = datetime.today().strftime("%d/%m/%Y")
    if(record["chon_gddn"]=="BC"):
        await page.frame_locator("iframe[title=\"Coach\"]").get_by_label("Giao dịch đề nghị").select_option("BC")
        await page.frame_locator("iframe[title=\"Coach\"]").get_by_label("Nghiệp vụ").select_option("XN")
        await page.frame_locator("iframe[title=\"Coach\"]").get_by_role("button", name=" Khởi tạo").click(timeout=100000)
        extracted_data = await page.frame_locator("iframe[title=\"Khởi tạo yêu cầu\"]").frame_locator("iframe[title=\"HO BC\"]").locator("[id='outputtext-text-TEMPLATE1:LAYOUT_ITEM_ID1:Output_Text1']").inner_text()       
        # Set the extracted data as an environment variable
        page1 = page.frame_locator("iframe[title=\"Khởi tạo yêu cầu\"]").frame_locator("iframe[title=\"HO BC\"]")
        os.environ["EXTRACTED_DATA"] = extracted_data
        print(f"{extracted_data}")
        await page1.locator("[id='datetimepicker-input-TTGD_MT1031:TTGD_PARENT1:Date_Time_Picker1']").fill(today_date)
        await page1.get_by_placeholder("Nhập nội dung", exact=True).fill("000018687464")
        await page1.locator("[id='singleselect-TTGD_MT1031:RmTest:brnDVKD']").click()
        await asyncio.sleep(1)
        await page1.get_by_role("option", name="- Chi nhánh Tp.Hồ Chí Minh").click()
        await page1.locator("[id='singleselect-TTGD_MT1031:RmTest:Single_Select2']").click()
        await page1.get_by_role("option", name="Xác nhận nội dung, cung cấp").click()
        await page1.get_by_role("link", name="Trao đổi thông tin").click()
        await page1.get_by_placeholder("Nhập nội dung trao đổi").fill("Maker HO khởi tạo nhập nội dung")
        await page1.get_by_role("button", name=" Gửi").click(timeout=100000)
        await page1.get_by_role("link", name="Danh mục hồ sơ").click()
        file_input = page1.locator("div[id='div_136'] >> input[type='file'][aria-label='File Uploader']")
        await file_input.set_input_files("D:\WORK\AutoInward\Inward-Auto\File.txt", timeout=100000)
        await page1.get_by_role("button", name=" Chuyển xử lý").click()
        await page1.get_by_role("tabpanel", name="Kiểm tra").get_by_label("Luồng duyệt:").select_option("HTPD01")
        await asyncio.sleep(1)
        await page1.locator("[id='singleselect-TEMPLATE1:ApprovePopup:Approve_Modal_Child_1:NXLTT']").click(timeout = 100000)
        await page1.get_by_role("option", name="Trần Thị Mỹ Hương").click()
        await page1.get_by_role("button", name=" Xác nhận").click(timeout=100000)
    if(record["chon_gddn"]=="PHIHO"):
        await page.frame_locator("iframe[title=\"Coach\"]").get_by_label("Giao dịch đề nghị").select_option("PHIHO")
        await page.frame_locator("iframe[title=\"Coach\"]").get_by_label("Nghiệp vụ").select_option("OUR")
        await page.frame_locator("iframe[title=\"Coach\"]").get_by_role("button", name=" Khởi tạo").click(timeout=100000)
        extracted_data = await page.frame_locator("iframe[title=\"Khởi tạo yêu cầu\"]").frame_locator("iframe[title=\"HO \\!\\= BC\"]").locator("[id='outputtext-text-TEMPLATE1:LAYOUT_ITEM_ID1:Output_Text1']").inner_text()       
        os.environ["EXTRACTED_DATA"] = extracted_data
        print(f"{extracted_data}")
        page11 = page.frame_locator("iframe[title=\"Khởi tạo yêu cầu\"]").frame_locator("iframe[title=\"HO \\!\\= BC\"]")
        await page11.locator("[id='singleselect-TTGD_MT1031:Single_Select1']").click()
        await asyncio.sleep(1)
        await page11.get_by_role("option", name="- Chi nhánh Tp.Hồ Chí Minh").click()
        await page11.locator("[id='datetimepicker-input-TTGD_MT1031:Date_Time_Picker1']").fill(today_date)
        await page11.get_by_role("link", name="Trao đổi thông tin").click()
        await page11.get_by_placeholder("Nhập nội dung trao đổi").fill("Maker HO khởi tạo nhập nội dung")
        await page11.get_by_role("button", name=" Gửi").click(timeout=100000)
        file_import = page11.locator("div[id='div_54_1_2_1_2_1_1_1_2'] >> input[type='file'][aria-label='File Uploader']")
        await file_import.set_input_files("D:\WORK\AutoInward\Inward-Auto\Temlate_OUR_kho_doi.xlsx", timeout=100000)
        await page11.get_by_role("link", name="Danh mục hồ sơ").click()
        file_input = page11.locator("div[id='div_127'] >> input[type='file'][aria-label='File Uploader']")
        await file_input.set_input_files("D:\WORK\AutoInward\Inward-Auto\File.txt", timeout=100000)
        await page11.get_by_role("button", name=" Chuyển xử lý").click()
        await asyncio.sleep(1)
        await page11.locator("[id='singleselect-TEMPLATE1:ApprovePopup:Approve_Modal_Child_2:NXLTT']").click(timeout = 100000)
        await page11.get_by_role("option", name="HUỲNH ĐOÀN DUY KHƯƠNG").click()
        await page11.get_by_role("button", name=" Xác nhận").click(timeout=100000)
    if(record["chon_gddn"]=="RP"):
        await page.frame_locator("iframe[title=\"Coach\"]").get_by_label("Giao dịch đề nghị").select_option("RP")
        await page.frame_locator("iframe[title=\"Coach\"]").get_by_label("Nghiệp vụ").select_option("RP")
        await page.frame_locator("iframe[title=\"Coach\"]").get_by_role("button", name=" Khởi tạo").click(timeout=100000)
        extracted_data = await page.frame_locator("iframe[title=\"Khởi tạo yêu cầu\"]").frame_locator("iframe[title=\"HO \\!\\= BC\"]").locator("[id='outputtext-text-TEMPLATE1:LAYOUT_ITEM_ID1:Output_Text1']").inner_text()       
        os.environ["EXTRACTED_DATA"] = extracted_data
        print(f"{extracted_data}")
    if(record["chon_gddn"]=="XLK"):
        await page.frame_locator("iframe[title=\"Coach\"]").get_by_label("Giao dịch đề nghị").select_option("XLK")
        await page.frame_locator("iframe[title=\"Coach\"]").get_by_label("Nghiệp vụ").select_option("XLK")
        await page.frame_locator("iframe[title=\"Coach\"]").get_by_role("button", name=" Khởi tạo").click(timeout=100000)
        extracted_data = await page.frame_locator("iframe[title=\"Khởi tạo yêu cầu\"]").frame_locator("iframe[title=\"HO \\!\\= BC\"]").locator("[id='outputtext-text-TEMPLATE1:LAYOUT_ITEM_ID1:Output_Text1']").inner_text()       
        os.environ["EXTRACTED_DATA"] = extracted_data
        print(f"{extracted_data}")
        


