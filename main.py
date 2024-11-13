import asyncio
import os
from datetime import datetime
from playwright.async_api import async_playwright
from Functions.UserInfo import jira_url, jira_username, jira_password, data_file_path, data_file_path1, network_data_path, security_test_path
from Functions.read_excel_file import read_excel_file
from Functions.take_screenshot import take_screenshot
from Functions.log_task_in_jira import log_task_in_jira
# from Functions.capture_network import capture_networks
from Functions.log_console import log_console
from Steps.khoitaoDTCDVKD import khoitaoDTCDVKD
from Steps.khoitaoDTCHO import khoitaoDTCHO


# Import the database functions
from Functions.QueryDB import run_multiple_queries_and_save

async def process_workflow(playwright, jira_url, jira_username, jira_password, data, start_index=0, run_all=False, chon_qt=None):
    os.makedirs('screenshots', exist_ok=True)
    os.makedirs(network_data_path, exist_ok=True)
    os.makedirs(security_test_path, exist_ok=True)
    
    index = start_index
    while index < len(data):
        exception_logged = False
        record = data[index]
        print(f"Running testcase {index}")
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context(ignore_https_errors=True)
        page = await context.new_page()
        await page.goto("https://172.29.255.116:9444/ProcessPortal/login.jsp")
        # Generate timestamp for filenames
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Capture network
        network_output_file = os.path.join(network_data_path, f"network_data_{index}_{timestamp}.xlsx")
        # asyncio.create_task(capture_network(page, network_output_file, index))

        # Capture console
        console_log_output_file = os.path.join(network_data_path, f"console_log_{index}_{timestamp}.xlsx")
        asyncio.create_task(log_console(page, console_log_output_file))
        update_action_label = await log_console(page, console_log_output_file)


        try:
    # Your code start here -------------------------------------------------------------------------------------------------------------------------------------------------
            print (f"{chon_qt}")
            if (chon_qt == 'dvkd'):
            # try:
                await khoitaoDTCDVKD(page,record)
            else:
                if (chon_qt == 'ho'):
                # try:
                    await khoitaoDTCHO(page,record)

            # except Exception as e:
            #     screenshot_path = await take_screenshot(page, str(e), 'QDE')
            #     await log_task_in_jira(jira_url, jira_username, jira_password, f"Lỗi ở màn hình QDE với testcase số {index}", str(e), screenshot_path)
            #     exception_logged = True
            # await TTGD_E(page,record)
            print("Script finished")
            input("Press Enter to close the browser...")


    # Your code end here ----------------------------------------------------------------------------------------------------------------------------------------------------

        # except Exception as e:
        #     if not exception_logged:
        #         screenshot_path = await take_screenshot(page, str(e), 'General')
        #         await log_task_in_jira(jira_url, jira_username, jira_password, f"General Error on record {index}", str(e), screenshot_path)
        #         exception_logged = True
        
        finally:
            try:
                await context.close()
                await browser.close()
            except Exception as close_error:
                print(f"Failed to close browser: {close_error}")

        if not run_all:
            continue_running = input(f"Test case {index} finished. Run the rest of the test cases (from {index})? (Yes/No): ")
            if continue_running.lower() == 'yes':
                run_all = True  # Set run_all to True to run the rest without further prompts
            else:
                break
        
        index += 1


async def main():
    # Read data from Excel file
    chon_qt = input("Start DTC from DVKD or from HO? (type 'HO' or a 'DVKD'): ")
    print (f"{chon_qt}")
    if chon_qt.lower() == 'dvkd':
        data = read_excel_file(data_file_path)
    else:
        if chon_qt.lower() == 'ho':
            data = read_excel_file(data_file_path1)
    choice = input("Run all test cases or just 1? (type 'all' or a number): ")
    print(f"{data}")

    if choice.lower() == 'all':
        async with async_playwright() as playwright:
            await process_workflow(playwright, jira_url, jira_username, jira_password, data, run_all=True, chon_qt=chon_qt)
    else:
        try:
            specific_test = int(choice)
            async with async_playwright() as playwright:
                await process_workflow(playwright, jira_url, jira_username, jira_password, data, start_index=specific_test, chon_qt=chon_qt)
        except ValueError:
            print("Invalid input. Please type 'all' or a number.")

# Run the script using asyncio
asyncio.run(main())
