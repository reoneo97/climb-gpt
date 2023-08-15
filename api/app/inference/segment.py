from PIL import Image
import numpy as np
from segment_anything import SamPredictor, sam_model_registry, SamAutomaticMaskGenerator
import matplotlib.pyplot as plt
import torch
import cv2
from ..config import AppConfig
from pathlib import Path
from loguru import logger

def load_sam_model():
    ## TODO: Using MPS Shaders should be a configuration 
    mps_device = torch.device("mps")

    model_type = AppConfig.segment.type
    ckpt_path = AppConfig.segment.checkpoint
    
    sam = sam_model_registry[model_type](
        checkpoint=ckpt_path)
    sam.to(mps_device)
    model = SamPredictor(sam)
    logger.info('Model Loaded')
    return model

async def get_and_save_image_embedding(image_file, post_id:str):
    image_file = image_file.read()
    image = np.frombuffer(image_file, np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)  
    save_path = AppConfig.segment.save_path

    model = load_sam_model()
    model.set_image(image)
    logger.info('Getting Embedding')
    image_embedding = model.get_image_embedding().cpu().numpy()
    logger.info('Saving Embedding')
    np.save(Path(save_path, post_id), image_embedding)
    logger.debug(f"{Path(save_path, post_id).absolute()}.png")
    cv2.imwrite(f"{Path(save_path, post_id).absolute()}.png", image)


load_sam_model()