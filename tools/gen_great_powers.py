# -*- coding: utf-8 -*-
"""生成 EU4 主要国家·时代专属修正事件包（含本地化）。"""
import os

GAME = r"D:\steam\steamapps\common\Europa Universalis IV"

ERAS = [(1444, 1500), (1500, 1600), (1600, 1700), (1700, 1800), (1800, 9999)]

ERAS_DEFAULT = [(1444, 1500), (1500, 1600), (1600, 1700), (1700, 1800), (1800, 9999)]


def E(start, end, title, desc, mods, extra=None):
    return dict(start=start, end=end, title=title, desc=desc, mods=mods, extra=extra or [])


def norm_eras(eras):
    out = []
    for i, en in enumerate(eras):
        if isinstance(en, dict):
            out.append(en)
            continue
        t, d, m = en
        st, ed = ERAS_DEFAULT[i]
        out.append(E(st, ed, t, d, m))
    return out


GROUPS = [
    dict(key="fra", tags=["FRA"], name="法兰西", pic="LAND_MILITARY_eventPicture",
         opt="王国的意志不容置疑。",
         eras=[
             ("百年战争的余烬", "鲁昂与波尔多的硝烟散尽。被战火犁过二十年的土地上，骑士、自由弓手与王室的军械官第一次站在同一面王旗下——法兰西的军队不再只为封臣而战。",
              [("land_morale", 0.10), ("manpower_recovery_speed", 0.10)]),
             ("意大利战争", "查理八世跨过阿尔卑斯山。意大利的富庶与分裂让法兰西看清了一件事：决定战场的不再是骑士的冲锋，而是纪律严明的步兵方阵与重炮。",
              [("infantry_power", 0.10), ("land_forcelimit_modifier", 0.10)]),
             ("太阳王的宫廷", "凡尔赛的镜厅里，法语取代拉丁语成为欧洲宫廷的语言。太阳王的荣耀就是法兰西的荣耀，而荣耀需要一场永不落幕的阅兵。",
              [("discipline", 0.05), ("prestige", 0.5), ("state_maintenance_modifier", -0.05)]),
             ("启蒙的沙龙", "沙龙、百科全书与《论法的精神》。伏尔泰与卢梭的笔，比任何一支军队攻城更快——思想正在成为这个国家最锋利的武器。",
              [("technology_cost", -0.10), ("idea_cost", -0.10)]),
             ("大军团", "大革命给了每个人一个理由去死，拿破仑给了他们一套编制去赢。全民征兵、师级纵队与荣誉感，把整个国家变成了一座军营。",
              [("land_morale", 0.15), ("discipline", 0.10), ("manpower_recovery_speed", 0.10)]),
         ]),
    dict(key="gbr", tags=["ENG", "GBR"], name="不列颠", pic="NAVAL_MILITARY_eventPicture",
         opt="海权即国运。",
         eras=[
             ("都铎的舰炮", "泰晤士河口的船坞昼夜不歇，长弓退场，舷侧炮登场。谁能控制海峡，谁就能决定这个岛国的命运。",
              [("naval_morale", 0.10), ("ship_durability", 0.05)]),
             ("皇家海军", "朴茨茅斯的龙骨一艘接一艘下水。两强标准不是野心，是国策——海军的账本比陆军的战报更长。",
              [("naval_forcelimit_modifier", 0.15), ("ship_durability", 0.10), ("naval_morale", 0.05)]),
             ("光荣革命", "国王被议会赶走之后，英格兰银行与国债让伦敦的信用比任何王冠都值钱。战争从此由债券而不是税收来打。",
              [("interest", -1), ("trade_efficiency", 0.10)]),
             ("联合王国的工场", "曼彻斯特的纺织机昼夜不停，煤与铁把乡野变成了工场。财富第一次不再来自土地，而来自蒸汽与齿轮。",
              [("production_efficiency", 0.10), ("technology_cost", -0.05)]),
             ("工业革命", "蒸汽机轰鸣，铁路把内陆与港口缝在一起。世界工厂不需要殖民地来卖货，它需要殖民地来买货。",
              [("production_efficiency", 0.15), ("trade_efficiency", 0.10), ("global_trade_power", 0.10)]),
         ]),
    dict(key="spa", tags=["CAS", "SPA"], name="西班牙", pic="COLONIZATION_eventPicture",
         opt="为了黄金、上帝与荣耀。",
         eras=[
             ("收复失地的余晖", "格拉纳达陷落，半岛上最后一面新月旗降下。十字架与战马成就了卡斯蒂利亚的军魂，也成就了一个刚刚统一的王国。",
              [("land_morale", 0.05), ("global_missionary_strength", 0.02)]),
             ("征服者", "科尔特斯与皮萨罗的船队驶向未知的西海岸。帝国的边界不由条约划定，而由征服者的靴子划定。",
              [("range", 0.20), ("colonists", 1)]),
             ("白银帝国", "波托西的白银经塞维利亚流入欧洲，西班牙的旗帜插满两大洲。代价是本土的工场一片荒芜，而没人愿意承认这一点。",
              [("trade_efficiency", 0.10), ("prestige", 0.5)]),
             ("波旁改革", "波旁王朝的官吏丈量土地、整顿税册、重编舰队。衰落并非不可逆转，只要账本还在王室手里。",
              [("build_cost", -0.10), ("development_cost", -0.05), ("global_tax_modifier", 0.05)]),
             ("加的斯的议会", "拿破仑的军队踏破国门，加的斯的议会却在炮火中写下了第一部宪法。帝国失去了美洲，却开始重新定义自己。",
              [("stability_cost_modifier", -0.10), ("administrative_efficiency", 0.05)]),
         ]),
    dict(key="tur", tags=["TUR"], name="奥斯曼", pic="CONSTANTINOPLE_eventPicture",
         opt="帝国仍在，只是慢了半拍。",
         eras=[
             ("加齐的弯刀", "君士坦丁堡的城墙在重炮下崩塌。边疆战士的信仰与战利品，就是奥斯曼扩张最原始的燃料。",
              [("land_morale", 0.10), ("manpower_recovery_speed", 0.10)]),
             ("苏莱曼的法典", "苏莱曼把土地、税收与军役写进同一部法典。帝国不靠血统运转，靠的是律法与一支领薪水的常备军。",
              [("discipline", 0.05), ("administrative_efficiency", 0.05)]),
             ("苏丹的深宫", "后宫、太监与禁卫军的要挟取代了御驾亲征。舰队在勒班陀折戟，而帝国的账本仍在按旧日的方式计算胜负。",
              [("land_morale", -0.05), ("technology_cost", 0.05), ("global_tax_modifier", -0.05)]),
             ("郁金香与停滞", "郁金香在伊斯坦布尔的花园里盛开，维也纳城下却留下了惨败的印记。西方在按新方法练兵，帝国还在数旧账。",
              [("land_morale", -0.10), ("discipline", -0.05), ("technology_cost", 0.10),
               ("global_tax_modifier", -0.10), ("global_unrest", 1)]),
             ("西亚病夫", "希腊独立、埃及失控、列强环伺。疆域还在，但军队、财政与制度一同落在了时代后面。",
              [("land_morale", -0.15), ("discipline", -0.10), ("global_tax_modifier", -0.15),
               ("global_manpower_modifier", -0.20), ("technology_cost", 0.20),
               ("administrative_efficiency", -0.10), ("stability_cost_modifier", 0.20), ("global_unrest", 2)]),
         ]),
    dict(key="hab", tags=["HAB"], name="奥地利", pic="COURT_eventPicture",
         opt="让哈布斯堡继续统治。",
         eras=[
             ("婚姻外交", "「让别人去打仗吧，你，幸福的奥地利，结婚。」哈布斯堡的婚约比刀剑收获更多，欧洲的地图由嫁妆重新绘制。",
              [("diplomatic_reputation", 1), ("improve_relation_modifier", 0.20)]),
             ("反宗教改革", "耶稣会的教士与特伦托的决议，把帝国的天主教重新钉回原位。信仰的统一，就是领地的统一。",
              [("global_missionary_strength", 0.03), ("stability_cost_modifier", -0.05)]),
             ("三十年战争", "布拉格的窗口扔出了三个人，也扔出了三十年的血火。维也纳终于明白：要维持帝国，先要有一支能打的常备军。",
              [("discipline", 0.05), ("global_manpower_modifier", 0.10)]),
             ("玛丽亚·特蕾莎的改革", "义务教育、统一税制、新的官僚体系与宫廷军事委员会。一个松散的王朝，正在被改造成一台国家机器。",
              [("global_tax_modifier", 0.10), ("administrative_efficiency", 0.05)]),
             ("梅特涅体系", "维也纳会议之后的欧洲：均势、会议与秘密警察。稳定就是奥地利最大的利益，动荡则是它最大的敌人。",
              [("diplomatic_reputation", 2), ("improve_relation_modifier", 0.30)]),
         ]),
    dict(key="rus", tags=["MOS", "RUS"], name="俄罗斯", pic="MILITARY_CAMP_eventPicture",
         opt="为了沙皇与祖国。",
         eras=[
             ("摆脱枷锁", "乌格拉河畔的僵持结束了两个世纪的臣服。莫斯科终于可以自称第三罗马，而它的底气是无穷无尽的人。",
              [("global_manpower_modifier", 0.15), ("manpower_recovery_speed", 0.10)]),
             ("特辖军", "黑骑在诺夫哥罗德街头驰过。沙皇的意志就是法律，而法律由鞭子与绞架来执行。",
              [("discipline", 0.05), ("global_unrest", -1)]),
             ("罗曼诺夫王朝", "混乱时代之后，新王朝重建秩序。西伯利亚的毛皮与乌拉尔的盐，换来国库里堆积的白银。",
              [("governing_capacity_modifier", 0.10), ("global_tax_modifier", 0.10)]),
             ("彼得大帝的西化", "涅瓦河口筑起新都，贵族被剃掉了胡子。海军、学院与工厂一起开张——俄国要用一代人的时间追上欧洲。",
              [("technology_cost", -0.10), ("discipline", 0.05)]),
             ("1812 年的冬天", "焦土、游击与严寒。大军团在莫斯科的灰烬里化为乌有，而俄国的军队跟进了巴黎。",
              [("manpower_recovery_speed", 0.20), ("land_morale", 0.10), ("global_manpower_modifier", 0.10)]),
         ]),
    dict(key="mng", tags=["MNG"], name="明", pic="GREAT_BUILDING_eventPicture",
         opt="天朝自有天朝的章法。",
         eras=[
             E(1444, 1500, "永乐遗产", "紫禁城的钟声犹在，宝船与朝贡体系撑起了一个以中原为中心的天下。秩序，本身就是最大的财富。",
               [("global_tax_modifier", 0.10), ("stability_cost_modifier", -0.10)]),
             E(1500, 1600, "土木之变", "土木堡的惨败让天子成了俘虏，京营精锐覆没。此后的朝堂以太监、党争与内帑为轴心，边患与财政一起松动。",
               [("land_morale", -0.10), ("discipline", -0.05), ("global_tax_modifier", -0.05), ("global_unrest", 1)]),
             E(1600, 1700, "大厦将倾", "万历数十年不朝，辽东的军饷年年拖欠。白银断流、卫所崩坏、党争不休——庞大的帝国正在从内部被蛀空，而关外的马蹄声越来越近。",
               [("land_morale", -0.20), ("discipline", -0.10), ("global_tax_modifier", -0.20),
                ("development_cost", 0.20), ("global_manpower_modifier", -0.25), ("manpower_recovery_speed", -0.30),
                ("stability_cost_modifier", 0.25), ("global_unrest", 2), ("technology_cost", 0.15),
                ("administrative_efficiency", -0.10), ("land_forcelimit_modifier", -0.20), ("build_cost", 0.15)]),
             E(1700, 1800, "流寇与南明", "李自成的队伍与关外的铁骑同时压来。京师陷落，江南诸镇各自拥立——正统不再只有一个，而战火没有一天停过。",
               [("land_morale", -0.15), ("global_tax_modifier", -0.20), ("global_unrest", 3),
                ("administrative_efficiency", -0.15), ("manpower_recovery_speed", -0.20)]),
             E(1800, 9999, "天朝残喘", "海疆洞开，白银外流，团练与厘金取代了旧的卫所与户部。帝国还在，但它已经不再能决定自己的命运。",
               [("global_tax_modifier", -0.20), ("technology_cost", 0.25), ("build_cost", 0.15),
                ("global_unrest", 3), ("land_morale", -0.10)]),
         ]),
    dict(key="qng", tags=["QNG"], name="清", pic="GREAT_BUILDING_eventPicture",
         opt="守成，亦是一种本事。",
         eras=[
             E(1600, 1700, "入关", "山海关的城门打开，八旗的铁骑踏入中原。新王朝接手了旧官僚，也接手了旧难题——但它手里有一支真正能打的军队。",
               [("land_morale", 0.10), ("discipline", 0.10), ("administrative_efficiency", 0.05)]),
             E(1700, 1800, "康乾盛世", "人口过亿，府库充盈，疆域极盛。皇帝南巡的船队沿着运河一路南下，沿途是百年不遇的太平。",
               [("global_tax_modifier", 0.15), ("development_cost", -0.15), ("build_cost", -0.10),
                ("stability_cost_modifier", -0.10)]),
             E(1800, 9999, "嘉道中衰", "白莲教、鸦片与漕运的亏空一起压来。盛世的账本已经算完，接下来是赔款、条约与割地。",
               [("global_tax_modifier", -0.15), ("technology_cost", 0.20), ("global_unrest", 2), ("build_cost", 0.10)]),
         ]),
    dict(key="mch", tags=["MCH", "MJZ", "MHX", "MYR"], name="满洲", pic="HUSSARS_eventPicture",
         opt="八旗所向，皆我疆土。",
         eras=[
             E(1600, 9999, "八旗", "十三副遗甲起兵，牛录与旗分把渔猎的部族编成了一支军队。骑射、赏罚与一统满洲的野心合在一起，足以撼动中原。",
               [("land_morale", 0.20), ("discipline", 0.15), ("infantry_power", 0.20), ("cavalry_power", 0.20),
                ("global_manpower_modifier", 0.50), ("manpower_recovery_speed", 0.50), ("global_regiment_cost", -0.40),
                ("land_forcelimit_modifier", 0.50), ("war_exhaustion", -0.05)],
               extra=["if = {", "\tlimit = { exists = MNG }",
                      "\tadd_casus_belli = { target = MNG type = cb_conquest months = 240 }", "}",
                      "add_yearly_manpower = 3", "add_army_tradition = 10"]),
         ]),
    dict(key="pol", tags=["POL", "PLC"], name="波兰", pic="HUSSARS_eventPicture",
         opt="联邦的荣耀不容侵犯。",
         eras=[
             ("翼骑兵", "维也纳城下，羽翼与长枪一同张开。重骑兵最后的辉煌属于波兰，也只在波兰。",
              [("cavalry_power", 0.15), ("land_morale", 0.05)]),
             ("黄金自由", "贵族共和强盛一时，选举君主与自由否决权让联邦成为欧洲最自由的国家，也让它成为最难统治的国家。",
              [("cavalry_power", 0.10), ("diplomatic_reputation", 1)]),
             ("大洪水", "瑞典与俄国的铁蹄踏遍联邦，城市被焚、国库被掠。联邦靠游击、信仰与一点点运气活了下来。",
              [("land_morale", 0.10), ("manpower_recovery_speed", 0.10)]),
             ("四年的瑟姆", "欧洲第一部成文宪法在 Warsaw 通过。改革与瓜分在同一张桌子上赛跑，而时间不在联邦这一边。",
              [("stability_cost_modifier", -0.10), ("administrative_efficiency", 0.05)]),
             ("民族之春", "军团在流亡中高唱《波兰没有灭亡》。国家可以亡，民族不会——这份执念最终会换来一个国家。",
              [("land_morale", 0.10), ("infantry_power", 0.10)]),
         ]),
    dict(key="swe", tags=["SWE"], name="瑞典", pic="BATTLE_eventPicture",
         opt="北方的雄狮已经醒来。",
         eras=[
             ("铜与铁", "法伦的铜矿与达拉纳的铁，让这个北方小国第一次有了打仗的本钱。",
              [("production_efficiency", 0.05), ("build_cost", -0.05)]),
             ("古斯塔夫·阿道夫的战术", "炮兵、骑兵与步兵被编成一台会跳舞的杀人机器：小型战术单位、齐射与机动，欧洲战争从此改写法。",
              [("infantry_power", 0.15), ("discipline", 0.05)]),
             ("大国时代", "波罗的海几乎成为瑞典的内湖。军役制把农民变成士兵，铁矿石把士兵变成军费。",
              [("manpower_recovery_speed", 0.10), ("land_forcelimit_modifier", 0.10)]),
             ("自由时代", "议会政治取代了王权专制，无战事的年代里，瑞典悄悄积蓄着国力。",
              [("technology_cost", -0.10), ("idea_cost", -0.10)]),
             ("贝尔纳多特", "一位法国元帅成了瑞典的王储，旧王朝在炮声中落幕，新王朝带着拿破仑的操典走上战场。",
              [("land_morale", 0.10), ("discipline", 0.05)]),
         ]),
    dict(key="bra", tags=["BRA"], name="勃兰登堡", pic="MILITARY_CAMP_eventPicture",
         opt="选侯的军队，先要活下去。",
         eras=[
             E(1444, 1500, "选侯的军队", "贫瘠的沙地与分散的领地，让勃兰登堡只能靠一支常备军撑住场面。霍亨索伦家的算盘很简单：先站住，再往前走。",
               [("land_morale", 0.10), ("discipline", 0.05), ("manpower_recovery_speed", 0.15),
                ("ae_impact", -0.20), ("improve_relation_modifier", 0.15)]),
             E(1500, 1600, "霍亨索伦的家业", "宗教改革的风从维滕贝格吹出，选侯把教会的地产收进自己的账册。北德的诸侯还在观望，勃兰登堡已经在扩军。",
               [("land_morale", 0.10), ("discipline", 0.10), ("infantry_power", 0.10),
                ("global_manpower_modifier", 0.25), ("ae_impact", -0.25), ("technology_cost", -0.05)]),
             E(1600, 9999, "北方的军械库", "如果普鲁士始终没有立起来，勃兰登堡自己就得当那把刀。征兵区、军械所与一支不靠雇佣兵的常备军，把沙地变成了兵营。",
               [("discipline", 0.10), ("land_morale", 0.10), ("land_forcelimit_modifier", 0.25),
                ("ae_impact", -0.15), ("global_tax_modifier", 0.10)]),
         ]),
    dict(key="pru", tags=["PRU"], name="普鲁士", pic="SIEGE_eventPicture",
         opt="纪律就是一切。",
         eras=[
             E(1500, 1600, "普鲁士公国", "条顿骑士团的残部世俗化，公国在波罗的海边立起第一支真正意义上的常备军。小国要活下去，只能比大国更早起床。",
               [("discipline", 0.10), ("land_morale", 0.10), ("infantry_power", 0.10),
                ("ae_impact", 0.10), ("max_absolutism", 5), ("legitimacy", 1)]),
             E(1600, 1700, "大选帝侯的常备军", "柏林在强国林立中保住了自己的位置——靠的不是疆域，而是一支随时能出动的军队，和一个说了算的宫廷。",
               [("discipline", 0.10), ("land_morale", 0.10), ("infantry_power", 0.15),
                ("global_manpower_modifier", 0.20), ("ae_impact", 0.15), ("max_absolutism", 10),
                ("all_power_cost", -0.05)]),
             E(1700, 1800, "腓特烈的斜线战术", "斜线战术：以少打多，靠的是操练、纪律与速度。军队成了国王的手艺，而邻国开始把普鲁士的每一次扩军都记在账上。",
               [("discipline", 0.15), ("land_morale", 0.15), ("infantry_power", 0.20), ("artillery_power", 0.05),
                ("ae_impact", 0.20), ("max_absolutism", 10), ("yearly_absolutism", 0.5),
                ("all_power_cost", -0.05)]),
             E(1800, 9999, "沙恩霍斯特改革", "耶拿的惨败之后，征兵制、总参谋部与军官教育把军队从国王的工具改造成民族的学校。重建的普鲁士比从前更危险。",
               [("discipline", 0.10), ("land_morale", 0.10), ("manpower_recovery_speed", 0.20),
                ("infantry_power", 0.10), ("ae_impact", 0.15), ("max_absolutism", 5)]),
         ]),
    dict(key="ned", tags=["HOL", "NED"], name="尼德兰", pic="NAVAL_MILITARY_eventPicture",
         opt="低地人算得清账，也算得清枪口该指向哪儿。",
         eras=[
             E(1444, 1500, "市镇与城垣", "低地的财富堆在城墙后面。佛兰德斯的织工、布拉班特的商人，一个个自治市镇凑钱雇人、修墙、挖壕——这片土地从来不是靠人多，靠的是谁能把城守住。",
               [("defensiveness", 0.10), ("land_morale", 0.05), ("global_regiment_cost", -0.05),
                ("merc_maintenance_modifier", -0.10)]),
             E(1500, 1600, "低地雇佣兵", "勃艮第的遗产换了主人，低地成了哈布斯堡的钱袋。钱袋的好处是能雇最贵的兵：瑞士长枪、德意志火绳枪，打完仗就结账走人。",
               [("infantry_power", 0.05), ("discipline", 0.03), ("defensiveness", 0.15),
                ("merc_maintenance_modifier", -0.15)]),
             E(1600, 1700, "荷兰学派", "莫里茨把军队拆成一百五十人的连，统一操典，排枪齐射；斯蒂文把围城算成一门数学。这套东西后来被古斯塔夫和克伦威尔学了去——荷兰人不以野战闻名，但他们定义了什么叫操练。",
               [("discipline", 0.05), ("infantry_power", 0.10), ("land_morale", 0.10),
                ("siege_ability", 0.10), ("defensiveness", 0.25), ("drill_gain_modifier", 0.50),
                ("drill_decay_modifier", -0.25), ("land_forcelimit_modifier", 0.10)]),
             E(1700, 1800, "屏障要塞", "共和国把国防外包给了石墙和条约：屏障要塞交给奥地利，水线留给自己的工兵。守得住，但打不出去——1713 年之后的荷兰陆军，账面上还在，营里已经没人了。",
               [("defensiveness", 0.30), ("fort_maintenance_modifier", -0.25), ("siege_ability", 0.05),
                ("land_morale", -0.05), ("discipline", -0.03), ("land_forcelimit_modifier", -0.10)]),
             E(1800, 9999, "王国的新军", "巴达维亚共和国与威廉一世的王国重新拉起一支近代军队。1831 年十日出征，荷兰人证明自己还能打——只是此后低地再没当过陆军强国。",
               [("discipline", 0.05), ("land_morale", 0.05), ("infantry_power", 0.05),
                ("land_forcelimit_modifier", 0.10)]),
         ]),
]

GROUPS = [dict(g, eras=norm_eras(g["eras"])) for g in GROUPS]

EXTRA_MODS = [
    dict(host="lcs_ned_3", mid="lcs_ned_navy", name="尼德兰 · 海上马车夫",
         desc="船坞连成一片，货还没卸完又装出港；陆战队随舰而行，攻城时先搭梯子。",
         mods=[("global_ship_recruit_speed", -0.90), ("infantry_fire", 1),
               ("regiment_manpower_usage", -0.40), ("assault_fort_ability", 0.50)]),
    dict(host="lcs_ned_3", mid="lcs_ned_marine", name="尼德兰 · 陆战队操典",
         desc="登船是水兵，上岸是步兵——按陆军操典训练的海军陆战队。",
         mods=[("discipline", 0.10)], marine=True),
]

SPECIALS = [
    dict(key="ned_peak", mid="lcs_ned_peak", name="尼德兰", title="操典与围城",
         tags=["HOL", "NED"], year=1570, months=600, pic="SIEGE_eventPicture",
         desc="1570 年代的尼德兰正处在八十年战争最吃劲的年份：西班牙的大军压境，共和国把每一分钱都花在墙、壕和操练场上。莫里茨与斯蒂文的工兵在泥地里算出了一套让整个欧洲后来都在模仿的战争方法。",
         opt="把城墙算清楚，把枪练熟。",
         mods=[("defensiveness", 0.50), ("siege_ability", 0.40), ("global_sailors_modifier", 1.00)]),
]

N_EVENTS = sum(len(g["eras"]) for g in GROUPS) + len(SPECIALS)

LABELS = {
    "land_morale": ("陆军士气", "%"), "discipline": ("训练度", "%"),
    "infantry_power": ("步兵战斗力", "%"), "cavalry_power": ("骑兵战斗力", "%"),
    "artillery_power": ("炮兵战斗力", "%"), "manpower_recovery_speed": ("人力恢复", "%"),
    "global_manpower_modifier": ("人力上限", "%"), "land_forcelimit_modifier": ("陆军上限", "%"),
    "administrative_efficiency": ("行政效率", "%"), "technology_cost": ("科技花费", "%"),
    "idea_cost": ("理念花费", "%"), "prestige": ("每年威望", ""),
    "global_missionary_strength": ("传教强度", "%"), "range": ("殖民范围", "%"),
    "colonists": ("殖民者", " 名"), "trade_efficiency": ("贸易效率", "%"),
    "global_trade_power": ("贸易竞争力", "%"), "production_efficiency": ("生产效率", "%"),
    "naval_morale": ("海军士气", "%"), "ship_durability": ("船只耐久", "%"),
    "naval_forcelimit_modifier": ("海军上限", "%"), "interest": ("贷款利息", ""),
    "stability_cost_modifier": ("稳定花费", "%"), "diplomatic_reputation": ("外交声望", ""),
    "improve_relation_modifier": ("改善关系", "%"), "global_unrest": ("全国动乱", ""),
    "governing_capacity_modifier": ("治理容量", "%"), "global_tax_modifier": ("税收", "%"),
    "development_cost": ("发展成本", "%"), "build_cost": ("建筑花费", "%"),
    "state_maintenance_modifier": ("行政维护", "%"),
    "global_regiment_cost": ("陆军募兵花费", "%"), "war_exhaustion": ("战争疲劳", ""),
    "ae_impact": ("侵略扩张影响", "%"), "max_absolutism": ("最大专制主义", ""),
    "yearly_absolutism": ("每年专制主义", ""), "all_power_cost": ("全点数花费", "%"),
    "legitimacy": ("每年正统性", ""),
    "defensiveness": ("防御", "%"), "siege_ability": ("攻城能力", "%"),
    "drill_gain_modifier": ("操练获取", "%"), "drill_decay_modifier": ("操练损耗", "%"),
    "fort_maintenance_modifier": ("要塞维护费", "%"),
    "merc_maintenance_modifier": ("雇佣兵维护费", "%"),
    "global_ship_recruit_speed": ("海军建造速度", "%"),
    "infantry_fire": ("步兵火力", ""), "regiment_manpower_usage": ("部队人力花费", "%"),
    "assault_fort_ability": ("强攻能力", "%"),
    "global_sailors_modifier": ("水手", "%"),
}


def eff_text(mods):
    out = []
    for k, v in mods:
        label, unit = LABELS[k]
        if unit == "%":
            out.append("%s %+d%%" % (label, round(v * 100)))
        elif unit == " 名":
            out.append("%s %+g%s" % (label, v, unit))
        else:
            out.append("%s %+g" % (label, v))
    return "；".join(out)


def fmt_val(v):
    if isinstance(v, int) or float(v) == int(v):
        return str(int(v))
    return ("%.4f" % v).rstrip("0").rstrip(".")


ev, mod, loc_en = [], [], []
ev.append("########################################\n"
          "# 主要国家 · 时代专属修正 (Little Code Sauce)\n"
          "# 每个国家在自己所属的时代各触发一次，进入时代后数日内自动发生\n"
          "# 共有 %d 个事件 / %d 个专属修正\n"
          "########################################\n\nnamespace = lcs_gp\n" % (N_EVENTS, N_EVENTS))
mod.append("########################################\n"
           "# 主要国家 · 时代专属修正数值\n"
           "# 全部 duration = -1（永久），由 events/lcs_great_powers.txt 施加\n"
           "########################################\n")

loc_en.append('l_english:')
loc_cn = []  # 同一内容写两份语言文件

eid = 0
for g in GROUPS:
    for i, e in enumerate(g["eras"]):
        eid += 1
        start, end = e["start"], e["end"]
        title, desc, mods = e["title"], e["desc"], e["mods"]
        mid = "lcs_%s_%d" % (g["key"], i + 1)
        flag = "lcs_gp_%s_%d" % (g["key"], i + 1)
        tagcond = ("\t\ttag = %s\n" % g["tags"][0]) if len(g["tags"]) == 1 else \
                  ("\t\tOR = {\n" + "".join("\t\t\ttag = %s\n" % t for t in g["tags"]) + "\t\t}\n")
        endcond = "" if end > 9000 else "\t\tNOT = { is_year = %d }\n" % end
        xeff = "".join("\t\t%s\n" % ln for ln in e["extra"])

        ev.append("country_event = {\n"
                  "\tid = lcs_gp.%d\n"
                  "\ttitle = \"lcs_gp.%d.t\"\n"
                  "\tdesc = \"lcs_gp.%d.d\"\n"
                  "\tpicture = %s\n"
                  "\tmajor = yes\n"
                  "\tfire_only_once = yes\n"
                  "\ttrigger = {\n"
                  "%s"
                  "\t\tNOT = { has_country_flag = %s }\n"
                  "\t\tis_year = %d\n"
                  "%s"
                  "\t}\n"
                  "\tmean_time_to_happen = { days = 5 }\n"
                  "\toption = {\n"
                  "\t\tname = \"lcs_gp.%d.a\"\n"
                  "\t\tadd_country_modifier = { name = %s duration = -1 }\n"
                  "%s"
                  "\t\tset_country_flag = %s\n"
                  "\t}\n"
                  "}\n\n" % (eid, eid, eid, g["pic"], tagcond, flag, start, endcond, eid, mid, xeff, flag))

        mod.append("%s = {\n%s}\n\n" % (mid, "".join("\t%s = %s\n" % (k, fmt_val(v)) for k, v in mods)))

        loc_en.append(' lcs_gp.%d.t:0 "%s · %s"' % (eid, g["name"], title))
        loc_en.append(' lcs_gp.%d.d:0 "%s"' % (eid, desc))
        loc_en.append(' lcs_gp.%d.a:0 "%s"' % (eid, g["opt"]))
        loc_en.append(' %s:0 "%s · %s"' % (mid, g["name"], title))
        loc_en.append(' desc_%s:0 "%s"' % (mid, eff_text(mods)))

# ---------- 附加：宿主修正之外的追加修正（海军 / 陆战队） ----------
for _ex in EXTRA_MODS:
    _needle = "add_country_modifier = { name = %s duration = -1 }" % _ex["host"]
    _addition = "".join("\n\t\tadd_country_modifier = { name = %s duration = -1 }" % _ex["mid"])
    for _i in range(len(ev)):
        if _needle in ev[_i]:
            ev[_i] = ev[_i].replace(_needle, _needle + _addition)
            break
    _body = "".join("\t%s = %s\n" % (k, "yes" if v is True else fmt_val(v)) for k, v in _ex["mods"])
    if _ex.get("marine"):
        _body += "\tis_marine_modifier = yes\n"
    mod.append("%s = {\n%s}\n\n" % (_ex["mid"], _body))
    loc_en.append(' %s:0 "%s"' % (_ex["mid"], _ex["name"]))
    loc_en.append(' desc_%s:0 "%s%s"' % (_ex["mid"], eff_text(_ex["mods"]), "（仅海军陆战队）" if _ex.get("marine") else ""))

# ---------- 附加：一次性限时事件（1570 尼德兰巅峰） ----------
for _sp in SPECIALS:
    eid += 1
    _tagcond = "\t\tOR = {\n" + "".join("\t\t\ttag = %s\n" % t for t in _sp["tags"]) + "\t\t}\n"
    ev.append("country_event = {\n"
              "\tid = lcs_gp.%d\n"
              "\ttitle = \"lcs_gp.%d.t\"\n"
              "\tdesc = \"lcs_gp.%d.d\"\n"
              "\tpicture = %s\n"
              "\tmajor = yes\n"
              "\tfire_only_once = yes\n"
              "\ttrigger = {\n"
              "%s"
              "\t\tNOT = { has_country_flag = %s }\n"
              "\t\tis_year = %d\n"
              "\t}\n"
              "\tmean_time_to_happen = { days = 5 }\n"
              "\toption = {\n"
              "\t\tname = \"lcs_gp.%d.a\"\n"
              "\t\tadd_country_modifier = { name = %s duration = %d }\n"
              "\t\tset_country_flag = %s\n"
              "\t}\n"
              "}\n\n" % (eid, eid, eid, _sp["pic"], _tagcond, _sp["mid"], _sp["year"],
                         eid, _sp["mid"], _sp["months"], _sp["mid"]))
    mod.append("%s = {\n%s}\n\n" % (_sp["mid"], "".join("\t%s = %s\n" % (k, fmt_val(v)) for k, v in _sp["mods"])))
    loc_en.append(' lcs_gp.%d.t:0 "%s · %s"' % (eid, _sp["name"], _sp["title"]))
    loc_en.append(' lcs_gp.%d.d:0 "%s"' % (eid, _sp["desc"]))
    loc_en.append(' lcs_gp.%d.a:0 "%s"' % (eid, _sp["opt"]))
    loc_en.append(' %s:0 "%s · %s"' % (_sp["mid"], _sp["name"], _sp["title"]))
    loc_en.append(' desc_%s:0 "%s（持续 %d 年）"' % (_sp["mid"], eff_text(_sp["mods"]), _sp["months"] // 12))

files = []
files.append((os.path.join(GAME, "events", "lcs_great_powers.txt"), "\n".join(ev)))
files.append((os.path.join(GAME, "common", "event_modifiers", "zz_lcs_great_power_modifiers.txt"), "\n".join(mod)))
body = "\n".join(loc_en[1:])
files.append((os.path.join(GAME, "localisation", "lcs_gp_l_english.yml"),
              "\ufeff" + loc_en[0] + "\n" + body + "\n"))
files.append((os.path.join(GAME, "localisation", "lcs_gp_l_simp_chinese.yml"),
              "\ufeff" + "l_simp_chinese:\n" + body + "\n"))

for path, text in files:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("written:", path, len(text), "chars")

# 自检
ev_text = files[0][1]
print("events:", ev_text.count("country_event = {"), "braces:", ev_text.count("{"), ev_text.count("}"))
mod_text = files[1][1]
print("modifiers:", mod_text.count(" = {"), "braces:", mod_text.count("{"), mod_text.count("}"))
print("loc lines:", body.count("\n"))

# ---------- 生成 README 段落并插入仓库 ----------
rows = ["| 国家 | 时代 | 修正 id | 效果 |", "|---|---|---|---|"]
eid = 0
for g in GROUPS:
    for i, e in enumerate(g["eras"]):
        eid += 1
        start, end = e["start"], e["end"]
        title, desc, mods = e["title"], e["desc"], e["mods"]
        span = "%d–%d" % (start, end - 1) if end < 9000 else "%d+" % start
        rows.append("| %s | %s | `lcs_%s_%d` | %s |" % (g["name"], span, g["key"], i + 1, eff_text(mods)))

for _ex in EXTRA_MODS:
    rows.append("| %s | 随 `%s` 生效 | `%s` | %s%s |" % (
        _ex["name"], _ex["host"], _ex["mid"], eff_text(_ex["mods"]),
        "（仅海军陆战队）" if _ex.get("marine") else ""))
for _sp in SPECIALS:
    rows.append("| %s · %s | %d 起（持续 %d 年） | `%s` | %s |" % (
        _sp["name"], _sp["title"], _sp["year"], _sp["months"] // 12, _sp["mid"], eff_text(_sp["mods"])))

md = ("## 三、主要国家 · 时代专属修正（新增）\n\n"
      "`eu4/events/lcs_great_powers.txt`，namespace `lcs_gp`：%d 组国家 / %d 个事件 / %d 个 `duration = -1` 专属修正"
      "（数值在 `eu4/common/event_modifiers/zz_lcs_great_power_modifiers.txt`）。\n\n"
      "每个事件的触发条件 = 国家标签匹配 + 当前年份落在该时代区间 + 未持有该时代的 flag，`mean_time_to_happen = { days = 5 }`，"
      "进入时代后几天内自动弹出，点掉即永久生效；同一时代不会重复弹。国家若在后期才成立（如大清、大不列颠），只拿当前及之后时代的加成。\n\n"
      "后期国家会拿到**衰退修正**：明自 1500 起逐级下滑、1600 年「大厦将倾」为大衰退，奥斯曼自 1600 年起停滞、1800 年「西亚病夫」，清 1800 年「嘉道中衰」；"
      "数值为负是刻意的历史模拟。满洲（建州/海西/野人女真/满洲）在 1600 年后获得「八旗」超强修正，并对明取得征服宣战理由。\n\n"
      "勃兰登堡（BRA）在成军前拿到强力的陆军与减 AE 修正，帮 AI 活到能成立普鲁士；普鲁士（PRU）改成陆军质量 + 君主系统（正统性 / 最大专制 / 全点数花费）的强权，但背负 +10~20% 的侵略扩张影响——打得越快，邻国结的盟越多。\n\n"
      "每个修正都作用于**拥有该 tag 的国家本身**，玩家和 AI 一视同仁；只想给自己用，就在对应事件的 `trigger` 里加一行 `ai = no`。\n\n"
      + "\n".join(rows) + "\n\n"
      "生成器：`tools/gen_great_powers.py`（改数值直接改 `GROUPS`，重跑即可整套重生成）。\n")

_nev = N_EVENTS
import re as _re
_it = iter([str(len(GROUPS)), str(_nev), str(_nev)])
md = _re.sub(r"%d", lambda _m: next(_it), md)

_ned = ("尼德兰（HOL / NED）五档走的是「小而精的工程化军队」这条史实线：早期靠市镇城防与雇佣兵，"
        "1600 年莫里茨改革到顶（纪律 / 攻城 / 防御 / 操练），1713 年后转为屏障要塞（守得住、打不出去），"
        "1800 年后回补为王国新军。1600 年档额外附带两个修正：`lcs_ned_navy`（海军建造速度 -90%、步兵火力 +1、"
        "部队人力花费 -40%、强攻能力 +50%）与 `lcs_ned_marine`（海军陆战队专属 +10% 训练度，"
        "用 `is_marine_modifier = yes` 限定只作用于陆战队）。另外 1570 年会单独弹一次限时事件 `lcs_ned_peak`"
        "（防御 +50%、攻城 +40%、水手 +100%，持续 50 年 = 600 个月）。\n\n")
md = md.replace("生成器：", _ned + "生成器：")

readme = r"D:\DSH\new_study\README.md"
if os.path.exists(readme):
    txt = open(readme, encoding="utf-8").read()
    i = txt.find("## 三、主要国家")
    j = txt.find("## 四、还原")
    if i >= 0 and j > i:
        txt = txt[:i] + md + "\n" + txt[j:]
        print("README section rebuilt")
    else:
        if "## 四、备注" in txt:
            txt = txt.replace("## 四、备注", "## 五、备注")
        if "## 三、还原" in txt:
            txt = txt.replace("## 三、还原", "## 四、还原")
        k2 = txt.find("## 四、还原")
        txt = (txt[:k2] + md + "\n" + txt[k2:]) if k2 >= 0 else (txt + "\n" + md)
        print("README section inserted")
    open(readme, "w", encoding="utf-8", newline="\n").write(txt)
