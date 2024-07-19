from playwright.sync_api import *
from playwright_stealth import stealth_sync
import time
from config import *

with sync_playwright() as playwright:
    
    
    browser=playwright.firefox.launch(headless=False,slow_mo=500)
    context = browser.new_context(extra_http_headers = extra_headers)
    page = context.new_page()
    stealth_sync(page)
    
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

