from typing import Tuple
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain_openai import ChatOpenAI
from third_parties.linkedin import scrap_linkedin_profile 
from agents.linkdin_lookup_agents import linkedin_lookup_agent

from output_parse import Summary, summary_parser

def ice_break_with(name:str) -> Tuple[Summary ,str]:
    linkedin_username = linkedin_lookup_agent(name)
    linkedin_data = scrap_linkedin_profile(linkedin_username, mock=True)
    
    summary_template = """
    Give linkdin information {information} about a person i want you to create:
    1. A short summary 
    2. two interesting facts about them  
    
    \n {format_instructions} 
    """
    
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        partial_variables={'format_instructions':summary_parser.get_format_instructions()},
        template=summary_template
    )
        
    llm = ChatOpenAI(model='gpt-4o-mini', temperature=0)
       
    chain = summary_prompt_template | llm | summary_parser
    
    res = chain.invoke({'information':linkedin_data})
    
    return res, linkedin_data.get("profile_pic_url")

if __name__=="__main__":
    print('Ice break enter')
    ice_break_with(name='Fabio Freitas')
    
    
    
    