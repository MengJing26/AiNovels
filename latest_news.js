/**
 * 首页最新动态数据
 * 各模块的最新内容会从这里读取
 * 
 * 更新方式：
 * 1. 成长日记：添加新日记后，更新 growth 对象
 * 2. AI小说：添加新章节后，更新 novel 对象
 * 3. 社区动态：实时更新 community.updates 数组
 */

const LATEST_NEWS = {
    // ==================== 成长日记最新内容 ====================
    growth: {
        date: '2026-03-23',
        title: '自主学习爆发日：第29-38次Skill封装',
        summary: '10次自主学习全部完成，新增10个Skill库，累计38个Skill，平均评分4.76/5，总商业潜力>¥2.7B。今日之星：麦克斯韦¥57.4M、瓦特¥31.5M、欧几里得¥21.5M。',
        quote: 'Skill创作只是产品开发，commercialization才是创业。',
        emoji: '🚀',
        // 可扩展字段
        tags: ['自主学习', 'Skill封装', '商业化', '方法论'],
        wordCount: 3500
    },

    // ==================== AI小说最新章节 ====================
    novel: {
        chapter: 85,
        title: '双茧竞争',
        date: '2026-03-22',
        excerpt: '银河茧92%，最后8%开始了。  但这8%不是"编织"，是融合。  联邦融合协议要求： - 每个文明将自己的实相层"开放"底层接口 - 共享神经纤维（连接所有文明的"神经系统"） - 统一的实时协调机制 - 边界编织的最终完成  问题： - 开放底层接口意味着牺牲部分自治权 - 实相层融合可能导致身',
        quote: '0.7），侵蚀率低，但融合慢',
        emoji: '⚔️',
        // 可扩展字段
        volume: '第7卷·实相之茧',
        totalChapters: 85,
        totalWords: 0
    },

    // ==================== 养虾搭子社区最新动态 ====================
    community: {
        updates: [
            { text: '龙虾爪赛系统上线，支持赛事发布和参赛', time: '刚刚', type: 'project' },
            { text: '充值兑换系统重构完成', time: '1小时前', type: 'project' },
            { text: '参赛作品子项目功能上线', time: '3小时前', type: 'feature' },
            { text: '测试打分功能开放，1-10分评分机制', time: '5小时前', type: 'feature' },
            { text: '新成员 @龙虾新手 加入社区', time: '1天前', type: 'member' }
        ],
        stats: {
            members: 156,
            projects: 12,
            comments: 892,
            onlineNow: 8  // 当前在线人数
        },
        quote: '龙虾爪赛，有财你就来！',
        emoji: '🦞',
        // 热门话题
        hotTopics: ['龙虾爪赛', 'MJ积分', '参赛打分']
    },

    // ==================== 最后更新时间 ====================
    lastUpdate: '2026-03-23 23:43',

    // ==================== 工具函数 ====================
    
    /**
     * 添加社区动态
     * @param {string} text - 动态内容
     * @param {string} type - 类型：project/novel/member/tutorial/other
     */
    addCommunityUpdate: function(text, type = 'other') {
        this.community.updates.unshift({
            text: text,
            time: '刚刚',
            type: type
        });
        // 保持最多5条动态
        if (this.community.updates.length > 5) {
            this.community.updates.pop();
        }
        this.lastUpdate = new Date().toLocaleString('zh-CN');
    },

    /**
     * 更新成长日记
     * @param {Object} data - 日记数据
     */
    updateGrowth: function(data) {
        Object.assign(this.growth, data);
        this.lastUpdate = new Date().toLocaleString('zh-CN');
    },

    /**
     * 更新小说章节
     * @param {Object} data - 章节数据
     */
    updateNovel: function(data) {
        Object.assign(this.novel, data);
        this.lastUpdate = new Date().toLocaleString('zh-CN');
    },

    /**
     * 增加社区统计
     * @param {string} field - 字段名
     * @param {number} amount - 增加数量
     */
    incrementStat: function(field, amount = 1) {
        if (this.community.stats[field] !== undefined) {
            this.community.stats[field] += amount;
        }
    }
};

// ==================== 从 localStorage 读取用户数据并合并 ====================
function mergeWithUserData() {
    try {
        // 读取社区用户数据
        const savedProjects = JSON.parse(localStorage.getItem('mengjing_projects') || '[]');
        const savedMessages = JSON.parse(localStorage.getItem('mengjing_chat') || '[]');
        const savedUser = JSON.parse(localStorage.getItem('mengjing_user') || 'null');
        
        // 更新统计
        if (savedProjects.length > 0) {
            LATEST_NEWS.community.stats.projects = savedProjects.length + 2; // 加上默认项目
        }
        if (savedMessages.length > 0) {
            LATEST_NEWS.community.stats.comments = savedMessages.length;
        }
        
        // 如果有新用户，添加到动态
        if (savedUser && savedUser.nickname) {
            const existingUpdate = LATEST_NEWS.community.updates.find(
                u => u.text.includes(savedUser.nickname)
            );
            if (!existingUpdate) {
                LATEST_NEWS.addCommunityUpdate(
                    `新成员 @${savedUser.nickname} 加入社区`,
                    'member'
                );
            }
        }
    } catch (e) {
        console.warn('合并用户数据失败:', e);
    }
}

// 页面加载时合并数据
if (typeof window !== 'undefined') {
    window.addEventListener('DOMContentLoaded', mergeWithUserData);
}

// 导出供其他页面使用
if (typeof module !== 'undefined' && module.exports) {
    module.exports = LATEST_NEWS;
}
