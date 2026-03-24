#!/usr/bin/env python3
"""
Churchill Crisis Speech Engine
模块化危机讲话生成器
"""

import json
from typing import Dict, List, Optional


class ChurchillSpeechTemplate:
    """Churchill 式讲话模板"""
    
    # Churchill 经典讲话结构
    STRUCTURE = {
        "opening": {
            "length": "1-2句话",
            "purpose": "直接切入危机现实，不回避",
            "example": "各位同胞，我们正面临国家历史上最黑暗的时刻。"
        },
        "reality": {
            "length": "1段",
            "purpose": "客观描述危机现状，用数据/事实",
            "example": "纳粹德国已经占领了法国，不列颠之战随时可能开始。我们的空军损失惨重，物资短缺，但我们依然屹立。"
        },
        "historical_reference": {
            "length": "1段",
            "purpose": "引用历史先例，证明困境可克服",
            "example": "回想1940年5月，敦刻尔克撤退后我们失去了所有的重型装备。但我们没有投降，而是在丘吉尔首相的领导下重新组织防御。"
        },
        "irony": {
            "length": "1-2句",
            "purpose": "用反讽解构对手/困难，削弱其气势",
            "example": "希特勒以为我们会在强大的攻势下屈服，但他不知道英国人的品格是什么。"
        },
        "spirit_call": {
            "length": "1段",
            "purpose": "唤醒集体精神品质，赋予意义",
            "example": "正是这种永不屈服的精神，让我们在历史上无数次击败外敌。现在，轮到我们再次证明这一点。"
        },
        "vision": {
            "length": "1-2段",
            "purpose": "描绘胜利后的世界，激励人心",
            "example": "我相信，当我们最终胜利，我们将建立一个更自由、更和平的世界。我们的孩子将在没有恐惧的环境中成长。"
        },
        "closing": {
            "length": "1-2句",
            "purpose": "坚定决心，以战斗口号结束",
            "example": "因此，各位同胞，我号召你们：让我们携手战斗到底！我们将在任何地方战斗：海滩、登陆场、田野、街道、山地。我们绝不投降！"
        }
    }
    
    # Churchill 常用修辞手法
    RHETORIC = {
        "parallelism": "排比：'我们将在海滩上战斗，我们将在登陆场战斗...'",
        "antithesis": "对比：'成功不是最终的，失败不是致命的'",
        "alliteration": "头韵：'We shall fight on the beaches'",
        "anaphora": "反复：'我们将在...'重复",
        "metaphor": "隐喻：'黑暗时刻'、'风暴'、'黎明'",
        "irony": "反讽：'希特勒以为...但我们...'",
        "tricolon": "三连：'我们将在任何地方战斗：在X，在Y，在Z'"
    }
    
    # Churchill 经典讲话案例
    CLASSIC_SPEECHES = {
        "1940-06-04": {
            "title": "我们将战斗 Victory 演讲",
            "core_quote": "We shall fight on the beaches, we shall fight on the landing grounds, we shall fight in the fields and in the streets, we shall fight in the hills; we shall never surrender",
            "structure": ["现实描述", "敦刻尔克撤退", "战斗决心", "胜利愿景"],
            "context": "敦刻尔克大撤退后，法国即将投降，英国孤立无援"
        },
        "1940-06-18": {
            "title": "这将是他们最光辉的时刻",
            "core_quote": "This was their finest hour",
            "structure": ["历史回顾", "敌人分析", "英国精神", "必胜信念"],
            "context": "法国投降前一天，Battle of Britain即将开始"
        },
        "1941-12-08": {
            "title": "珍珠港后宣战演讲",
            "core_quote": "We have at least four-fifths of the population of the globe with us",
            "structure": ["事件陈述", "道德立场", "联盟力量", "最终胜利"],
            "context": "日本偷袭珍珠港后，美国参战"
        }
    }


class CrisisSpeechGenerator(ChurchillSpeechTemplate):
    """危机讲话生成器"""
    
    def __init__(self, language="zh-CN"):
        self.language = language
        self.templates = self._load_templates()
    
    def _load_templates(self):
        """加载讲话模板"""
        return {
            "product_failure": {
                "reality": "我们的核心产品遭遇重大挫折，用户流失率达到{流失率}，市场份额被竞争对手侵蚀。",
                "historical": "回想{公司历史}，我们也曾面临类似困境，但通过{应对措施}重新崛起。",
                "irony": "那些认为{竞争对手}已经赢了他们的人，低估了我们的韧性和创新能力。",
                "spirit": "我们公司的文化核心是{公司价值观}，这种精神让我们在每次危机中变得更强大。",
                "vision": "我将带领大家推出一款颠覆性产品，不仅挽回市场份额，更要重新定义行业标准。"
            },
            "financial_crisis": {
                "reality": "公司现金流紧张，可能面临{具体问题}，我们需要立即采取行动。",
                "historical": "2008年金融危机时，许多公司选择了缩减，但我们选择了投入研发，结果是我们的市场份额翻倍。",
                "irony": "经济下行或许会淘汰弱者，但也会给真正的创新者机会，而我们要成为后者。",
                "spirit": "正是我们{公司特质}，让我们在每次周期性危机中找到新机会。",
                "vision": "通过本轮的危机应对，我们将建立行业中最健康的财务报表结构，赢得未来十年的竞争优势。"
            },
            "pr_disaster": {
                "reality": "我们遇到了严重的公关危机，{具体事件}已经造成了广泛的负面舆论。",
                "historical": "2010年BP墨西哥湾漏油事件后，他们通过彻底改革安全流程重建了信任。",
                "irony": "那些在社交媒体上批评我们的人，如果没有我们的{产品/服务}，他们的生活会更好吗？",
                "spirit": "透明度、责任感、对错误的快速纠正，是我们企业的DNA。",
                "vision": "危机过后，我们将成为行业中最透明、最受信赖的品牌，这次危机将成为我们文化转型的转折点。"
            }
        }
    
    def generate(self, crisis_type: str, **params) -> Dict:
        """生成危机讲话
        
        Args:
            crisis_type: 危机类型（product_failure/financial_crisis/pr_disaster）
            **params: 填充模板的参数
            
        Returns:
            Dict: 包含完整讲话和结构化分析
        """
        if crisis_type not in self.templates:
            return {"error": f"暂不支持{crisis_type}类型，支持: {list(self.templates.keys())}"}
        
        template = self.templates[crisis_type]
        
        # 填充模板
        speech_parts = {
            "opening": f"各位{params.get('audience', '同事')}：",
            "reality": template["reality"].format(**params),
            "historical": template["historical"].format(**params),
            "irony": template["irony"].format(**params),
            "spirit": template["spirit"].format(**params),
            "vision": template["vision"].format(**params),
            "closing": " Churchill 说：'成功不是最终的，失败不是致命的：重要的是继续前进的勇气。'\n\n我们将战斗到底！我们绝不放弃！",
        }
        
        full_speech = "\n\n".join(speech_parts.values())
        
        # 修辞分析
        rhetoric_used = self._analyze_rhetoric(full_speech)
        
        return {
            "crisis_type": crisis_type,
            "audience": params.get("audience", "团队"),
            "speech": full_speech,
            "structure": speech_parts,
            "rhetoric_analysis": rhetoric_used,
            "churchill_score": self._score_churchilliness(full_speech),
            "delivery_tips": [
                "语速放慢，关键句停顿",
                "说到'战斗'时握拳，语气坚定",
                "说到'愿景'时眼神望向远方，语气充满希望",
                "最后一句'绝不惜弃'用尽全力，力量饱满"
            ]
        }
    
    def _analyze_rhetoric(self, text: str) -> List[str]:
        """分析修辞手法使用"""
        used = []
        if "我们将在" in text and ("战斗" in text or "努力" in text):
            used.append("parallelism-排比")
        if ("不是" in text and "不是" in text) or ("成功" in text and "失败" in text):
            used.append("antithesis-对比")
        if "以为" in text and ("但" in text or "却" in text):
            used.append("irony-反讽")
        if text.count("我们") > 10:
            used.append("anaphora-反复")
        return used
    
    def _score_churchilliness(self, text: str) -> Dict:
        """Churchill 风格评分（0-100）"""
        score = 0
        reasons = []
        
        # 长度适中（Churchill 讲话通常15-20分钟）
        word_count = len(text)
        if 300 <= word_count <= 1000:
            score += 20
            reasons.append("讲话长度 Churchill 化")
        
        # 包含现实承认
        if any(word in text for word in ["黑暗", "困难", "危机", "挑战", "不好", "严重"]):
            score += 15
            reasons.append("承认现实")
        
        # 包含历史类比
        if any(word in text for word in ["历史", "回想", "过去", "曾经", "类似"]):
            score += 15
            reasons.append("历史类比")
        
        # 包含反讽
        if "以为" in text and ("但" in text or "却" in text):
            score += 15
            reasons.append("反讽对手")
        
        # 包含精神召唤
        if any(word in text for word in ["精神", "品格", "文化", "价值观"]):
            score += 15
            reasons.append("精神召唤")
        
        # 包含 Victory 愿景
        if any(word in text for word in ["胜利", "成功", "未来", "美好", "自由"]):
            score += 10
            reasons.append("胜利愿景")
        
        #  Churchill 标志性结尾
        if "绝不" in text and ("放弃" in text or "投降" in text):
            score += 10
            reasons.append("Churchill 式坚定结尾")
        
        return {"score": min(score, 100), "reasons": reasons, "max_score": 100}
    
    def create_custom_template(self, crisis_name: str, structure: List[str]) -> str:
        """创建自定义讲话模板
        
        Args:
            crisis_name: 危机名称
            structure: 讲话结构列表
            
        Returns:
            str: JSON 格式的模板
        """
        template = {
            "crisis": crisis_name,
            "structure": structure,
            "sections": {}
        }
        
        for section in structure:
            template["sections"][section] = {
                "purpose": "待定义",
                "example": "待填充",
                "churchill_style": "参考 Churchill 经典讲话中的对应部分"
            }
        
        return json.dumps(template, ensure_ascii=False, indent=2)


# 快速使用
if __name__ == "__main__":
    generator = CrisisSpeechGenerator()
    
    # 示例：产品失败危机
    result = generator.generate(
        "product_failure",
        audience="全体员工",
        流失率="40%",
        公司历史="苹果公司在1997年",
        应对措施="推出iPod、iPhone等革命性产品",
        竞争对手="那些只知跟随、不知创新的保守者",
        公司价值观="永不放弃的创新精神"
    )
    
    print("=== Churchill 式危机讲话 ===")
    print(result["speech"])
    print(f"\n Churchill 风格评分: {result['churchill_score']['score']}/100")
    print(f"评分理由: {', '.join(result['churchill_score']['reasons'])}")
    print(f"\n修辞分析: {', '.join(result['rhetoric_used'])}")
    print("\n=== 交付技巧 ===")
    for tip in result["delivery_tips"]:
        print(f"- {tip}")