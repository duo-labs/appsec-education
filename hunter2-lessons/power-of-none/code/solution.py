def secureCompare(input1, input2):
    if not isinstance(input1, six.string_types):
        return False

    if not isinstance(input2, six.string_types):
        return False

    bytes1 = bytearray(str(input1))
    bytes2 = bytearray(str(input2))

    return len(bytes1) == len(bytes2)
