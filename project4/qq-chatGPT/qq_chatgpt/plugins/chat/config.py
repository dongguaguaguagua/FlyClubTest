from pydantic import BaseSettings

default_config = {
    # 记录上下文
    "context": "",
    # Creates a completion for the provided prompt and parameters
    "completion": {
        # ID of the model to use.
        # You can use the List models API to see all of your available models,
        # or see our Model overview for descriptions of them.
        "model": "text-davinci-003",
        # The prompt(s) to generate completions for, encoded as a string,
        # array of strings, array of tokens, or array of token arrays.
        "prompt": "",
        # What sampling temperature to use.
        # Higher values means the model will take more risks.
        # Try 0.9 for more creative applications,
        # and 0 (argmax sampling) for ones with a well-defined answer.
        # We generally recommend altering this or top_p but not both.
        "temperature": 0.0,
        # max_tokens is a parameter in the ChatGPT API that indicates the \
        # maximum number of tokens (words) that should be generated \
        # in the response. Increasing this number can make the response \
        # longer and more detailed, but it can also make the model slower.
        # The maximum number of tokens to generate in the completion.
        "max_tokens": 3000,
        # # An alternative to sampling with temperature, called nucleus sampling,
        # # where the model considers the results of the tokens with top_p probability mass.
        # # So 0.1 means only the tokens comprising the top 10% probability mass are considered.
        # # We generally recommend altering this or temperature but not both.
        # "top_p": 1,
        # How many completions to generate for each prompt.
        "n": 1,
        # Whether to stream back partial progress.
        # If set, tokens will be sent as data-only server-sent events as they b
        # ecome available, with the stream terminated by a data: [DONE] message
        "stream": False,
        # Echo back the prompt in addition to the completion
        "echo": False,
        # The suffix that comes after a completion of inserted text.
        "suffix": None,
        # Up to 4 sequences where the API will stop generating further tokens.
        # The returned text will not contain the stop sequence.
        "stop": None,
    },
    # Given a prompt and an instruction,
    # the model will return an edited version of the prompt.
    "edit_text": {
        # ID of the model to use.
        # You can use the List models API to see all of your available models,
        # or see our Model overview for descriptions of them.
        "model": "text-davinci-edit-001",
        # The input text to use as a starting point for the edit.
        "input": "",
        # The instruction that tells the model how to edit the prompt.
        "instruction": "",
        # How many edits to generate for the input and instruction.
        "n": 1,
        # Defaults to 1, What sampling temperature to use.
        # Higher values means the model will take more risks.
        # Try 0.9 for more creative applications,
        # and 0 (argmax sampling) for ones with a well-defined answer.
        "temperature": 0.9,
        # An alternative to sampling with temperature, called nucleus sampling,
        # where the model considers the results of the tokens with top_p
        # probability mass. So 0.1 means only the tokens comprising the top 10%
        # probability mass are considered.
        # # "top_p" = 1,
    },
    "generate_image": {
        # A text descr/iption of the desired image(s).
        # The maximum length is 1000 characters.
        "prompt": "",
        # The number of images to generate. Must be between 1 and 10.
        "n": 1,
        # The size of the generated images.
        # Must be one of 256x256, 512x512, or 1024x1024.
        "size": "256x256",
        # The format in which the generated images are returned.
        # Must be one of url or b64_json.
        "response_format": "url",
    },
    "edit_image": {
        # The image to edit. Must be a valid PNG file,
        # less than 4MB, and square. If mask is not provided,
        # image must have transparency, which will be used as the mask.
        "image": "",
        # An additional image whose fully transparent areas
        # (e.g. where alpha is zero) indicate where image should be edited.
        # Must be a valid PNG file, less than 4MB,
        # and have the same dimensions as image.
        "mask": "",
        # A text descr/iption of the desired image(s).
        # The maximum length is 1000 characters.
        "prompt": "",
        # The number of images to generate. Must be between 1 and 10.
        "n": 1,
        # The size of the generated images.
        # Must be one of 256x256, 512x512, or 1024x1024.
        "size": "256x256",
        # The format in which the generated images are returned.
        # Must be one of url or b64_json.
        "response_format": "url",
    }
}


class OpenAIConfig(BaseSettings):
    openai_api_key: str
    openai_organization: str

    class Config:
        extra = "ignore"
