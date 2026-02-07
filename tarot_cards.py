"""塔罗牌数据模型"""

class TarotCard:
    def __init__(self, card_id, name, name_en, card_type, meaning_upright, meaning_reversed):
        self.id = card_id
        self.name = name
        self.name_en = name_en
        self.type = card_type  # 'major' 或 'minor'
        self.meaning_upright = meaning_upright
        self.meaning_reversed = meaning_reversed
        self.image_path = f"/static/images/cards/{card_id:02d}.png"


class TarotDeck:
    def __init__(self):
        self.cards = self._initialize_deck()
    
    def _initialize_deck(self):
        """初始化78张塔罗牌"""
        cards = []
        
        # 大阿卡纳 (22张)
        major_arcana = [
            (0, "愚者", "The Fool", "major", 
             "新的开始、冒险、天真、自由、潜力",
             "鲁莽、冒险、被愚弄、风险"),
            (1, "魔术师", "The Magician", "major",
             "创造力、技能、能力、意志力、自信",
             "操纵、欺骗、意志薄弱、技巧误用"),
            (2, "女祭司", "The High Priestess", "major",
             "直觉、神秘、潜意识、智慧、内在声音",
             "秘密、压抑、直觉受阻、表面化"),
            (3, "皇后", "The Empress", "major",
             "丰饶、母性、自然、滋养、创造力",
             "依赖、创造受抑制、空虚、缺乏情感"),
            (4, "皇帝", "The Emperor", "major",
             "权威、结构、控制、领导、父亲形象",
             "暴政、僵化、冷血、过度控制"),
            (5, "教皇", "The Hierophant", "major",
             "传统、精神指引、宗教、信仰、教育",
             "反叛、非传统、新的信仰、限制"),
            (6, "恋人", "The Lovers", "major",
             "爱、和谐、关系、选择、价值观",
             "分离、分歧、不和谐、糟糕的选择"),
            (7, "战车", "The Chariot", "major",
             "控制、意志力、胜利、决心、自律",
             "失控、缺乏方向、侵略、挫败"),
            (8, "力量", "Strength", "major",
             "勇气、耐心、控制、同情、内在力量",
             "软弱、自我怀疑、缺乏纪律、缺乏耐心"),
            (9, "隐士", "The Hermit", "major",
             "内省、孤独、寻求真理、智慧、指引",
             "孤立、孤独、退缩、迷失方向"),
            (10, "命运之轮", "Wheel of Fortune", "major",
             "变化、周期、命运、转折点、好运",
             "厄运、抵抗变化、破坏、不幸"),
            (11, "正义", "Justice", "major",
             "正义、公平、真理、法律、因果",
             "不公、缺乏责任、不诚实、偏见"),
            (12, "倒吊人", "The Hanged Man", "major",
             "牺牲、放手、新视角、等待、启示",
             "停滞、抵抗、牺牲无用、延误"),
            (13, "死神", "Death", "major",
             "结束、转变、重生、新开始、放下",
             "抵抗改变、停滞、无法放手、拖延"),
            (14, "节制", "Temperance", "major",
             "平衡、适度、耐心、目的、和谐",
             "失衡、过度、缺乏长期愿景、冲突"),
            (15, "恶魔", "The Devil", "major",
             "束缚、成瘾、物质主义、欲望、不安全感",
             "解放、从束缚中解脱、重获力量"),
            (16, "高塔", "The Tower", "major",
             "突然变化、混乱、启示、觉醒、破坏",
             "避免灾难、恐惧改变、延迟"),
            (17, "星星", "The Star", "major",
             "希望、信念、目的、更新、精神力量",
             "绝望、缺乏信心、消极、脱离现实"),
            (18, "月亮", "The Moon", "major",
             "幻觉、恐惧、焦虑、潜意识、直觉",
             "困惑、恐惧消除、释放压抑、真相揭示"),
            (19, "太阳", "The Sun", "major",
             "积极、温暖、成功、活力、快乐",
             "悲伤、暂时的挫折、缺乏成功、悲观"),
            (20, "审判", "Judgement", "major",
             "复活、觉醒、内心召唤、宽恕、决定",
             "自我怀疑、拒绝召唤、缺乏自我意识"),
            (21, "世界", "The World", "major",
             "完成、整合、成就、旅行、圆满",
             "未完成、缺乏闭环、缺乏成功、停滞")
        ]
        
        for card in major_arcana:
            cards.append(TarotCard(*card))
        
        # 小阿卡纳 - 权杖 (Wands - 火元素)
        wands = [
            (22, "权杖王牌", "Ace of Wands", "minor",
             "灵感、新的开始、创造性火花、行动力",
             "延误、缺乏方向、缺乏动力、错误的开端"),
            (23, "权杖二", "Two of Wands", "minor",
             "规划、发现、未来展望、决策",
             "恐惧未知、缺乏计划、犹豫不决"),
            (24, "权杖三", "Three of Wands", "minor",
             "扩张、远见、进步、领导力",
             "缺乏远见、进展缓慢、失望"),
            (25, "权杖四", "Four of Wands", "minor",
             "庆祝、和谐、团聚、稳定",
             "缺乏和谐、过渡、缺乏稳定性"),
            (26, "权杖五", "Five of Wands", "minor",
             "冲突、竞争、张力、斗争",
             "避免冲突、和谐、妥协"),
            (27, "权杖六", "Six of Wands", "minor",
             "成功、胜利、骄傲、公众认可",
             "傲慢、缺乏成功、缺乏自信"),
            (28, "权杖七", "Seven of Wands", "minor",
             "挑战、防御、坚持、立场",
             "放弃、不堪重负、缺乏信念"),
            (29, "权杖八", "Eight of Wands", "minor",
             "速度、行动、快速进展、旅行",
             "延迟、挫折、缺乏进展"),
            (30, "权杖九", "Nine of Wands", "minor",
             "韧性、坚持、毅力、最后防线",
             "疲惫、放弃、缺乏耐力"),
            (31, "权杖十", "Ten of Wands", "minor",
             "负担、额外责任、辛苦工作、完成",
             "缺乏方向、不堪重负、倦怠"),
            (32, "权杖侍从", "Page of Wands", "minor",
             "灵感、探索、热情、新想法",
             "缺乏热情、拖延、缺乏新想法"),
            (33, "权杖骑士", "Knight of Wands", "minor",
             "行动、冒险、冲动、热情",
             "缺乏方向、匆忙、缺乏激情"),
            (34, "权杖王后", "Queen of Wands", "minor",
             "自信、独立、热情、社交",
             "缺乏自信、依赖他人、缺乏热情"),
            (35, "权杖国王", "King of Wands", "minor",
             "领导力、愿景、企业家精神、创造力",
             "控制欲、傲慢、缺乏愿景")
        ]
        
        for card in wands:
            cards.append(TarotCard(*card))
        
        # 小阿卡纳 - 圣杯 (Cups - 水元素)
        cups = [
            (36, "圣杯王牌", "Ace of Cups", "minor",
             "爱、新的关系、情感满足、直觉",
             "情感阻塞、缺乏爱、空虚、悲伤"),
            (37, "圣杯二", "Two of Cups", "minor",
             "伙伴关系、统一、连接、关系",
             "分离、冲突、不和谐、不平衡"),
            (38, "圣杯三", "Three of Cups", "minor",
             "庆祝、友谊、社交、快乐",
             "孤独、社交孤立、缺乏庆祝"),
            (39, "圣杯四", "Four of Cups", "minor",
             "反思、冥想、厌倦、不满",
             "参与、重新联系、新的机会"),
            (40, "圣杯五", "Five of Cups", "minor",
             "失落、悲伤、后悔、失望",
             "接受、继续前进、找到平静"),
            (41, "圣杯六", "Six of Cups", "minor",
             "怀旧、童年记忆、快乐、纯真",
             "活在过去、不愿成长、幼稚"),
            (42, "圣杯七", "Seven of Cups", "minor",
             "选择、幻想、愿望、机会",
             "缺乏选择、困惑、现实检验"),
            (43, "圣杯八", "Eight of Cups", "minor",
             "失望、离开、寻求新事物、情感抽离",
             "害怕离开、停留在不快乐中"),
            (44, "圣杯九", "Nine of Cups", "minor",
             "满足、快乐、愿望实现、享受",
             "不满、缺乏快乐、物质主义"),
            (45, "圣杯十", "Ten of Cups", "minor",
             "和谐、家庭、幸福、情感满足",
             "家庭冲突、缺乏和谐、情感不满"),
            (46, "圣杯侍从", "Page of Cups", "minor",
             "创造力、敏感、直觉、新情感",
             "情感阻塞、缺乏创造力、不敏感"),
            (47, "圣杯骑士", "Knight of Cups", "minor",
             "浪漫、魅力、想象力、情感表达",
             "情绪化、逃避现实、缺乏承诺"),
            (48, "圣杯王后", "Queen of Cups", "minor",
             "直觉、同情心、情感智慧、关怀",
             "情感阻塞、缺乏同情心、不安全感"),
            (49, "圣杯国王", "King of Cups", "minor",
             "情感平衡、智慧、同情心、控制",
             "情绪不稳定、缺乏控制、操纵")
        ]
        
        for card in cups:
            cards.append(TarotCard(*card))
        
        # 小阿卡纳 - 宝剑 (Swords - 风元素)
        swords = [
            (50, "宝剑王牌", "Ace of Swords", "minor",
             "清晰、突破、新想法、心理敏锐",
             "困惑、思维阻塞、缺乏清晰"),
            (51, "宝剑二", "Two of Swords", "minor",
             "决策困难、僵局、避免选择、平衡",
             "冲动、失衡、决策过快"),
            (52, "宝剑三", "Three of Swords", "minor",
             "心碎、情感痛苦、悲伤、背叛",
             "治愈、放下、从痛苦中恢复"),
            (53, "宝剑四", "Four of Swords", "minor",
             "休息、恢复、沉思、准备",
             "紧张、缺乏休息、焦虑"),
            (54, "宝剑五", "Five of Swords", "minor",
             "冲突、竞争、失败、空胜利",
             "避免冲突、妥协、和平"),
            (55, "宝剑六", "Six of Swords", "minor",
             "过渡、改变、从痛苦中恢复、前行",
             "停滞、不愿改变、被困"),
            (56, "宝剑七", "Seven of Swords", "minor",
             "欺骗、策略、回避、欺骗",
             "诚实、直率、面对真相"),
            (57, "宝剑八", "Eight of Swords", "minor",
             "束缚、自我限制、受害者心态、恐惧",
             "解放、突破、克服恐惧"),
            (58, "宝剑九", "Nine of Swords", "minor",
             "焦虑、担忧、恐惧、噩梦",
             "释放焦虑、找到平静、克服恐惧"),
            (59, "宝剑十", "Ten of Swords", "minor",
             "痛苦结束、转变、重生、最低点",
             "拒绝结束、持续的痛苦、恐惧变化"),
            (60, "宝剑侍从", "Page of Swords", "minor",
             "好奇心、新想法、沟通、监视",
             "缺乏好奇心、沟通不畅、缺乏监视"),
            (61, "宝剑骑士", "Knight of Swords", "minor",
             "行动、雄心、驱动力、冲动",
             "缺乏方向、鲁莽、缺乏驱动力"),
            (62, "宝剑王后", "Queen of Swords", "minor",
             "独立、直接、诚实的沟通、边界",
             "情绪化、缺乏边界、缺乏直接"),
            (63, "宝剑国王", "King of Swords", "minor",
             "智力、权威、清晰、客观思维",
             "情感化、缺乏权威、混乱的思维")
        ]
        
        for card in swords:
            cards.append(TarotCard(*card))
        
        # 小阿卡纳 - 星币 (Pentacles - 土元素)
        pentacles = [
            (64, "星币王牌", "Ace of Pentacles", "minor",
             "新的机会、繁荣、物质财富、稳定",
             "错失机会、缺乏繁荣、不稳定"),
            (65, "星币二", "Two of Pentacles", "minor",
             "平衡、适应、时间管理、优先级",
             "失衡、缺乏适应、不良的时间管理"),
            (66, "星币三", "Three of Pentacles", "minor",
             "团队合作、协作、技能、工作",
             "缺乏团队合作、缺乏协作、工作差"),
            (67, "星币四", "Four of Pentacles", "minor",
             "稳定、安全、控制、保守",
             "贪婪、缺乏控制、不稳定"),
            (68, "星币五", "Five of Pentacles", "minor",
             "经济困难、贫困、缺乏、挣扎",
             "财务恢复、富足、摆脱挣扎"),
            (69, "星币六", "Six of Pentacles", "minor",
             "慷慨、慈善、分享、财富",
             "贪婪、自私、缺乏分享"),
            (70, "星币七", "Seven of Pentacles", "minor",
             "耐心、投资、长期视角、耐心等待",
             "不耐烦、缺乏长期愿景、匆忙"),
            (71, "星币八", "Eight of Pentacles", "minor",
             "工匠精神、技能、勤奋、奉献",
             "缺乏技能、懒惰、缺乏奉献"),
            (72, "星币九", "Nine of Pentacles", "minor",
             "富足、奢华、自给自足、财务独立",
             "缺乏富足、过度依赖、财务不稳定"),
            (73, "星币十", "Ten of Pentacles", "minor",
             "财富、家庭遗产、长期成功、稳定",
             "缺乏财富、家庭问题、缺乏成功"),
            (74, "星币侍从", "Page of Pentacles", "minor",
             "学习、勤奋、实用、抱负",
             "缺乏学习、懒惰、不切实际"),
            (75, "星币骑士", "Knight of Pentacles", "minor",
             "勤奋、常规、保守、可靠",
             "懒惰、缺乏常规、不可靠"),
            (76, "星币王后", "Queen of Pentacles", "minor",
             "养育、务实、慷慨、关怀",
             "缺乏养育、不切实际、自私"),
            (77, "星币国王", "King of Pentacles", "minor",
             "财富、商业、领导力、稳定",
             "缺乏财富、商业失败、不稳定")
        ]
        
        for card in pentacles:
            cards.append(TarotCard(*card))
        
        return cards