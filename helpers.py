import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get API keys from environment variables
YOU_COM_API_KEY = os.getenv('YOU_API_KEY')
TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')
PERPLEXITY_API_KEY = os.getenv('PPLX_API_KEY')
BRAVE_API_KEY = os.getenv('BRAVESEARCH_API_KEY')

def query_you_com(query):
    headers = {"X-API-Key": YOU_COM_API_KEY}
    params = {"query": query}
    try:
        response = requests.get(
            "https://api.ydc-index.io/rag",  # Verify the correctness of the API endpoint
            params=params,
            headers=headers,
        )
        response.raise_for_status()  # Raises an HTTPError if the response code was unsuccessful
        resp = response.json()
        return resp['answer']
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except Exception as err:
        return f"An error occurred: {err}"


def query_tavily(query):
    payload = {
        "api_key": TAVILY_API_KEY,
        "query": query,
        "search_depth": "basic",
        "include_answer": True,
        "include_images": False,
        "include_raw_content": False,
        "max_results": 1,
        "include_domains": [],
        "exclude_domains": []
    }
    response = requests.post("https://api.tavily.com/search", json=payload)
    if response.status_code == 200:
        resp = response.json()
        return resp['answer']
    else:
        return f"Request failed with status code: {response.status_code}"

def query_perplexity(query):
    url = 'https://api.perplexity.ai/chat/completions'
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {PERPLEXITY_API_KEY}'
    }
    data = {
        "model": "llama-3-sonar-large-32k-online",
        "stream": False,
        "max_tokens": 1024,
        "frequency_penalty": 1,
        "temperature": 0.0,
        "messages": [
            {
                "role": "system", 
                "content": "Be precise and concise in your responses."
            },
            {
                "role": "user",
                "content": query
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content']
    else:
        return f"Request failed with status code: {response.status_code}"

# def query_brave(query):
#     headers = {"X-API-Key": BRAVE_API_KEY}
#     params = {
#         "q": query,
#         "count": 1,
#         "summary": True
#     }
#     response = requests.get("https://api.search.brave.com/res/v1/web/search", params=params, headers=headers)
#     if response.status_code == 200:
#         return response.json().get("summary", "No summary available.")
#     else:
#         return f"Request failed with status code: {response}"
    

# def brave_search_summarization(query):
#     # Endpoint for web search with summary
#     web_search_url = "https://api.search.brave.com/res/v1/web/search"
#     summarizer_url = "https://api.search.brave.com/res/v1/summarizer/search"
    
#     # Headers for the requests
#     headers = {
#         "Accept": "application/json",
#         "Accept-Encoding": "gzip",
#         "X-Subscription-Token": BRAVE_API_KEY
#     }
    
#     # Parameters for the initial web search request
#     web_search_params = {
#         "q": query,
#         "summary": 1
#     }
    
#     # Make the initial request to the web search endpoint
#     web_search_response = requests.get(web_search_url, headers=headers, params=web_search_params)
    
#     # Check if the request was successful
#     if web_search_response.status_code != 200:
#         raise Exception(f"Web search request failed with status code {web_search_response.status_code}")
    
#     web_search_data = web_search_response.json()
    
#     # Extract the summarizer key from the response
#     summarizer_key = web_search_data.get('summarizer', {}).get('key')
#     if not summarizer_key:
#         raise Exception("No summarizer key found in the web search response")
    
#     # Parameters for the summarizer request
#     summarizer_params = {
#         "key": summarizer_key,
#         "entity_info": 1
#     }
    
#     # Make the request to the summarizer endpoint
#     summarizer_response = requests.get(summarizer_url, headers=headers, params=summarizer_params)
    
#     # Check if the request was successful
#     if summarizer_response.status_code != 200:
#         raise Exception(f"Summarizer request failed with status code {summarizer_response.status_code}")
    
#     summarizer_data = summarizer_response.json()
    
#     # Return the summarized content
#     return summarizer_data

def ProcessQuestion(question, model):
    if model == "You.com":
        return query_you_com(question)
    elif model == "Tavily.com":
        return query_tavily(question)
    elif model == "Perplexity.ai":
        return query_perplexity(question)
    elif model == "Brave.com":
        return query_brave(question)
    else:
        return "Model not supported"
