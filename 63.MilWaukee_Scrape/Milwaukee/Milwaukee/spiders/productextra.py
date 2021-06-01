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



data = ["48-73-2010","48-73-2011","48-73-2015","48-73-2016","48-73-2052","48-73-2054","48-73-2100","48-73-2101","48-73-2105","48-73-2106","48-73-2200","48-73-2201","48-73-2202","48-73-2203","48-73-2204","48-73-2205","48-73-2206","48-73-2207","48-73-2208","48-73-2209","49-56-9658","49-56-9659","49-56-9662","49-56-9663","49-56-9664","49-56-9665","49-56-9666","49-56-9667","49-56-9668","49-56-9669","49-56-9670","49-56-9671","49-56-9680","49-56-9682","49-56-9685","49-56-9687","49-56-9689","49-56-9698","48-13-7703","48-13-7705","48-13-7707","48-13-7709","48-13-7805","48-13-7807","48-13-7809","49-25-1101","49-25-1103","49-25-1109","49-25-1111","49-25-1113","49-25-1119","49-25-1121","48-62-4087","48-62-4250","48-62-4084","48-62-4252","48-62-4089","48-62-4258","49-25-1131","49-25-1133","49-25-1139","49-25-1151","49-25-1153","49-25-1159","49-25-2120","49-25-2012","49-25-2180","49-25-2240","49-25-2025","49-25-2060","49-25-2080","49-66-5141","49-66-5142","49-66-5144","49-66-5145","49-66-5146","49-66-5151","49-66-5152","49-66-5154","49-66-5155","49-66-5156","48-20-5400","48-20-5402","48-20-5404","48-20-5406","48-20-5408","48-20-5410","48-20-5412","48-20-5414","48-20-5420","48-20-5422","48-20-5428","48-20-5430","48-20-5432","48-20-5434","48-20-5436","48-20-5438","48-20-5440","48-20-5495","48-20-5497","48-20-2100","48-20-2102","48-20-2106","48-20-2110","48-20-2114","48-20-2118","48-62-4075","48-62-4175","48-62-4077","48-62-4177","48-62-4062","48-62-4079","48-62-4179","48-62-4081","48-62-4181","48-62-4064","48-62-4082","48-62-4085","48-62-4185","48-62-4187","48-62-4086","48-62-4088","48-62-4097","48-62-4098","48-62-4080","48-62-4065","48-62-4063","48-62-4073","48-62-4074","48-62-4066","48-62-4094","48-62-4194","48-62-4091","48-62-4092","48-52-5040","48-52-5050","48-52-5067","48-52-1350","48-52-1650","48-52-5060","48-52-5065","48-52-1300","48-52-1400","48-52-1600","48-52-5010","48-52-5000","48-52-1700","48-52-1715","48-52-5030","48-52-5020","48-52-1725","48-52-5070","49-94-4510","49-94-4515","49-94-4520","49-94-4525","49-94-4570","49-94-4580","49-94-4585","49-94-5010","49-94-5020","49-94-5730","49-94-6330","49-94-6340","49-94-6360","49-94-7015","49-94-7020","49-94-7025","49-94-7075","49-94-7085","49-94-9025","49-94-9085","49-94-9735","49-94-5080","49-94-1500","49-94-4500","49-94-5000","49-94-6300","49-94-7050","49-94-7055","49-94-9000","49-66-5101","49-66-5102","49-16-2651C","49-16-2653C","49-16-2654C","49-16-2655C","49-16-2656C","49-16-2657C","49-56-0296","49-56-0300","49-56-0303","49-56-0305","49-56-0310","49-56-0315","48-32-4115","48-32-4116","48-32-4117","48-32-4118","48-32-4119","48-32-4155","48-32-4156","48-32-4157","48-32-4158","48-32-4159","48-32-4416","48-32-4417","48-32-4418","48-32-4715","48-32-4716","48-32-4717","48-32-4718","48-32-4719","48-32-4755","48-32-4756","48-32-4757","48-32-4758","48-32-4759","48-32-4916","48-32-4918","48-32-4919","48-32-4920","48-28-1030","48-28-1040","48-28-1050","48-28-1060","48-28-2010","48-28-2020","48-28-2030","48-28-2040","48-53-2852","48-53-2851","48-53-2854","49-94-1270","49-94-1275","49-94-1280","49-94-1285","49-94-1470","49-94-1475","49-94-1480","49-94-1485","48-52-1305","48-52-1315","48-52-1325","48-52-1335","48-89-2739","48-89-2740","48-89-2741","48-89-2742","48-89-2743","48-89-2744","48-89-2745","48-89-2746","48-89-2747","48-89-2748","48-89-2749","48-89-2750","48-89-2751","48-89-2752","48-89-2753","48-89-2754","48-89-2755","48-89-2756","48-89-2757","48-89-2758","48-89-4601","48-89-4602","48-89-4603","48-89-4604","48-89-4605","48-89-4606","48-89-4607","48-89-4608","48-89-4609","48-89-4610","48-89-4611","48-89-4612","48-89-4613","48-89-4614","48-89-4615","48-89-4616","48-89-4617","48-89-4618","48-89-4619","48-89-4620","48-89-4621","48-89-4622","48-89-4623","48-89-4624","48-89-4625","48-89-4626","48-89-4627","48-89-4628","48-89-4629","48-89-2201","48-89-2202","48-89-2203","48-89-2204","48-89-2205","48-89-2206","48-89-2207","48-89-2208","48-89-2209","48-89-2210","48-89-2211","48-89-2212","48-89-2213","48-89-2214","48-89-2215","48-89-2216","48-89-2217","48-89-2218","48-89-2219","48-89-2220","48-89-2221","48-89-2222","48-89-2223","48-89-2224","48-89-2225","48-89-2226","48-89-2227","48-89-2228","48-89-2229","48-00-5090","48-00-5181","48-00-5183","48-00-5185","48-00-5092","48-01-7092","48-00-5182","48-00-8182","48-01-2162","48-01-6182","48-01-2182","48-00-5184","48-00-8184","48-01-2164","48-01-2184","48-01-6184","48-01-2186","48-01-6186","48-00-8186","48-00-5186","48-00-5187","48-00-5188","48-01-2167","48-01-2168","48-01-7182","48-01-7184","48-01-7186","48-01-2187","48-01-6187","48-01-7187","48-01-2188","48-01-6188","48-01-7188","48-00-5189","48-01-2169","48-01-6189","48-01-7189","48-00-5021","48-00-8021","48-01-2001","48-01-2021","48-01-7021","48-00-5026","48-00-8026","48-01-2006","48-01-2026","48-01-7026","48-00-5027","48-00-8027","48-01-2007","48-01-2027","48-01-7027","48-13-0373","48-13-0503","48-13-0623","48-13-0683","48-13-0753","48-13-0813","48-13-0873","48-13-0933","48-13-1003","48-13-1063","48-13-1123","48-13-1253","48-13-1373","48-13-1503","48-13-5500","48-13-5520","48-13-5620","48-13-5680","48-13-5750","48-13-5810","48-13-5870","48-13-5930","48-13-6000","48-13-6010","48-13-6120","48-13-6250","48-13-6370","48-13-6500","48-89-2301","48-89-2302","48-89-2303","48-89-2304","48-89-2305","48-89-2306","48-89-2307","48-89-2308","48-89-2309","48-89-2310","48-89-2311","48-89-2312","48-89-2313","48-89-2314","48-89-2315","48-89-2316","48-89-2317","48-89-2318","48-89-2319","48-89-2320","48-89-2321","48-89-2322","48-89-2323","48-89-2324","48-89-2325","48-89-2326","48-89-2327","48-89-2328","48-89-2329","48-22-8822","48-22-8823","48-22-8825","48-22-8830","48-22-8835","48-32-5020","48-32-5021","48-32-5022","48-32-5720","48-32-5721","48-32-5722","9770-20","9771-20","9772-20","9773-20","48-08-0500","48-44-0070","48-44-0112","48-44-0122","48-44-0151","48-44-0160","48-44-0170","48-44-0400","48-44-0405","48-20-8880","48-20-8882","48-20-8884","48-20-8886","48-20-8888","48-20-8890","48-20-8892"]