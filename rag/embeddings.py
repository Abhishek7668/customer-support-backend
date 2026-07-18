from langchain_huggingface import HuggingFaceEmbeddings


class EmbeddingModel:

    _embeddings = None

    @classmethod
    def get_embeddings(cls):

        if cls._embeddings is None:

            print("Loading Embedding Model...")

            cls._embeddings = HuggingFaceEmbeddings(

                model_name=r"D:\HF_CACHE\hub\models--sentence-transformers--all-MiniLM-L6-v2\snapshots\1110a243fdf4706b3f48f1d95db1a4f5529b4d41",

                model_kwargs={

                    "device": "cpu",

                    "local_files_only": True

                },

                encode_kwargs={

                    "normalize_embeddings": True

                }

            )

        return cls._embeddings