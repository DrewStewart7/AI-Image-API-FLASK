from gradio_client import Client
from flask import Flask, request, jsonify
import base64,os,requests,random, urllib.request
from PIL import Image
cwd = os.getcwd()
imgbb = "https://api.imgbb.com/1/upload"
imgkey = "<IMGBB API KEY>"
datas = {
    "key": imgkey,
}

def genImage(prompt,style):
    random.seed()
    client = Client("http://127.0.0.1:7865/", serialize=False)
    if style == None:
        result = client.predict(
        prompt,
        "",
        [],
        "Extreme Speed",
        '1024×1024 <span style=\"color: grey;\"> ∣ 1:1</span>',
        1,
        str(random.randint(1902712440476856465, 9999999999999999999)),
        2,
        4,
        "juggernautXL_version6Rundiffusion.safetensors",
        "None",
        0.5,
        "sd_xl_offset_example-lora_1.0.safetensors",
        0.1,
        "None",
        1,
        "None",
        1,
        "None",
        1,
        "None",
        1,
        False,
        "uov",
        "Disabled",
        None,
        [],
        None,
        "",
        None,
        0.5,
        0.6,
        "ImagePrompt",
        None,
        0.5,
        0.6,
        "ImagePrompt",
        None,
        0.5,
        0.6,
        "ImagePrompt",
        None,
        0.5,
        0.6,
        "ImagePrompt",
        fn_index=32
    )
    else:
        result = client.predict(
            prompt,
            "",
            [style],
            "Extreme Speed",
            '1024×1024 <span style=\"color: grey;\"> ∣ 1:1</span>',
            1,
            str(random.randint(1902712440476856465, 9999999999999999999)),
            2,
            4,
            "juggernautXL_version6Rundiffusion.safetensors",
            "None",
            0.5,
            "sd_xl_offset_example-lora_1.0.safetensors",
            0.1,
            "None",
            1,
            "None",
            1,
            "None",
            1,
            "None",
            1,
            False,
            "uov",
            "Disabled",
            None,
            [],
            None,
            "",
            None,
            0.5,
            0.6,
            "ImagePrompt",
            None,
            0.5,
            0.6,
            "ImagePrompt",
            None,
            0.5,
            0.6,
            "ImagePrompt",
            None,
            0.5,
            0.6,
            "ImagePrompt",
            fn_index=32
        )
    
    home = os.path.expanduser("~")

# This will get you the root directory of the OS
    formatted_name = result[3]["value"][0]["name"]
    cwd = os.getcwd()
    final_string = "http://127.0.0.1:7865/file=" + formatted_name
    print(final_string)
    urllib.request.urlretrieve(final_string, cwd + f"/images/{prompt}.png") 
    
    path = cwd + f"/images/{prompt}.png"
    # Read the image file
    with open(path, "rb") as image_file:
        data = base64.b64encode(image_file.read())
        datas["image"] = data
        datas["name"] = prompt
        imgreq = requests.post(imgbb, data=datas)
        print(imgreq.json()["data"]["url"])
        return imgreq.json()["data"]["url"]



app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()  # Get JSON data sent to the endpoint
    if request.headers["auth"] == "bop123!":
        prompt = data.get('prompt', '')  # Extract the 'prompt' parameter
        style = data.get('style', '')
        print(prompt)
        print(style)
        if style == "no":
            style = None
        prompt = prompt.strip()
        rVal = genImage(prompt,style)
        return jsonify({'url': rVal})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1100, debug=True)
