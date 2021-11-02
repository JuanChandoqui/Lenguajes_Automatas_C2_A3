import http.client
import json

def verificationCURP(curp):
    conn = http.client.HTTPSConnection("curp-renapo.p.rapidapi.com")

    payload = "{\r\"curp\": \""+curp +"\"\r}"

    headers = {
        'content-type': "application/json",
        'x-rapidapi-host': "curp-renapo.p.rapidapi.com",
        'x-rapidapi-key': '2bb1ef27a7msha5384ba529377eep139a3djsnf3789d4c40ab' # 4 request limit
    }

    conn.request("POST", "/v1/curp", payload, headers)

    res = conn.getresponse()
    data = res.read()

    curp = data.decode("utf-8")
    curp_json = json.loads(curp)

    return curp_json