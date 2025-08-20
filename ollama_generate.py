import json
import http.client

def generate_code(prompt, model="llama3:latest"):
    conn = http.client.HTTPConnection("localhost", 11434)
    headers = {"Content-Type": "application/json"}
    payload = json.dumps({"model": model, "prompt": prompt})

    conn.request("POST", "/api/generate", body=payload, headers=headers)
    response = conn.getresponse()

    code = ""
    while True:
        chunk = response.readline()
        if not chunk:
            break
        try:
            data = json.loads(chunk.decode("utf-8"))
            if "response" in data:
                part = data["response"]
                print(part, end="", flush=True)  
                code += part
        except Exception as e:
            print("Error decoding:", e, chunk)

    conn.close()
    return code

if __name__ == "__main__":
    prompt = "Write a simple Python program for Tic Tac Toe game with two players."
    code = generate_code(prompt)
    with open("tic_tac_toe.py", "w") as f:
        f.write(code)
    print("Code generated successfully")
