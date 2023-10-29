# Teachable AI
# Version: AXYS
# Module: Database Operations
# Filepath: `/db/database.py`
# Updated: 10-28-2023

import os
import sqlite3
import pickle
from sentence_transformers import SentenceTransformer, util
from ..main import logger


class MemoStore:
    """
    Provides memory storage and retrieval for a TeachableAgent, using an SQLite vector database.
    """

    def __init__(self, verbosity=0, reset=False, db_filename="app.db",
                 model_name='distilbert-base-nli-stsb-mean-tokens'):
        """
        Initialize the MemoStore with optional verbosity and database filename.

        Args:
            verbosity (int, optional): Verbosity level. Defaults to 0.
            reset (bool, optional): Whether to reset the DB. Defaults to False.
            db_filename (str, optional): Filename of the database. Defaults to "app.db".
            model_name (str, optional): Model name for generating embeddings. Defaults to 'distilbert-base-nli-stsb-mean-tokens'.
        """
        self.verbosity = verbosity
        self.model = SentenceTransformer(model_name)

        # Update to consider the db file is in the same directory as this file
        self.path_to_db_file = os.path.join(
            os.path.dirname(__file__), db_filename)

        logger.debug(
            f"Attempting to connect to database at: {self.path_to_db_file}")

        try:
            self.conn = sqlite3.connect(self.path_to_db_file)
        except sqlite3.OperationalError as oe:
            logger.error(
                f"Unable to open database file: {self.path_to_db_file}")
            raise RuntimeError(
                f"Unable to open database file: {self.path_to_db_file}") from oe

        if reset:
            self.reset_db()

        self._initialize_db()
        logger.debug("Database initialized successfully.")

    def _initialize_db(self):
        try:
            with self.conn:
                self.conn.execute("""
                    CREATE TABLE IF NOT EXISTS memos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        input_text TEXT NOT NULL,
                        output_text TEXT NOT NULL,
                        input_embedding BLOB NOT NULL,
                        output_embedding BLOB NOT NULL
                    );
                """)
        except Exception as e:
            logger.error(f"Failed to initialize database: {e}")
            raise

    def reset_db(self):
        try:
            with self.conn:
                self.conn.execute("DROP TABLE IF EXISTS memos")
            self._initialize_db()
        except Exception as e:
            logger.error(f"Failed to reset database: {e}")
            raise

    def close(self):
        """
        Cleanly closes the database connection.
        """
        try:
            self.conn.close()
        except Exception as e:
            logger.error(f"Failed to close database connection: {e}")
            raise

    # add_input_output_pair method
    def add_input_output_pair(self, input_text, output_text):
        """
        Adds an input-output pair to the vector database.

        Args:
            input_text (str): The input text.
            output_text (str): The output text.
        """
        try:
            # Generate embeddings
            input_embedding = self.model.encode(
                input_text, convert_to_tensor=True)
            output_embedding = self.model.encode(
                output_text, convert_to_tensor=True)
        except Exception as e:
            # Corrected error message
            logger.error(f"Failed to generate embeddings: {e}")
            raise

        # Serialize the tensor for storage
        input_embedding_serialized = pickle.dumps(input_embedding)
        output_embedding_serialized = pickle.dumps(output_embedding)
        try:
            with self.conn:
                self.conn.execute(
                    "INSERT INTO memos (input_text, output_text, input_embedding, output_embedding) VALUES (?, ?, ?, ?)",
                    (input_text, output_text, input_embedding_serialized,
                     output_embedding_serialized)
                )
        except Exception as e:
            logger.error(f"Failed to insert into memos: {e}")
            raise

    def get_nearest_memo(self, query_text):
        """
        Retrieves the nearest memo to the given query text.

        Args:
            query_text (str): The query text.

        Returns:
            dict: The nearest memo as a dictionary with keys 'input_text' and 'output_text'.
        """
        try:
            query_embedding = self.model.encode(
                query_text, convert_to_tensor=True)

            nearest_memo = None
            min_distance = float("inf")

            for row in self.conn.execute("SELECT * FROM memos"):
                db_input_embedding = pickle.loads(row[3])
                distance = util.pytorch_cos_sim(
                    query_embedding, db_input_embedding).item()

                if distance < min_distance:
                    min_distance = distance
                    nearest_memo = {
                        'input_text': row[1],
                        'output_text': row[2]
                    }
        except Exception as e:
            logger.error(f"Failed to retrieve nearest memo: {e}")
            raise

        return nearest_memo

    def get_related_memos(self, query_text, n_results=10, threshold=1.5):
        """
        Retrieves memos that are related to the given query text within the specified distance threshold.

        Args:
            query_text (str): The query text.
            n_results (int, optional): The number of results to retrieve. Defaults to 10.
            threshold (float, optional): The distance threshold. Defaults to 1.5.

        Returns:
            list: A list of related memos as dictionaries with keys 'input_text' and 'output_text'.
        """

        try:
            query_embedding = self.model.encode(
                query_text, convert_to_tensor=True)

            related_memos = []

            for row in self.conn.execute("SELECT * FROM memos"):
                db_input_embedding = pickle.loads(row[3])
                distance = util.pytorch_cos_sim(
                    query_embedding, db_input_embedding).item()

                if distance < threshold:
                    related_memos.append({
                        'input_text': row[1],
                        'output_text': row[2],
                        'distance': distance
                    })

            # Sort by distance and take the top n_results
            related_memos = sorted(related_memos, key=lambda x: x['distance'])[
                :n_results]

            return related_memos
        except Exception as e:
            logger.error(f"Failed to retrieve related memos: {e}")
            raise

    def prepopulate(self):
        """
        Adds a few arbitrary examples to the vector database, just to make retrieval less trivial.
        """
        examples = [
            ("What's the weather like?",
             "I can't browse the internet to check the weather for you."),
            ("Tell me a joke.",
             "Why did the chicken cross the road? To get to the other side."),
            ("How are you?", "I'm just a computer program, so I don't have feelings, but thanks for asking!")
        ]

        for input_text, output_text in examples:
            self.add_input_output_pair(input_text, output_text)

    def list_memos(self):
        """
        Prints the contents of MemoStore.
        """
        try:
            for row in self.conn.execute("SELECT * FROM memos"):
                print(
                    f"ID: {row[0]}, Input Text: {row[1]}, Output Text: {row[2]}")
        except Exception as e:
            logger.error(f"Failed to print memos: {e}")
            raise
