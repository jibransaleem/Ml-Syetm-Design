# this pattern is same as wbe_single not diff is we are sprating the model file from base project image
# we are storing the model files seprate from docker images
# so if the model updates frequently it does not effects the image updates
# example image[api+preprocessing] =>ecr ,  model[xgboot.pkl] =>aws_s3

from fastapi import FastAPI
app =  FastAPI()

# defining the preprocessing functions  : usually it is a complte pipline imported
# loading normalize words

class base_image:
    def __init__(self):
        pass
    def normalize(self  , value:str):
        return value.lower() 

    # loading prericessing

    def preprocess(self , value:str):
        return value.strip()

    # tokenization
    def tokenize(self , value:str):
        return list(value)

class model_from_s3: #  if something changes in image no isssue here , model can frequently changed updated all u need to change is s3 uri
    def load_model():
        return "model"  # in real actual model object is return

@app.get("/pred/{value}")
def pred(value:str):
    image =  base_image()
    model = model_from_s3
    model_object = model.load_model()
    normalize_ =  image.normalize(value)
    preprocess_ =  image.preprocess(normalize_)
    tokenize_ =  image.tokenize(preprocess_)
    return {
        "value" : tokenize_,
        "prediction" : len(tokenize_)
    }
        
    
    

