from langchain_huggingface import HuggingFaceEmbeddings


class EmbeddingModel:

    _embeddings = None

    @classmethod
    def get_embeddings(cls):

        if cls._embeddings is None:

            print("Loading Embedding Model...")

            cls._embeddings = HuggingFaceEmbeddings(

                model_name="sentence-transformers/all-MiniLM-L6-v2",

                model_kwargs={
                    "device": "cpu"
                },

                encode_kwargs={
                    "normalize_embeddings": True
                }

            )

        return cls._embeddings