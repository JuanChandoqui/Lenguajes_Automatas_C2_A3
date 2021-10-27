import http.client
import json

def verificationCURP(curp):
    conn = http.client.HTTPSConnection("curp-renapo.p.rapidapi.com")

    payload = "{\r\"curp\": \""+curp +"\"\r}"

    headers = {
        'content-type': "application/json",
        'x-rapidapi-host': "curp-renapo.p.rapidapi.com",
        'x-rapidapi-key': "761522b92amsh4a4cddc0ed6980fp1e53f0jsnd6db755e86db"
        }

    conn.request("POST", "/v1/curp", payload, headers)

    res = conn.getresponse()
    data = res.read()

    curp = data.decode("utf-8")
    curp_json = json.loads(curp)

    return curp_json