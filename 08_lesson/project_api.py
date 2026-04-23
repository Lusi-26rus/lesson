import requests

class ProjectAPI:
    def __init__(self, url, token, company_id):
        self.url = url
        self.company_id = company_id
        self.headers = {
            # Попробуем самый надежный для Yougile заголовок для API-ключей
            "Authorization": "Bearer gRJOhVTXUueK40M2BH2j2wAcB8Nc+WKWOrmgv2DOhIw3wuyhfE82vrO21aCPbPFo", 
            "Content-Type": "application/json"
        }

    def create_project(self, title):
        body = {
            "title": title,
            
            #"companyId": self.company_id 
        }
        return requests.post(f"{self.url}/api-v2/projects", json=body, headers=self.headers)

    def get_project(self, project_id):
        return requests.get(f"{self.url}/api-v2/projects/{project_id}", headers=self.headers)

    def update_project(self, project_id, new_title):
        body = {
            "title": new_title,
            #"companyId": self.company_id
        }
        return requests.put(f"{self.url}/api-v2/projects/{project_id}", json=body, headers=self.headers)