***UserInfo : Khai báo thông tin jira, đường dẫn testcase


***read_excel_file : Khai báo testcase


***log_task_in_jira : Auto log jira
Với mỗi hàm mình muốn gọi, chỉ cần làm theo cấu trúc :
   try:
        (Tên hàm python của mình)
   except Exception as e:
                screenshot_path = await take_screenshot(page, str(e), 'General')
                await log_task_in_jira(jira_url, jira_username, jira_password, f"General Error on record {index}", str(e), screenshot_path)
                exception_logged = True


