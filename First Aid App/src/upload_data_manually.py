import os
from utils.prepare_vectordb import PrepareVectorDB
from utils.load_config import LoadConfig

CONFIG = LoadConfig()

def upload_data_manually() -> None:
    """
    Uploads data manually to the VectorDB.

    This function initializes a PrepareVectorDB instance with configuration parameters
    such as data_directory, persist_directory, embedding_model_engine, chunk_size,
    and chunk_overlap. It then checks if the VectorDB already exists in the specified
    persist_directory. If not, it calls the prepare_and_save_vectordb method to
    create and save the VectorDB. If the VectorDB already exists, a message is printed
    indicating its presence.

    Returns:
        None
    """
    prepare_vectordb_instance = PrepareVectorDB(
        data_directory=CONFIG.data_directory,
        persist_directory=CONFIG.persist_directory,
        embedding_model_engine=CONFIG.embedding_model_engine,
        chunk_size=CONFIG.chunk_size,
        chunk_overlap=CONFIG.chunk_overlap,
    )

    # ✅ Corrected condition to check if directory is empty
    if not os.path.exists(CONFIG.persist_directory) or not os.listdir(CONFIG.persist_directory):
        print("🔄 Creating new ChromaDB Vector Database...")
        prepare_vectordb_instance.prepare_and_save_vectordb()
        print("✅ VectorDB successfully created and saved!")
    else:
        print(f"⚠️ VectorDB already exists in {CONFIG.persist_directory}, skipping creation.")
    
    return None


if __name__ == "__main__":
    upload_data_manually()
