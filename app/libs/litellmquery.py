from litellm import completion

class litellmContruct:
    def __init__(self, model="ollama/llama2", api_base="http://localhost:11434", message="Why is the sky Blue?"):
        self.model = model
        self.api_base = api_base
        self.message = message

    def model_completion(self):
        
        response = completion(
            model="ollama/llama2",
            messages = [{ "content": self.message,"role": "user"}],
            api_base=self.api_base
        )

        return response

response = litellmContruct()
print(response.model_completion())
