import scrapy


class ProductSpider(scrapy.Spider):
    name = "product1"
    start_urls = [
        "https://www.milwaukeetool.com/Products/Accessories/Metal-Drilling/Twist-Drill-Bits/Aircraft-Length-Black-Oxide-Drill-Bits ",
        "https://www.milwaukeetool.com/Products/Hand-Tools/Fastening/Wrenches/Aluminum-Offset-Pipe-Wrenches ",
        "https://www.milwaukeetool.com/Products/Plumbing/Aluminum-Pipe-Wrenches",
        "https://www.milwaukeetool.com/Products/Accessories/Abrasives/Diamond-Blades-and-Cups/Asphalt-and-Green-Concrete-Blades ",
        "https://www.milwaukeetool.com/Products/Accessories/Cutting/Band-Saw-Blades/Band-Saw-Blades ",
        "https://www.milwaukeetool.com/Products/Accessories/Wood-Drilling/Bellhanger-Bits/Bellhanger-Bits",
        "https://www.milwaukeetool.com/Products/Accessories/Hole-Saws/Big-Hawg/BIG-HAWG-with-Carbide-Teeth",
        "https://www.milwaukeetool.com/Products/Hand-Tools/Cutting/Bolt-Cutters/Bolt-Cutters",
        "https://www.milwaukeetool.com/Products/Hand-Tools/Cutting/Bolt-Cutters/Bolt-Cutters-with-POWERMOVE-Extendable-Arms",
        "https://www.milwaukeetool.com/Products/Accessories/Wood-Drilling/Brad-Points/Brad-Point-Bits",
        "https://www.milwaukeetool.com/Products/Accessories/Bucket-Hooks",
        "https://www.milwaukeetool.com/Products/Accessories/Wood-Drilling/Cable-Bits/Cable-Bits",
        "https://www.milwaukeetool.com/Products/Power-Tools/Electrical-Installation/Cable-Strippers/Cable-Stripper-Bushings",
        "https://www.milwaukeetool.com/Products/Accessories/Concrete-Drilling-and-Chiseling/Adaptors/Carbide-Bit-Adapters",
        "https://www.milwaukeetool.com/Products/Accessories/Metal-Drilling/Carbide-Cutters/Carbide-Cutter-Accessories",
        "https://www.milwaukeetool.com/Products/Accessories/Metal-Drilling/Carbide-Cutters/Carbide-Cutters---Sheet-Metal",
        "https://www.milwaukeetool.com/Products/Accessories/Metal-Drilling/Carbide-Cutters/Carbide-Cutters---Steel-Plate",
        "https://www.milwaukeetool.com/Products/Accessories/Hole-Saws/Carbide-Grit/Carbide-Grit-Hole-Saws",
        "https://www.milwaukeetool.com/Products/Accessories/Concrete-Drilling-and-Chiseling/Hammer-Drill-Bits/Carbide-Hammer-Drill-Bits",
        "https://www.milwaukeetool.com/Products/Hand-Tools/Cutting/Knives-and-Blades/Carton-Utility-Blades",
        "https://www.milwaukeetool.com/Products/Accessories/Cutting/Circular-Saw-Blades/Circular-Saw-Fiber-Cement-Blades",
        "https://www.milwaukeetool.com/Products/Accessories/Cutting/Circular-Saw-Blades/Circular-Saw-Metal-Cutting-Blades",
        "https://www.milwaukeetool.com/Products/Accessories/Cutting/Circular-Saw-Blades/Circular-Saw-Tool-Accessories",
        "https://www.milwaukeetool.com/Products/Accessories/Cutting/Circular-Saw-Blades/Circular-Saw-Wood-Cutting-Blades",
        "https://www.milwaukeetool.com/Products/Safety-Solutions/Personal-Protective-Equipment/High-Visibility-Safety-Vests/Class-2-High-Visibility-Mesh-Safety-Vests",
        "https://www.milwaukeetool.com/Products/Safety-Solutions/Personal-Protective-Equipment/High-Visibility-Safety-Vests/Class-2-High-Visibility-Performance-Safety-Vests",
        "https://www.milwaukeetool.com/Products/Safety-Solutions/Personal-Protective-Equipment/High-Visibility-Safety-Vests/Class-2-High-Visibility-Safety-Vests",
        "https://www.milwaukeetool.com/Products/Safety-Solutions/Personal-Protective-Equipment/High-Visibility-Safety-Vests/Class-2-Surveyors-High-Visibility-Safety-Vest",
        "https://www.milwaukeetool.com/Products/Safety-Solutions/Personal-Protective-Equipment/High-Visibility-Safety-Vests/Class-3-High-Visibility-Mesh-Safety-Vest",
        "https://www.milwaukeetool.com/Products/Safety-Solutions/Personal-Protective-Equipment/High-Visibility-Safety-Vests/Class-3-High-Visibility-Safety-Vest",
        "https://www.milwaukeetool.com/Products/Accessories/Metal-Drilling/Step-Drill-Bits/Cobalt-Step-Drill-Bits",
        "https://www.milwaukeetool.com/Products/Hand-Tools/Measuring/Short-Tape-Measures/Compact-Auto-Lock-Tape-Measures",
        "https://www.milwaukeetool.com/Products/Hand-Tools/Measuring/Short-Tape-Measures/Compact-Tape-Measures",
        "https://www.milwaukeetool.com/Products/Hand-Tools/Measuring/Short-Tape-Measures/Compact-Wide-Blade-Magnetic-Tape-Measures",
        "https://www.milwaukeetool.com/Products/Hand-Tools/Measuring/Short-Tape-Measures/Compact-Wide-Blade-Tape-Measures",
        "https://www.milwaukeetool.com/Products/Equipment/Concrete-Finishing/Concrete-Vibrator-Heads",
        "https://www.milwaukeetool.com/Products/Equipment/Concrete-Finishing/Concrete-Vibrator-Shafts",
        "https://www.milwaukeetool.com/Products/Work-Gear/Gloves/Dipped-Gloves/Cut-Level-1-Nitrile-Dipped-Gloves",
        "https://www.milwaukeetool.com/Products/Work-Gear/Gloves/Cut-Level-1-Winter-Dipped-Gloves",
        "https://www.milwaukeetool.com/Products/Work-Gear/Gloves/Dipped-Gloves/Cut-Level-3-Nitrile-Dipped-Gloves",
        "https://www.milwaukeetool.com/Products/Work-Gear/Gloves/Cut-Level-3-Winter-Dipped-Gloves",
        "https://www.milwaukeetool.com/Products/Work-Gear/Gloves/Dipped-Gloves/Cut-Level-5-Nitrile-Dipped-Gloves",
        "https://www.milwaukeetool.com/Products/Work-Gear/Gloves/Jobsite-Work-Gloves/Demolition-Gloves",
        "https://www.milwaukeetool.com/Products/Accessories/Concrete-Drilling-and-Chiseling/Core-Bits/Diamond-Core-Bit-Accessories",
        "https://www.milwaukeetool.com/Products/Accessories/Abrasives/Diamond-Blades-and-Cups/Diamond-Cup-Double-Row",
        "https://www.milwaukeetool.com/Products/Accessories/Abrasives/Diamond-Blades-and-Cups/Diamond-Cup-Single-Row",
        "https://www.milwaukeetool.com/Products/Accessories/Abrasives/Diamond-Blades-and-Cups/Diamond-Cup-Turbo-Row",
        "https://www.milwaukeetool.com/Products/Accessories/Concrete-Drilling-and-Chiseling/Core-Bits/Diamond-Dry-Core-Bits",
        "https://www.milwaukeetool.com/Products/Accessories/Tile-Drilling/Diamond-Max-Hole-Saws",
        "https://www.milwaukeetool.com/Products/Accessories/Abrasives/Diamond-Blades-and-Cups/Diamond-Point-Tuck-Blade",
        "https://www.milwaukeetool.com/Products/Accessories/Abrasives/Diamond-Blades-and-Cups/Diamond-Premium-Segmented-Blades",
    ]

    def parse(self, response):
        data_ = []
        sku_code_data = response.css("div.table__cell-inn::text").getall()
        sku_code = [
            sku_code_data[a]
            for a in range(0, len(sku_code_data))
            if "-" in sku_code_data[a]
        ]
        for a in sku_code:
            data_.append(a.split(","))
        yield {"file": data_}



