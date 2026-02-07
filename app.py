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
        interpretation['overall_guidance'] = f"您抽到的「{cards[0]['card']['name']}」（{status_text}）给您带来了重要的指引。{cards[0]['card']['meaning']}请根据这张牌的含义来指导您的下一步行动。"
    elif spread_type == 'three':
        position_names = ['过去', '现在', '未来']
        past_card = cards[0]
        present_card = cards[1]
        future_card = cards[2]
        
        interpretation['summary'] = '这三张牌呈现了过去、现在和未来的发展脉络。'
        interpretation['overall_guidance'] = f"""从过去到现在，您经历了「{past_card['card']['name']}」（{'逆位' if past_card['is_reversed'] else '正位'}）的影响，它代表着{past_card['card']['meaning']}。
当前您正处在「{present_card['card']['name']}」（{'逆位' if present_card['is_reversed'] else '正位'}）的时期，{present_card['card']['meaning']}。
根据当前的轨迹，未来可能出现「{future_card['card']['name']}」（{'逆位' if future_card['is_reversed'] else '正位'}）的局面，{future_card['card']['meaning']}。
建议您结合这三张牌的指引，积极调整自己的态度和行动，朝着理想的方向前进。"""
    elif spread_type == 'love':
        position_names = ['现状', '感受', '挑战', '建议', '结果']
        status_card = cards[0]
        feeling_card = cards[1]
        challenge_card = cards[2]
        advice_card = cards[3]
        outcome_card = cards[4]
        
        interpretation['summary'] = '这五张牌揭示了您爱情状况的完整图景。'
        interpretation['overall_guidance'] = f"""您的爱情现状由「{status_card['card']['name']}」（{'逆位' if status_card['is_reversed'] else '正位'}）所代表，{status_card['card']['meaning']}。
您内心的真实感受是「{feeling_card['card']['name']}」（{'逆位' if feeling_card['is_reversed'] else '正位'}），{feeling_card['card']['meaning']}。
目前面临的挑战是「{challenge_card['card']['name']}」（{'逆位' if challenge_card['is_reversed'] else '正位'}），{challenge_card['card']['meaning']}。
塔罗牌给出的建议是「{advice_card['card']['name']}」（{'逆位' if advice_card['is_reversed'] else '正位'}），{advice_card['card']['meaning']}。
如果按照这个方向发展，可能的结果是「{outcome_card['card']['name']}」（{'逆位' if outcome_card['is_reversed'] else '正位'}），{outcome_card['card']['meaning']}。
请记住，塔罗牌的指引可以帮助您更好地理解自己的感情，但最终的选择权在您手中。"""
    
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
        'interpretation': f"在{position_name}的位置上，「{card['name']}」（{'逆位' if is_reversed else '正位'}）{card['meaning']}"
    }

@app.route('/api/spread/<spread_type>')
def get_spread(spread_type):
    """获取指定牌阵的解读"""
    return jsonify({'spread_type': spread_type})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    app.run(debug=debug, host='0.0.0.0', port=port)