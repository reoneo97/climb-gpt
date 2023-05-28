# Beta GPT

Beta GPT is an application that uses Machine Learning to do perform grading of climbs.


# TODO
1. Learn about YARN webpack
2. How to do prompting
3. Format of the masks that is returned by the model
4. Running of Model iwth ONNX run time
5. Incorporate model with frontend

# Design Docs

## Phase 1: Segmentation
- Simple problem of segmenting a climb into different components based on the colour of the holds

Things to do:
- Grade Tags
- All handholds and footholds
- Clustering same coloured routes together
- Hold Classification
- Wall Angles





## Features Roadmap


## ML Features
- Grading of climbs
- Beta generation
  - Step by Step format 

## Climb Grader

### Image Segmentation
- Isolate the different routes by colour
- Identify the different types of holds
- Identify the type of terrain

### Beta Generation

- Accumulate the information about the different holds
- Perform generation using GPT model

### Software Engineering
- Able to submit route posts
- What is the schema for the database
  - Cloud Architecture for the database


### Route Identification
- Provide information about the routes
- Perform clustering
  - Cluster routes which are the same together
  - Allow people to submit their own videos

### Video Guide
- Generate video on how to send the route
- Translate the GPT output into a video guide using DALLE/ Diffusion Models

## Production
1. How to use ONNX with Browser runtime


## Technical Understanding
- Preprocessing Pipeline
- Patch Size
- Prompting - How to edit prompting for the model
- 