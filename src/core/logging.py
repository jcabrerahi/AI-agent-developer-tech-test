import logging
import sys
from typing import Optional


def setup_logger(
    name: str = "ai_agent",
    level: int = logging.INFO,
    log_format: Optional[str] = None,
) -> logging.Logger:
    """
    Configure and return a logger with the specified name and level.
    
    Args:
        name: The name of the logger
        level: The logging level (default: INFO)
        log_format: Custom log format string (optional)
        
    Returns:
        A configured logger instance
    """
    if log_format is None:
        log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    logger = logging.getLogger(name)
    
    # Avoid adding handlers if they already exist
    if not logger.handlers:
        logger.setLevel(level)
        
        # Create console handler
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(level)
        
        # Create formatter
        formatter = logging.Formatter(log_format)
        handler.setFormatter(formatter)
        
        # Add handler to logger
        logger.addHandler(handler)
    
    return logger


# Create a default logger instance that can be imported directly
logger = setup_logger()