#!/usr/bin/env python3
"""
Churchill Decision Engine
危机决策节奏引擎 - Churchill 如何在不确定性和时间压力下做出高质量决策
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional
from enum import Enum
import json


class DecisionType(Enum):
    """决策类型"""
    STRATEGIC = "战略级"  # 影响6个月以上
    TACTICAL = "战术级"   # 影响1-4周
    OPERATIONAL = "操作级"  # 影响<1周
    CRISIS_RESPONSE = "危机响应"  # 需要立即行动


class DecisionUrgency(Enum):
    """紧急程度"""
    IMMEDIATE = "立即"  # 2小时内决策
    URGENT = "紧急"     # 24小时内决策
    IMPORTANT = "重要"  # 72小时内决策
    NORMAL = "常规"     # 1周以上


class ChurchillDecisionRecord:
    """ Churchill 式决策记录"""
    
    def __init__(self, question: str, decision_type: DecisionType, urgency: DecisionUrgency):
        self.question = question
        self.type = decision_type
        self.urgency = urgency
        self.start_time = datetime.now()
        self.deadline = self._calculate_deadline(urgency)
        self.core_team_size = 6  # Churchill 标准
        self.parallel_inputs = 0
        self.options_generated = 0
        self.final_decision = None
        self.process_log = []
    
    def _calculate_deadline(self, urgency: DecisionUrgency) -> datetime:
        """根据紧急程度计算截止时间"""
        hours_map = {
            DecisionUrgency.IMMEDIATE: 2,
            DecisionUrgency.URGENT: 24,
            DecisionUrgency.IMPORTANT: 72,
            DecisionUrgency.NORMAL: 168
        }
        return self.start_time + timedelta(hours=hours_map[urgency])
    
    def add_parallel_input(self, source: str, perspective: str, recommendation: str):
        """添加并行输入（ Churchill 同时听取多方意见）"""
        self.parallel_inputs += 1
        self.process_log.append({
            "timestamp": datetime.now(),
            "type": "parallel_input",
            "source": source,
            "perspective": perspective,
            "recommendation": recommendation
        })
    
    def generate_options(self, options: List[Dict]):
        """生成决策选项"""
        self.options_generated = len(options)
        for opt in options:
            self.process_log.append({
                "timestamp": datetime.now(),
                "type": "option",
                "description": opt.get("description"),
                "pros": opt.get("pros", []),
                "cons": opt.get("cons", [])
            })
    
    def record_dissent(self, source: str, argument: str):
        """记录反对意见（ Churchill 特别重视）"""
        self.process_log.append({
            "timestamp": datetime.now(),
            "type": "dissent",
            "source": source,
            "argument": argument
        })
    
    def set_solo_thinking(self, hours: float):
        """设置独立思考时间"""
        self.solo_thinking_hours = hours
        self.process_log.append({
            "timestamp": datetime.now(),
            "type": "solo_thinking",
            "hours": hours,
            "note": " Churchill 习惯夜间独自思考"
        })
    
    def make_decision(self, decision: str, reasoning: str, announce_to: List[str]):
        """做出最终决策"""
        self.final_decision = decision
        self.decision_time = datetime.now()
        self.decision_reasoning = reasoning
        self.announce_to = announce_to
        self.process_log.append({
            "timestamp": self.decision_time,
            "type": "final_decision",
            "decision": decision,
            "reasoning": reasoning,
            "announce_to": announce_to
        })
        
        # 检查是否超时
        if self.decision_time > self.deadline:
            self.overdue = True
            self.overdue_hours = (self.decision_time - self.deadline).total_seconds() / 3600
        else:
            self.overdue = False
    
    def get_quality_score(self) -> Dict:
        """ Churchill 决策质量评分"""
        score = 0
        reasons = []
        
        # 时效性（ Churchill 标准：战略决策≤72小时）
        if self.urgency == DecisionUrgency.IMPORTANT:
            time_limit = 72
        elif self.urgency == DecisionUrgency.URGENT:
            time_limit = 24
        else:
            time_limit = 2
        
        time_taken = (self.decision_time - self.start_time).total_seconds() / 3600 if self.decision_time else 999
        if time_taken <= time_limit:
            score += 20
            reasons.append(f"时效性优秀（{time_taken:.1f}小时 ≤ {time_limit}小时）")
        else:
            reasons.append(f"时效性不足（{time_taken:.1f}小时 > {time_limit}小时）")
        
        # 并行输入数量（ Churchill 同时听取多方意见）
        if self.parallel_inputs >= 5:
            score += 20
            reasons.append(f"并行视角丰富（{self.parallel_inputs}个来源）")
        elif self.parallel_inputs >= 3:
            score += 15
            reasons.append(f"并行视角充足（{self.parallel_inputs}个来源）")
        else:
            reasons.append(f"并行视角不足（仅{self.parallel_inputs}个来源， Churchill 标准≥3）")
        
        # 选项数量（ Churchill 要求3-5个选项）
        if 3 <= self.options_generated <= 5:
            score += 20
            reasons.append(f"选项数量 Churchill 化（{self.options_generated}个）")
        elif self.options_generated >= 6:
            score += 10
            reasons.append(f"选项过多（{self.options_generated}个， Churchill 认为太多选项导致分析瘫痪）")
        else:
            reasons.append(f"选项不足（仅{self.options_generated}个）")
        
        # 反对意见记录（ Churchill 重视不同声音）
        dissent_count = sum(1 for log in self.process_log if log["type"] == "dissent")
        if dissent_count > 0:
            score += 15
            reasons.append(f"记录了{dissent_count}条反对意见（ Churchill 特别重视）")
        else:
            reasons.append("缺少反对意见记录（ Churchill 会主动征求不同意见）")
        
        # 独立思考时间（ Churchill 习惯2-3小时）
        solo_hours = getattr(self, 'solo_thinking_hours', 0)
        if solo_hours >= 2:
            score += 15
            reasons.append(f"独立思考时间充足（{solo_hours:.1f}小时）")
        else:
            reasons.append(f"独立思考时间不足（{solo_hours:.1f}小时， Churchill 标准≥2小时）")
        
        # 决策明确性
        if self.final_decision:
            clarity_score = 5 if len(self.final_decision) > 10 and "不" not in self.final_decision else 3
            score += clarity_score
            reasons.append("决策表述明确" if clarity_score == 5 else "决策表述需更明确")
        else:
            reasons.append("尚未做出决策")
            score += 0
        
        return {
            " Churchill 决策质量": f"{score}/100",
            "评分详情": reasons,
            " Churchill 格言": " Churchill : 'Better to decide and be wrong than continue uncertainty.'",
            "改进方向": self._get_improvement_suggestions(time_taken, self.parallel_inputs, 
                                                         self.options_generated, dissent_count, solo_hours)
        }
    
    def _get_improvement_suggestions(self, time_taken, parallel, options, dissent, solo):
        """获取改进建议"""
        suggestions = []
        if time_taken > 72 and self.urgency == DecisionUrgency.IMPORTANT:
            suggestions.append("⏱️ 决策时间过长， Churchill 标准≤72小时")
        if parallel < 3:
            suggestions.append("👥 并行收集观点不足， Churchill 同时听取≥3方意见")
        if options < 3 or options > 5:
            suggestions.append("📋 选项数量异常， Churchill 标准3-5个")
        if dissent == 0:
            suggestions.append("⚠️ 未记录反对意见， Churchill 会主动征求不同声音")
        if solo < 2:
            suggestions.append("🧠 独立思考时间不足， Churchill 习惯2-3小时")
        return suggestions if suggestions else ["✅ 符合 Churchill 决策标准"]


class ChurchillDecisionEngine:
    """ Churchill 式决策引擎"""
    
    def __init__(self):
        self.active_decisions = {}
        self.historical_decisions = []
        self.churchill_principles = self._load_principles()
    
    def _load_principles(self) -> List[Dict]:
        """加载 Churchill 决策原则"""
        return [
            {
                "原则": "不等待完美信息",
                " Churchill 实践": "1940年5月 Churchill 上任时，法国即将崩溃，他没有等所有信息完备就决定继续战斗",
                "现代应用": "收集到足够决策的信息（3-5个视角）后立即决定，不要追求100%信息"
            },
            {
                "原则": "并行收集而非顺序",
                " Churchill 实践": " Churchill 同时听取陆军、海军、空军、外交的意见，而非一个个听汇报",
                "现代应用": "同时召集多个利益相关者，给出2小时准备时间，所有人同时给出建议"
            },
            {
                "原则": "明确截止时间",
                " Churchill 实践": "每次会议开始时， Churchill 会说：'今天必须做出决定'",
                "现代应用": "决策会议开始时宣布：'我们在会议结束前必须做出选择'"
            },
            {
                "原则": "要求选项而非分析",
                " Churchill 实践": " Churchill 会说：'不要告诉我问题是什么，告诉我你有哪几个解决方案'",
                "现代应用": "每次输入必须附带推荐方案， Churchill 式提问：'如果是你会怎么做？'"
            },
            {
                "原则": "记录并重视反对意见",
                " Churchill 实践": " Churchill 的会议室里有专人记录不同意见，他会亲自阅读",
                "现代应用": "每次决策会议必须有'魔鬼代言人'，所有反对意见写入记录"
            },
            {
                "原则": "深夜独立思考",
                " Churchill 实践": " Churchill 习惯凌晨1-3点独自在卧室思考重大决策",
                "现代应用": "重大决策前确保2-3小时不被打扰的独立思考时间"
            },
            {
                "原则": "拍板清晰不含糊",
                " Churchill 实践": " Churchill 的决定从来不会模棱两可，他会说：'我们将在海滩上战斗'，而非'我们或许应该...'",
                "现代应用": "决策表述使用肯定句，避免'可能'、'也许'、'考虑'等词"
            }
        ]
    
    def start_decision(self, question: str, decision_type: str = "战略级", 
                      urgency: str = "重要") -> ChurchillDecisionRecord:
        """启动 Churchill 式决策流程
        
        Args:
            question: 决策问题
            decision_type: 决策类型（战略级/战术级/操作级/危机响应）
            urgency: 紧急程度（立即/紧急/重要/常规）
            
        Returns:
            ChurchillDecisionRecord: 决策记录对象
        """
        type_enum = {
            "战略级": DecisionType.STRATEGIC,
            "战术级": DecisionType.TACTICAL,
            "操作级": DecisionType.OPERATIONAL,
            "危机响应": DecisionType.CRISIS_RESPONSE
        }.get(decision_type, DecisionType.STRATEGIC)
        
        urgency_enum = {
            "立即": DecisionUrgency.IMMEDIATE,
            "紧急": DecisionUrgency.URGENT,
            "重要": DecisionUrgency.IMPORTANT,
            "常规": DecisionUrgency.NORMAL
        }.get(urgency, DecisionUrgency.IMPORTANT)
        
        record = ChurchillDecisionRecord(question, type_enum, urgency_enum)
        decision_id = f"DEC-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        self.active_decisions[decision_id] = record
        
        return record, decision_id
    
    def conduct_decision_meeting(self, decision_id: str, participants: List[Dict]) -> Dict:
        """召开 Churchill 式决策会议
        
        Args:
            decision_id: 决策ID
            participants: 参与者列表，每个参与者包含name, perspective, recommendation
            
        Returns:
            Dict: 会议记录和下一步
        """
        if decision_id not in self.active_decisions:
            return {"error": "Decision not found"}
        
        record = self.active_decisions[decision_id]
        meeting_record = {
            "meeting_type": " Churchill 式决策会议",
            "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "participants": len(participants),
            "inputs": []
        }
        
        # Churchill 会议规则
        meeting_rules = """
        Churchill 会议规则:
        1. 会议开始宣布: '今天必须做出决定'
        2. 每人2分钟陈述 + 1分钟推荐（禁止纯分析）
        3. 所有意见同时收集，不顺序汇报
        4. 指定1人记录反对意见
        5. 会议结束前必须生成3-5个选项
        """
        
        # 收集并行输入
        for p in participants:
            record.add_parallel_input(
                source=p["name"],
                perspective=p.get("perspective", "未指定"),
                recommendation=p.get("recommendation", "无")
            )
            meeting_record["inputs"].append({
                "name": p["name"],
                "perspective": p.get("perspective"),
                "recommendation": p.get("recommendation")
            })
        
        return {
            "meeting_rules": meeting_rules.strip(),
            "meeting_record": meeting_record,
            "parallel_inputs_collected": len(participants),
            "next_steps": [
                " Churchill : '现在我们有足够的信息，请在接下来的1小时内起草3-5个选项'",
                " Churchill : '记住，不要告诉我问题，告诉我解决方案'",
                " Churchill : '我们需要听到不同的声音，指定[某人]担任魔鬼代言人'"
            ]
        }
    
    def generate_options_with_churchill_style(self, decision_id: str, 
                                             options: List[Dict]) -> Dict:
        """生成 Churchill 风格的选项"""
        if decision_id not in self.active_decisions:
            return {"error": "Decision not found"}
        
        record = self.active_decisions[decision_id]
        record.generate_options(options)
        
        # Churchill 选项评估框架
        evaluation_framework = {
            " Churchill 评估维度": [
                "对最终胜利的贡献度（是否解决问题根源）",
                "风险与不确定性 Churchill : '战争中没有确定性'",
                "资源需求 Churchill : '我们永远资源不足'",
                "道德维度 Churchill : '我们不仅在为胜利而战，更为价值观而战'",
                "舆论影响（对内/对外） Churchill : '语言本身就是武器'"
            ],
            " Churchill 警告": [
                "避免'折中方案' - Churchill : '折中是懦夫的专利'",
                "避免过度分析 - Churchill : '完美是好的敌人'",
                "避免等待更多信息 - Churchill : '我们永远不会100%确定'"
            ]
        }
        
        return {
            "options_recorded": len(options),
            " Churchill 框架": evaluation_framework,
            "principles_applied": [
                "3-5个选项（ Churchill 标准）",
                "每个选项附带明确理由和风险",
                " Churchill : '给我选项，而不是问题'"
            ],
            "next": " Churchill : '现在，让我在今晚思考。明天早上我会宣布决定。'"
        }
    
    def record_solo_thinking(self, decision_id: str, hours: float = 2.0) -> Dict:
        """记录 Churchill 式独立思考"""
        if decision_id not in self.active_decisions:
            return {"error": "Decision not found"}
        
        record = self.active_decisions[decision_id]
        record.set_solo_thinking(hours)
        
        return {
            " Churchill 格言": " Churchill 习惯凌晨1-3点独自在卧室思考重大决策",
            "thinking_hours": hours,
            " Churchill 建议": [
                "关掉所有通知",
                "不要在思考时查阅新信息（避免干扰已形成的判断）",
                "用纸笔写，而非屏幕",
                "想象决策成功和失败的场景",
                " Churchill : '在深夜，真相会浮现'"
            ]
        }
    
    def make_final_decision(self, decision_id: str, decision: str, 
                          reasoning: str, announce_to: List[str]) -> Dict:
        """做出 Churchill 式最终决策"""
        if decision_id not in self.active_decisions:
            return {"error": "Decision not found"}
        
        record = self.active_decisions[decision_id]
        record.make_decision(decision, reasoning, announce_to)
        
        quality = record.get_quality_score()
        
        #  Churchill 决策宣布模板
        announcement_template = f"""
        📢 Churchill 式决策宣布
        
        决策问题: {record.question}
        决策内容: {decision}
        
        决策理由:
        {reasoning}
        
         Churchill 风格检查:
        - ✅ 明确不含糊（ Churchill : '我们将在海滩上战斗'）
        - ✅ 有 Vision（描绘胜利后的状态）
        - ✅ 承担责任（ Churchill : '我承担全部责任'）
        - ✅ 号召行动（给出具体下一步）
        
         Churchill 格言: "Success is not final, failure is not fatal: it is the courage to continue that counts."
        """
        
        # 移动到历史记录
        self.historical_decisions.append(record)
        del self.active_decisions[decision_id]
        
        return {
            "announcement_template": announcement_template.strip(),
            "quality_score": quality,
            "decision_id": decision_id,
            " Churchill 式果断度": self._evaluate_decisiveness(decision),
            "后续行动": [
                f"立即向 {', '.join(announce_to)} 宣布决策",
                " Churchill : '现在，立即执行，不要再开会讨论'",
                " Churchill : '我会每周检查进展，但具体执行你们全权负责'"
            ]
        }
    
    def _evaluate_decisiveness(self, decision: str) -> str:
        """评估决策的 Churchill 式果断度"""
        bad_words = ["也许", "可能", "考虑", "或许", "应该可以", "评估一下"]
        good_words = ["将", "必须", "立即", "坚决", "我们将在", "我决定"]
        
        has_bad = any(word in decision for word in bad_words)
        has_good = any(word in decision for word in good_words)
        
        if has_good and not has_bad:
            return "⭐⭐⭐⭐⭐ Churchill 式果断（明确、肯定、有力）"
        elif has_good and has_bad:
            return "⭐⭐⭐  基本 Churchill 化，但可更果断"
        else:
            return "⭐⭐   不够 Churchill ，建议使用肯定句"
    
    def get_decision_templates(self) -> Dict:
        """获取 Churchill 决策模板"""
        return {
            " Churchill 决策宣布模板": """
            各位：
            
            经过 Churchill 式决策流程（并行输入+独立思考+选项生成），
            我决定：{decision}
            
            理由：
            1. {reason_1}
            2. {reason_2}
            3. {reason_3}
            
            下一步：
            - [执行者A] 负责 {task_a}，{deadline_a}
            - [执行者B] 负责 {task_b}，{deadline_b}
            - [沟通者] 向 {audience} 宣布此决定
            
             Churchill 说："我承担全部责任。"
            """,
            
            " Churchill 式决策提问模板": [
                "不要告诉我问题是什么，告诉我你有哪几个解决方案",
                "如果是你会怎么做？（不要'如果我是你'，直接说'你会怎么做'）",
                "这个决定失败的最可能原因是什么？",
                "反对这个决定的最有力论点是什么？",
                " Churchill : '如果希特勒知道我们会怎么做，他会怎么应对？'"
            ],
            
            " Churchill 式决策会议开场": [
                " Churchill : '各位，我们今天必须做出决定。'",
                " Churchill : '我不需要更多分析，我需要选项。'",
                " Churchill : '告诉我你的判断，不是你的顾虑。'",
                " Churchill : '我们而不是希特勒来主导这场会议的结果。'"
            ]
        }
    
    def get_decision_health_score(self, decision_id: str) -> Dict:
        """获取决策健康度评分"""
        if decision_id not in self.active_decisions:
            return {"error": "Decision not found or already completed"}
        
        record = self.active_decisions[decision_id]
        return record.get_quality_score()
    
    def get_principles(self) -> List[Dict]:
        """获取 Churchill 决策原则"""
        return self.churchill_principles


# 快速测试
if __name__ == "__main__":
    engine = ChurchillDecisionEngine()
    
    print("=== Churchill 决策引擎 - 原则概览 ===")
    principles = engine.get_principles()
    for i, p in enumerate(principles, 1):
        print(f"\n{i}. {p['原则']}")
        print(f"    Churchill 实践: {p[' Churchill 实践']}")
        print(f"   现代应用: {p['现代应用']}")
    
    print("\n" + "="*60)
    print("=== 示例：启动一个 Churchill 式决策 ===")
    
    # 启动一个决策
    record, dec_id = engine.start_decision(
        question="是否应该在预算削减5%的情况下继续维持R&D投入？",
        decision_type="战略级",
        urgency="重要"
    )
    
    print(f"决策ID: {dec_id}")
    print(f"问题: {record.question}")
    print(f"截止时间: {record.deadline.strftime('%Y-%m-%d %H:%M')}")
    print(f" Churchill 标准时效: {72}小时")
    
    print("\n" + "="*60)
    print("=== Churchill 式决策会议 ===")
    
    # 模拟会议
    participants = [
        {"name": "CFO", "perspective": "财务可持续性", "recommendation": "削减R&D 5%，保现金流"},
        {"name": "CTO", "perspective": "技术竞争力", "recommendation": "保持R&D，削减市场费用"},
        {"name": "CPO", "perspective": "产品路线图", "recommendation": "分阶段削减，不影响关键项目"},
        {"name": "Sales VP", "perspective": "短期收入", "recommendation": "加大销售投入，R&D可以等等"},
        {"name": "HR Director", "perspective": "人才保留", "recommendation": "避免核心研发人员流失，保持R&D基本盘"}
    ]
    
    meeting_result = engine.conduct_decision_meeting(dec_id, participants)
    print(f"会议记录: {meeting_result['meeting_record']['participants']}人参与")
    print(f"并行输入: {meeting_result['parallel_inputs_collected']}个来源")
    print(" Churchill 会议规则:")
    for rule in meeting_result['meeting_rules'].split('\n'):
        print(f"  {rule}")
    
    print("\n" + "="*60)
    print("=== 生成决策选项 ===")
    
    options = [
        {
            "description": "维持R&D预算不变，削减其他部门5%",
            "pros": ["保持技术创新优势", "核心人才稳定"],
            "cons": ["影响其他部门运营", "现金流压力"]
        },
        {
            "description": "R&D削减3%，其他削减7%",
            "pros": ["平衡各部门", "部分保护研发"],
            "cons": ["两边都不讨好", "仍可能流失人才"]
        },
        {
            "description": "R&D削减5%，同时承诺24个月后恢复并追加10%",
            "pros": ["短期过冬", "长期承诺保留希望"],
            "cons": ["信任受损", "执行难度大"]
        },
        {
            "description": "R&D维持，立即启动紧急融资",
            "pros": ["一劳永逸解决资金问题", "保持战略投入"],
            "cons": ["融资不确定性", "时间窗口可能错过"]
        }
    ]
    
    options_result = engine.generate_options_with_churchill_style(dec_id, options)
    print(f"生成选项: {options_result['options_recorded']}个")
    print(" Churchill 评估维度:")
    for dim in options_result[' Churchill 框架'][' Churchill 评估维度']:
        print(f"  • {dim}")
    
    print("\n=== 独立思考 ===")
    thinking = engine.record_solo_thinking(dec_id, 2.5)
    print(f"独立思考: {thinking['thinking_hours']}小时")
    print(" Churchill 建议:")
    for tip in thinking[' Churchill 建议']:
        print(f"  - {tip}")
    
    print("\n" + "="*60)
    print("=== 做出最终决策 ===")
    
    decision = """
    决定：选项3（R&D削减5%，承诺24个月后恢复并追加10%）
    
    理由：
    1. 短期现金流必须保证（CFO立场）
    2. 技术创新是长期命脉（CTO立场），我们不能失去信心
    3. 24个月承诺给团队明确的信心（HR立场）
    4. 这是 Churchill 式的"冬季战略"：承认困难，但不放弃愿景
    
     Churchill 说："We shall fight on the beaches, we shall fight on the landing grounds..."
    今晚，我们选择战斗，而不是投降。
    """
    
    final = engine.make_final_decision(
        decision_id=dec_id,
        decision="R&D削减5%，同时承诺24个月后恢复并追加10%",
        reasoning=decision,
        announce_to=["全体员工", "董事会", "核心投资者"]
    )
    
    print(" Churchill 式决策质量:")
    print(f"  {final['quality_score'][' Churchill 决策质量']}")
    print("  评分详情:")
    for reason in final['quality_score']['评分详情']:
        print(f"    • {reason}")
    
    print("\n Churchill 宣布模板:")
    print(final['announcement_template'][:500] + "...")
    
    print("\n Churchill 式果断度:", final[' Churchill 式果断度'])
    
    print("\n后续行动:")
    for action in final['后续行动']:
        print(f"  {action}")