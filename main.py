from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()


@app.get("/home")
def home():

    return [{"pages": "300 lbs Electromagnetic Locks"}, {"pages": "400 lbs Electromagnetic Locks"}, {"pages": "600 lbs Electromagnetic Locks"}, {"pages": "800 lbs Electromagnetic Locks"}, {"pages": "1200 lbs Electromagnetic Locks"}, {"pages": "1500 lbs Electromagnetic Locks"}, {"pages": "Brackets & Covers"}]


@app.get("/menu_1")
def menu_1():

    return [{"pages": "400mm Aluminium Door Handles with Electromagnetic Lock"}, {"pages": "600mm Aluminium Door Handles with Electromagnetic Lock"}, {"pages": "2500mm Aluminium Door Handles with Electromagnetic Lock"}, {"pages": "3000mm Aluminium Door Handles with Electromagnetic Lock"}, {"pages": "Extensions"}]


@app.get("/menu_2")
def menu_2():

    return [{"pages": "Door Loops"}, {"pages": "Push Buttons"}, {"pages": "Catalog"}]


@app.get("/top_menu")
def top_menu():

    return [{"pages": "300 lbs Electromagnetic Locks"}, {"pages": "400 lbs Electromagnetic Locks"}, {"pages": "600 lbs Electromagnetic Locks"}, {"pages": "800 lbs Electromagnetic Locks"}, {"pages": "1200 lbs Electromagnetic Locks"}, {"pages": "1500 lbs Electromagnetic Locks"}, {"pages": "Brackets & Covers"}, {"pages": "400mm Aluminium Door Handles with Electromagnetic Lock"}, {"pages": "600mm Aluminium Door Handles with Electromagnetic Lock"}, {"pages": "2500mm Aluminium Door Handles with Electromagnetic Lock"}, {"pages": "3000mm Aluminium Door Handles with Electromagnetic Lock"}, {"pages": "Extensions"}, {"pages": "Door Loops"}, {"pages": "Push Buttons"}]


@app.get("/api_about")
def api_about():
    return {"map": "map.png", "background": "Our Background", "philosophy": "Philosophy and Business Commitment", "commitment": "Sewosy has proven over the years to be a total reliable partner with true commitment, dedication and integrity to forge a long term successful business relationship with its partners.<br />Sewosy will focus on building and strengthening confidence, trust and innovation of its products for ultimate customers' satisfaction and loyalty."}


@app.get("/api_300lbs")
def api_300lbs():
    return [
        {"product_code": "EF150", "title": "300 lbs Surface Electromagnetic Lock Unmonitored 12-24V DC", "body": "Suitable for single aluminium, glass and not too heavy wooden doors this lock is small, compact and easy to mount on any types of doors with its range of brackets to complement it. <br/><br/>Set at 12VDC at factory outlet, this unmonitored lock is meant for convenience in exit and entry situations when in used with any access control systems.",
            "ip": "42", "voltage": "12 / 24VDC", "current": "480 / 240mA", "holding_force": "300lbs / 150kg", "body_dimension": "170 x 35 x 21mm", "operating_temparature": "-10° to 55°C", "armature_plate_dimension": "130 x 33 x 11mm"},

        {"product_code": "EF150-2", "title": "2x 300 lbs Surface Double Electromagnetic Lock Unmonitored 12-24V DC", "body": "Specifically for use on double doors of glass, wooden and aluminium, this double lock does not compromise on the aesthetic value of the whole access control system. <br/><br/>It holds two doors at the same time each with a 300lb holding force. Set at 12VDC, it can be converted to 24VDC at prior request. <br/><br/>This double lock is unmonitored and is good for the purpose of exit and entry situations when used with any access control systems.",
            "ip": "42", "voltage": "12/24VDC", "current": "960/480mA", "holding_force": "300lbs x 2", "body_dimension": "420 x 35 x 21mm", "operating_temparature": "-10° to 55°C", "armature_plate_dimension": "130 x 33 x 11mm"},

        {"product_code": "EF150CTC", "title": "300 lbs Surface Electromagnetic Lock Monitored 12-24V DC Contact + LED", "body": "This lock is small, compact and monitored and can be in either 12VDC or 24VDC. The CTC model is with light emitting diode or LED for monitoring purpose and is compatible with all kinds of access control systems.<br/><br/>Though it is suitable for all types of doors it is not recommended for too heavy wooden doors because it has only a 300lb holding force.",
            "ip": "42", "voltage": "12/24VDC", "operating_temparature": "-10° to 55°C", "holding_force": "300lbs", "body_dimension": "210 x 35 x 21mm", "armature_plate_dimension": "130 x 33 x 11mm", "current": "480/240mA"},

        {"product_code": "EF150CTC-2", "title": "2x 300 lbs Surface Double Electromagnetic Lock Monitored 12-24V DC", "body": "This lock is meant for double leaf doors of glass, aluminium and wooden make. It is monitored with visual monitoring of the LED and can be used with any access control systems and alarm systems.<br/><br/>The double lock is for double doors to be operational at the same time or for any one door to be operational.<br/><br/>The range of brackets available for this lock enables easy mounting.",
            "ip": "42", "voltage": "12/24VDC", "operating_temparature": "-10° to 55°C", "holding_force": "300lbs x 2", "body_dimension": "210 x 35 x 11mm", "armature_plate_dimension": "130 x 33 x 11mm", "current": "960/480mA"},

        {"product_code": "EF150ENCCTC CA", "ip": "42", "voltage": "12/24VDC", "operating_temparature": "-10° to 55°C", "holding_force": "300lbs", "body_dimension": "173 x 32 x 26mm", "armature_plate_dimension": "130 x 33 x 11mm", "current": "480/240mA",
            "title": "300 lbs 12-24V DC Mortise Electromagnetic Lock + Contact", "body": "This lock is specially designed for light aluminium and even glass doors whereby it is concealed into a hollow aluminium or metal frame.<br/><br/>Easy to fix onto door frames, it is a fail-safe lock with 300lbs of holding force."}
    ]


@app.get("/api_600lbs")
def api_600lbs():
    return [
        {"product_code": "EF300", "ip": "42", "voltage": "12/24VDC", "operating_temparature": "-10° to 55°C", "holding_force": "600lbs", "body_dimension": "250 x 42 x 25mm",
            "armature_plate_dimension": "180 x 38 x 11mm", "current": "480/240mA", "title": "600 lbs Surface Electromagnetic Lock Unmonitored 12-24V DC", "body": "This lock can be mounted on all types of doors and compatible with any access control systems. Powered with direct current at a voltage of 12V or 24V, this fail safe lock is widely used for exit and entry applications.<br/><br/>Its comprehensive range of brackets ensures easy fixing for either in-swing or out-swing doors with little or no maintenance required. "},

        {"product_code": "EF300-2", "ip": "42", "voltage": "12/24VDC", "operating_temparature": "-10° to 55°C", "holding_force": "600lbs x 2", "body_dimension": "500 x 42 x 25mm", "armature_plate_dimension": "180 x 38 x 11mm", "current": "480/240mA", "title": "2x 600 lbs Surface Double Electromagnetic Lock 12-24V DC",
            "body": "This double locks each with 600lb holding force is specifically for double swing doors and most suitable for glass, wooden and aluminium doors.<br/><br/>The unmonitored double locks is fail safe and comes with its own range of brackets to ensure easy mounting."},

        {"product_code": "EF300CTC", "ip": "42", "voltage": "12/24VDC", "operating_temparature": "-10° to 55°C", "holding_force": "600lbs", "body_dimension": "250 x 42 x 25mm", "armature_plate_dimension": "180 x 38 x 11mm", "current": "480/240mA", "title": "600 lbs Surface Electromagnetic Lock Monitored 12-24V DC",
            "body": "This lock can be mounted on all types of doors and compatible with any access control systems. Powered with direct current at a voltage of 12V or 24V, this fail safe lock is widely used for exit and entry applications.<br/><br/>It is built-in with bond sensor and LED monitoring status.<br/><br/>Its comprehensive range of brackets ensures easy fixing for either in-swing or out-swing doors with little or no maintenance required."},

        {"product_code": "EF300CTC-2", "ip": "42", "voltage": "12/24VDC", "operating_temparature": "-10° to 55°C", "holding_force": "600lbs x 2", "body_dimension": "500 x 42 x 25mm", "armature_plate_dimension": "180 x 38 x 11mm", "current": "960/480mA", "title": "2x 600 lbs Surface Double Electromagnetic Lock Monitored 12-24V DC",
            "body": "This double locks each with 600lb holding force is specifically for double swing doors and most suitable for glass, wooden and aluminium doors. It has a built-in bond sensor and has LED monitoring.<br/><br/>It can interface with virtually all types of access control systems and alarm systems."}
    ]


@app.get("/api_1200lbs")
def api_1200lbs():
    return [
        {"product_code": "EF550", "ip": "42", "voltage": "12/24VDC", "operating_temparature": "-10° to 55°C", "holding_force": "1200lbs",
            "body_dimension": "266 x 67 x 39mm", "armature_plate_dimension": "185 x 61 x 17mm", "current": "480/240mA", "title": "1200 lbs Surface Electromagnetic Lock Unmonitored 12-24V DC", "body": "This lock can be mounted on all types of doors and compatible with any access control systems. Powered with direct current at a voltage of 12V or 24V, this fail safe lock is widely used for exit and entry applications.<br/><br/>Its comprehensive range of brackets ensures easy fixing for either in-swing or out-swing doors with little or no maintenance required."},

        {"product_code": "EF550-2", "ip": "42", "voltage": "12/24VDC", "operating_temparature": "-10° to 55°C", "holding_force": "1200lbs x 2",
            "body_dimension": "532 x 67 x 39mm", "armature_plate_dimension": "185 x 61 x 17mm", "current": "960/480mA", "title": "2x 1200 lbs Surface Double Electromagnetic Lock 12-24V DC", "body": "This double locks each with 1200lb holding force is specifically for double swing doors and most suitable for glass, wooden and aluminium doors.<br/><br/>The unmonitored double locks is fail safe and comes with its own range of brackets to ensure easy mounting."},

        {"product_code": "EF550CTC", "ip": "42", "voltage": "12/24VDC", "operating_temparature": "-10° to 55°C", "holding_force": "1200lbs",
            "body_dimension": "266 x 67 x 39mm", "armature_plate_dimension": "185 x 61 x 17mm", "current": "480/240mA", "title": "1200 lbs Surface Electromagnetic Lock Monitored 12-24V DC", "body": "This lock can be mounted on all types of doors and compatible with any access control systems. Powered with direct current at a voltage of 12V or 24V, this fail safe lock is widely used for exit and entry applications.  It is built-in with bond sensor and LED monitoring status.<br/><br/>Its comprehensive range of brackets ensures easy fixing for either in-swing or out-swing doors with little or no maintenance required."},

        {"product_code": "EF550CTC-2", "ip": "42", "voltage": "12/24VDC", "operating_temparature": "-10° to 55°C", "holding_force": "1200lbs x 2",
            "body_dimension": "532 x 67 x 39mm", "armature_plate_dimension": "185 x 61 x 17mm", "current": "960/480mA", "title": "2x 1200 lbs Surface Double Electromagnetic Lock Monitored 12-24V DC", "body": "This double locks each with 1200lb holding force is specifically for double swing doors and most suitable for glass, wooden and aluminium doors. It has a built-in bond sensor and has LED monitoring.<br/><br/>It can interface with virtually all types of access control systems and alarm systems."},

        {"product_code": "EF550ENCCTC CA", "ip": "42", "voltage": "12/24VDC", "operating_temparature": "-10° to 55°C", "holding_force": "1200lbs",
            "body_dimension": "190 x 61.3 x 38mm", "armature_plate_dimension": "185 x 61 x 16.5mm", "current": "480/240mA", "title": "1200 lbs Mortise Electromagnetic Lock 12-24V DC + Contact", "body": "This heavy duty lock is for applications of locking and monitoring all applications of entry and exit doors of all make. <br/><br/>It can be mortised into existing hollow metal or aluminium door frames for single swing doors and compatible with all types of access control systems."}
    ]


@app.get("/api_400lbs")
def api_400lbs():
    return [
        {"product_code": "EXT200CTC", "ip": "67", "voltage": "12/24VDC", "operating_temparature": "-10° to 55°C", "holding_force": "400lbs",
            "body_dimension": "165 x 34.5 x 27.5mm", "armature_plate_dimension": "130 x 33 x 11mm", "current": "500/250mA", "title": "400 lbs Surface Electromagnetic Lock Stainless Steel 12-24V DC", "body": "This model can be used for both indoor and outdoor as the body is encased in stainless steel. With holding force of about 400lbs, it is suitable for not too heavy doors. It is compatible with any access control and burglar alarm systems."}
    ]


@app.get("/api_800lbs")
def api_800lbs():
    return [
        {"product_code": "EXT400CTC", "ip": "67", "voltage": "12/24VDC", "operating_temparature": "-10° to 55°C", "holding_force": "800lbs",
            "body_dimension": "220 x 46 x 28mm", "armature_plate_dimension": "182 x 44 x 12mm", "current": "500/250mA", "title": "800 lbs Surface Electromagnetic Lock Stainless Steel 12-24V DC", "body": "This model can be used for both indoor and outdoor as the body is encased in stainless steel.<br/><br/>This lock is suitable for all types of doors and the available bracket accessories can facilitate all installation configurations.<br/><br/> Also compatible for use with any alarm or access control systems."}
    ]


@app.get("/api_1500lbs")
def api_800lbs():
    return [
        {"product_code": "EXT750CTC", "ip": "67", "voltage": "12/24VDC", "operating_temparature": "-10° to 55°C", "holding_force": "1500lbs",
            "body_dimension": "222 x 62 x 42mm", "armature_plate_dimension": "185 x 61 x 16.5mm", "current": "500/250mA", "title": "1500 lbs Surface Electromagnetic Lock Stainless Steel 12-24V DC", "body": "Encased in stainless steel, this lock is suitable for outdoors and swing gates. It can be configured in alarm and access control systems. L and Z brackets are available for easy mounting."}
    ]


@app.get("/api_door_loops")
def api_door_loops():
    return [
        {"product_code": "DLI7", "title": "9/7mm Stainless Steel Door Loop",
            "body": "Stainless steel door loop 50cm, diameter 9/7mm. This door loop has an inner diameter of 7mm for concealed wires to run through, 9mm outer dimension."},

        {"product_code": "DLI7/30", "title": "9/7mm Stainless Steel Door Loop",
            "body": "Stainless steel door loop 30cm, diameter 9/7mm. This door loop has an inner diameter of 7mm for concealed wires to run through, 9mm outer dimension."},

        {"product_code": "DLI10", "title": "13/10mm Stainless Steel Door Loop",
            "body": "Stainless steel door loop 50cm, diameter 13/10mm. This door loop has an inner diameter of 10mm for concealed wires to run through, 13mm outer dimension."},

        {"product_code": "DLRI10", "title": "13/10mm Reinforced Stainless Steel Door Loop",
            "body": "Reinforced stainless steel door loop 50cm, diameter 13/10mm. This door loop has an inner diameter of 10mm for concealed wires to run through, 13mm outer dimension."},

        {"product_code": "DLRI10EC", "title": "13/10mm Reinforced Stainless Steel Door Loop",
            "body": "Reinforced stainless steel door loop 50cm, diameter 13/10mm with square end caps. This door loop has an inner diameter of 10mm for concealed wires to run through, 13mm outer dimension."},

        {"product_code": "DLN7", "title": "9/7mm Black Door Loop",
            "body": "Black door loop 50cm, diameter 9/7mm. This door loop has an inner diameter of 7mm for concealed wires to run through, 9mm outer dimension."},

        {"product_code": "DLN10", "title": "13/10mm Black Door Loop",
            "body": "Black door loop 50cm, diameter 13/10mm. This door loop has an inner diameter of 10mm for concealed wires to run through, 13mm outer dimension."},

        {"product_code": "DLB7", "title": "9/7mm White Door Loop",
            "body": "White door loop 50cm, diameter 9/7mm. This door loop has an inner diameter of 7mm for concealed wires to run through, 9mm outer dimension."},

        {"product_code": "DLB10", "title": "9/7mm White Door Loop",
            "body": "White door loop 50cm, diameter 13/10mm. This door loop has an inner diameter of 10mm for concealed wires to run through, 13mm outer dimension."},

        {"product_code": "RLI7", "title": "9/7mm Stainless Steel Door Loop",
            "body": "Stainless Steel Door Loop 10m roll, diameter 9/7mm. Optional accessory is nickel-plated end caps product code ECRLI7."},

        {"product_code": "RLI10", "title": "13/10mm Stainless Steel Door Loop",
            "body": "Stainless Steel Door Loop 10m roll, diameter 13/10mm. Optional accessory is nickel-plated end caps product code ECRLI10."},

        {"product_code": "RLN7", "title": "9/7mm Black Door Loop",
            "body": "Black Door Loop 10m roll, diameter 13/10mm. Optional accessory is black end caps product code ECRLN7."},

        {"product_code": "RLN10", "title": "13/10mm Black Door Loop",
            "body": "Black Door Loop 10m roll, diameter 13/10mm. Optional accessory is black end caps product code ECRLN10."},

        {"product_code": "RLB7", "title": "9/7mm White Door Loop",
            "body": "White Door Loop 10m roll, diameter 9/7mm. Optional accessory is white end caps product code ECRLB7."},

        {"product_code": "RLB10", "title": "13/10mm White Door Loop",
            "body": "White Door Loop 10m roll, diameter 13/10mm. Optional accessory is white end caps product code ECRLB10."},

        {"product_code": "ECRLI7", "title": "Nickel Plated End Caps for RLI7",
            "body": "This nickel plated end cap is for stainless steel door loop of 9mm diameter. "},

        {"product_code": "ECRLI10", "title": "Nickel Plated End Caps for RLI10",
            "body": "This nickel plated end cap is for stainless steel door loop of 13mm diameter. "},

        {"product_code": "ECRLN7", "title": "Black End Caps for RLN7",
            "body": "This black end cap is for black door loop of 9mm diameter. "},

        {"product_code": "ECRLN10", "title": "Black End Caps for RLN7",
            "body": "This black end cap is for black door loop of 13mm diameter. "},

        {"product_code": "ECRLB7", "title": "White End Caps for RLB7",
            "body": "This white end cap is for white door loop of 9mm diameter. "},

        {"product_code": "ECRLB10", "title": "White End Caps for RLB10",
            "body": "This white end cap is for white door loop of 13mm diameter. "},

        {"product_code": "DLMC", "title": "Adjustable Mortise Casing 260-480mm",
            "body": "This is a mortised type with metal casing. It can be concealed into wooden and aluminium door frame. The length can be adjusted up to 480mm from 260mm."},

        {"product_code": "DLS170", "title": "170mm Spring",
            "body": "Opening angle up to 90°"},

        {"product_code": "DLS210", "title": "210mm Spring",
            "body": "Opening angle up to 110°"},

        {"product_code": "DLS390", "title": "390mm Spring",
            "body": "Opening angle up to 180°"}
    ]


@app.get("/api_push_buttons")
def api_push_buttons():
    return [
        {"product_code": "PBHI1", "title": "Surface Mounting Housing",
            "body": "Stainless Steel Housing for Push Button on Narrow Plate"},

        {"product_code": "PBHI2", "title": "Surface Mounting Housing",
            "body": "Stainless Steel Housing for Push Button on Square Plate"},

        {"product_code": "PBP19/3", "title": "Stainless Steel Plate for PB19",
            "body": "With Laser Labelling Finger + Key"},

        {"product_code": "PBP19/4", "title": "Stainless Steel Plate for PB19",
            "body": "With Laser Labelling Finger + Key + Braille \"Porte\""},

        {"product_code": "PBP19/FL", "title": "Stainless Steel Plate",
            "body": "For BP19 Neutral"},

        {"product_code": "PBP19/B", "title": "Stainless Steel Plate",
            "body": "With Braille Marking Plate for PB19"},

        {"product_code": "PBP19/TL", "title": "Stainless Steel Plate",
            "body": "For Neutral"},

        {"product_code": "PBP19NO", "title": "Stainless Steel Push Button",
            "body": "No Screw Terminals"},

        {"product_code": "PBP19NC+NO", "title": "Stainless Steel Push Button",
            "body": "(NO+NC) Crimp-Type Terminals"}
    ]


@app.get("/api_400mm_door_handles")
def api_400mm_door_handles():
    return [

        {"product_code": "CPREG-1/400AS", "ip": "42", "voltage": "12/24VDC", "operating_temparature": "-10° to 60°C", "holding_force": "300lbs", "current": "480/240mA",
            "title": "Natural Anodizing Door Handle 12/24V DC + Contact", "body": "CPREG-1/400mm is a door handle incorporating a stainless steel electromagnetic lock with 600lb holding force.<br/><br/>It comes in 2 pieces, one with the lock and wires already fitted and the other with armature plate installed.<br/><br/>All screw holes have been pre-drilled for ease of installation.<br/><br/>Installed vertically at mid-section of the door, the design of this product ensures perfect alignment and prevents tampering.<br/><br/>This is because the wires, screws and armature plate are all hidden by metal covers and end caps.<br/><br/>CPREG-1/400 is compatible with any alarm and access control systems.<br/><br/>This handle can be installed only on aluminium and wooden doors.", "downloads": ["product_catalog", "dimensional_drawing_1", "dimensional_drawing_2", "mounting_diagram_1", "mounting_diagram_2", "mounting_diagram_3"]},

        {"product_code": "CPREG-1/400B", "ip": "42", "voltage": "12/24VDC", "operating_temparature": "-10° to 60°C", "holding_force": "300lbs", "current": "480/240mA",
            "title": "Non-Anodized Door Handle 12/24V DC + Contact", "body": "This aluminium door handle can be fitted with a stainless steel electromagnetic lock of 600lbs holding force.<br/><br/>It can be powder-coated to colour of choice to suit the colour of door or surrounding.<br/><br/>Screw holes are pre-drilled and armature plate fitted into place.<br/><br/>The design of this product ensures perfect alignment and prevents tampering as the wires, screws and armature plates are concealed by aluminium covers and end caps.<br/><br/>It can be incorporated with alarm and access control systems.<br/><br/>Installation is easy, fast and convenient.<br/><br/>This handle can be installed only on aluminium and wooden doors.", "downloads": ["product_catalog"]},

        {"product_code": "CPREG-P/400AS", "ip": "", "voltage": "", "operating_temparature": "", "holding_force": "", "current": "",
            "title": "Natural Anodizing Reinforcement Profile with Handle", "body": "This aluminium handle is an accessory for CPREG-1/400.<br/><br/>It is an added compliment to the whole installation.<br/><br/>This part is fixed to the other side of the door parallel to CPREG-1/400 on another side. ", "downloads": ["product_catalog", "dimensional_drawing", "mounting_diagram"]},

        {"product_code": "CPREG-P/400B", "ip": "", "voltage": "", "operating_temparature": "", "holding_force": "", "current": "",
            "title": "Non-Anodized Reinforcement Profile with Handle", "body": "This non-anodized aluminium handle is an accessory for CPREG-1/400.<br/><br/>It is an added compliment to the whole installation.<br/><br/> This part is fixed to the other side of the door parallel to CPREG-1/400 on another side.", "downloads": ["product_catalog"]},

        {"product_code": "CPREG-S/400AS", "ip": "", "voltage": "", "operating_temparature": "", "holding_force": "", "current": "",
            "title": "Natural Anodizing Reinforcement Profile", "body": "This part acts as an optional accessory for CPREG-1/400 whereby it is fixed to the other side of the door parallel to CPREG-1/400 on another side. ", "downloads": ["product_catalog", "dimensional_drawing", "mounting_diagram"]},

        {"product_code": "CPREG-S/400B", "ip": "", "voltage": "", "operating_temparature": "", "holding_force": "", "current": "",
            "title": "Non-Anodized Reinforcement Profile", "body": "This part acts as an optional accessory for CPREG-1/400 whereby it is fixed to the other side of the door parallel to CPREG-1/400 on another side. ", "downloads": ["product_catalog"]},

        {"product_code": "CPREG-2/40B", "ip": "", "voltage": "", "operating_temparature": "", "holding_force": "", "current": "",
            "title": "Non-Anodized Electromagnetic Handle", "body": "400mm Electromagnetic handle CPREG-2 600lbs 12-24V DC + Contact.", "downloads": []},

        {"product_code": "CPREG-2/40AS", "ip": "", "voltage": "", "operating_temparature": "", "holding_force": "", "current": "",
            "title": "Natural Anodizing Electromagnetic Handle", "body": "400mm Electromagnetic handle CPREG-2 600lbs 12-24V DC + Contact.", "downloads": []}
    ]


@app.get("/api_600mm_door_handles")
def api_600mm_door_handles():
    return [
        {"product_code": "CPREG-1/600AS", "ip": "42", "voltage": "12/24VDC", "operating_temparature": "-10° to 60°C", "holding_force": "300lbs x 2", "current": "960/480mA",
            "title": "Natural Anodizing Electromagnetic Door Handle 12/24V DC + Contact", "body": "This is an aluminium door handle incorporating two 600lb holding force of stainless steel electromagnetic locks into it.<br/><br/>The door handle lock comes in 2 pieces whereby the locks are already pre-mounted with wires and connectors on one piece and the armature plates are fitted on the other. Even the screw holes are pre-drilled for ease of installation.<br/><br/>The design of this product ensures perfect alignment and prevents tampering as the wires, screws and armature plates are concealed by aluminium covers and end caps.<br/><br/>It can be incorporated with any alarm and access control systems.<br/><br/>Installation is easy, fast and convenient.<br/><br/>Only wooden and aluminium doors are recommended for this product.", "downloads": ["product_catalog", "dimensional_drawing_1", "dimensional_drawing_2", "mounting_diagram_1", "mounting_diagram_2", "mounting_diagram_3"]},

        {"product_code": "CPREG-1/600B", "ip": "42", "voltage": "12/24VDC", "operating_temparature": "-10° to 60°C", "holding_force": "300lbs x 2", "current": "960/480mA",
            "title": "Non-Anodized Electromagnetic Door Handle 12/24V DC + Contact", "body": "This is an aluminium door handle that can be fitted with 2 stainless steel electromagnetic locks each with 600lb holding force.<br/><br/>The door handle can be powder-coated to the colour of choice to suit the door or surrounding.<br/><br/>Screw holes are pre-drilled and armature plates fitted into place.<br/><br/>The design of this product ensures perfect alignment and prevents tampering as the wires, screws and armature plates are concealed by aluminium covers and end caps.<br/><br/>It can be incorporated with any alarm and access control systems.<br/><br/>Installation is easy, fast and convenient.<br/><br/>Only wooden and aluminium doors are recommended for this product.", "downloads": ["product_catalog"]},

        {"product_code": "CPREG-P/600AS", "ip": "", "voltage": "", "operating_temparature": "", "holding_force": "", "current": "",
            "title": "Natural Anodizing Reinforcement Profile with Handle", "body": "This aluminium handle is an accessory for CPREG-1/600.<br/><br/>It is an added compliment to the whole installation.<br/><br/>This part is fixed to the other side of the door parallel to CPREG-1/600 on another side. ", "downloads": ["product_catalog", "dimensional_drawing", "mounting_diagram"]},

        {"product_code": "CPREG-P/600B", "ip": "", "voltage": "", "operating_temparature": "", "holding_force": "", "current": "",
            "title": "Non-Anodized Reinforcement Profile with Handle", "body": "This non-anodized aluminium handle is an accessory for CPREG-1/600.<br/><br/>It is an added compliment to the whole installation.<br/><br/> This part is fixed to the other side of the door parallel to CPREG-1/600 on another side.", "downloads": ["product_catalog"]},

        {"product_code": "CPREG-S/600AS", "ip": "", "voltage": "", "operating_temparature": "", "holding_force": "", "current": "",
            "title": "Natural Anodizing Reinforcement Profile", "body": "This part acts as an optional accessory for CPREG-1/600 whereby it is fixed to the other side of the door parallel to CPREG-1/600 on another side. ", "downloads": ["product_catalog", "dimensional_drawing", "mounting_diagram"]},

        {"product_code": "CPREG-S/600B", "ip": "", "voltage": "", "operating_temparature": "", "holding_force": "", "current": "",
            "title": "Non-Anodized Reinforcement Profile", "body": "This part acts as an optional accessory for CPREG-1/600 whereby it is fixed to the other side of the door parallel to CPREG-1/600 on another side. ", "downloads": ["product_catalog"]},
    ]


@app.get("/api_2500mm_door_handles")
def api_2500mm_door_handles():
    return [
        {"product_code": "CPREG-1/2500AS", "ip": "42", "voltage": "12/24VDC", "operating_temparature": "-10° to 60°C", "holding_force": "300lbs x 2", "current": "960/480mA",
            "title": "Natural Anodizing Electromagnetic Door Handle 12/24V DC + Contact", "body": "This is an aluminium door handle incorporating two 600lb holding force of stainless steel electromagnetic locks into it.<br/><br/>The door handle lock comes in 2 pieces whereby the locks are already pre-mounted with wires and connectors on one piece and the armature plates are fitted on the other.<br/><br/>Even the screw holes are pre-drilled for ease of installation.<br/><br/>The length of 2500mm can be specified and adjusted to the length of the doors if requested before delivery.<br/><br/>Tampering of this product is made extremely difficult because the wires, screws and armature plates are concealed by its aluminium covers and end caps.<br/><br/>The design of this product ensures perfect alignment.<br/><br/>This CPREG handle is compatible with any alarm and access control systems.<br/><br/>This handle can be installed only on aluminium and wooden doors.", "downloads": ["product_catalog", "dimensional_drawing_1", "dimensional_drawing_2", "mounting_diagram_1", "mounting_diagram_2", "mounting_diagram_3"]},

        {"product_code": "CPREG-1/2500B", "ip": "42", "voltage": "12/24VDC", "operating_temparature": "-10° to 60°C", "holding_force": "300lbs x 2", "current": "960/480mA",
            "title": "Non Anodized Electromagnetic Door Handle 12/24V DC + Contact", "body": "This is an aluminium door handle that can be fitted with 2 stainless steel electromagnetic locks each with 600lb holding force.<br/><br/> The door handle can be powder-coated to the colour of choice and the length can be adapted to the length of the door.<br/><br/>The design of this product ensures perfect alignment and prevents tampering as the wires, screws and armature plates are concealed by aluminium covers and end caps.<br/><br/> It can be incorporated with alarm and access control systems.<br/><br/> This handle can be installed only on aluminium and wooden doors.", "downloads": ["product_catalog"]},

        {"product_code": "CPREG-P/2500AS", "ip": "", "voltage": "", "operating_temparature": "", "holding_force": "", "current": "",
            "title": "Natural Anodizing Reinforcement Profile with Handle", "body": "This aluminium handle is an accessory for CPREG-1/2500.<br/><br/>It is an added compliment to the whole installation.<br/><br/>This part is fixed to the other side of the door parallel to CPREG-1/2500 on another side. ", "downloads": ["product_catalog", "dimensional_drawing", "mounting_diagram"]},

        {"product_code": "CPREG-P/2500B", "ip": "", "voltage": "", "operating_temparature": "", "holding_force": "", "current": "",
            "title": "Non-Anodized Reinforcement Profile with Handle", "body": "This non-anodized aluminium handle is an accessory for CPREG-1/2500.<br/><br/>It is an added compliment to the whole installation.<br/><br/>This part is fixed to the other side of the door parallel to CPREG-1/2500 on another side. ", "downloads": ["product_catalog"]},

        {"product_code": "CPREG-S/2500AS", "ip": "", "voltage": "", "operating_temparature": "", "holding_force": "", "current": "",
            "title": "Natural Anodizing Reinforcement Profile", "body": "This part acts as an optional accessory for CPREG-1/2500 whereby it is fixed to the other side of the door parallel to CPREG-1/2500 on another side.", "downloads": ["product_catalog", "dimensional_drawing", "mounting_diagram"]},

        {"product_code": "CPREG-S/2500B", "ip": "", "voltage": "", "operating_temparature": "", "holding_force": "", "current": "",
            "title": "Non-Anodized Reinforcement Profile", "body": "This part acts as an optional accessory for CPREG-1/2500 whereby it is fixed to the other side of the door parallel to CPREG-1/2500 on another side.", "downloads": ["product_catalog"]},
    ]


@app.get("/api_3000mm_door_handles")
def api_3000mm_door_handles():
    return [
        {"product_code": "CPREG-1/3000AS", "ip": "42", "voltage": "12/24VDC", "operating_temparature": "-10° to 60°C", "holding_force": "300lbs x 2", "current": "960/480mA",
            "title": "Natural Anodizing Electromagnetic Door Handle 12/24V DC + Contact", "body": "This is an aluminium door handle incorporating two 600lb holding force of stainless steel electromagnetic locks into it.<br/><br/>The door handle lock comes in 2 pieces whereby the locks are already pre-mounted with wires and connectors on one piece and the armature plates are fitted on the other.<br/><br/>Even the screw holes are pre-drilled for ease of installation.<br/><br/>The length of 2500mm can be specified and adjusted to the length of the doors if requested before delivery.<br/><br/>Tampering of this product is made extremely difficult because the wires, screws and armature plates are concealed by its aluminium covers and end caps.<br/><br/>The design of this product ensures perfect alignment.<br/><br/>This CPREG handle is compatible with any alarm and access control systems.<br/><br/>This handle can be installed only on aluminium and wooden doors.", "downloads": ["product_catalog", "dimensional_drawing_1", "dimensional_drawing_2", "mounting_diagram_1", "mounting_diagram_2", "mounting_diagram_3"]},

        {"product_code": "CPREG-1/3000B", "ip": "42", "voltage": "12/24VDC", "operating_temparature": "-10° to 60°C", "holding_force": "300lbs x 2", "current": "960/480mA",
            "title": "Non Anodized Electromagnetic Door Handle 12/24V DC + Contact", "body": "This is an aluminium door handle that can be fitted with 2 stainless steel electromagnetic locks each with 600lb holding force.<br/><br/> The door handle can be powder-coated to the colour of choice and the length can be adapted to the length of the door.<br/><br/>The design of this product ensures perfect alignment and prevents tampering as the wires, screws and armature plates are concealed by aluminium covers and end caps.<br/><br/> It can be incorporated with alarm and access control systems.<br/><br/> This handle can be installed only on aluminium and wooden doors.", "downloads": ["product_catalog"]},

        {"product_code": "CPREG-P/3000AS", "ip": "", "voltage": "", "operating_temparature": "", "holding_force": "", "current": "",
            "title": "Natural Anodizing Reinforcement Profile with Handle", "body": "This aluminium handle is an accessory for CPREG-1/3000.<br/><br/>It is an added compliment to the whole installation.<br/><br/>This part is fixed to the other side of the door parallel to CPREG-1/3000 on another side. ", "downloads": ["product_catalog", "dimensional_drawing", "mounting_diagram"]},

        {"product_code": "CPREG-P/3000B", "ip": "", "voltage": "", "operating_temparature": "", "holding_force": "", "current": "",
            "title": "Non-Anodized Reinforcement Profile with Handle", "body": "This non-anodized aluminium handle is an accessory for CPREG-1/3000.<br/><br/>It is an added compliment to the whole installation.<br/><br/>This part is fixed to the other side of the door parallel to CPREG-1/3000 on another side. ", "downloads": ["product_catalog"]},

        {"product_code": "CPREG-S/3000AS", "ip": "", "voltage": "", "operating_temparature": "", "holding_force": "", "current": "",
            "title": "Natural Anodizing Reinforcement Profile", "body": "This part acts as an optional accessory for CPREG-1/3000 whereby it is fixed to the other side of the door parallel to CPREG-1/3000 on another side.", "downloads": ["product_catalog", "dimensional_drawing", "mounting_diagram"]},

        {"product_code": "CPREG-S/3000B", "ip": "", "voltage": "", "operating_temparature": "", "holding_force": "", "current": "",
            "title": "Non-Anodized Reinforcement Profile", "body": "This part acts as an optional accessory for CPREG-1/3000 whereby it is fixed to the other side of the door parallel to CPREG-1/3000 on another side.", "downloads": ["product_catalog"]},
    ]


@app.get("/api_extensions")
def api_extensions():
    return [
        {"product_code": "CPREG-E/300B",
            "title": "Mill Finish Extension", "body": "For CPREG-2/300B"},
        {"product_code": "CPREG-E/300AS",
            "title": "Natural Anodizing Extension", "body": "For CPREG-2/300AS"},
        {"product_code": "CPREG-E/250B",
            "title": "Mill Finish Extension", "body": "For CPREG-2/250B"},
        {"product_code": "CPREG-E/250AS",
            "title": "Natural Anodizing Extension", "body": "For CPREG-2/250AS"},
        {"product_code": "CPREG-E/220B",
            "title": "Mill Finish Extension", "body": "For CPREG-2/220B"},
        {"product_code": "CPREG-E/220AS",
            "title": "Natural Anodizing Extension", "body": "For CPREG-2/220AS"},
        {"product_code": "CPREG-E/60B",
            "title": "Mill Finish Extension", "body": "For CPREG-2/60B"},
        {"product_code": "CPREG-E/60AS",
            "title": "Natural Anodizing Extension", "body": "For CPREG-2/60AS"},
        {"product_code": "CPREG-E/40B",
            "title": "Mill Finish Extension", "body": "For CPREG-2/40B"},
        {"product_code": "CPREG-E/40AS",
            "title": "Natural Anodizing Extension", "body": "For CPREG-2/40AS"},

    ]


@app.get("/api_brackets_and_covers")
def api_brackets_and_covers():
    return [
        {"product_code": "EF150LS", "title": "Bracket LS-300", "body": "This bracket is for in-swing or out-swing doors. It is to mount EF150 lock.",
            "downloads": ["product_catalog", "dimensional_drawing"]},

        {"product_code": "EF150ZL", "title": "Bracket ZL-300", "body": "This bracket is made up of Z and L brackets to mount the armature plate and electromagnetic lock respectively.<br/><br/> Depending on where the lock faces, it can be for either in-swing or out-swing doors. It is for EF150 or EF150CTC.",
            "downloads": ["product_catalog", "dimensional_drawing_1", "dimensional_drawing_2"]},

        {"product_code": "EF150U", "title": "Bracket U1-300", "body": "This bracket is for glass doors of 10-13mm thickness. It is for EF150 and EF150CTC. ",
            "downloads": ["product_catalog", "dimensional_drawing"]},

        {"product_code": "EF300L", "title": "Adjustable L Bracket For EF300 Range", "body": "This adjustable L bracket is to mount electromagnetic lock for best alignment with the armature plate. It is for EF300 or EF300CTC electromagnetic locks.",
            "downloads": ["product_catalog", "dimensional_drawing", "mounting_diagram"]},

        {"product_code": "EF300L-2", "title": "Adjustable L Bracket For EF300 Double Lock Range", "body": "This adjustable bracket is specially for double lock meant for EF300-2 or EF300CTC-2 only.",
            "downloads": ["product_catalog", "dimensional_drawing"]},

        {"product_code": "EF300SCP", "title": "Mounting Housing For Armature Plate EF300 Range", "body": "This bracket is to mount EF300 armature plate.<br/><br/>Using this bracket does not require drilling a hole through the door to fix the armature plate which is a prerequisite of a fire door rating.",
            "downloads": ["product_catalog", "dimensional_drawing", "mounting_diagram"]},

        {"product_code": "EF300C", "title": "Aluminium Cover For EF300 Lock Range", "body": "This aluminium cover is designed to conceal the electromagnetic lock with its bracket when the door is closed.<br/><br/>It is a cover for EF300 lock series with EF300L and EF300/550Z brackets.",
            "downloads": ["product_catalog", "dimensional_drawing"]},

        {"product_code": "EF300/550Z", "title": "Adjustable Z Bracket", "body": "This bracket is for EF300 and EF550 lock series.<br/><br/>The adjustable bracket ensures good alignment with the armature plate for optimum holding force.<br/><br/>It is meant for any types of swing doors. ",
            "downloads": ["product_catalog", "dimensional_drawing", "mounting_diagram_1", "mounting_diagram_2", "mounting_diagram_3", "mounting_diagram_4", "mounting_diagram_5", "mounting_diagram_6"]},

        {"product_code": "EF300/550UL", "title": "U-Mounting Sleeve for Glass Door", "body": "This bracket is for glass doors. It is for EF300 lock series or EF550 lock series.<br/><br/>It is used with bracket EF300L or EF550L bracket. It is for glass thickness of 10-13mm.",
            "downloads": ["product_catalog", "mounting_diagram_1", "mounting_diagram_2"]},

        {"product_code": "EF300/550UZAP", "title": "U-Mounting Sleeve for Glass Door", "body": "This bracket is for glass doors. It is for either EF300 lock series or EF550 lock series.<br/><br/>It is used together with EF300/550Z bracket. It is for glass thickness of 10-13mm. ",
            "downloads": ["product_catalog", "dimensional_drawing", "mounting_diagram_1", "mounting_diagram_2", "mounting_diagram_3", "mounting_diagram_4", "mounting_diagram_5", "mounting_diagram_6"]},

        {"product_code": "EF550L", "title": "Adjustable L Bracket for EF550 Range", "body": "This adjustable L bracket is to mount electromagnetic lock for best alignment with the armature plate.<br/><br/> It is for EF550 or EF550CTC electromagnetic locks. ",
            "downloads": ["product_catalog", "dimensional_drawing", "mounting_diagram"]},

        {"product_code": "EF550L", "title": "Adjustable L Bracket for EF550 Double Lock Range", "body": "This adjustable bracket is specially for double lock meant for EF550-2 or EF550CTC-2 only.",
            "downloads": ["product_catalog", "dimensional_drawing"]},

        {"product_code": "EF550SCP", "title": "Mounting Housing For Armature Plate EF550 Range", "body": "This bracket is to mount EF550 armature plate.<br/><br/>Using this bracket does not require drilling a hole through the door to fix the armature plate which is a prerequisite of a fire door rating. ",
            "downloads": ["product_catalog", "dimensional_drawing", "mounting_diagram"]},

        {"product_code": "EF550C", "title": "Aluminium Cover For EF550 Lock Range", "body": "This aluminium cover is designed to conceal the electromagnetic lock with its bracket when the door is closed.<br/><br/>It is a cover for EF550 lock series with EF500L and EF300/550Z brackets.",
            "downloads": ["product_catalog", "dimensional_drawing", "mounting_diagram_1", "mounting_diagram_2", "mounting_diagram_3", "mounting_diagram_4"]},

        {"product_code": "EXT200L", "title": "Adjustable L Bracket for EXT200CTC", "body": "This bracket is to mount EXT200CTC lock whereby it can be adjusted to have perfect alignment with the armature plate.",
            "downloads": ["product_catalog", "dimensional_drawing", "mounting_diagram"]},

        {"product_code": "EXT200Z", "title": "Adjustable Z Bracket for EXT200CTC", "body": "The Z bracket is to mount armature plate of EXT200CTC. It can be adjusted to have perfect alignment with the electromagnetic lock. ",
            "downloads": ["product_catalog", "dimensional_drawing", "mounting_diagram"]},

        {"product_code": "EXT400L", "title": "Adjustable L Bracket for EXT400CTC", "body": "This bracket is to mount EXT400CTC lock whereby it can be adjusted to have perfect alignment with the armature plate.",
            "downloads": ["product_catalog", "dimensional_drawing", "mounting_diagram"]},

        {"product_code": "EXT400Z", "title": "Adjustable Z Bracket for EXT400CTC", "body": "The Z bracket is to mount armature plate of EXT400CTC. It can be adjusted to have perfect alignment with the electromagnetic lock. ",
            "downloads": ["product_catalog", "dimensional_drawing", "mounting_diagram"]},

        {"product_code": "EXT750L", "title": "Adjustable L Bracket for EXT750CTC", "body": "This bracket is to mount EXT750CTC lock whereby it can be adjusted to have perfect alignment with the armature plate.",
            "downloads": ["product_catalog", "dimensional_drawing", "mounting_diagram"]},

        {"product_code": "EXT750Z", "title": "Adjustable Z Bracket for EXT750CTC", "body": "The Z bracket is to mount armature plate of EXT750CTC. It can be adjusted to have perfect alignment with the electromagnetic lock. ",
            "downloads": ["product_catalog", "dimensional_drawing", "mounting_diagram"]}
    ]


app.mount("/", StaticFiles(directory="static", html=True), name="static")
