import scrapy
import json


class ProductSpider(scrapy.Spider):
    name = "product1"
    product_url = []
    start_urls = [
        "https://www.milwaukeetool.com/Products/Safety-Solutions/Personal-Protective-Equipment/Safety-Glasses/Safety-Glasses-Anti-Scratch-Lenses",
        "https://www.milwaukeetool.com/Products/Safety-Solutions/Personal-Protective-Equipment/Safety-Glasses/Safety-Glasses-Fog-Free-Lenses",
        "https://www.milwaukeetool.com/Products/Accessories/Cutting/Multi-Tool-Blades/Universal-Fit-Open-Lok-Triangle-Sandpaper",
        "https://www.milwaukeetool.com/Products/Accessories/Cutting/Multi-Tool-Blades/Universal-Fit-Open-Lok-Japanese-Tooth-Hardwood-Blades",
        "https://www.milwaukeetool.com/Products/Accessories/Cutting/Multi-Tool-Blades/Universal-Fit-Open-Lok-High-Carbon-Steel-Wood-Blades",
        "https://www.milwaukeetool.com/Products/Accessories/Concrete-Drilling-and-Chiseling/SHOCKWAVE-Multi-Material-Drill-Bits/SHOCKWAVE-Carbide-Multi-Material-Drill-Bits",
        "https://www.milwaukeetool.com/Products/Accessories/Concrete-Drilling-and-Chiseling/Chisels/SDS-MAX-Chisels/SDS-MAX-Self-Sharpening-Chisels",
        "https://www.milwaukeetool.com/Products/Hand-Tools/Mechanics-Tools/Combination-Wrenches/sae-ratcheting-combination-wrenches",
        "https://www.milwaukeetool.com/Products/Hand-Tools/Measuring/Short-Tape-Measures/Wide-Blade-Tape-Measures",
        "https://www.milwaukeetool.com/Products/Hand-Tools/Measuring/Short-Tape-Measures/Wide-Blade-Magnetic-Tape-Measures",
        "https://www.milwaukeetool.com/Products/Safety-Solutions/Personal-Protective-Equipment/Safety-Glasses/Performance-Safety-Glasses",
        "https://www.milwaukeetool.com/Products/Accessories/Driving-and-Fastening/SHOCKWAVE-Linemans-Sockets-and-Adapters/Shockwave-Linemans-Hex-Bit-Sockets",
        "https://www.milwaukeetool.com/Products/Accessories/Concrete-Drilling-and-Chiseling/SDS-Max-Drill-Bits/SDS-MAX-One-Piece-Core-Bits",
        "https://www.milwaukeetool.com/Products/Accessories/Concrete-Drilling-and-Chiseling/Chisels/SDS-MAX-Chisels/SDS-MAX-Chisels",
        "https://www.milwaukeetool.com/Products/Power-Tools/Dust-Management/Drilling----Dust-Management/SDS-Plus-Vacuum-Bits",
        "https://www.milwaukeetool.com/Products/Hand-Tools/Layout/Levels/REDSTICK-Magnetic-Compact-Box-Levels",
        "https://www.milwaukeetool.com/Products/Power-Utility/REDSTICK-Magnetic-Box-Levels",
        "https://www.milwaukeetool.com/Products/Hand-Tools/Layout/Levels/REDSTICK-Compact-Box-Levels",
        "https://www.milwaukeetool.com/Products/Accessories/Abrasives/Wire-Wheels-and-Brushes/Wire-Cup-Brush",
        "https://www.milwaukeetool.com/Products/Accessories/Abrasives/Wire-Wheels-and-Brushes/Wire-Brush-Wheel",
        "https://www.milwaukeetool.com/Products/Accessories/Abrasives/Grinding-and-Cut-Off-Wheels/Type-27-Grinding-Wheels",
        "https://www.milwaukeetool.com/Products/Accessories/Abrasives/Wire-Wheels-and-Brushes/Wire-Brush-Bevel",
        "https://www.milwaukeetool.com/Products/Accessories/Abrasives/Grinding-and-Cut-Off-Wheels/Type-1-Cut-Off-Wheels-for-Handheld-Cut-Off-Tools",
        "https://www.milwaukeetool.com/Products/Accessories/Abrasives/Grinding-and-Cut-Off-Wheels/Type-1-Cut-Off-Wheels",
        "https://www.milwaukeetool.com/Products/Plumbing/PEX-Crimp-Jaws-for-M18-FORCE-LOGIC-Press-Tools",
        "https://www.milwaukeetool.com/Products/Accessories/Driving-and-Fastening/SHOCKWAVE-Driver-Bits/SHOCKWAVE-Impact-Slotted-Bits",
        "https://www.milwaukeetool.com/Products/Accessories/Driving-and-Fastening/SHOCKWAVE-Linemans-Sockets-and-Adapters/SHOCKWAVE-Linemans-3-in-1-Utility-Sockets",
        "https://www.milwaukeetool.com/Products/Accessories/Hole-Saws/Recessed-Light/Recessed-Light-Hole-Saws---Continuous-Grit",
        "https://www.milwaukeetool.com/Products/Accessories/Hole-Saws/Hole-Saw-Accessories/Quik-Lok-Holesaw-Extensions",
        "https://www.milwaukeetool.com/Products/Accessories/Driving-and-Fastening/SHOCKWAVE-Sockets-and-Adapters/SHOCKWAVE-Insert-Impact-Socket-Adapters",
        "https://www.milwaukeetool.com/Products/Power-Tools/Drain-Cleaning/Drain-Cleaning-Cables/Sewer-Sectional-Cables",
        "https://www.milwaukeetool.com/Products/Accessories/Metal-Drilling/Twist-Drill-Bits/S-and-D-Black-Oxide-Drill-Bits",
        "https://www.milwaukeetool.com/Products/Accessories/Metal-Drilling/Twist-Drill-Bits/SHOCKWAVE-RED-HELIX-Impact-Drill-Bits",
        "https://www.milwaukeetool.com/Products/Accessories/Metal-Drilling/Twist-Drill-Bits/THUNDERBOLT-Titanium-Coated-Drill-Bits",
        "https://www.milwaukeetool.com/Products/Accessories/Metal-Drilling/Twist-Drill-Bits/RED-HELIX-Cobalt-Drill-Bits",
        "https://www.milwaukeetool.com/Products/Accessories/Cutting/Shear-and-Nibbler-Blades/Shear-Blades",
        "https://www.milwaukeetool.com/Products/Accessories/Cutting/SAWZALL-Blades/SAWZALL-Metal-Blades",
        "https://www.milwaukeetool.com/Products/Accessories/Cutting/SAWZALL-Blades/SAWZALL-The-AX-Nail-Embedded-Wood-Blades",
        "https://www.milwaukeetool.com/Products/Accessories/Wood-Drilling/Auger-BIts/Ship-Auger-Bits",
        "https://www.milwaukeetool.com/Products/Safety-Solutions/Tool-Lanyards/Quick-Connect-Accessories",
        "https://www.milwaukeetool.com/Products/Safety-Solutions/Tool-Lanyards/Wrist-Lanyards",
        "https://www.milwaukeetool.com/Products/Power-Tools/Specialty-Tools/Hoists/1-Ton-Chain-Hoists",
    ]

    def parse(self, response):
        sku_code = []
        data_ = []
        with open("data1.json", encoding="utf8") as data_file:
            data = json.load(data_file)
            for a in range(0, len(data)):
                data_.append(data[a])
        sku_code_data = response.css("div.table__cell-inn::text").getall()
        sku_code = [
            sku_code_data[a]
            for a in range(0, len(sku_code_data))
            if "-" in sku_code_data[a]
        ]
        for a in sku_code:
            data_.append(a)
        for a in data_:
            data_json = {"Sku": a}
        with open("data2.json") as json_file:
            json.dumps(data_json)
