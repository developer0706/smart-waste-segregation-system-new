# database.py

CATEGORIES = {
    "biodegradable": {
        "name": "Biodegradable / Organic Waste",
        "color": "#166534",
        "bg": "#dcfce7",
        "description": "Compostable organic matter that decomposes naturally."
    },

    "plastic": {
        "name": "Recyclable Plastic",
        "color": "#1d4ed8",
        "bg": "#dbeafe",
        "description": "Clean plastics with recycling symbols (types 1-7)."
    },

    "non-recyclable": {
        "name": "Non-Recyclable Plastic",
        "color": "#c2410c",
        "bg": "#ffedd5",
        "description": "Plastics that cannot be processed by standard recycling facilities."
    },

    "paper": {
        "name": "Paper & Cardboard",
        "color": "#92400e",
        "bg": "#fef3c7",
        "description": "Clean, dry paper products and flattened cardboard."
    },

    "metal": {
        "name": "Metal Waste",
        "color": "#374151",
        "bg": "#f3f4f6",
        "description": "Aluminum and steel cans."
    },

    "glass": {
        "name": "Recyclable Glass",
        "color": "#0f766e",
        "bg": "#ccfbf1",
        "description": "Glass bottles and jars."
    },

    "hazardous": {
        "name": "Hazardous Waste",
        "color": "#b91c1c",
        "bg": "#fee2e2",
        "description": "Toxic materials requiring special disposal."
    },

    "ewaste": {
        "name": "E-Waste",
        "color": "#4338ca",
        "bg": "#e0e7ff",
        "description": "Electronic devices and accessories."
    }
}


WASTE_DB = {
    "banana peel": ("biodegradable",
                    "Compost at home or place in wet waste."),
    "apple core": ("biodegradable",
                   "Add to compost bin."),
    "plastic bottle": ("plastic",
                       "Rinse and place in recycling."),
    "plastic bag": ("plastic",
                    "Reuse or recycle at collection centers."),
    "food wrapper": ("non-recyclable",
                     "Dispose in general waste."),
    "glass bottle": ("glass",
                     "Rinse and recycle."),
    "paper": ("paper",
              "Keep dry and recycle."),
    "cardboard": ("paper",
                  "Flatten and recycle."),
    "aluminium can": ("metal",
                      "Crush and recycle."),
    "battery": ("hazardous",
                "Take to battery disposal center."),
    "mobile phone": ("ewaste",
                     "Donate or recycle via e-waste center."),
}
