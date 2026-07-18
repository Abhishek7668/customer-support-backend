import google.generativeai as genai

from core.config import Settings


class GeminiClient:

    _model = None

    @classmethod
    def get_model(cls):

        if cls._model is None:

            print("Loading Gemini Model...")

            genai.configure(

                api_key=Settings.GEMINI_API_KEY

            )

            cls._model = genai.GenerativeModel(

                model_name="gemini-3.5-flash",

                generation_config={

                    "temperature": 0.2,

                    "top_p": 0.9,

                    "top_k": 40,

                    "max_output_tokens": 2048

                }

            )

        return cls._model