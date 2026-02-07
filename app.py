from flask import Flask, render_template, jsonify, request
from tarot_cards import TarotDeck
import random
import os

app = Flask(__name__)

# 初始化塔罗牌组
deck = TarotDeck()

@app.route('/')
def index():
    """首页"""
    return render_template('index.html')

@app.route('/api/deck')
def get_deck():
    """获取所有塔罗牌信息"""
    cards = []
    for card in deck.cards:
        cards.append({
            'id': card.id,
            'name': card.name,
            'name_en': card.name_en,
            'type': card.type,
            'meaning_upright': card.meaning_upright,
            'meaning_reversed': card.meaning_reversed,
            'image_path': card.image_path
        })
    return jsonify({'cards': cards, 'total': len(cards)})

@app.route('/api/draw', methods=['POST'])
def draw_cards():
    """随机抽取塔罗牌并提供解读"""
    data = request.get_json()
    count = data.get('count', 1)
    spread_type = data.get('spread_type', 'single')
    count = min(max(count, 1), 78)  # 限制在1-78张之间
    
    drawn_cards = random.sample(deck.cards, count)
    
    result = []
    for i, card in enumerate(drawn_cards):
        is_reversed = random.choice([True, False])
        meaning = card.meaning_reversed if is_reversed else card.meaning_upright
        result.append({
            'position': i + 1,
            'card': {
                'id': card.id,
                'name': card.name,
                'name_en': card.name_en,
                'type': card.type,
                'image_path': card.image_path,
                'meaning_upright': card.meaning_upright,
                'meaning_reversed': card.meaning_reversed,
                'meaning': meaning
            },
            'is_reversed': is_reversed
        })
    
    # 生成牌阵综合解读
    interpretation = generate_interpretation(result, spread_type)
    
    return jsonify({
        'cards': result,
        'count': len(result),
        'spread_type': spread_type,
        'interpretation': interpretation
    })

def generate_interpretation(cards, spread_type):
    """生成牌阵综合解读"""
    interpretation = {
        'summary': '',
        'detailed': [],
        'overall_guidance': ''
    }
    
    position_names = []
    
    if spread_type == 'single':
        position_names = ['指引']
        interpretation['summary'] = '这张牌代表了您当前的状况或需要关注的重要信息。'
        status_text = '逆位' if cards[0]['is_reversed'] else '正位'
        card_name = cards[0]['card']['name']
        card_meaning = cards[0]['card']['meaning']
        
        interpretation['overall_guidance'] = f"""您抽到的「{card_name}」（{status_text}）给您带来了重要的指引。

【核心含义】
{card_meaning}

【深度解读】
这张牌的出现并非偶然，它反映了您内心深处最真实的想法和感受。{card_name}所代表的力量正在您的生活中发挥作用，{card_meaning}。

【行动建议】
• 保持开放的心态，接受这张牌带来的信息
• 思考这张牌如何与您当前的处境相关联
• 根据牌的指引，调整你的计划和期望
• 相信自己的直觉，它将引导你做出正确的选择

【注意事项】
请记住，塔罗牌的解读不是固定的预言，而是帮助你更好地理解自己的工具。最终的决策权始终在你手中。

{card_meaning}请根据这张牌的含义来指导你的下一步行动。"""
    elif spread_type == 'three':
        position_names = ['过去', '现在', '未来']
        past_card = cards[0]
        present_card = cards[1]
        future_card = cards[2]
        
        interpretation['summary'] = '这三张牌呈现了过去、现在和未来的发展脉络。'
        
        past_status = '逆位' if past_card['is_reversed'] else '正位'
        present_status = '逆位' if present_card['is_reversed'] else '正位'
        future_status = '逆位' if future_card['is_reversed'] else '正位'
        
        interpretation['overall_guidance'] = f"""【三牌阵解读：时间线的流动】

【过去的影响】
从过去到现在，您经历了「{past_card['card']['name']}」（{past_status}）的影响。
它代表着：{past_card['card']['meaning']}
这段经历塑造了您现在的思维模式和行为方式，是理解当前状况的关键。

【当前的处境】
当前您正处在「{present_card['card']['name']}」（{present_status}）的时期。
这张牌显示：{present_card['card']['meaning']}
您现在面临的挑战和机遇都集中体现在这张牌上，它指引着您当下的行动方向。

【未来的趋势】
根据当前的轨迹，未来可能出现「{future_card['card']['name']}」（{future_status}）的局面。
预示着：{future_card['card']['meaning']}
这是基于当前选择和行动可能产生的结果，但未来并非不可改变。

【综合分析】
这三张牌构成了一个完整的时间线故事：
• 过去的经验为您提供了宝贵的教训
• 现在的状况需要您的关注和行动
• 未来的可能性取决于您当下如何应对

【行动建议】
• 回顾过去：从「{past_card['card']['name']}」中吸取经验
• 把握现在：根据「{present_card['card']['name']}」的指引行动
• 面向未来：以「{future_card['card']['name']}」的愿景为目标
• 保持平衡：在时间线的流动中找到自己的节奏

【最终指引】
建议您结合这三张牌的指引，积极调整自己的态度和行动，朝着理想的方向前进。每一步都很重要，每一个选择都会影响最终的结果。"""
    elif spread_type == 'love':
        position_names = ['现状', '感受', '挑战', '建议', '结果']
        status_card = cards[0]
        feeling_card = cards[1]
        challenge_card = cards[2]
        advice_card = cards[3]
        outcome_card = cards[4]
        
        interpretation['summary'] = '这五张牌揭示了您爱情状况的完整图景。'
        
        interpretation['overall_guidance'] = f"""【爱情阵解读：五维情感地图】

【1. 现状分析】
您的爱情现状由「{status_card['card']['name']}」（{'逆位' if status_card['is_reversed'] else '正位'}）所代表。
{status_card['card']['meaning']}
这是您当前感情状态的真实写照，反映了您在感情中遇到的具体情况。

【2. 内心感受】
您内心的真实感受是「{feeling_card['card']['name']}」（{'逆位' if feeling_card['is_reversed'] else '正位'}）。
{feeling_card['card']['meaning']}
这张牌揭示了您在情感层面最真实的需求和渴望，有些感受可能连您自己都未曾察觉。

【3. 面临的挑战】
目前面临的挑战是「{challenge_card['card']['name']}」（{'逆位' if challenge_card['is_reversed'] else '正位'}）。
{challenge_card['card']['meaning']}
这是您在感情道路上需要克服的障碍，正视挑战是解决问题的第一步。

【4. 塔罗建议】
塔罗牌给出的建议是「{advice_card['card']['name']}」（{'逆位' if advice_card['is_reversed'] else '正位'}）。
{advice_card['card']['meaning']}
这是一个来自宇宙的指引，帮助您找到处理感情问题的最佳方式。

【5. 可能的结果】
如果按照这个方向发展，可能的结果是「{outcome_card['card']['name']}」（{'逆位' if outcome_card['is_reversed'] else '正位'}）。
{outcome_card['card']['meaning']}
这是基于当前趋势的预测，提醒您关注行动可能带来的长远影响。

【深度解析】
五张牌形成了一个完整的情感图景：
• 现状让您认清自己在哪里
• 感受让您明白自己要什么
• 挑战让您知道要克服什么
• 建议为您提供行动指南
• 结果让预见可能的方向

【行动指南】
• 面对现实：接受「{status_card['card']['name']}」所示的状态
• 倾听内心：重视「{feeling_card['card']['name']}」表达的感受
• 直面困难：勇敢应对「{challenge_card['card']['name']}」的挑战
• 采纳建议：按照「{advice_card['card']['name']}」的指引行动
• 展望未来：以「{outcome_card['card']['name']}」的愿景为目标

【最终提醒】
请记住，塔罗牌的指引可以帮助您更好地理解自己的感情，但最终的选择权在您手中。真正的幸福来自于自己的选择和行动，相信你的心，它会指引你走向正确的方向。"""
    
    # 为每张牌生成详细解读
    for i, card_data in enumerate(cards):
        position_name = position_names[i] if i < len(position_names) else f'第{i+1}张'
        position_interpretation = generate_position_interpretation(card_data, position_name)
        interpretation['detailed'].append(position_interpretation)
    
    return interpretation

def generate_position_interpretation(card_data, position_name):
    """生成单个位置的解读"""
    card = card_data['card']
    is_reversed = card_data['is_reversed']
    
    return {
        'position': position_name,
        'card_name': card['name'],
        'is_reversed': is_reversed,
        'interpretation': f"""【{position_name}位置解读】

在{position_name}的位置上，「{card['name']}」（{'逆位' if is_reversed else '正位'}）带来了重要的信息。

【牌面含义】
{card['meaning']}

【位置解读】
这张牌出现在{position_name}的位置，特别强调了{'阻碍' if is_reversed else '支持'}的方面。{'逆位表示能量的阻滞或内在阻力，需要你深入思考其中的原因。' if is_reversed else '正位显示能量流动顺畅，这是一个积极的信号。'}

【实践建议】
• 关注这张牌在{position_name}层面给出的具体指引
• {'调整心态，克服内心的障碍' if is_reversed else '保持当前积极的状态'}
• 将牌的智慧应用到实际的{position_name}情境中
• 相信这张牌会帮助你在{position_name}方面做出正确的决定

【核心信息】
{card['meaning']}这是宇宙在{position_name}方面给你的重要提醒，请用心体会。"""
    }

@app.route('/api/spread/<spread_type>')
def get_spread(spread_type):
    """获取指定牌阵的解读"""
    return jsonify({'spread_type': spread_type})

@app.route('/api/ask', methods=['POST'])
def ask_question():
    """根据抽牌结果回答用户问题"""
    data = request.get_json()
    
    cards = data.get('cards', [])
    interpretation = data.get('interpretation', {})
    question = data.get('question', '')
    
    # 构建上下文信息
    context_parts = []
    
    # 添加牌面信息
    card_info = []
    for card in cards:
        status = '逆位' if card['is_reversed'] else '正位'
        card_info.append(f"- {card['card']['name']}（{status}）：{card['card']['meaning']}")
    
    context_parts.append("抽牌结果：")
    context_parts.extend(card_info)
    
    # 添加解读信息
    if interpretation.get('overall_guidance'):
        context_parts.append("\n综合解读：")
        context_parts.append(interpretation['overall_guidance'])
    
    # 添加用户问题
    context_parts.append(f"\n用户问题：{question}")
    
    context = "\n".join(context_parts)
    
    # 生成回答（这里使用预设的回答模板，实际可以接入大模型API）
    answer = generate_ai_answer(question, cards, interpretation)
    
    return jsonify({
        'answer': answer,
        'question': question
    })

def generate_ai_answer(question, cards, interpretation):
    """生成AI回答（模拟大模型回复）"""
    # 获取第一张牌的信息作为参考
    if cards:
        first_card = cards[0]
        card_name = first_card['card']['name']
        card_meaning = first_card['card']['meaning']
        status = '逆位' if first_card['is_reversed'] else '正位'
        
        # 根据问题类型生成不同的回答
        if '建议' in question or '怎么办' in question:
            return f"根据「{card_name}」（{status}）的指引，{card_meaning}。\n\n具体建议：\n1. 深入思考当前的状况，不要急于做决定\n2. 关注牌面所强调的核心意义\n3. 结合实际情况灵活运用牌的指引\n4. 保持开放的心态，接受可能的变化\n\n记住，塔罗牌提供的是参考和启发，最终的决定权在你手中。"
        
        elif '感情' in question or '爱情' in question:
            return f"在感情方面，「{card_name}」（{status}）提示你{card_meaning}。\n\n这暗示着：\n- 需要更加关注自己的内心感受\n- 沟通和理解是关系的关键\n- 保持真诚和耐心\n- 相信自己的直觉\n\n建议你与伴侣坦诚交流，共同面对挑战。"
        
        elif '事业' in question or '工作' in question:
            return f"在事业上，「{card_name}」（{status}）预示着{card_meaning}。\n\n这提醒你：\n- 把握当前的机会\n- 保持专注和决心\n- 勇于面对挑战\n- 学会从经验中成长\n\n相信自己的能力，坚持下去会看到成果。"
        
        else:
            return f"关于你问到的问题，「{card_name}」（{status}）的深层含义是{card_meaning}。\n\n这张牌提醒你：\n- 相信自己的直觉和判断\n- 保持积极乐观的心态\n- 从挑战中寻找成长的机会\n- 与信任的人分享你的想法\n\n塔罗牌的指引是帮助你更好地理解当前状况，请结合实际情况来参考这些建议。"
    
    return "请先抽牌，然后我才能根据牌面信息回答你的问题。"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    app.run(debug=debug, host='0.0.0.0', port=port)