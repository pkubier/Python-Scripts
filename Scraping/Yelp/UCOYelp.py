import pandas as pd 
import time as t
from lxml import html  
import requests

reviews_df=pd.DataFrame()
  



numbr=['30'] # 0,30,60,90,120...
u=[]
for n in numbr:
    
    searchlink='https://www.yelp.com/search?find_desc=Restaurants&find_loc=Chicago,+IL&start='+str(n)

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'
    headers = {'User-Agent': user_agent}
    
    page = requests.get(searchlink, headers = headers)
    parser = html.fromstring(page.content)


    businesslink=parser.xpath('//a[@class="biz-name js-analytics-click"]')
    links = [l.get('href') for l in businesslink]
    
    for link in links:
        
        u.append('https://www.yelp.com'+ str(link))

for item in u:
    

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'
    headers = {'User-Agent': user_agent}
    
    
    t.sleep(5)
    page = requests.get(item, headers = headers)
    parser = html.fromstring(page.content)
    
    print(item)


    page_nums = '//a[@class="available-number pagination-links_anchor"]'
    pg = parser.xpath(page_nums)

    max_pg=len(pg)+1

    ab=['0','20','40','60','80','100','120','140','160','180','200','220','240','260','280','300','320','340','360','380','400','420',
    '440','460','480','500','520','540','560','580','600','620','640','660','680','700','720','740','760','780','800']
    
    if 3<max_pg:
        scrapepg=3
    else:
        scrapepg=1

    for p in (ab[:scrapepg]):
    
        newurl=item.split('?')[0]+'?start='+str(p)
        
        
        t.sleep(5)
        
    
        page = requests.get(newurl, headers = headers)
        parser = html.fromstring(page.content )
        
        
        xpath_reviews = '//div[@class="review review--with-sidebar"]'
        reviews = parser.xpath(xpath_reviews)

        for review in reviews:
            temp = review.xpath('.//div[contains(@class, "i-stars i-stars--regular")]')
      
            rating = [td.get('title') for td in temp]
        

            xpath_author  = './/a[@id="dropdown_user-name"]//text()'
            xpath_body    = './/p[@lang="en"]//text()'
    
            author  = review.xpath(xpath_author)
    
            date    = review.xpath('.//span[@class="rating-qualifier"]//text()')
    
            body    = review.xpath(xpath_body)
        
            heading= parser.xpath('//h1[contains(@class,"biz-page-title embossed-text-white")]')
            bzheading = [td.text for td in heading]
             
    
    
            review_dict = {'restaurant' : bzheading,
                                    'rating': rating,
                                  
                                       'author': author,             
                                       'date': date,
                                           'Review': body,
                                      }
            reviews_df = reviews_df.append(review_dict, ignore_index=True)
            
         
        
reviews_df
