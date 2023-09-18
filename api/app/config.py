import yaml
from pydantic import BaseModel
from pathlib import Path

class ModelConfig(BaseModel):
    checkpoint: str
    type: str
    save_path: str

class Config(BaseModel):
    segment: ModelConfig
    
def read_config():
    """
    Reads config file which has path ../cfg.yaml relative to this python file
    """
    cfg_path = Path(__file__).parent.parent.resolve().joinpath('cfg.yml')
    with open(cfg_path) as f:
        config = yaml.safe_load(f)
    

    return Config(**config)

AppConfig = read_config()
