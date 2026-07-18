from langchain_text_splitters import RecursiveCharacterTextSplitter


class DocumentChunker:

    @staticmethod
    def split(documents):

        splitter = RecursiveCharacterTextSplitter(

            chunk_size=500,

            chunk_overlap=100,

            separators=[

                "\n\n",

                "\n",

                ".",

                " ",

                ""

            ]

        )

        chunks = splitter.split_documents(documents)

        return chunks