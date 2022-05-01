import webbrowser
import requests 

print("Deployment completed")
webbrowser.open("http://localhost:8080")
sess = requests.get("http://localhost:8080")
print(sess)