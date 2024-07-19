from playwright.sync_api import *
from playwright_stealth import stealth_sync
import time
from config import *

with sync_playwright() as playwright:
    extra_headers = {
    'Sec-Ch-Ua':
    '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'Sec-Ch-Ua-Mobile':
    '?0',
    'Sec-Ch-Ua-Platform':
    "Linux",
    'Sec-Fetch-Dest':
    'empty',
    'Sec-Fetch-Mode':
    'cors',
    'Sec-Fetch-Site':
    'same-site',
    }
    # Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    browser=playwright.firefox.launch(headless=False,slow_mo=500)
    # page= browser.new_page()
    context = browser.new_context(extra_http_headers = extra_headers)
    page = context.new_page()
    stealth_sync(page)
    
    # page.goto('https://www.delta.nl/')
    
    # close_btn=page.get_by_role('button',name='Ja, dat is prima')
    # close_btn.click()
    
    # main_menu=['At Home','For Companies']
   

    # core_menu=['Internet','Television','Mobile']
   

    # title=page.locator(selector='head > title').text_content()
    # whole=page.locator(selector='.base').all_inner_texts()

    # f=open(f'ScrapedData/{list(main_menu_urls.keys())[0]}/{title}.txt','w')
    # f.write(title[0])
    # f.close()

    for j in range(2):

        url=list(main_menu_urls.values())[j]

        page.goto(f'{original_url}/{url}')
        title=page.locator(selector='head > title').text_content()
        whole=page.locator(selector='.base').all_inner_texts()

        f=open(f'ScrapedData/{list(main_menu_urls.keys())[j]}/{title}.txt','w')
        f.write(title[0])
        f.close()
        

        for i in range(1,main_menu_index_last[j]):
            nav_element=page.locator(f'#coreMenu > li:nth-child({i})')
        # # nav_bar=page.locator(selector=f'#coreMenu')
            links=nav_element.all_text_contents()[0]
            links=links.replace('\n',',')
            links=links.split(',')
            links = [i for i in links if i != '']
            core_menu.append(links[0])
            if i==3:
                links=links[2:-1]
            else:
                links=links[1:-1] 
            print(links)
            nav_element.hover() 

            visited=[]
            for link in links:
                elements=page.locator(f'text={link}').all()
                for element in elements:
                    href=element.get_attribute('href')
                    print(f'Element: {element.all_inner_texts()}, href: {href}')
                    if href:
                        if href not in visited:
                            page.goto(original_url+href)
                            title=page.locator(selector='head > title').text_content()
                            print(f'TITLE: {title}')
                            print(f'HREF: {href}')
                            content=page.locator(selector='.base').all_inner_texts()
                            f=open(f'ScrapedData/{list(main_menu_urls.keys())[j]}/{core_menu[i-1]}/{title}.txt','w')
                            f.write(content[0])
                            f.close()
                            visited.append(href)
                            break
        
        page.goto(f'{original_url}/{url}')
        core_menu=[]
        nav_element5=page.locator(f'#{service_page_selector[j]} > header > div.df-header-main > div > div > div.df-header-navigation-primary > div:nth-child({service_page_index[j]}) > a ')
        nav_element5.click()
        title=page.locator(selector='head > title').text_content()
        print(f'TITLE: {title}')
        print(f'HREF: {page.url}')
        content=page.locator(selector='.base').all_inner_texts()
        f=open(f'ScrapedData/{list(main_menu_urls.keys())[j]}/{title}.txt','w')
        f.write(content[0])
        f.close()

#homepage > header > div.df-header-main > div > div > div.df-header-navigation-primary > div:nth-child(4) > a
#homepagezakelijk > header > div.df-header-main > div > div > div.df-header-navigation-primary > div:nth-child(3) > a

#     url='https://www.delta.nl/zakelijk'
#     # For Companies
# #coreMenu > li:nth-child(1)

#     nav_element4=page.locator('#homepage > header > div.df-header-main > div > div > div.df-header-navigation-primary > div:nth-child(3) > a ')
#     nav_element4.click()
#     for i in range(1,4):
#         nav_element=page.locator(f'#coreMenu > li:nth-child({i})')
#     # # nav_bar=page.locator(selector=f'#coreMenu')
#         links=nav_element.all_text_contents()[0]
#         links=links.replace('\n',',')
#         links=links.split(',')
#         links = [i for i in links if i != '']
#         if i==3:
#             links=links[2:-1]
#         else:
#             links=links[1:-1] 
#         print(links)
#         nav_element.hover() 

#         visited=[]
#         for link in links:
#             elements=page.locator(f'text={link}').all()
#             for element in elements:
#                 href=element.get_attribute('href')
#                 print(f'Element: {element.all_inner_texts()}, href: {href}')
#                 if href:
#                     if href not in visited:
#                         page.goto(url+href)
#                         title=page.locator(selector='head > title').text_content()
#                         print(f'TITLE: {title}')
#                         print(f'HREF: {href}')
#                         content=page.locator(selector='.base').all_inner_texts()
#                         f=open(f'ScrapedData/{main_menu[0]}/{core_menu[i-1]}/{title}.txt','w')
#                         f.write(content[0])
#                         f.close()
#                         visited.append(href)
#                         break







    








    
    
    
    
    
    