from dotenv import load_dotenv

load_dotenv()

from src.application.services.vector_search_service import create_vector_search_service
from src.core.logging import setup_logger

# Configure logger
logger = setup_logger("vector_search_test", level=20)  # INFO level

def test_vector_search():
    """Tests the vector search functionality."""
    logger.info("Starting vector search test...")
    
    # Create search service
    search_service = create_vector_search_service()
    
    # List of test queries
    test_queries = [
        "What is the property tax rate in Travis County?",        
        "Which counties have the lowest property tax rates?"
    ]
    
    # Test each query
    for query in test_queries:
        logger.info(f"Query: {query}")
        
        # Perform search
        results = search_service.search_documents_with_score(query, k=2)
        
        # Display results
        logger.info(f"Number of results: {len(results)}")
        
        assert len(results) > 0, f"Could not find any results for query: {query}"                
        logger.info("=" * 80)
    
    logger.info("Vector search test completed.")
