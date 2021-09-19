import requests
import os
URL = f"http://{os.environ.get('TF_HOST')}:{os.environ.get('TF_PORT')}/v1/models/{os.environ.get('TF_MODEL')}:predict"

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False


def main():
    
    while (text:=input("Enter comma seperated values:").lower()) != "exit":
        print(text)
        values = text.split(",")
        if not all((isfloat(v) for v in values)):
            print("invalid input")
            continue
        values = [float(v) for v in values]
        data = {"instances": values}
        try:
            r = requests.post(url = URL, json = data)
            
            if r.status_code == 200:
                result = r.text
                print(result)
            else:
                print("fail to predict , error code:",r.status_code)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            print("fail to reach service due to ",e)
        

if __name__=="__main__":
    main()
    

