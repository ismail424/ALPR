from isort import file
import requests
from bs4 import BeautifulSoup

class GetLicensePlateDemo:
    def __init__(self, file_src: str):
        self.session = requests.Session() 
        self.file_src = file_src
        self.token = self.get_free_token()
        print("Token generated:",self.token)   
        print("License image generated from "+file_src+" :", self.get_license_img())
        
    def get_free_token(self):
        res = self.session.get('https://app.platerecognizer.com/alpr-demo')
        soup = BeautifulSoup(res.text, 'html.parser')
        token = soup.find('input', {'name': 'csrfmiddlewaretoken'})["value"]
        return str(token) if token else None

    def get_license_img(self, file_src = None):
        if file_src == None:
            file_src = self.file_src
        files = {'upload': open(self.file_src,'rb')}
        data = {'csrfmiddlewaretoken': self.token}
        response  = self.session.post(
            "https://app.platerecognizer.com/alpr-demo", 
            params = data,
            files=files)
        soup = BeautifulSoup(response.text, 'html.parser')
        licenses = soup.find_all('ul', {'class': 'plate-items'})
        all_found_licenses = []
        for license in licenses:
            print(license.span.findAll("li")[1].text.strip())
            all_found_licenses.append(license.span.findAll("li")[1].text.strip())
        return all_found_licenses
        
class GetLicensePlate:
    def __init__(self, token: str):
        self.token = token 

    def get_license(self, file_src: str):
        try:  
            with open(file_src, 'rb') as fp:
                response = requests.post(
                    'https://api.platerecognizer.com/v1/plate-reader/',
                    files=dict(upload=fp),
                    headers={'Authorization': f'Token {self.token}'})
                
            return response.json()
        except FileNotFoundError:
            raise FileNotFoundError("File not found")
        except Exception as e:
            raise e("Something went wrong")

                
if __name__ == "__main__":
    #get_license("ALPR/test.jpg", "")
    # GetFreeLicense('test.jpg')
    pass