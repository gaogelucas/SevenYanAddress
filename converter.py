# %%
import math

def coordinate_to_grid(latitude, longitude, origin=(0, 0)):
    origin_lat, origin_lon = origin
    assert -90 <= latitude <= 90, "Latitude must be between -90 and 90 degrees"
    assert -180 <= longitude <= 180, "Longitude must be between -180 and 180 degrees"
    assert -90 <= origin_lat <= 90, "Origin latitude must be between -90 and 90 degrees"
    assert -180 <= origin_lon <= 180, "Origin longitude must be between -180 and 180 degrees"

    # Constants
    meters_per_degree = 111320  # Approximate meters per degree latitude

    # Calculate grid cell size in degrees
    latitude_spacing = 3 / meters_per_degree
    longitude_spacing = 3 / (meters_per_degree * math.cos(math.radians(latitude)))

    # Calculate grid indices
    lat_index = int((latitude - origin_lat) / latitude_spacing)
    lon_index = int((longitude - origin_lon) / longitude_spacing)

    return (lat_index, lon_index)

def grid_to_coordinate(lat_index, lon_index, origin=(0, 0)):
    origin_lat, origin_lon = origin
    # Constants
    meters_per_degree = 111320  # Approximate meters per degree latitude

    # Calculate grid cell size in degrees
    approximate_latitude = origin_lat + (lat_index * (3 / meters_per_degree))
    latitude_spacing = 3 / meters_per_degree
    longitude_spacing = 3 / (meters_per_degree * math.cos(math.radians(approximate_latitude)))

    # Calculate central point of the grid cell
    latitude = round(approximate_latitude + (latitude_spacing / 2), 5)
    longitude = round(origin_lon + (lon_index * longitude_spacing) + (longitude_spacing / 2), 5)

    # Normalize coordinates
    if latitude > 90:
        latitude = 90
    elif latitude < -90:
        latitude = -90
    if longitude > 180:
        longitude = 180
    elif longitude < -180:
        longitude = -180

    return (latitude, longitude)

def distance_between_coordinates(lat1, lon1, lat2, lon2):
    # Constants
    earth_radius = 6371000  # Radius of Earth in meters

    # Convert latitude and longitude from degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Calculate change in latitude and longitude
    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad

    # Calculate distance using Haversine formula
    a = (math.sin(delta_lat / 2) * math.sin(delta_lat / 2) +
         math.cos(lat1_rad) * math.cos(lat2_rad) *
         math.sin(delta_lon / 2) * math.sin(delta_lon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = earth_radius * c

    return distance

# %%
hanzi_list = [
    ("an", "安"),
    ("bai", "百"),
    ("ban", "半"),
    ("bao", "宝"),
    ("ben", "本"),
    ("biao", "标"),
    ("bin", "宾"),
    ("cai", "才"),
    ("cui", "翠"),
    ("cun", "村"),
    ("dai", "待"),
    ("dan", "旦"),
    ("dao", "到"),
    ("dou", "豆"),
    ("dui", "对"),
    ("dun", "顿"),
    ("duo", "多"),
    ("fan", "泛"),
    ("fei", "飞"),
    ("fen", "分"),
    ("gai", "盖"),
    ("gan", "感"),
    ("gao", "告"),
    ("gen", "根"),
    ("gou", "够"),
    ("gua", "瓜"),
    ("guan", "关"),
    ("gui", "归"),
    ("guo", "过"),
    ("han", "汉"),
    ("hao", "号"),
    ("hua", "华"),
    ("huan", "换"),
    ("hui", "会"),
    ("huo", "活"),
    ("jia", "家"),
    ("jian", "见"),
    ("jiao", "教"),
    ("jie", "解"),
    ("jin", "金"),
    ("jiu", "久"),
    ("juan", "卷"),
    ("jue", "决"),
    ("jun", "军"),
    ("kai", "开"),
    ("ken", "肯"),
    ("kou", "扣"),
    ("kuai", "快"),
    ("kuo", "扩"),
    ("lai", "来"),
    ("lan", "蓝"),
    ("lei", "类"),
    ("lian", "连"),
    ("liao", "料"),
    ("lie", "列"),
    ("lin", "林"),
    ("liu", "六"),
    ("lou", "楼"),
    ("lun", "论"),
    ("luo", "落"),
    ("mai", "买"),
    ("man", "满"),
    ("mei", "美"),
    ("men", "门"),
    ("mian", "面"),
    ("pai", "派"),
    ("pan", "盘"),
    ("pao", "跑"),
    ("pin", "品"),
    ("qia", "恰"),
    ("qian", "前"),
    ("qiao", "桥"),
    ("qie", "切"),
    ("qin", "亲"),
    ("qiu", "球"),
    ("quan", "全"),
    ("que", "却"),
    ("qun", "群"),
    ("sao", "扫"),
    ("sen", "森"),
    ("sui", "岁"),
    ("sun", "孙"),
    ("tan", "谈"),
    ("tao", "讨"),
    ("tian", "田"),
    ("tou", "头"),
    ("tuo", "拓"),
    ("wai", "外"),
    ("wan", "晚"),
    ("wei", "为"),
    ("wen", "问"),
    ("yan", "烟"),
    ("yao", "要"),
    ("ye", "也"),
    ("yin", "音"),
    ("you", "友"),
    ("yu", "鱼"),
    ("yuan", "元"),
    ("yue", "月"),
    ("yun", "云"),
]
# %%

# hanzi_list = [
#     ("Hydrogen", "氢", 1),
#     ("Helium", "氦", 2),
#     ("Lithium", "锂", 3),
#     ("Beryllium", "铍", 4),
#     ("Boron", "硼", 5),
#     ("Carbon", "碳", 6),
#     ("Nitrogen", "氮", 7),
#     ("Oxygen", "氧", 8),
#     ("Fluorine", "氟", 9),
#     ("Neon", "氖", 10),
#     ("Sodium", "钠", 11),
#     ("Magnesium", "镁", 12),
#     ("Aluminum", "铝", 13),
#     ("Silicon", "硅", 14),
#     ("Phosphorus", "磷", 15),
#     ("Sulfur", "硫", 16),
#     ("Chlorine", "氯", 17),
#     ("Argon", "氩", 18),
#     ("Potassium", "钾", 19),
#     ("Calcium", "钙", 20),
#     ("Scandium", "钪", 21),
#     ("Titanium", "钛", 22),
#     ("Vanadium", "钒", 23),
#     ("Chromium", "铬", 24),
#     ("Manganese", "锰", 25),
#     ("Iron", "铁", 26),
#     ("Cobalt", "钴", 27),
#     ("Nickel", "镍", 28),
#     ("Copper", "铜", 29),
#     ("Zinc", "锌", 30),
#     ("Gallium", "镓", 31),
#     ("Germanium", "锗", 32),
#     ("Arsenic", "砷", 33),
#     ("Selenium", "硒", 34),
#     ("Bromine", "溴", 35),
#     ("Krypton", "氪", 36),
#     ("Rubidium", "铷", 37),
#     ("Strontium", "锶", 38),
#     ("Yttrium", "钇", 39),
#     ("Zirconium", "锆", 40),
#     ("Niobium", "铌", 41),
#     ("Molybdenum", "钼", 42),
#     ("Technetium", "锝", 43),
#     ("Ruthenium", "钌", 44),
#     ("Rhodium", "铑", 45),
#     ("Palladium", "钯", 46),
#     ("Silver", "银", 47),
#     ("Cadmium", "镉", 48),
#     ("Indium", "铟", 49),
#     ("Tin", "锡", 50),
#     ("Antimony", "锑", 51),
#     ("Tellurium", "碲", 52),
#     ("Iodine", "碘", 53),
#     ("Xenon", "氙", 54),
#     ("Cesium", "铯", 55),
#     ("Barium", "钡", 56),
#     ("Lanthanum", "镧", 57),
#     ("Cerium", "铈", 58),
#     ("Praseodymium", "镨", 59),
#     ("Neodymium", "钕", 60),
#     ("Promethium", "钷", 61),
#     ("Samarium", "钐", 62),
#     ("Europium", "铕", 63),
#     ("Gadolinium", "钆", 64),
#     ("Terbium", "铽", 65),
#     ("Dysprosium", "镝", 66),
#     ("Holmium", "钬", 67),
#     ("Erbium", "铒", 68),
#     ("Thulium", "铥", 69),
#     ("Ytterbium", "镱", 70),
#     ("Lutetium", "镥", 71),
#     ("Hafnium", "铪", 72),
#     ("Tantalum", "钽", 73),
#     ("Tungsten", "钨", 74),
#     ("Rhenium", "铼", 75),
#     ("Osmium", "锇", 76),
#     ("Iridium", "铱", 77),
#     ("Platinum", "铂", 78),
#     ("Gold", "金", 79),
#     ("Mercury", "汞", 80),
#     ("Thallium", "铊", 81),
#     ("Lead", "铅", 82),
#     ("Bismuth", "铋", 83),
#     ("Polonium", "钋", 84),
#     ("Astatine", "砹", 85),
#     ("Radon", "氡", 86),
#     ("Francium", "钫", 87),
#     ("Radium", "镭", 88),
#     ("Actinium", "锕", 89),
#     ("Thorium", "钍", 90),
#     ("Protactinium", "镤", 91),
#     ("Uranium", "铀", 92),
#     ("Neptunium", "镎", 93),
#     ("Plutonium", "钚", 94),
#     ("Americium", "镅", 95),
#     ("Curium", "锔", 96),
#     ("Berkelium", "锫", 97),
#     ("Californium", "锎", 98),
#     ("Einsteinium", "锿", 99),
#     ("Fermium", "镄", 100)
# ]

LAT_NUMBER = 3339600 # 如果3x3的格子
LON_NUMBER = 6679200 # 如果3x3的格子

def grid_to_array_format(lat_index, lon_index):
    def convert_to_array(number, lat=True):
        if number > 9999999 or number < -9999999:
            raise ValueError("Number exceeds 7 digits")
        
        # Check if the number has more than 7 digits and handle it
        if number < 0:
            # Double the number to make it positive
            if lat:
                number = -number + LAT_NUMBER
            else:
                number = -number + LON_NUMBER
        
        # Convert the number to a string
        num_str = str(number)
        
        # Pad the string with zeros on the left to make it 8 characters long
        padded_num_str = num_str.zfill(8)
        
        # Convert the padded string to a list of integers (digits)
        num_array = [int(char) for char in padded_num_str]
        
        return num_array

    lat_array = convert_to_array(lat_index, lat=True)
    lon_array = convert_to_array(lon_index, lat=False)
    return (lat_array, lon_array)

def grid_array_format_to_grid(lat_array, lon_array):
    def convert_to_index(num_array, lat=True):
        # Convert the array of integers back to a single string
        num_str = ''.join(map(str, num_array))
        
        # Convert the string to an integer
        number = int(num_str)
        
        # Check if the original number was negative
        # Previously, negative numbers were doubled to make them positive
        # To reverse this, check if the number is greater than the max possible value for 7 digits
            # Convert back to the original negative number
        if lat:
            if number > LAT_NUMBER:
                number = LAT_NUMBER - number
        else:
            if number > LON_NUMBER:
                number = LON_NUMBER - number
        return number

    lat_index = convert_to_index(lat_array, lat=True)
    lon_index = convert_to_index(lon_array, lat=False)
    return lat_index, lon_index

def grid_array_to_hanzi_index_array(lat_array, lon_array):
    result = []
    for i in range(8):
        result.append(lat_array[-i-1]*10 + lon_array[-i-1])
    # reduce
    for i in range(6):
        result[i+1] += result[i]
        result[i+1] = result[i+1] % 100
    result.reverse()
    return result

def hanzi_index_array_to_grid_array(hanzi_index_array):
    hanzi_index_array = hanzi_index_array[::-1]
    lat_array = []
    lon_array = []
    
    index_array_unreduce = []
    for i in range(7):
        if i == 0:
            index_array_unreduce.append(hanzi_index_array[i])
        else:
            if hanzi_index_array[i] >= hanzi_index_array[i-1]:
                index_array_unreduce.append(hanzi_index_array[i] - hanzi_index_array[i-1])
            else:
                index_array_unreduce.append(100 + hanzi_index_array[i] - hanzi_index_array[i-1])
    
    index_array_unreduce.append(hanzi_index_array[7])
    
    for i in range(8):
        lat_array.append(index_array_unreduce[i] // 10)
        lon_array.append(index_array_unreduce[i] % 10)

    lat_array.reverse()
    lon_array.reverse()

    return lat_array, lon_array

def hanzi_lookup(hanzi_index):
    return hanzi_list[hanzi_index][1]

def hanzi_index_lookup(hanzi_char):
    for index, (_, char) in enumerate(hanzi_list):
        if char == hanzi_char:
            return index
    raise ValueError("Hanzi character not found in the hanzi_list")

def hanzi_index_array_to_hanzi_string(hanzi_index_array):
    hanzi_result = []
    for i in range(1 if hanzi_index_array[0] == 0 else 0, 8):
        hanzi_result.append(hanzi_lookup(hanzi_index_array[i]))

    return "".join(hanzi_result)

def hanzi_string_to_hanzi_index_array(hanzi_string):
    if len(hanzi_string) == 7:
        hanzi_string = hanzi_list[0][1] + hanzi_string

    hanzi_index_array = []
    for i in range(8):
        hanzi_index_array.append(hanzi_index_lookup(hanzi_string[i]))

    return hanzi_index_array

def coordinate_to_hanzi(latitude, longitude):
    print("经纬度：", latitude, longitude)
    lat_index, lon_index = coordinate_to_grid(latitude, longitude)
    print("经纬度索引：", lat_index, lon_index)
    lat_array, lon_array = grid_to_array_format(lat_index, lon_index)
    print("经纬度数组：", lat_array, lon_array)
    hanzi_index_array = grid_array_to_hanzi_index_array(lat_array, lon_array)
    print("汉字索引数组：", hanzi_index_array)
    hanzi_string = hanzi_index_array_to_hanzi_string(hanzi_index_array)
    print("汉字字符串：", hanzi_string)
    return hanzi_string

def hanzi_to_coordinate(hanzi_string):
    print("汉字字符串：", hanzi_string)
    hanzi_index_array = hanzi_string_to_hanzi_index_array(hanzi_string)
    print("汉字索引数组：", hanzi_index_array)
    lat_array, lon_array = hanzi_index_array_to_grid_array(hanzi_index_array)
    print("经纬度数组：", lat_array, lon_array)
    lat_index, lon_index = grid_array_format_to_grid(lat_array, lon_array)
    print("经纬度索引：", lat_index, lon_index)
    latitude, longitude = grid_to_coordinate(lat_index, lon_index)
    print("经纬度：", latitude, longitude)
    return latitude, longitude
