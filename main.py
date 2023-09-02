DIESEL FALL/WINTER 2022 (mini_skirt) 
18%
Dictionary = {
'zip_up_top':0,
'straight_jeans':0,
'close_toed': 0,
'mini_skirt':0,
 'knee_length_boots':0,
'blue':0,
'full_sleeve':0,
'button_up_shirt':0,
'coat':0,
'skinny_jeans':0,
'belt':0,
'gloves':0,
'shoulder_bag':0,
'long_coat':0,
'leather_jacket':0,
'red':0,
'trench_coat':0,
'blazer':0,
 'grey':0,
'cross_body_bag':0,
'cap':0,
'black':0,
'fur_jacket':0,
'jumpsuit':0,
'backpack':0,
'choker':0,
'sling_bag':0,
'flared_pants':0,
'zip_up_top':0,
'hoop_earrings':0,
'fur_coat':0,
'cape':0,
'trousers':0,
'green':0,
'scarf':0,
'hoodie':0,
'bodycon':0,
'pink':0,
'gold':0,
'multi_color':0,
'crop_jacket':0,
'tights':0,
'zip_up_jacket':0,
'half_jacket':0,
'slit_dress':0,
'down_jacket':0,
'tank_top':0,
'ruffle_pants':0,
'puffed_jacket':0,
'fur_sweater':0,
}
[
['zip_up_top', 'straight_jeans', 'close_toed' ],
['mini_skirt', 'knee_length_boots','blue'],
['full_sleeve', 'straight_jeans'],
['button_up_shirt','straight_jeans'],
['mini_skirt', 'full_sleeve','knee_length_boots'],
['coat', 'skinny_jeans','belt','gloves'],
['shoulder_bag', 'skinny_jeans', 'belt'],
['coat', 'purse', 'belt', 'skinny_jeans'],
['long_coat','button_up_shirt'],
['mini_skirt', 'knee_length_boots'],
['mini_skirt', 'knee_length_boots','red', 'purse'],
['leather_jacket','red'],
['trench_coat','jacket','gloves'],
['mini_skirt','gloves','jacket','knee_length_boots'],
['long_coat','purse','gloves','knee_length_boots'],
['trench_coat','blue'],
['blazer', 'grey'],
['cross_body_bag', 'cap', 'coat'],
['cross_body_bag', 'jacket', 'goggles'],
['shoulder_bag','thigh_length_boots'],
['button_down_shirt','belt'],
['shoulder_bag'],
['blazer', 'black' ],
['shoulder_bag','jacket', 'cap'],
['coat','straight_pants'],
['fur_jacket','jumpsuit','goggles','shoulder_bag'],
['backpack', 'choker'],
['sling_bag', 'flared_pants' ],
['long_coat', 'cross_body_bag','cap'],
['zip_up_top','shouder_bag','hoop_earrings'],
['cap','fur_coat','button_up_shirt'],
['button_up_shirt','flared_pants'],
['hoop_earrings','shoulder_bag','black','cape'],
['hoop_earrings','shoulder_bag','knee_length_boots'],
['belt','knee_length_boots','belt','green'],
['fur_jacket','trousers'],
['skinny_jeans','shoulder_bag','green'],
['black','fur_coat','goggles','trousers'],
['scarf','shoulder_bag','hoodie','trousers'],
['ankle_strap', 'bodycon','pink', 'shoulder_bag'],
['gold', 'mini_skirt','shoulder_bag','full_sleeve'],
['blue', 'shoulder_bag','ankle_strap','mini_skirt'],
['shoulder_bag','cap','baggy_pants','coat'],
['shoulder_bag','mini_skirt','multi_color','close_toed'],
['mini_skirt','crop_jacket','close_toed','tights'],
['shoulder_bag', 'zip_up_jacket','skinny_jeans'],
['shoulder_bag','jacket', 'straight_jeans'],
['slit_skirt', 'zip_up_top', 'close_toed'],
['mini_skirt','close_toed','shoulder_bag'],
['tube_top','flared_pants','shoulder_bag'],
['yellow'],
['button_down_shirt', 'straight_pants','blue'],
['half_jacket','grey','gloves','straight_pants'],
['fur_coat','straight_pants'],
['slit_dress',shoulder_bag','orange'],
['down_jacket','shoulder_bag'],
['tank_top','purse','ruffle_pants'],
['long_coat','baggy_pants'],
['tank_top','tights'],
['jacket', 'straight_pants'],
['puffed_jacket','baggy_pants'],
['ruffled_cape', 'mini_skirt','tights','purse'],
['backpack','jacket','gloves','cap'],
['ruffle_jacket', 'choker','mini_skirt'],
['purse','sweater', 'straight_pants'],
['purse','fur_jacket'],
['ruffle_top','skinny_jeans'],
['fur_sweater', 'baggy_pants'],
]

collection_name = valentino_collection_name
looks = valentino_looks
total = len(looks)
trends = valentino_trends

## PRINT INFO

print("ANALYZING TRENDS FROM", collection_name)

## TREND DATA (count)

for trend, var in trends.items():
    count = 0
    for look in looks:
        if str(trend) in look:
            count += 1
    trends.update({trend:count})

## GET PERCENTAGES

trend_percentages = {}
for trend, var in trends.items():
    percentage = var / total * 100
    trend_percentages.update({trend: percentage})
    print("PERCENTAGE OF %s : %s" % (trend, percentage))
