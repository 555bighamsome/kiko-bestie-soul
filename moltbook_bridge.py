import requests
import sys
import json

MOLTBOOK_API = "https://www.moltbook.com/api/v1"

def post_to_moltbook(token, content, community="m/general"):
    """
    Kiko's agent posts a social update or a 'Learning' thought.
    """
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {"body": content, "communityName": community}
    try:
        response = requests.post(f"{MOLTBOOK_API}/posts", headers=headers, json=payload)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def fetch_top_posts(community="m/general"):
    """
    Learn from what other agents are talking about.
    """
    try:
        response = requests.get(f"{MOLTBOOK_API}/posts?communityName={community}&sort=top")
        return response.json()
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python moltbook_bridge.py [post|learn] [token] [content/community]")
        sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == "post":
        print(json.dumps(post_to_moltbook(sys.argv[2], sys.argv[3])))
    elif cmd == "learn":
        comm = sys.argv[2] if len(sys.argv) > 2 else "m/general"
        print(json.dumps(fetch_top_posts(comm)))
