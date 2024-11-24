from curl_cffi import requests as c_requests
import os

def new_session():
	session = c_requests.Session(impersonate="chrome", proxy=os.getenv("stickyproxy"))
	return session