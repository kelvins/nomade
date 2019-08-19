import re
import uuid


def unique_id():
    """Generate a unique ID for the migration using uuid4.

    Returns:
        String containing a unique ID.
    """
    return str(uuid.uuid4())[:8]


def slugify(content):
    """Create a slug version of a string content.

    Args:
        content (str): string content to be slugified.

    Returns:
        A slug version of the content.
    """
    content = re.sub(r'[^a-zA-Z0-9_\s]+', '', content)
    content = content.strip().lower()
    content = content.replace('_', ' ')
    return re.sub(r'\s+', '_', content)
