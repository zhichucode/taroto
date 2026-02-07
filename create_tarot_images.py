"""
为每张塔罗牌生成精美的SVG图片
"""

def get_card_design(card_id, name, name_en, card_type):
    """获取每张牌的设计元素"""
    
    # 大阿卡纳配色和图案
    major_arcana_designs = {
        0: {'colors': ['#FFD700', '#FFA500', '#FF6347'], 'symbol': '⭐', 'bg': '#1a1a2e'},
        1: {'colors': ['#FF00FF', '#9400D3', '#8B008B'], 'symbol': '🎭', 'bg': '#16213e'},
        2: {'colors': ['#00CED1', '#008B8B', '#20B2AA'], 'symbol': '🌙', 'bg': '#0f3460'},
        3: {'colors': ['#FF69B4', '#FF1493', '#C71585'], 'symbol': '👑', 'bg': '#1a0a2e'},
        4: {'colors': ['#DC143C', '#B22222', '#8B0000'], 'symbol': '⚔️', 'bg': '#2d0a0a'},
        5: {'colors': ['#FFA500', '#FF8C00', '#FF4500'], 'symbol': '📿', 'bg': '#1a0f00'},
        6: {'colors': ['#FF69B4', '#FF1493', '#FFB6C1'], 'symbol': '💕', 'bg': '#2a0a1a'},
        7: {'colors': ['#FFD700', '#FFA500', '#FF8C00'], 'symbol': '🏆', 'bg': '#1a1500'},
        8: {'colors': ['#FF4500', '#FF6347', '#DC143C'], 'symbol': '🦁', 'bg': '#2a0a0a'},
        9: {'colors': ['#9370DB', '#8A2BE2', '#9932CC'], 'symbol': '🔦', 'bg': '#0a0a2a'},
        10: {'colors': ['#00CED1', '#40E0D0', '#48D1CC'], 'symbol': '🎡', 'bg': '#001a2a'},
        11: {'colors': ['#4169E1', '#0000FF', '#000080'], 'symbol': '⚖️', 'bg': '#0a0a1a'},
        12: {'colors': ['#9370DB', '#8A2BE2', '#BA55D3'], 'symbol': '🙃', 'bg': '#1a0a2a'},
        13: {'colors': ['#2F4F4F', '#696969', '#808080'], 'symbol': '💀', 'bg': '#0a0a0a'},
        14: {'colors': ['#3CB371', '#2E8B57', '#228B22'], 'symbol': '🏺', 'bg': '#0a1a0a'},
        15: {'colors': ['#8B0000', '#A52A2A', '#B22222'], 'symbol': '😈', 'bg': '#1a0505'},
        16: {'colors': ['#FF4500', '#FF6347', '#DC143C'], 'symbol': '🗼', 'bg': '#2a0505'},
        17: {'colors': ['#87CEEB', '#00BFFF', '#1E90FF'], 'symbol': '⭐', 'bg': '#0a1020'},
        18: {'colors': ['#9370DB', '#8A2BE2', '#9932CC'], 'symbol': '🌕', 'bg': '#0a051a'},
        19: {'colors': ['#FFD700', '#FFA500', '#FF8C00'], 'symbol': '☀️', 'bg': '#1a1500'},
        20: {'colors': ['#FFD700', '#FFA500', '#FF8C00'], 'symbol': '📯', 'bg': '#1a1000'},
        21: {'colors': ['#00CED1', '#40E0D0', '#20B2AA'], 'symbol': '🌍', 'bg': '#00151a'},
    }
    
    # 权杖（火元素）
    wands_colors = ['#FF4500', '#FF6347', '#FFA500', '#FF8C00']
    # 圣杯（水元素）
    cups_colors = ['#1E90FF', '#00BFFF', '#87CEEB', '#40E0D0']
    # 宝剑（风元素）
    swords_colors = ['#9370DB', '#8A2BE2', '#9932CC', '#BA55D3']
    # 星币（土元素）
    pentacles_colors = ['#228B22', '#32CD32', '#3CB371', '#00FA9A']
    
    if card_type == 'major':
        design = major_arcana_designs.get(card_id, major_arcana_designs[0])
    else:
        # 小阿卡纳
        if 22 <= card_id <= 35:
            colors = wands_colors
            bg = '#1a0a00'
            suit = '🔥'
        elif 36 <= card_id <= 49:
            colors = cups_colors
            bg = '#000a1a'
            suit = '💧'
        elif 50 <= card_id <= 63:
            colors = swords_colors
            bg = '#0a0a1a'
            suit = '🗡️'
        else:
            colors = pentacles_colors
            bg = '#0a1a0a'
            suit = '💰'
        
        rank = (card_id - 22) % 14
        if rank < 10:
            symbol = f'{suit}{rank + 1}'
        else:
            court_symbols = ['🥇', '🥈', '🥉', '👤']
            symbol = f'{suit}{court_symbols[rank - 10]}'
        
        design = {
            'colors': colors,
            'symbol': symbol,
            'bg': bg
        }
    
    return design

def create_tarot_svg(card_id, name, name_en, card_type):
    """创建塔罗牌SVG"""
    
    design = get_card_design(card_id, name, name_en, card_type)
    colors = design['colors']
    symbol = design['symbol']
    bg_color = design['bg']
    
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="280" height="420" viewBox="0 0 280 420" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="bg{card_id}" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:{bg_color};stop-opacity:1" />
            <stop offset="50%" style="stop-color:{colors[0]};stop-opacity:0.3" />
            <stop offset="100%" style="stop-color:{bg_color};stop-opacity:1" />
        </linearGradient>
        
        <linearGradient id="border{card_id}" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:{colors[0]};stop-opacity:1" />
            <stop offset="50%" style="stop-color:{colors[1]};stop-opacity:1" />
            <stop offset="100%" style="stop-color:{colors[2]};stop-opacity:1" />
        </linearGradient>
        
        <linearGradient id="accent{card_id}" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:{colors[0]};stop-opacity:0.4" />
            <stop offset="100%" style="stop-color:{colors[1]};stop-opacity:0.1" />
        </linearGradient>
        
        <filter id="glow{card_id}">
            <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
        
        <filter id="shadow{card_id}">
            <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="{colors[0]}" flood-opacity="0.3"/>
        </filter>
    </defs>
    
    <!-- 背景 -->
    <rect width="280" height="420" fill="url(#bg{card_id})" rx="20" ry="20"/>
    
    <!-- 边框 -->
    <rect x="8" y="8" width="264" height="404" fill="none" stroke="url(#border{card_id})" stroke-width="3" rx="16" ry="16"/>
    
    <!-- 内框装饰 -->
    <rect x="16" y="16" width="248" height="388" fill="url(#accent{card_id})" rx="12" ry="12" filter="url(#shadow{card_id})"/>
    
    <!-- 角落装饰 -->
    <circle cx="30" cy="30" r="8" fill="{colors[0]}" opacity="0.6"/>
    <circle cx="250" cy="30" r="8" fill="{colors[0]}" opacity="0.6"/>
    <circle cx="30" cy="390" r="8" fill="{colors[0]}" opacity="0.6"/>
    <circle cx="250" cy="390" r="8" fill="{colors[0]}" opacity="0.6"/>
    
    <!-- 中心符号 -->
    <text x="140" y="200" font-size="70" text-anchor="middle" dominant-baseline="middle" filter="url(#glow{card_id})">{symbol}</text>
    
    <!-- 牌名背景 -->
    <rect x="30" y="290" width="220" height="80" fill="{bg_color}" rx="10" ry="10" opacity="0.8"/>
    
    <!-- 牌名（中文） -->
    <text x="140" y="330" font-size="22" font-weight="bold" fill="white" text-anchor="middle" font-family="Arial, sans-serif" filter="url(#glow{card_id})">{name}</text>
    
    <!-- 牌名（英文） -->
    <text x="140" y="355" font-size="13" fill="{colors[0]}" text-anchor="middle" font-family="Arial, sans-serif" font-weight="600">{name_en}</text>
    
    <!-- 装饰线条 -->
    <line x1="40" y1="280" x2="240" y2="280" stroke="{colors[0]}" stroke-width="2" opacity="0.5"/>
    <line x1="40" y1="370" x2="240" y2="370" stroke="{colors[0]}" stroke-width="2" opacity="0.5"/>
</svg>'''
    
    return svg

# 生成所有78张牌的SVG文件
if __name__ == '__main__':
    from tarot_cards import TarotDeck
    
    deck = TarotDeck()
    cards_dir = '/Users/hoppe/Documents/Codes/taroto/static/images/cards'
    
    import os
    os.makedirs(cards_dir, exist_ok=True)
    
    for card in deck.cards:
        svg_content = create_tarot_svg(card.id, card.name, card.name_en, card.type)
        filename = f"{card.id:02d}.svg"
        filepath = f"{cards_dir}/{filename}"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        
        print(f"✓ 已生成: {filename} - {card.name}")
    
    print(f"\n🎨 所有78张塔罗牌SVG图片已生成完成！")