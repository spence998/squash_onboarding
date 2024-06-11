from apps.gcp_llm import textbison_llm_pt, gemini_llm_pt
import numpy as np
import ast

def create_ticket(
        ticket_description,
        ticket_detail,
        tools,
        features,
    ):
    """returns the ticket in the form of a dictionary"""
    quote = f'''
    Hi, I need to write a jira ticket please. I need a summary name, description and acceptance criteria please.
    Can you give me it back in JSON form please with keys: name, desciption, acceptance_criteria, story_points please.
    ticket_description:
    {ticket_description}

    ticket_detail:
    {ticket_detail}

    tools:
    {tools}

    features:
    {features}

    '''
    if np.random.random() < 0.1:
        quote += '\nPlease speak as Donald Trump.'
    
    initial_output = gemini_llm_pt(prompt=quote)

    quote = 'Can you make this like json please with the keys name, desciption, acceptance_criteria, story_points:\n'
    quote += initial_output
    quote += '\nPlease dont write anything else.'
    
    final_output = gemini_llm_pt(prompt=quote)

    # Convert to dict.
    trimmed_output = final_output.split("```json")[1]
    trimmed_output = trimmed_output.split("```")[0]
    dict_output = ast.literal_eval(trimmed_output)

    return dict_output

if __name__ == '__main__':
    task = 'I need to build an end-to-end pipeline for feature ingestion.'
    dict_output = create_ticket(task)
    print(dict_output)
