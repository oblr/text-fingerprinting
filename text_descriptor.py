
# text
def text_as_descriptor(text):
    return "text-fingerprinting.descriptor.text#%s" % text


def text_from_descriptor(descriptor):
    return descriptor[descriptor.index("#")+1:]


# shingle
def shingle(array):
    return "text-fingerprinting.descriptor.shingle#%s" % " " \
                                                         "".join(a.__str__() for a in array)