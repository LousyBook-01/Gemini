import subprocess
import json

save_file = "files\save.sv"
save_data = ""

def load():
    global save_data
    global save_file
    try:
        save_data = json.load(open(save_file))
    except FileNotFoundError:
        print("All save data can be changed later by deleting the save.sv in the files folder in current directory or by changing it directly [JSON Format]")
        save_data = {
            "model": "null",
            "temperature": input("Enter the temperature of the model [Recommended : 1] : ") ,  
            "top_p": input("Enter the 'TOP P' of the model [Recommended : 0.95] : "),
            "top_k": input("Enter the 'TOP K' of the model [Recommended : 64] : "),
            "max_output_tokens": input("Enter the 'MAX OUTPUT TOKENS' of the model [Recommended : 8192] : "),
            "response_mime_type": input("Enter the 'RESPONSE TYPE' of the model [Recommended : text/plain] : "),
            "model_ins": input("Enter system prompt ['You are a very helpful AI assistant'] : ")
        }
        save(save_data, save_file)
    return save_data

def resave_model(model_name):
    global save_data
    global save_file
    global model
    try:
        save_data = json.load(open(save_file))
    except FileNotFoundError:
        print("All save data can be changed later by deleting the save.sv in the files folder in current directory or by changing it directly [JSON Format]")
        save_data = {
            "model": model,
            "temperature": save_data["temperature"] ,  
            "top_p": save_data["top_p"],
            "top_k": save_data["top_k"],
            "max_output_tokens": save_data["max_output_tokens"],
            "response_mime_type": save_data["response_mine_type"],
            "model_ins": save_data["model_ins"]
        }
        save(save_data, save_file)

def save(save, path):
    with open(path, "w") as cfg:
        json.dump(save, cfg, indent=4)

load()

while True:
    option = input("Enter model ['Gemini-1.5-Pro' , 'Gemini-1.0-Pro' , 'Gemini-1.5-Flash'] : ")
    option = option.lower()
    model = option
    resave_model(option)
    if option == "gemini-1.5-pro":
        break
    if option == "gemini-1.5-flash":
        break
    if option == "gemini-1.0-pro":
        break

subprocess.run(['python', 'files\chat.py'])