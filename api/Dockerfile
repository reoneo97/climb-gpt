FROM python:3.11

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN wget -P /code/app/checkpoints https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth 
RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY . /code
# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

