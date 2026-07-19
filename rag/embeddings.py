print("========== 15. embeddings.py loaded ==========")

from langchain_huggingface import HuggingFaceEmbeddings

print("========== 16. HuggingFace imported ==========")


class EmbeddingModel:

    _embeddings = None

    @classmethod
    def get_embeddings(cls):

        print("========== Loading Embedding Model ==========")

        if cls._embeddings is None:

            cls._embeddings = HuggingFaceEmbeddings(

                model_name="sentence-transformers/all-MiniLM-L6-v2",

                model_kwargs={
                    "device": "cpu"
                },

                encode_kwargs={
                    "normalize_embeddings": True
                }

            )

            print("========== Embedding Model Loaded ==========")

        return cls._embeddings