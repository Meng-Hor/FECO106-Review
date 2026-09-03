window.quizData.push({
    "set": "IPv4_and_Subnetting_Exercises",
    "questions": [
        {
            "type": "multiple_choice",
            "question": "How many total bits are in an IPv4 address?",
            "options": [
                "16",
                "32",
                "64",
                "128"
            ],
            "correctOption": 2,
            "explanation": "An IPv4 address consists of 4 octets, and each octet is 8 bits. 4 * 8 = 32 bits.",
            "timeLimit": 30
        },
        {
            "type": "multiple_choice",
            "question": "Complete the missing values in binary place values: 128 | 64 | __ | 16 | __ | 4 | __ | 1",
            "options": [
                "32, 8, 2",
                "32, 12, 2",
                "48, 8, 2",
                "32, 8, 3"
            ],
            "correctOption": 1,
            "explanation": "The place values in an octet are 128, 64, 32, 16, 8, 4, 2, 1.",
            "timeLimit": 30
        },
        {
            "type": "multiple_choice",
            "question": "Convert the binary value 11000000 to decimal.",
            "options": [
                "128",
                "192",
                "224",
                "255"
            ],
            "correctOption": 2,
            "explanation": "128 + 64 = 192.",
            "timeLimit": 30
        },
        {
            "type": "multiple_choice",
            "question": "Convert the decimal value 192 to 8-bit binary.",
            "options": [
                "10000000",
                "11000000",
                "11100000",
                "11110000"
            ],
            "correctOption": 2,
            "explanation": "192 = 128 + 64, so the first two bits are 1, resulting in 11000000.",
            "timeLimit": 30
        },
        {
            "type": "multiple_choice",
            "question": "Convert the IP address 192.168.1.10 to binary.",
            "options": [
                "11000000.10101000.00000001.00001010",
                "10000000.10101000.00000001.00001010",
                "11000000.11101000.00000001.00001110",
                "11000000.10101000.00000011.00001010"
            ],
            "correctOption": 1,
            "explanation": "192 = 11000000, 168 = 10101000, 1 = 00000001, 10 = 00001010.",
            "timeLimit": 45
        },
        {
            "type": "multiple_choice",
            "question": "Convert 11000000.10101000.00000001.00011001 to decimal.",
            "options": [
                "192.168.1.25",
                "192.168.1.19",
                "192.168.1.20",
                "192.168.1.33"
            ],
            "correctOption": 1,
            "explanation": "11000000 = 192, 10101000 = 168, 00000001 = 1, 00011001 = 16 + 8 + 1 = 25.",
            "timeLimit": 45
        },
        {
            "type": "multiple_choice",
            "question": "Identify whether 172.16.5.10 is a Public or Private address.",
            "options": [
                "Public",
                "Private",
                "Multicast",
                "Loopback"
            ],
            "correctOption": 2,
            "explanation": "172.16.0.0 to 172.31.255.255 is the Class B private IP range.",
            "timeLimit": 30
        },
        {
            "type": "multiple_choice",
            "question": "Match the subnet mask 255.255.255.0 to its CIDR prefix.",
            "options": [
                "/8",
                "/16",
                "/24",
                "/32"
            ],
            "correctOption": 3,
            "explanation": "255.255.255.0 has 24 bits set to 1 (8 + 8 + 8), so its CIDR is /24.",
            "timeLimit": 30
        },
        {
            "type": "multiple_choice",
            "question": "What is the subnet mask for a /26 prefix?",
            "options": [
                "255.255.255.128",
                "255.255.255.192",
                "255.255.255.224",
                "255.255.255.240"
            ],
            "correctOption": 2,
            "explanation": "A /26 mask has 26 ones. 24 are in the first three octets (255.255.255), and the last octet has 2 ones (11000000 = 128 + 64 = 192).",
            "timeLimit": 30
        },
        {
            "type": "multiple_choice",
            "question": "What is the CIDR prefix for 255.255.255.128?",
            "options": [
                "/24",
                "/25",
                "/26",
                "/27"
            ],
            "correctOption": 2,
            "explanation": "255.255.255 accounts for 24 bits. 128 is 10000000, adding 1 more bit. Total: 25.",
            "timeLimit": 30
        },
        {
            "type": "multiple_choice",
            "question": "Calculate the number of host bits for a /27 prefix.",
            "options": [
                "3",
                "4",
                "5",
                "6"
            ],
            "correctOption": 3,
            "explanation": "Host bits = 32 - prefix. 32 - 27 = 5 host bits.",
            "timeLimit": 30
        },
        {
            "type": "multiple_choice",
            "question": "Calculate the total number of addresses for a /26 prefix.",
            "options": [
                "32",
                "64",
                "128",
                "256"
            ],
            "correctOption": 2,
            "explanation": "Host bits = 32 - 26 = 6. Total addresses = 2^6 = 64.",
            "timeLimit": 30
        },
        {
            "type": "multiple_choice",
            "question": "Calculate the number of usable hosts for a /25 prefix.",
            "options": [
                "62",
                "64",
                "126",
                "128"
            ],
            "correctOption": 3,
            "explanation": "Host bits = 32 - 25 = 7. Total addresses = 2^7 = 128. Usable hosts = 128 - 2 = 126.",
            "timeLimit": 30
        },
        {
            "type": "multiple_choice",
            "question": "Given 192.168.1.0/24, find the first and last usable addresses.",
            "options": [
                "192.168.1.0 - 192.168.1.255",
                "192.168.1.1 - 192.168.1.254",
                "192.168.1.1 - 192.168.1.255",
                "192.168.1.0 - 192.168.1.254"
            ],
            "correctOption": 2,
            "explanation": "The network address is .0 and broadcast is .255. The usable range is everything in between: .1 to .254.",
            "timeLimit": 30
        },
        {
            "type": "multiple_choice",
            "question": "For the network 192.168.1.0/24, is 192.168.1.255 a usable address for a PC?",
            "options": [
                "Yes, it is usable.",
                "No, it is the broadcast address.",
                "No, it is the network address.",
                "Yes, it is the gateway."
            ],
            "correctOption": 2,
            "explanation": "In a /24 network, the highest address (.255) is reserved as the broadcast address and cannot be assigned to a host.",
            "timeLimit": 30
        },
        {
            "type": "multiple_choice",
            "question": "Divide 192.168.1.0/24 into two equal /25 subnets. What are the network addresses of the two subnets?",
            "options": [
                "192.168.1.0 and 192.168.1.128",
                "192.168.1.0 and 192.168.1.64",
                "192.168.1.0 and 192.168.1.255",
                "192.168.1.1 and 192.168.1.129"
            ],
            "correctOption": 1,
            "explanation": "A /25 subnet has a block size of 128. So the first subnet starts at 0, and the second starts at 0 + 128 = 128.",
            "timeLimit": 45
        },
        {
            "type": "multiple_choice",
            "question": "Divide 192.168.10.0/24 into four /26 subnets. What is the network address of the third subnet?",
            "options": [
                "192.168.10.64",
                "192.168.10.128",
                "192.168.10.192",
                "192.168.10.255"
            ],
            "correctOption": 2,
            "explanation": "A /26 subnet has a block size of 64. The subnets start at .0, .64, .128, and .192. The third subnet is .128.",
            "timeLimit": 45
        },
        {
            "type": "multiple_choice",
            "question": "Which /26 subnet contains the IP address 192.168.1.150/26?",
            "options": [
                "192.168.1.0",
                "192.168.1.64",
                "192.168.1.128",
                "192.168.1.192"
            ],
            "correctOption": 3,
            "explanation": "The /26 ranges are 0-63, 64-127, 128-191, and 192-255. 150 falls within the 128-191 range, so its network is 192.168.1.128.",
            "timeLimit": 45
        },
        {
            "type": "multiple_choice",
            "question": "Are the addresses 192.168.1.20/26 and 192.168.1.70/26 in the same subnet?",
            "options": [
                "Yes",
                "No",
                "Depends on the gateway",
                "Depends on the MAC address"
            ],
            "correctOption": 2,
            "explanation": "No. The /26 block size is 64. .20 is in the first subnet (0-63), and .70 is in the second subnet (64-127).",
            "timeLimit": 45
        },
        {
            "type": "multiple_choice",
            "question": "For the network 192.168.5.0/24, what is the valid subnet mask and broadcast address?",
            "options": [
                "Mask: 255.255.255.0, Broadcast: 192.168.5.255",
                "Mask: 255.255.255.128, Broadcast: 192.168.5.127",
                "Mask: 255.255.0.0, Broadcast: 192.168.255.255",
                "Mask: 255.255.255.0, Broadcast: 192.168.5.0"
            ],
            "correctOption": 1,
            "explanation": "A /24 means the first 3 octets are network (255.255.255.0). The broadcast address sets all host bits to 1 (192.168.5.255).",
            "timeLimit": 45
        }
    ]
});