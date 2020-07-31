

# text
def verify_is_text_descriptor(descriptor):
    assert descriptor.startswith("text-fingerprinting.descriptor.text#")


def text_as_descriptor(text):
    return "text-fingerprinting.descriptor.text#%s" % text


def text_from_descriptor(descriptor):
    return descriptor[descriptor.index("#")+1:]


# shingle
def shingle(array):
    return "text-fingerprinting.descriptor.shingle#%s" % " " \
                                                         "".join(a.__str__() for a in array)


# sentence
def sentence(windowed_text):
    return "text-fingerprinting.descriptor.sentence#%s" % windowed_text


def text_from_sentence_descriptor(sentence_descriptor):
    return text_from_descriptor(sentence_descriptor)