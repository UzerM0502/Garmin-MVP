import os
from dotenv import load_dotenv
from langchain.utilities import SQLDatabase
from langchain.chat_models import init_chat_model
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType

# Load environment variables securely
load_dotenv()

def get_database(db_path: str) -> SQLDatabase:
    """Initialize SQLDatabase connection."""
    return SQLDatabase.from_uri(f"sqlite:///{db_path}")

def get_llm(model_name: str = "gemini-2.0-flash", provider: str = "google_genai"):
    """Initialize chat model for agent."""
    return init_chat_model(model_name, model_provider=provider)

def create_agent(db: SQLDatabase, llm) -> object:
    """Create a SQL agent using LangChain best practices."""
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    agent = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    )
    return agent

def main():
    # Use absolute path for reliability
    db_path = os.getenv("GARMIN_DB_PATH")
    db = get_database(db_path)
    llm = get_llm()
    agent = create_agent(db, llm)

    # Example query
    query = "What is my most popular activity and how many have I done of each?"
    result = agent.invoke(query)
    print(result)

if __name__ == "__main__":
    main()