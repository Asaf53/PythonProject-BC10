from requests import request
from bs4 import BeautifulSoup
import json

def scrape_link(link):
    url: str = link
    domain = url.split(".com")[0] + ".com"

    json_file: str = "jobs.json"
    data: list = []

    resp = request("GET", url)

    if resp.status_code == 200:
        bs = BeautifulSoup(resp.text, "html.parser")
        links = bs.find_all("a", {"class": "JobSearchCard-primary-heading-link"})
        for link in links[0:2]:
            link_response = request("GET", domain + link["href"])
            if link_response.status_code == 200:
                lbs = BeautifulSoup(link_response.text, "html.parser")

                title = lbs.title.text

                price = lbs.select_one(
                    "body > app-root > app-logged-out-shell > div > app-project-view > app-project-view-logged-out > fl-container > fl-container > app-project-view-logged-out-main > div:nth-child(2) > div.Project-heading > div:nth-child(2) > fl-heading > h2"
                )

                if price is not None:
                    price = price.text
                else:
                    price = 0

                job_link = domain + link["href"]

                if job_link is not None:
                    job_link = domain + link["href"]
                else:
                    job_link = ""

                description = lbs.select_one(
                    "body > app-root > app-logged-out-shell > div > app-project-view > app-project-view-logged-out > fl-container > fl-container > app-project-view-logged-out-main > div:nth-child(2) > fl-text.Project-description > div"
                )

                if description is not None:
                    description = description.text
                else:
                    description = ""

                posted = lbs.select_one(
                    "body > app-root > app-logged-out-shell > div > app-project-view > app-project-view-logged-out > fl-container > fl-container > app-project-view-logged-out-main > div:nth-child(2) > div.Project-heading > div.Project-heading-title > div > fl-tag > div > fl-text > span > div > fl-text > div"
                )

                if posted is not None:
                    posted = posted.text
                else:
                    posted = ""

                deadline = lbs.select_one(
                    "body > app-root > app-logged-out-shell > div > app-project-view > app-project-view-logged-out > fl-container > fl-container > app-project-view-logged-out-main > div:nth-child(2) > div.Project-heading > div.Project-heading-title > div > fl-text:nth-child(4) > div"
                )

                if deadline is not None:
                    deadline = deadline.text
                else:
                    deadline = ""

                clientFlag = lbs.select_one(
                    "body > app-root > app-logged-out-shell > div > app-project-view > app-project-view-logged-out > fl-container > app-project-view-logged-out-side > fl-container > div:nth-child(2) > app-project-view-logged-out-client-info > div:nth-child(2) > div > fl-flag > img"
                )

                if clientFlag is not None:
                    clientFlag = clientFlag["src"]
                else:
                    clientFlag = ""

                clientLocation = lbs.select_one(
                    "body > app-root > app-logged-out-shell > div > app-project-view > app-project-view-logged-out > fl-container > app-project-view-logged-out-side > fl-container > div:nth-child(2) > app-project-view-logged-out-client-info > div:nth-child(2) > fl-text > div"
                )

                if clientLocation is not None:
                    clientLocation = clientLocation.text
                else:
                    clientLocation = ""

                category = lbs.select_one(
                    "body > app-root > app-logged-out-shell > div > app-project-view > app-project-view-logged-out > fl-container > fl-container > app-project-view-logged-out-main > div:nth-child(2) > div.ng-star-inserted > fl-tag:nth-child(1) > fl-link > a > fl-text > span > div"
                )
                if category is not None:
                    category = category.text
                else:
                    category = ""

                project_id = lbs.select_one(
                    "body > app-root > app-logged-out-shell > div > app-project-view > app-project-view-logged-out > fl-container > fl-container > app-project-view-logged-out-main > div:nth-child(2) > fl-text:nth-child(4) > div"
                )
                if project_id is not None:
                    project_id = project_id.text
                else:
                    project_id = ""

                work_type = lbs.select_one(
                    "body > app-root > app-logged-out-shell > div > app-project-view > app-project-view-logged-out > fl-container > fl-container > app-project-view-logged-out-main > div:nth-child(2) > app-project-view-logged-out-about > fl-grid > fl-col:nth-child(3) > fl-text > div"
                )
                if work_type is not None:
                    work_type = work_type.text
                else:
                    work_type = ""

                propesals = lbs.select_one(
                    "body > app-root > app-logged-out-shell > div > app-project-view > app-project-view-logged-out > fl-container > fl-container > app-project-view-logged-out-main > div:nth-child(2) > app-project-view-logged-out-about > fl-grid > fl-col:nth-child(1) > fl-text > div"
                )
                if propesals is not None:
                    propesals = propesals.text
                else:
                    propesals = ""

                data.append(
                    {
                        "title": title,
                        "job_link": job_link,
                        "description": description,
                        "price": price,
                        "clientFlag": clientFlag,
                        "clientLocation": clientLocation,
                        "category": category,
                        "deadline": deadline,
                        "work_type": work_type,
                        "propesals": propesals,
                        "project_id": project_id,
                    }
                )

                print(f'Scraping: "{title}"')
    else:
        print(f"Error: URL returned status code {resp.status_code}")

    if len(data) > 0:
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    else:
        print("Error: Data list is empty!")
