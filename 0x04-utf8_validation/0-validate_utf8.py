def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Masks to check the most significant bits of a byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Get the 8 least significant bits
        byte = num & 0xFF

        if n_bytes == 0:
            # Count the number of leading 1's in the current byte
            mask = 1 << 7
            while mask & byte:
                n_bytes += 1
                mask >>= 1
            
            # 1 byte character
            if n_bytes == 0:
                continue

            # If the number of bytes is more than 4 or less than 2, return False
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # For n_bytes > 0, check if the byte starts with '10'
            if not (byte & mask1 and not (byte & mask2)):
                return False
        
        # Decrement the number of bytes to check
        n_bytes -= 1

    # If we have processed all bytes correctly, n_bytes should be 0
    return n_bytes == 0
