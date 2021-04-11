from bs4 import BeautifulSoup
import requests
import time

def find_jobs():
    print("Enter the type of job you want:")
    job_search=input('>')
    link='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords='+job_search+'&txtLocation='

    html_content=requests.get(link).text
    soup=BeautifulSoup(html_content,'lxml')
    job_li_tags=soup.findAll('li',class_='clearfix job-bx wht-shd-bx')
    print("Enter a skill you are unfamiliar with: ")
    unfamiliar=input('>')
    for job in job_li_tags:
        published_date=job.find('span',class_='sim-posted').text.strip()
        if 'few' in published_date:
            skills_reqd=job.find('span',class_='srp-skills').text.strip().replace(' ','')
            if unfamiliar not  in skills_reqd:
                company_name=job.find('h3',class_='joblist-comp-name').text.strip()
                
                job_link=job.find('header',class_='clearfix').find('h2').a['href']
                print(f"Company name: {company_name}")
                print(f"Required skills:{skills_reqd}")
                print(f"More info: {job_link}")
                print("\n")



if __name__=="__main__":
    while True:
        find_jobs()
        time_wait=1
        print(f"Waiting for {time_wait} minutes....")
        time.sleep(time_wait*60)


