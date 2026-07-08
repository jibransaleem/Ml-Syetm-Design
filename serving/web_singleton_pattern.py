from fastapi import FastAPI
app =  FastAPI()

# defining the preprocessing functions  : usually it is a complte pipline imported
# imagine this class as a tighlty coupled image if something changes all things changes
class base_image:
    def __init__(self):
        pass
    def normalize(self,value:str):
        return value.lower() 

    # loading prericessing

    def preprocess(self,value:str):
        return value.strip()

    # tokenization
    def tokenize(self,value:str):
        return list(value)

    def load_model(self):
        return "model"  # in real actual model object is return

@app.get("/pred/{value}")
def pred(value:str):
    img =  base_image()
    model_object = img.load_model()
    normalize_ =  img.normalize(value)
    preprocess_ =  img.preprocess(normalize_)
    tokenize_ =  img.tokenize(preprocess_)
    return {
        "value" : tokenize_,
        "prediction" : len(tokenize_)
    }
        
    
    

