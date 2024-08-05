import os
import json
import keyboard
import time
import google.generativeai as genai

path = __file__
parent_directory_name = os.path.basename(os.path.dirname(path))

config_file = r"files\api.lb01"
save_file = r"files\save.sv"

if parent_directory_name == "files":
    config_file = "api.lb01"
    save_file = "save.sv"

def Run(message):
    response = chat_session.send_message(message)
    print("Gemini : ",response.text)

def load_cfg():
    global config
    try:
        with open(config_file, "r") as cfg:
            config = json.load(cfg)
    except FileNotFoundError:
        config = {
            "api_key": input("Enter your google gemini api key : ")
        }
        save_cfg(config)
    return config

def load_save():
    global save_data
    global save_file
    try:
        save_data = json.load(open(save_file))
    except FileNotFoundError:
        print("All save data can be changed later by deleting the save.sv in the files folder in current directory or by changing it directly [JSON Format]")
        save_data = {
            "model": input("Enter the name of the model you want to use [ Recommended 'gemini-1.5-pro', Available 'gemini-1.0-pro', 'gemini-1.5-pro', 'gemini-1.5-flash ]: "),
            "temperature": input("Enter the temperature of the model [Recommended : 1] : ") ,  
            "top_p": input("Enter the 'TOP P' of the model [Recommended : 0.95] : "),
            "top_k": input("Enter the 'TOP K' of the model [Recommended : 64] : "),
            "max_output_tokens": input("Enter the 'MAX OUTPUT TOKENS' of the model [Recommended : 8192] : "),
            "response_mime_type": input("Enter the 'RESPONSE TYPE' of the model [Recommended : text/plain] : "),
            "model_ins": input("Enter system prompt ['You are a very helpful AI assistant'] : ")
        }
        save(save_data)
    return save_data
    
def save(save_data):
    with open(save_file, "w") as cfg:
        json.dump(save_data, cfg, indent=4)

def save_cfg(config):
    with open(config_file, "w") as cfg:
        json.dump(config, cfg, indent=4)
    print("Saved API Key : " + config["api_key"])

def New_API():
    os.remove(config_file)
    time.sleep(0.5)
    load_cfg()

def SHOW_API():
    print(api)
    time.sleep(0.5)

load_save()

load_cfg()

print(config)

#with open(config_file, "r") as cfg:
    #config_check = json.load(cfg)

api = config["api_key"]

null = ""

if api is null:
    print("Invalid API Key")
    os.remove(config_file)
    load_cfg()

print("Press Q to Quit, W to Run, E to set new api key, R to show api key, T to remove api key")

while True:
    if(keyboard.is_pressed("Q")):
        quit()
    if(keyboard.is_pressed("W")):
        time.sleep(0.5)
        break
    if(keyboard.is_pressed("E")):
        New_API()
        print("Press Q to Quit, W to Run, E to set new api key, R to show api key, T to remove api key")
        
    if(keyboard.is_pressed("R")):
        SHOW_API()
        print("Press Q to Quit, W to Run, E to set new api key, R to show api key, T to remove api key")
    if(keyboard.is_pressed("T")):
        os.remove(config_file)
        load_cfg()
        print("Press Q to Quit, W to Run, E to set new api key, R to show api key, T to remove api key")

genai.configure(api_key=api)

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": float(save_data["temperature"]),
  "top_p": float(save_data["top_p"]),
  "top_k": int(save_data["top_k"]),
  "max_output_tokens": int(save_data["max_output_tokens"]),
  "response_mime_type": str(save_data["response_mime_type"]),
}

#model instructions
instruction = save_data["model_ins"]

if save_data["model_ins"] == "":
    instruction = "You are a very helpful AI assistant"

if save_data["model_ins"] == " ":
    instruction = "You are a very helpful AI assistant"


model = genai.GenerativeModel(
  model_name=save_data["model"],
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction=instruction,
  )

chat_session = model.start_chat()
print("press alt + f4 to quit, delete 'the config.lb01' to reset api key")

while True:
    model_input = input("Prompt : ")
    Run(model_input)