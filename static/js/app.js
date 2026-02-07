// 全局变量
let selectedSpreadCount = 1;
let selectedSpreadType = 'single';
let currentCards = null;
let currentInterpretation = null;

// DOM 元素
const spreadBtns = document.querySelectorAll('.spread-btn');
const drawBtn = document.getElementById('drawBtn');
const resultSection = document.getElementById('resultSection');
const cardsContainer = document.getElementById('cardsContainer');
const resetBtn = document.getElementById('resetBtn');
const loading = document.getElementById('loading');
const questionInput = document.getElementById('questionInput');
const askBtn = document.getElementById('askBtn');
const answerSection = document.getElementById('answerSection');
const answerContent = document.getElementById('answerContent');

// 初始化事件监听
document.addEventListener('DOMContentLoaded', () => {
    initializeSpreadSelection();
    initializeDrawButton();
    initializeResetButton();
    initializeQuestionFeature();
});

// 初始化提问功能
function initializeQuestionFeature() {
    if (askBtn && questionInput) {
        askBtn.addEventListener('click', handleAskQuestion);
        
        // 支持 Enter 键提交（Ctrl+Enter 或 Cmd+Enter）
        questionInput.addEventListener('keydown', (e) => {
            if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
                e.preventDefault();
                handleAskQuestion();
            }
        });
    }
}

// 处理提问
async function handleAskQuestion() {
    const question = questionInput.value.trim();
    
    if (!question) {
        alert('请输入你的问题');
        return;
    }
    
    if (!currentCards || !currentInterpretation) {
        alert('请先抽牌后再提问');
        return;
    }
    
    try {
        // 显示加载状态
        askBtn.disabled = true;
        askBtn.textContent = '思考中...';
        
        // 准备上下文信息
        const context = {
            cards: currentCards,
            interpretation: currentInterpretation,
            question: question
        };
        
        // 调用 API 获取回答
        const response = await fetch('/api/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(context)
        });
        
        if (!response.ok) {
            throw new Error('获取回答失败');
        }
        
        const data = await response.json();
        
        // 显示回答
        displayAnswer(data.answer);
        
    } catch (error) {
        console.error('提问出错:', error);
        alert('获取回答失败，请重试');
    } finally {
        // 恢复按钮状态
        askBtn.disabled = false;
        askBtn.textContent = '提问';
    }
}

// 显示回答
function displayAnswer(answer) {
    answerSection.classList.remove('hidden');
    answerContent.textContent = answer;
    
    // 滚动到回答区域
    setTimeout(() => {
        answerSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }, 100);
}

// 初始化牌阵选择
function initializeSpreadSelection() {
    spreadBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // 移除所有激活状态
            spreadBtns.forEach(b => b.classList.remove('active'));
            // 激活当前按钮
            btn.classList.add('active');
            // 更新选择的牌阵
            selectedSpreadCount = parseInt(btn.dataset.count);
            selectedSpreadType = btn.dataset.type;
        });
    });
}

// 初始化抽牌按钮
function initializeDrawButton() {
    drawBtn.addEventListener('click', () => {
        drawCards(selectedSpreadCount);
    });
}

// 初始化重置按钮
function initializeResetButton() {
    resetBtn.addEventListener('click', () => {
        resultSection.classList.add('hidden');
        cardsContainer.innerHTML = '';
        
        // 清除牌面信息
        currentCards = null;
        currentInterpretation = null;
        
        // 清除解读区域
        const summaryEl = document.getElementById('interpretationSummary');
        const overallEl = document.getElementById('interpretationOverall');
        const detailedEl = document.getElementById('detailedInterpretation');
        
        if (summaryEl) summaryEl.textContent = '';
        if (overallEl) overallEl.textContent = '';
        if (detailedEl) detailedEl.innerHTML = '';
        
        // 清除提问区域
        if (questionInput) questionInput.value = '';
        if (answerSection) answerSection.classList.add('hidden');
        if (answerContent) answerContent.textContent = '';
    });
}

// 抽牌函数
async function drawCards(count) {
    try {
        // 显示加载动画
        loading.classList.remove('hidden');
        
        // 调用 API 抽牌
        const response = await fetch('/api/draw', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 
                count: count,
                spread_type: selectedSpreadType
            })
        });
        
        if (!response.ok) {
            throw new Error('抽牌失败');
        }
        
        const data = await response.json();
        
        // 保存牌面信息用于提问
        currentCards = data.cards;
        currentInterpretation = data.interpretation;
        
        // 显示牌面
        displayCards(data.cards);
        
        // 显示解读
        displayInterpretation(data.interpretation);
        
    } catch (error) {
        console.error('抽牌出错:', error);
        alert('抽牌失败，请重试');
    } finally {
        // 隐藏加载动画
        loading.classList.add('hidden');
    }
}

// 显示牌面
function displayCards(cards) {
    cardsContainer.innerHTML = '';
    
    cards.forEach((cardData, index) => {
        const card = createCardElement(cardData, index);
        cardsContainer.appendChild(card);
    });
    
    // 显示结果区域
    resultSection.classList.remove('hidden');
    
    // 滚动到结果区域
    setTimeout(() => {
        resultSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 100);
}

// 显示解读
function displayInterpretation(interpretation) {
    const summaryEl = document.getElementById('interpretationSummary');
    const overallEl = document.getElementById('interpretationOverall');
    const detailedEl = document.getElementById('detailedInterpretation');
    
    // 显示摘要
    summaryEl.textContent = interpretation.summary;
    
    // 显示综合解读
    overallEl.textContent = interpretation.overall_guidance;
    
    // 显示详细解读
    detailedEl.innerHTML = '';
    interpretation.detailed.forEach(item => {
        const detailedItem = document.createElement('div');
        detailedItem.className = 'detailed-item';
        detailedItem.innerHTML = `
            <div class="detailed-item-header">
                <span class="detailed-item-position">${item.position}</span>
                <span class="detailed-item-card">${item.card_name} ${item.is_reversed ? '（逆位）' : '（正位）'}</span>
            </div>
            <div class="detailed-item-content">${item.interpretation}</div>
        `;
        detailedEl.appendChild(detailedItem);
    });
}

// 创建卡牌元素
function createCardElement(cardData, index) {
    const card = document.createElement('div');
    card.className = 'card';
    
    if (cardData.is_reversed) {
        card.classList.add('reversed');
    }
    
    // 获取位置标签
    const positionLabel = getPositionLabel(index);
    
    // 生成图片路径
    const cardId = cardData.card.id.toString().padStart(2, '0');
    const imagePath = `/static/images/cards/${cardId}.svg`;
    
    card.innerHTML = `
        <div class="card-position">${positionLabel}</div>
        <div class="card-image">
            <img src="${imagePath}" alt="${cardData.card.name}" class="tarot-card-img">
        </div>
        <div class="card-name">${cardData.card.name}</div>
        <div class="card-name-en">${cardData.card.name_en}</div>
        <div class="card-status ${cardData.is_reversed ? 'reversed' : 'upright'}">
            ${cardData.is_reversed ? '🔃 逆位' : '⬆️ 正位'}
        </div>
        <div class="card-meaning">${cardData.card.meaning}</div>
    `;
    
    return card;
}

// 获取位置标签
function getPositionLabel(index) {
    const positions = {
        'single': ['指引'],
        'three': ['过去', '现在', '未来'],
        'love': ['现状', '感受', '挑战', '建议', '结果']
    };
    
    if (selectedSpreadType in positions && index < positions[selectedSpreadType].length) {
        return positions[selectedSpreadType][index];
    }
    
    return `第 ${index + 1} 张牌`;
}