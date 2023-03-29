# import re
class CidrMaskConvert:
    def cidr_to_mask(self, val):
        val = int(val)
        mask = ""
        lastbit = 1
        if (isinstance(val, int) and val > 0 and val < 33):
            complete_octets = val // 8
            bits = val % 8
        else:
            return "Invalid"
        for i in range(complete_octets):
            if i < 3:
                mask += "255."
            else:
                mask += "255"
                lastbit = 0
        totalbits = "0b" + "1" * bits + ("0" * (8 - bits))
        totalbits = (int(totalbits, 2))
        zeroes = ".0" * (4 - (complete_octets + 1))
        val = (mask + (str(totalbits) * lastbit) + zeroes)
        return val

    def mask_to_cidr(self, val):
        cidr = 0
        octet_list = val.split(".")
        previous_octet = -1
        for i in octet_list:
            try:
                int(i)
            except ValueError as e:
                print(f"Error: {e}")
                return "Invalid"
            if (isinstance(int(i), int) and int(i) < 256 and len(octet_list) == 4 and (int(i) == 0 or int(i) > 127)):
                if (previous_octet == -1 or int(i) <= previous_octet):
                    if (int(i) != 0 and ((previous_octet == -1 or previous_octet == 255))):
                        previous_octet = int(i)
                        binary_value = bin(int(i))
                        binary_value_str = str(binary_value[2:])
                        zero_counter = 0
                        for i in range(8):
                            if (zero_counter == 0):
                                if (binary_value_str[i:i + 1] == "1"):
                                    cidr += int(binary_value_str[i:i + 1])
                                else:
                                    zero_counter += 1
                            elif (binary_value_str[i:i + 1] == "1"):
                                return "Invalid"  # cannot have a 1 after a 0 in a valid subnet
                    elif (int(i) != 0):
                        previous_octet = int(i)
                        return "Invalid"
                    elif (previous_octet == -1):
                        return "Invalid"
                    else:
                        previous_octet = int(i)
                else:  # this means it would not be a valid subnet mask
                    return "Invalid"
            else:
                return "Invalid"
        return str(cidr)


class IpValidate:
    def ipv4_validation(self, val):
        return True
