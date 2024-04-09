import subprocess
import shlex
import json

class MultiModelSupport:
    def __init__(self, question, content):
        self.question = question
        self.content = content

    def list_installed_models(self):
        curl_command = 'curl http://localhost:11434/api/tags'

        output = subprocess.check_output(curl_command, shell=True, encoding='utf-8')
        res = json.loads(output)

        # Extract only the 'name' attribute and remove ':latest'
        model_names = [model.get('name', '').replace(':latest', '') for model in res.get('models', [])]

        return model_names

    def run_model_chat(self):
        model_names = self.list_installed_models()

        all_responses = {}

        for model in model_names:
            quoted_question = shlex.quote(self.question)
            quoted_content = shlex.quote(self.content)

            data_payload = {
                "model": model,
                "messages": [
                    {"role":"system", "content":quoted_content},
                    {"role": "user", "content": quoted_question}
                ],
                "stream": False,
                "options": {"num_ctx": 32678}
            }

            json_data = json.dumps(data_payload)

            process = subprocess.Popen(['curl', 'http://localhost:11434/api/chat', '-d', json_data],
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()

            output_str = output.decode('utf-8')

            if process.returncode != 0:
                print(f"Error running command. Error message: {error.decode('utf-8')}")
                return

            try:
                response_json = json.loads(output_str)
                assistant_response = response_json.get('message', {}).get('content', '')
                all_responses[model] = assistant_response
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON response. Error message: {e}")
                return

        return all_responses

# Example usage:
question = "What's the weather like?"
content = "We are located in Washington State."
multi_support = MultiModelSupport(question, content)
print(multi_support.run_model_chat())
