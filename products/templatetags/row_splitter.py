from django import template


register = template.Library()

@register.filter(name='row_splitter')
def row_splitter(list ,chunk_size):
    """
    Splits a list into chunks of a specified size.
    
    :param list: The list to be split.
    :param chunk_size: The size of each chunk.
    :return: A list of lists, where each sublist is a chunk of the original list.
    """
    chunks = []
    i=0
    for data in list:
        list.append(data)
        i= i + 1
        if i==chunk_size:
            yield chunks
            chunks=[]
            yield chunks