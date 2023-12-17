# Ollama API: A backend service to stream Ollama model responses
Ollama is a fantastic software that allows you to get up and running open-source LLM models quickly. Credits to the team and contributors at Ollama for building such a great software.  The goal of this repository is spin up a version of Ollama running on your HPC / Cloud Service Provider of choice and still interact with the API.

## Current Product
We only support python based responses using a simple Flask Route API running on a Linux platform.

## Roadmap
- **Apache Support**:  We plan to support a production service API using WSGI 
- **Restful Support** Creating a quick RESTful deployment to query your favorite models with ease
- **Docker** Ensure deployment is seamless and simple using docker

## How to Run
#### Hardware Specs
Ensure that you have a machine with the following Hardware Specifications:
1. Ubuntu Linux or Macintosh (Windows is not supported)
2. 32 GB of RAM
3. 6 CPUs/vCPUs
4. 50 GB of Storage
5. NVIDIA GPU

#### Prerequisites
1. In order to run Ollama including Stable Diffusion models you must create a read-only HuggingFace API key.  [Creation of API Key](https://huggingface.co/docs/hub/security-tokens)
2. Upon completion of generating an API Key you need to edit the config.json located in the `./app/config.json`
![config](./assets/config_demo.gif)
3. Install neccessary dependencies and requirements: 

```sh
# Update your machine (Linux Only)
sudo apt-get update
# Install pip
sudo apt-get install python3-pip 
# Navigate to the directory containing requirements.txt
./app
# Run the pip install command
pip install -r requirements.txt
```
## Credits ✨
This project would not be possible without continous contributions from the Open Source Community.
### Ollama
[Ollama Github](https://github.com/jmorganca/ollama)

[Ollama Website](https://ollama.ai/)

### @cantrell
[Cantrell Github](https://github.com/cantrell)

[Stable Diffusion API Server](https://github.com/cantrell/stable-diffusion-api-server)

### Valdi
Our preferred HPC partner  🖥️

[Valdi](https://valdi.ai/)

[Support us](https://valdi.ai/signup?ref=YZl7RDQZ)

### Replit
Our preferred IDE and deployment platform  🚀

[Replit](https://replit.com/)

--
Created by [Dublit](https://dublit.org/) - Delivering Ollama to the masses
