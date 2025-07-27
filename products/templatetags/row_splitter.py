from django import template


register = template.Library()

@register.filter(name='row_splitter')
def row_splitter(lst, chunk_size):
    """
    Splits a list into chunks of a specified size.
    """
    chunk = []
    for item in lst:
        chunk.append(item)
        if len(chunk) == int(chunk_size):
            yield chunk
            chunk = []
    if chunk:
        yield chunk