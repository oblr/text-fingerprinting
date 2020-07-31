from descriptors import verify_is_text_descriptor, text_from_descriptor, sentence


def sentences(descriptor):
    verify_is_text_descriptor(descriptor)
    text = text_from_descriptor(descriptor)
    return [sentence(sent.strip()) for sent in text.split(".") if sent.strip() != ""]
