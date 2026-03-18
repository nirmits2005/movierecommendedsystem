import time
import requests
from datetime import datetime

# Set your URLs here. I have added the Vercel backend URL.
# If your Streamlit frontend is hosted on Render or somewhere else, add its URL below.
URLS_TO_PING = [
    "https://movierecommendedsystem-mf8k.vercel.app",
    # "https://your-streamlit-app-url.onrender.com"
]

PING_INTERVAL_MINUTES = 4

def keep_awake():
    print("=======================================")
    print("🚀 Keep-Awake Script Started!")
    print(f"Pinging every {PING_INTERVAL_MINUTES} minutes so it doesn't sleep.")
    print("Press Ctrl+C to stop this script whenever you want.")
    print("=======================================\n")
    
    while True:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for url in URLS_TO_PING:
            try:
                response = requests.get(url, timeout=10)
                status = response.status_code
                if status == 200:
                    status_text = "✅ 200 OK"
                else:
                    status_text = f"⚠️ {status}"
                print(f"[{now}] Pinged {url} -> {status_text}")
            except Exception as e:
                print(f"[{now}] ❌ Failed to ping {url} -> {e}")
        
        # Sleep for the interval
        time.sleep(PING_INTERVAL_MINUTES * 60)

if __name__ == "__main__":
    try:
        keep_awake()
    except KeyboardInterrupt:
        print("\nKeep-Awake Script stopped by user. 🛑")
