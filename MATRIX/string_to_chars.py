def toHex(dec):
    digits = "0123456789ABCDEF"
    x = (dec % 16)
    rest = dec // 16
    if (rest == 0):
        return digits[x]
    print(toHex(rest) + digits[x])

def hex_string_to_chars(hex_string):
    hex_values = hex_string.split()
    
    result = []
    for hex_val in hex_values:
        value = int(hex_val, 16)
        # print(value)
        
        if value in [0x00, 0x01, 0x10, 0x11, 0x12, 0x13, 0x14, 0x20, 0x21, 0x30, 0x31, 0x80, 0x81, 0xc0, 0xc1]:
            mapping = {
                0x00 : "\033[2m", # dim: does nothing and return 1
                0x01 : "\033[32m", # Green: determines whether you have successfully finished the challenge
                0x10 : "\033[33m", # orange: Copy value at s1[1] and push it to s1
                0x11 : "\033[34m", # Blue: pop s1
                0x12 : "\033[35m", # Purple: Add s1[1] to s1[2], then pop s1
                0x13 : "\033[4;31m", # underlined Red: Subtract s1[1] to s1[2], then pop s1
                0x14 : "\033[4;32m", # underlined Green: Swap s1[1] and s1[2]
                0x20 : "\033[4;33m", # underlined orange: pop s1 and push it to the s2
                0x21 : "\033[4;34m", # underlined Blue : pop s2 and push it to the s1
                0x30 : "\033[5;31m", # Blinking Red: put s1[1] to offset
                0x31 : "\033[5;32m", # Blinking Green: If s1[1]==0, then set offset to s1[2]. and pop stack1 twice 
                # 0x32 : "\033[5;33m", # Blinking orange
                # 0x33 : "\033[5;34m", # Blinking Blue
                # 0x34 : "\033[5;35m", # Blinking Purple
                0x80 : "\033[41m", # Background Red: push DAT[offset+1] to stack1. and add 2 to offset
                0x81 : "\033[42m", # Background Green: push DAT[offset+1], DAT[offset+2] to stack1. and add 3 to offset
                0xc0 : "\033[43m", # Background orange: take a char input from user and push it to s1
                0xc1 : "\033[44m"  # Background blue: pop s1 and output it
            }
            result.append(mapping[value] + '^' + "\033[0m")
        elif 32 <= value <= 126:
            result.append(chr(value))
        else:
            if value == 251:
                result.append("@")
            else:
                result.append(".")  # Placeholder
    result = result[::-1]
    return "".join(result)
# A0
# AA
# B4
# CC
# DA
# EF
# FB
# 7F
# 85
# CE
# Input string
input_string = "81 75 00 80 00 80 0a 80 3f 80 65 80 76 80 69 80 6c 80 61 80 20 80 74 80 75 80 6f 80 20 80 74 80 69 80 20 80 65 80 6b 80 61 80 6d 80 20 80 75 80 6f 80 79 80 20 80 6e 80 61 80 43 80 0a 80 58 80 20 80 49 80 20 80 52 80 20 80 54 80 20 80 41 80 20 80 4d 80 20 80 65 80 68 80 74 80 20 80 6f 80 74 80 20 80 65 80 6d 80 6f 80 63 80 6c 80 65 80 57 81 3b 01 30 80 01 80 01 80 00 c0 10 80 75 13 81 a0 00 31 10 80 64 13 81 aa 00 31 10 80 6c 13 81 b4 00 31 10 80 72 13 81 c0 00 31 81 fb 00 30 11 20 80 01 13 21 81 cc 00 30 11 20 80 01 12 21 81 cc 00 30 11 20 20 80 01 13 21 21 81 cc 00 30 11 20 20 80 01 12 21 21 81 cc 00 30 20 20 81 da 00 21 10 20 80 10 81 47 01 30 14 10 20 12 21 14 21 14 21 14 20 81 ef 00 21 80 02 81 61 01 30 81 7b 00 14 81 74 01 12 30 80 00 01 81 38 01 80 00 80 0a 80 2e 80 65 80 75 80 72 80 67 80 20 80 61 80 20 80 79 80 62 80 20 80 6e 80 65 80 74 80 61 80 65 80 20 80 65 80 72 80 65 80 77 80 20 80 75 80 6f 80 59 81 3b 01 30 80 01 01 10 81 45 01 31 c1 81 3b 01 30 11 30 80 00 20 20 10 81 5b 01 31 80 01 13 21 10 21 12 81 49 01 30 11 21 11 21 14 30 10 81 71 01 31 80 01 13 20 10 12 21 81 61 01 30 11 14 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 30 00 00 00 30 00 00 00 30 00 00 00 30 00 00 00 30 00 00 00 81 7f 05 30 81 fb 00 30 30 00 00 00 81 fb 00 30 81 7f 05 30 30 00 00 00 30 00 00 00 81 fb 00 30 30 00 00 00 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 74 05 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 30 00 00 00 81 fb 00 30 81 fb 00 30 81 fb 00 30 30 00 00 00 81 fb 00 30 30 00 00 00 81 fb 00 30 81 fb 00 30 30 00 00 00 30 00 00 00 30 00 00 00 30 00 00 00 30 00 00 00 30 00 00 00 30 00 00 00 30 00 00 00 30 00 00 00 30 00 00 00 81 fb 00 30 30 00 00 00 81 fb 00 30 30 00 00 00 81 fb 00 30 81 fb 00 30 81 fb 00 30 30 00 00 00 81 fb 00 30 30 00 00 00 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 30 00 00 00 81 fb 00 30 30 00 00 00 81 74 05 30 30 00 00 00 81 fb 00 30 81 fb 00 30 30 00 00 00 30 00 00 00 81 fb 00 30 30 00 00 00 81 fb 00 30 81 7f 05 30 30 00 00 00 30 00 00 00 81 fb 00 30 30 00 00 00 81 fb 00 30 30 00 00 00 81 fb 00 30 30 00 00 00 81 fb 00 30 81 fb 00 30 30 00 00 00 81 fb 00 30 81 fb 00 30 30 00 00 00 81 fb 00 30 81 fb 00 30 81 fb 00 30 30 00 00 00 81 fb 00 30 30 00 00 00 81 fb 00 30 30 00 00 00 81 fb 00 30 30 00 00 00 81 fb 00 30 81 fb 00 30 30 00 00 00 81 fb 00 30 30 00 00 00 30 00 00 00 30 00 00 00 30 00 00 00 30 00 00 00 30 00 00 00 81 fb 00 30 30 00 00 00 81 fb 00 30 30 00 00 00 81 fb 00 30 30 00 00 00 81 fb 00 30 81 fb 00 30 30 00 00 00 81 fb 00 30 30 00 00 00 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 30 00 00 00 81 fb 00 30 30 00 00 00 81 fb 00 30 30 00 00 00 81 fb 00 30 81 fb 00 30 30 00 00 00 81 fb 00 30 30 00 00 00 30 00 00 00 30 00 00 00 30 00 00 00 30 00 00 00 30 00 00 00 30 00 00 00 30 00 00 00 81 fb 00 30 30 00 00 00 81 fb 00 30 30 00 00 00 81 fb 00 30 81 fb 00 30 30 00 00 00 81 fb 00 30 81 fb 00 30 81 fb 00 30 30 00 00 00 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 30 00 00 00 81 fb 00 30 30 00 00 00 81 fb 00 30 81 fb 00 30 30 00 00 00 30 00 00 00 30 00 00 00 81 fb 00 30 30 00 00 00 30 00 00 00 81 74 05 30 30 00 00 00 30 00 00 00 81 fb 00 30 30 00 00 00 30 00 00 00 81 fb 00 30 30 00 00 00 81 fb 00 30 81 fb 00 30 30 00 00 00 81 fb 00 30 81 fb 00 30 81 fb 00 30 30 00 00 00 30 00 00 00 81 fb 00 30 30 00 00 00 30 00 00 00 81 fb 00 30 30 00 00 00 81 fb 00 30 30 00 00 00 30 00 00 00 81 fb 00 30 81 fb 00 30 30 00 00 00 81 fb 00 30 30 00 00 00 30 00 00 00 30 00 00 00 81 fb 00 30 81 fb 00 30 81 fb 00 30 30 00 00 00 81 fb 00 30 30 00 00 00 81 fb 00 30 81 74 05 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 30 00 00 00 81 fb 00 30 30 00 00 00 30 00 00 00 30 00 00 00 30 00 00 00 81 fb 00 30 30 00 00 00 30 00 00 00 81 74 05 30 30 00 00 00 81 fb 00 30 30 00 00 00 30 00 00 00 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 fb 00 30 81 85 05 30 81 fb 00 30 20 10 81 fb 00 31 80 01 13 21 30 20 80 01 12 21 30 11 11 11 11 81 ce 05 80 00 80 0a 80 21 80 74 80 69 80 20 80 65 80 64 80 61 80 6d 80 20 80 75 80 6f 80 79 80 20 80 2c 80 73 80 6e 80 6f 80 69 80 74 80 61 80 6c 80 75 80 74 80 61 80 72 80 67 80 6e 80 6f 80 43 81 3b 01 30 81 f8 00 30"

# Convert and print the result
converted_string = hex_string_to_chars(input_string)
print(converted_string)
