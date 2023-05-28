FROM python:3.11

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app
RUN wget -P /code/app/checkpoints https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth 
# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

