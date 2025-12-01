#!/usr/bin/env python3
# This script generates the remaining HTML pages for Machina website

pages = {
    "drones.html": {
        "title": "Drone Technology - Machina Tech Guide",
        "hero_emoji": "🚁",
        "hero_title": "Drone Technology",
        "hero_subtitle": "Taking flight with aerial innovation",
        "main_title": "The Age of Unmanned Aerial Vehicles",
        "topics": [
            ("Consumer Drones and Photography", "camera drones, aerial photography, videography, stabilization"),
            ("Racing and FPV Drones", "first-person view, racing drones, speed, agility"),
            ("Commercial Applications", "delivery, surveying, agriculture, inspection"),
            ("Regulations and Safety", "FAA rules, registration, no-fly zones, responsible flying")
        ]
    },
    "robots.html": {
        "title": "Robotics - Machina Tech Guide",
        "hero_emoji": "🤖",
        "hero_title": "Robotics Technology",
        "hero_subtitle": "Automation and intelligent machines",
        "main_title": "The Robotics Revolution",
        "topics": [
            ("Industrial Robotics", "manufacturing, automation, precision, efficiency"),
            ("Service Robots", "cleaning, delivery, assistance, hospitality"),
            ("Humanoid Robots", "bipedal robots, human interaction, AI integration"),
            ("The Future of Robotics", "AI, machine learning, autonomous systems")
        ]
    },
    "electric-vehicles.html": {
        "title": "Electric Vehicles - Machina Tech Guide",
        "hero_emoji": "🚗",
        "hero_title": "Electric Vehicles",
        "hero_subtitle": "The future of transportation",
        "main_title": "The Electric Revolution on Wheels",
        "topics": [
            ("Battery Technology", "lithium-ion, solid-state, range, charging speed"),
            ("Charging Infrastructure", "home charging, public chargers, fast charging"),
            ("Performance and Efficiency", "instant torque, regenerative braking, efficiency"),
            ("Market Leaders", "Tesla, traditional automakers, new startups")
        ]
    },
    "3d-printing.html": {
        "title": "3D Printing - Machina Tech Guide",
        "hero_emoji": "🖨️",
        "hero_title": "3D Printing Technology",
        "hero_subtitle": "Manufacturing revolution layer by layer",
        "main_title": "Additive Manufacturing Transforms Production",
        "topics": [
            ("3D Printing Technologies", "FDM, SLA, SLS, material extrusion"),
            ("Materials and Applications", "plastics, resins, metals, ceramics"),
            ("Consumer vs Professional", "hobbyist printers, industrial systems"),
            ("Future Applications", "bioprinting, construction, space manufacturing")
        ]
    },
    "microchips.html": {
        "title": "Microchip Technology - Machina Tech Guide",
        "hero_emoji": "💾",
        "hero_title": "Microchip & Processor Technology",
        "hero_subtitle": "The brains behind modern devices",
        "main_title": "Silicon That Powers Our World",
        "topics": [
            ("Chip Manufacturing", "photolithography, nanometer nodes, fabrication"),
            ("Processor Architecture", "CPUs, GPUs, NPUs, specialized chips"),
            ("Moore's Law and Limits", "transistor density, physical limits, innovation"),
            ("The Semiconductor Industry", "supply chains, geopolitics, future trends")
        ]
    },
    "gadgets.html": {
        "title": "Tech Gadgets - Machina Tech Guide",
        "hero_emoji": "🔌",
        "hero_title": "Tech Gadgets & Innovations",
        "hero_subtitle": "Cool devices that enhance daily life",
        "main_title": "Innovative Gadgets for Modern Living",
        "topics": [
            ("Portable Power", "power banks, wireless chargers, solar chargers"),
            ("Connected Accessories", "smart pens, digital notepads, translation devices"),
            ("Photography Gadgets", "gimbals, lights, lenses, remote triggers"),
            ("Emerging Gadgets", "new innovations, crowdfunded products, future tech")
        ]
    },
    "tools.html": {
        "title": "Smart Tools - Machina Tech Guide",
        "hero_emoji": "🔧",
        "hero_title": "Smart Tools & Equipment",
        "hero_subtitle": "Technology meets craftsmanship",
        "main_title": "The Digital Transformation of Tools",
        "topics": [
            ("Power Tools with Intelligence", "smart drills, laser levels, digital measuring"),
            ("Connected Workshop", "inventory management, project planning, tutorials"),
            ("Safety and Precision", "sensors, automatic shutoffs, accuracy improvements"),
            ("Professional vs Consumer", "contractor tools, DIY equipment, specifications")
        ]
    },
    "industrial.html": {
        "title": "Industrial Technology - Machina Tech Guide",
        "hero_emoji": "🏭",
        "hero_title": "Industrial Technology",
        "hero_subtitle": "Powering manufacturing and production",
        "main_title": "Industry 4.0 and Smart Manufacturing",
        "topics": [
            ("Automation Systems", "PLCs, SCADA, industrial IoT, sensors"),
            ("Predictive Maintenance", "AI monitoring, preventing downtime, optimization"),
            ("Quality Control", "machine vision, automated inspection, zero defects"),
            ("Supply Chain Technology", "tracking, logistics, inventory management")
        ]
    },
    "innovations.html": {
        "title": "Tech Innovations - Machina Tech Guide",
        "hero_emoji": "💡",
        "hero_title": "Technological Innovations",
        "hero_subtitle": "Breakthrough technologies shaping tomorrow",
        "main_title": "Innovations Transforming Our Future",
        "topics": [
            ("Quantum Computing", "qubits, superposition, cryptography, simulation"),
            ("Biotechnology", "gene editing, synthetic biology, medical advances"),
            ("Nanotechnology", "materials science, medicine, electronics"),
            ("Emerging Fields", "photonics, metamaterials, neuromorphic computing")
        ]
    },
    "smart-systems.html": {
        "title": "Smart Systems - Machina Tech Guide",
        "hero_emoji": "🌐",
        "hero_title": "Smart Systems & IoT",
        "hero_subtitle": "Connected intelligence everywhere",
        "main_title": "The Internet of Everything",
        "topics": [
            ("IoT Platforms", "AWS IoT, Azure IoT, Google Cloud IoT"),
            ("Edge Computing", "local processing, reduced latency, bandwidth savings"),
            ("Smart Cities", "traffic management, utilities, public services"),
            ("Security Challenges", "IoT security, privacy, authentication")
        ]
    },
    "professional-equipment.html": {
        "title": "Professional Equipment - Machina Tech Guide",
        "hero_emoji": "🎬",
        "hero_title": "Professional Equipment",
        "hero_subtitle": "Pro-grade technology for serious work",
        "main_title": "Professional Technology Solutions",
        "topics": [
            ("Broadcast Equipment", "cameras, audio, lighting, streaming"),
            ("Medical Technology", "imaging, diagnostics, patient monitoring"),
            ("Scientific Instruments", "microscopes, spectroscopy, analysis tools"),
            ("Enterprise Solutions", "servers, networking, data centers")
        ]
    }
}

print(f"Will generate {len(pages)} pages")
for filename in pages:
    print(f"  - {filename}")
