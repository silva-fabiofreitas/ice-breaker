import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrap_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """ Searches for Linkedin or Twitter Profile Page."""
    
    if mock:
        linkdin_profile = 'https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json'
        response = requests.get(
            linkdin_profile,
            timeout=10,
        )
    
    return response.json()
        

if __name__=="__main__":
    print(
        scrap_linkedin_profile(
            linkedin_profile_url='https://www.linkdin.com/in/fabio-freitas/',
            mock=True
        )
    )
    