import json
import os

questions = [
    {
        "type": "multiple_choice",
        "question": "Which of the following correctly lists the 7 OSI layers from Layer 1 to Layer 7?",
        "options": [
            "Application, Presentation, Session, Transport, Network, Data Link, Physical",
            "Physical, Data Link, Network, Transport, Session, Presentation, Application",
            "Physical, Network, Data Link, Transport, Presentation, Session, Application",
            "Data Link, Physical, Network, Transport, Session, Presentation, Application"
        ],
        "correct": 2,
        "explanation": "Layer 1 is the bottom (Physical) and Layer 7 is the top (Application). A common mnemonic from L1 to L7 is 'Please Do Not Throw Sausage Pizza Away'.",
        "timeLimit": 30
    },
    {
        "type": "multiple_choice",
        "question": "Which OSI model layers correspond to the single \"Application\" layer in the classic 4-layer TCP/IP model?",
        "options": [
            "Application only",
            "Application and Presentation",
            "Application, Presentation, and Session",
            "Presentation, Session, and Transport"
        ],
        "correct": 3,
        "explanation": "The TCP/IP model consolidates the top three OSI layers (Session, Presentation, and Application) into a single Application layer.",
        "timeLimit": 30
    },
    {
        "type": "multiple_choice",
        "question": "What are the 4 layers of the classic DoD / TCP/IP model from bottom to top?",
        "options": [
            "Physical, Data Link, Internet, Application",
            "Network Access (Link), Internet, Transport, Application",
            "Physical, Network, Transport, Application",
            "Data Link, Network, Host-to-Host, Process"
        ],
        "correct": 2,
        "explanation": "The 4-layer TCP/IP model consists of: 1. Network Access (Link), 2. Internet, 3. Transport (Host-to-Host), 4. Application (Process).",
        "timeLimit": 30
    },
    {
        "type": "multiple_choice",
        "question": "What is the correct Protocol Data Unit (PDU) name at OSI Layer 3 (Network layer)?",
        "options": [
            "Segment",
            "Frame",
            "Packet",
            "Bit"
        ],
        "correct": 3,
        "explanation": "Layer 1: Bits. Layer 2: Frames. Layer 3: Packets. Layer 4: Segments/Datagrams.",
        "timeLimit": 30
    },
    {
        "type": "multiple_choice",
        "question": "When data travels DOWN the protocol stack during transmission, what is this process called?",
        "options": [
            "Decapsulation",
            "De-multiplexing",
            "Encapsulation",
            "Fragmentation"
        ],
        "correct": 3,
        "explanation": "Encapsulation is the process where each descending layer wraps the payload from the layer above it with its own header.",
        "timeLimit": 30
    },
    {
        "type": "multiple_choice",
        "question": "Which layer adds a trailer (containing the Frame Check Sequence / CRC) in addition to a header?",
        "options": [
            "Physical Layer",
            "Data Link Layer",
            "Network Layer",
            "Transport Layer"
        ],
        "correct": 2,
        "explanation": "The Data Link layer encapsulates a packet into a frame by adding a header and a trailer containing the Frame Check Sequence (FCS) using CRC.",
        "timeLimit": 30
    },
    {
        "type": "multiple_choice",
        "question": "Data compression, character encoding (e.g., ASCII, UTF-8), and encryption/decryption are functions of which OSI layer?",
        "options": [
            "Application (Layer 7)",
            "Presentation (Layer 6)",
            "Session (Layer 5)",
            "Transport (Layer 4)"
        ],
        "correct": 2,
        "explanation": "The Presentation Layer ensures that data from the sender is formatted in a syntax that the receiver's application layer can understand (compression, encryption, formatting).",
        "timeLimit": 30
    },
    {
        "type": "multiple_choice",
        "question": "Establishing, maintaining, synchronizing, and terminating dialogues or checkpoints between two communicating applications is handled by which layer?",
        "options": [
            "Session Layer (Layer 5)",
            "Transport Layer (Layer 4)",
            "Network Layer (Layer 3)",
            "Presentation Layer (Layer 6)"
        ],
        "correct": 1,
        "explanation": "The Session Layer manages dialog control and sets synchronization checkpoints.",
        "timeLimit": 30
    },
    {
        "type": "multiple_choice",
        "question": "Which layer provides end-to-end communication, segmentation, port-based multiplexing, and optional reliable delivery with flow control?",
        "options": [
            "Network Layer",
            "Transport Layer",
            "Data Link Layer",
            "Session Layer"
        ],
        "correct": 2,
        "explanation": "The Transport Layer (Layer 4) handles end-to-end process-to-process communication using port numbers and segments user data.",
        "timeLimit": 30
    },
    {
        "type": "multiple_choice",
        "question": "Which protocol operates at the Network Layer (Layer 3) to send error messages and operational information (such as during a `ping` or `traceroute`)?",
        "options": [
            "ARP",
            "ICMP",
            "IGMP",
            "SNMP"
        ],
        "correct": 2,
        "explanation": "ICMP (Internet Control Message Protocol) operates at Layer 3 to deliver diagnostics, unreachable notifications, and echo request/reply messages.",
        "timeLimit": 30
    },
    {
        "type": "multiple_choice",
        "question": "What is the primary role of the Address Resolution Protocol (ARP)?",
        "options": [
            "Map an IP address to a domain name",
            "Map a known Layer 3 (IP) address to a Layer 2 (MAC) address",
            "Automatically assign IP addresses to hosts",
            "Route packets between different autonomous systems"
        ],
        "correct": 2,
        "explanation": "ARP is used on local subnets to discover the physical hardware address (MAC address) corresponding to a known logical address (IPv4 address).",
        "timeLimit": 30
    },
    {
        "type": "multiple_choice",
        "question": "The Data Link layer is divided into two IEEE 802 sublayers. What are they?",
        "options": [
            "Physical and Logical",
            "Media Access Control (MAC) and Logical Link Control (LLC)",
            "Network Interface and Frame Control",
            "CSMA and CD"
        ],
        "correct": 2,
        "explanation": "The IEEE 802 standard divides Layer 2 into LLC (Logical Link Control - 802.2) and MAC (Media Access Control - 802.3/802.11).",
        "timeLimit": 30
    },
    {
        "type": "multiple_choice",
        "question": "At which OSI layer does a standard Ethernet Switch make forwarding decisions?",
        "options": [
            "Layer 1 (Physical)",
            "Layer 2 (Data Link)",
            "Layer 3 (Network)",
            "Layer 4 (Transport)"
        ],
        "correct": 2,
        "explanation": "Standard switches inspect destination MAC addresses in the Layer 2 Ethernet frame header to look up entries in their MAC address table.",
        "timeLimit": 30
    },
    {
        "type": "multiple_choice",
        "question": "Which device operates strictly at Layer 1 (Physical layer) by simply repeating incoming electrical or optical signals to all other connected ports?",
        "options": [
            "Router",
            "Hub",
            "Switch",
            "Gateway"
        ],
        "correct": 2,
        "explanation": "A Hub is a multiport repeater operating at Layer 1. It simply regenerates and broadcasts incoming electrical signals.",
        "timeLimit": 30
    },
    {
        "type": "multiple_choice",
        "question": "What are the bit lengths of an Ethernet MAC address and an IPv4 address, respectively?",
        "options": [
            "32 bits and 128 bits",
            "48 bits and 32 bits",
            "64 bits and 32 bits",
            "48 bits and 128 bits"
        ],
        "correct": 2,
        "explanation": "MAC addresses (Layer 2) are 48 bits (6 bytes). IPv4 addresses (Layer 3) are 32 bits (4 bytes).",
        "timeLimit": 30
    },
    {
        "type": "multiple_choice",
        "question": "At which layer do port numbers (such as port 80 for HTTP or port 53 for DNS) reside?",
        "options": [
            "Layer 2",
            "Layer 3",
            "Layer 4",
            "Layer 7"
        ],
        "correct": 3,
        "explanation": "Port numbers are 16-bit fields found in the Transport layer (Layer 4) headers (TCP and UDP).",
        "timeLimit": 30
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following correctly describes a key conceptual difference between the OSI reference model and the TCP/IP model?",
        "options": [
            "OSI was developed based on existing protocols, while TCP/IP was created before protocols were written.",
            "OSI strictly distinguishes between services, interfaces, and protocols, whereas TCP/IP was built around working implementations.",
            "TCP/IP defines 7 layers while OSI defines 4 layers.",
            "OSI does not support connectionless communication at any layer."
        ],
        "correct": 2,
        "explanation": "OSI was a theoretical standard with clear boundaries. TCP/IP was developed empirically by DARPA/IETF to solve practical problems.",
        "timeLimit": 30
    },
    {
        "type": "multiple_choice",
        "question": "Which TCP mechanism at Layer 4 prevents a fast sender from transmitting data faster than the receiving host can process it?",
        "options": [
            "3-Way Handshake",
            "Sliding Window Flow Control",
            "Checksum Calculation",
            "Path MTU Discovery"
        ],
        "correct": 2,
        "explanation": "TCP uses sliding window flow control to let the sender know how much buffer space the receiver currently has available.",
        "timeLimit": 30
    },
    {
        "type": "multiple_choice",
        "question": "Which of the following pairs of protocols both operate at the TCP/IP Application Layer?",
        "options": [
            "BGP and IP",
            "DNS and DHCP",
            "TCP and UDP",
            "ARP and ICMP"
        ],
        "correct": 2,
        "explanation": "Both DNS (Domain Name System) and DHCP (Dynamic Host Configuration Protocol) are Application-layer services.",
        "timeLimit": 30
    },
    {
        "type": "multiple_choice",
        "question": "A router receives a packet. What headers does it inspect and modify before forwarding the packet to the next hop?",
        "options": [
            "It inspects only the Layer 4 header and modifies the port number.",
            "It inspects the Layer 3 destination IP, decrements the TTL, and strips/re-encapsulates the Layer 2 frame with new MAC addresses.",
            "It does not touch any headers; it only duplicates the bits.",
            "It strips all headers up to Layer 7 and re-encrypts the payload."
        ],
        "correct": 2,
        "explanation": "When routing, a router de-encapsulates the L2 frame, inspects L3 dest IP, decrements TTL, and re-encapsulates into a brand new L2 frame.",
        "timeLimit": 30
    }
]

quiz_data = {
    "title": "OSI and TCP/IP Model",
    "questions": questions
}

js_content = f"window.quizData.push({json.dumps(quiz_data, indent=4)});"

os.makedirs(r'C:\Users\Ly Meng Hor ING\Documents\Lesson-Review\web\sets\Networking_OSI_TCP_IP', exist_ok=True)
with open(r'C:\Users\Ly Meng Hor ING\Documents\Lesson-Review\web\sets\Networking_OSI_TCP_IP\data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Created data.js for new quiz")
