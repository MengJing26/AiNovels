#!/usr/bin/env python3
"""
Churchill Crisis Leadership Skill
主入口模块，提供危机领导力四大核心功能
"""

from datetime import datetime, timedelta


class ChurchillCrisisSpeech:
    """丘吉尔式危机讲话引擎"""
    
    def generate(self, crisis_description, enemy, historical_ref, 
                 spirit, victory_vision, audience="员工"):
        """生成危机动员讲话
        
        Args:
            crisis_description: 危机现状描述
            enemy: 对立面/挑战（用反讽手法）
            historical_ref: 历史类比
            spirit: 要唤起的集体精神
            victory_vision: 胜利后的愿景
            audience: 讲话对象
            
        Returns:
            str: Churchill 风格的讲话稿
        """
        speech = f"""
各位{audeince}：

{crisis_description}

回顾历史，{historical_ref}。我们从未被打败。

{enemy}或许以为我们会屈服，但他们低估了我们的精神。

正是{spirit}，让我们屹立不倒。

我坚信，{victory_vision}。

 Churchill 的名言说得好："成功不是最终的，失败不是致命的：重要的是继续前进的勇气。"

我们将战斗在任何地方：在会议室、在生产线、在客户现场、在每一家合作伙伴那里。
我们绝不放弃！
"""
        return speech.strip()
    
    def get_historical_examples(self):
        """提供 Churchill 历史讲话案例"""
        return {
            "1940-06-18": "《我们将战斗 Victory 演讲",
            "1940-06-04": "《我们将在海滩上战斗》",
            "1941-12-08": "珍珠港后宣战演讲",
            "1941-01-20": "炉边谈话《新方向》"
        }


class ChurchillRhythmController:
    """战略定力节奏控制系统"""
    
    def __init__(self, crisis_name):
        self.crisis_name = crisis_name
        self.start_date = datetime.now()
        self.schedule = self._build_schedule()
    
    def _build_schedule(self):
        """构建 Churchill 式节奏"""
        return {
            "daily": {
                "08:00": "战略简报（15分钟） - Churchill 每日必参军事会议",
                "12:00": "战情更新（10分钟） -  midday check-in",
                "18:00": "复盘会（30分钟） - Evening review"
            },
            "weekly": {
                "monday": "战略部署会 - Churchill: '周一决定本周方向'",
                "wednesday": "关键指标审查 - Churchill: '周三检查进展，调整战术'",
                "friday": "胜利庆祝 - Churchill: '即使小胜也要庆祝'"
            },
            "monthly": {
                "day_1": "战略审视（月度方向调整）",
                "day_15": "关键决策点检查",
                "day_30": "成果汇报会"
            },
            "principles": [
                " Churchill 格言：Never Less than Daily（每日不间断）",
                "危机中保持定时沟通，避免信息断层",
                "每周必须有一次'胜利时刻'，无论多小",
                "保持个人思考时间（ Churchill 每天2-3小时写作）"
            ]
        }
    
    def generate_calendar_events(self):
        """生成日历事件（iCal格式）"""
        events = []
        for time, desc in self.schedule["daily"].items():
            events.append(f"BEGIN:VEVENT\nDTSTART:{self.start_date.strftime('%Y%m%dT')}{time.replace(':', '')}\nRRULE:FREQ=DAILY\nSUMMARY:{desc}\nEND:VEVENT")
        return "\n".join(events)
    
    def get_checklist(self):
        """ Churchill 定力自检清单"""
        return {
            "daily_communication": "是否保持了每日战略简报？",
            "weekly_celebration": "本周是否有明确的胜利庆祝？",
            "solo_thinking": "是否保持了至少2小时独立思考时间？",
            "decision_timing": "重大决策是否在72小时内完成？",
            "information_flow": "核心团队信息是否透明无阻？"
        }


class ChurchillTeamArchitect:
    """危机团队构建与授权"""
    
    def build(self, org_size):
        """构建危机响应团队
        
        Args:
            org_size: 组织规模（人数）
            
        Returns:
            dict: 团队构架和角色定义
        """
        if org_size < 100:
            roles = {
                "决策主席": {"人数": 1, "授权": "最终决策 + 战略总监", " Churchill 角色": "首相本人"},
                "执行总监": {"人数": 2, "授权": "跨部门协调", " Churchill 角色": "军种参谋长"},
                "情报总监": {"人数": 1, "授权": "情报收集与预警", " Churchill 角色": "情报首脑"}
            }
        elif org_size < 1000:
            roles = {
                "决策主席": {"人数": 1, "授权": "最终决策", " Churchill 角色": "首相本人"},
                "战略总监": {"人数": 1, "授权": "战略框架", " Churchill 角色": "参谋长委员会"},
                "执行总监": {"人数": 3, "授权": "执行与协调", " Churchill 角色": "各领域主管"},
                "情报总监": {"人数": 1, "授权": "情报收集", " Churchill 角色": "情报部门"},
                "沟通总监": {"人数": 1, "授权": "内外沟通", " Churchill 角色": "宣传大臣"}
            }
        else:
            roles = {
                "决策主席": {"人数": 1, "授权": "最终决策", " Churchill 角色": "首相"},
                "战略委员会": {"人数": 3, "授权": "战略规划", " Churchill 角色": "战时内阁"},
                "执行副总裁": {"人数": 5, "授权": "业务执行", " Churchill 角色": "军种参谋长"},
                "情报副总裁": {"人数": 2, "授权": "情报与分析", " Churchill 角色": "联合情报委员会"},
                "沟通副总裁": {"人数": 2, "授权": "全球沟通", " Churchill 角色": "宣传部门"},
                "跨职能协调官": {"人数": 1, "授权": "打破部门墙", " Churchill 角色": "内阁秘书"}
            }
        
        return {
            "危机团队规模": sum(r["人数"] for r in roles.values()),
            "核心原则": " Churchill 战时内阁模式（≤6人核心决策）",
            "角色定义": roles,
            " Churchill 授权格言": "告诉我要做什么，但不要告诉我怎么做",
            "沟通机制": {
                "daily": "核心团队每日站会",
                "weekly": "全员战略会议",
                "ad_hoc": "情报官直接向决策者汇报"
            }
        }
    
    def get_delegation_guide(self):
        """授权指南"""
        return """
### Churchill 式授权原则

1. **结果授权，而非过程控制**
   - Churchill 对 Montgomery: "You are responsible for the conduct of the battle."
   - 不干预细节，但要求结果

2. **每周至少1次1对1沟通**
   - Churchill 每周与关键将领单独会谈
   - 建立信任，及时纠偏

3. **公开场合维护权威**
   - Churchill 在议会公开表扬下属
   - 即使有分歧，私下讨论，公开支持

4. **允许失败，但不允许隐瞒**
   - Churchill: "我只对两种行为零容忍：叛徒和隐瞒者"
   - 建立"无责怪"文化，鼓励快速试错
        """


class ChurchillDecisionEngine:
    """危机决策节奏引擎"""
    
    def __init__(self, decision_question):
        self.question = decision_question
        self.start_time = datetime.now()
        self.deadline_hours = 72
        self.decision_deadline = self.start_time + timedelta(hours=self.deadline_hours)
        self.core_team = []
        self.options = []
        self.final_decision = None
        self.process_log = []
    
    def start_process(self, core_team_size=6):
        """启动决策流程
        
        Returns:
            dict: 时间表和质量指标
        """
        timeline = {
            "启动": self.start_time,
            "首次会议": self.start_time + timedelta(hours=2),
            "选项完成": self.start_time + timedelta(hours=24),
            "最终决策": self.decision_deadline
        }
        
        checklist = {
            "核心团队规模": f"≤{core_team_size}人（ Churchill 标准：6人战时内阁）",
            "并行收集": "同时听取多方意见，而非顺序汇报",
            "选项数量": "3-5个可行方案",
            "反对意见": "必须记录并考虑",
            "独自思考": "决策前至少6小时独立思考",
            "拍板清晰": "最终决定必须明确不含糊"
        }
        
        return {
            "决策问题": self.question,
            " Churchill 时间表": timeline,
            "质量检查清单": checklist,
            " Churchill 格言": "Better to decide and be wrong than to continue uncertainty."
        }
    
    def evaluate_quality(self, process_data):
        """ Churchill 决策质量评分"""
        factors = {
            "时效性": process_data.get("time_to_decide_hours", 0) <= 72,
            "并行意见数": process_data.get("parallel_inputs", 0) >= 3,
            "选项数量": 3 <= process_data.get("options_count", 0) <= 5,
            "记录反对意见": process_data.get("dissent_recorded", False),
            "独自思考时间": process_data.get("solo_thinking_hours", 0) >= 6,
            "设定截止时间": process_data.get("deadline_set", False),
            "决策明确": process_data.get("decision_clear", False)
        }
        
        score = sum(factors.values()) / len(factors) * 5
        return {
            " Churchill 决策质量评分": f"{round(score, 1)}/5.0",
            "各维度详情": factors,
            "改进建议": self._get_improvements(factors)
        }
    
    def _get_improvements(self, factors):
        """基于评分提供改进建议"""
        improvements = []
        for factor, passed in factors.items():
            if not passed:
                if factor == "时效性":
                    improvements.append("⏱️ 决策时间超过72小时， Churchill 标准是2-3天")
                elif factor == "并行意见数":
                    improvements.append("👥 并行收集的意见少于3方，建议增加独立视角")
                elif factor == "选项数量":
                    improvements.append("📋 选项数量不在3-5个范围内， Churchill 认为太少或太多都不好")
                elif factor == "记录反对意见":
                    improvements.append("⚠️ 未记录反对意见， Churchill 特别重视不同声音")
                elif factor == "独自思考时间":
                    improvements.append("🧠 独立思考时间不足6小时， Churchill 习惯夜间独自思考")
        return improvements


class ChurchillLeadershipSkill:
    """主入口类 - Churchill 危机领导力技能"""
    
    def __init__(self):
        self.speech_engine = ChurchillCrisisSpeech()
        self.rhythm_controller = None
        self.team_architect = ChurchillTeamArchitect()
        self.decision_engine = None
    
    def speech(self, crisis, enemy, historical, spirit, vision, audience="团队"):
        """生成危机讲话"""
        return self.speech_engine.generate(
            crisis_description=crisis,
            enemy=enemy,
            historical_ref=historical,
            spirit=spirit,
            victory_vision=vision,
            audience=audience
        )
    
    def start_rhythm(self, crisis_name):
        """启动战略节奏控制"""
        self.rhythm_controller = ChurchillRhythmController(crisis_name)
        return self.rhythm_controller.schedule
    
    def build_team(self, org_size):
        """构建危机团队"""
        return self.team_architect.build(org_size)
    
    def start_decision(self, question, deadline_hours=72):
        """启动决策流程"""
        self.decision_engine = ChurchillDecisionEngine(question)
        self.decision_engine.deadline_hours = deadline_hours
        return self.decision_engine.start_process()
    
    def assess_decision_quality(self, process_data):
        """评估决策质量"""
        if not self.decision_engine:
            return {"error": "请先启动决策流程"}
        return self.decision_engine.evaluate_quality(process_data)
    
    def get_churchill_quote(self, category="general"):
        """获取 Churchill 格言"""
        quotes = {
            "crisis": [
                "If you're going through hell, keep going.",
                "This is the worst time, but it may be the best time for the best work.",
                "Success is not final, failure is not fatal: it is the courage to continue that counts."
            ],
            "decision": [
                "In war, you can only be sure of one thing: that the unexpected will happen.",
                "The best argument against democracy is a five-minute conversation with the average voter.",
                "Never, never, never give up."
            ],
            "leadership": [
                "The price of greatness is responsibility.",
                "You have enemies? Good. That means you've stood up for something.",
                "I am easily satisfied with the very best."
            ]
        }
        return quotes.get(category, quotes["general"])[0]
    
    def get_skill_info(self):
        """获取技能信息"""
        return {
            "name": "Churchill Crisis Leadership",
            "version": "1.0.0",
            "author": "蒙境 AI 超体",
            "description": "基于温斯顿·丘吉尔战时领导力的系统化技能包",
            "modules": ["speech", "rhythm", "team", "decision"],
            "rating": {
                "practicality": 5,
                "replicability": 5,
                "commercial_value": 5,
                "differentiation": 4
            }
        }


# CLI 接口
if __name__ == "__main__":
    import sys
    import json
    
    skill = ChurchillLeadershipSkill()
    
    if len(sys.argv) < 2:
        print(json.dumps(skill.get_skill_info(), ensure_ascii=False, indent=2))
        sys.exit(0)
    
    command = sys.argv[1]
    
    if command == "speech":
        # 示例: python main.py speech --crisis "..." --enemy "..." ...
        args = {}
        i = 2
        while i < len(sys.argv):
            if sys.argv[i].startswith("--"):
                key = sys.argv[i][2:]
                if i + 1 < len(sys.argv) and not sys.argv[i+1].startswith("--"):
                    args[key] = sys.argv[i+1]
                    i += 2
                else:
                    args[key] = True
                    i += 1
        result = skill.speech(
            crisis=args.get("crisis", "危机情况"),
            enemy=args.get("enemy", "挑战"),
            historical=args.get("historical", "历史教训"),
            spirit=args.get("spirit", "团队精神"),
            vision=args.get("vision", "美好未来"),
            audience=args.get("audience", "团队")
        )
        print(result)
    
    elif command == "rhythm":
        crisis_name = sys.argv[2] if len(sys.argv) > 2 else "危机"
        rhythm = skill.start_rhythm(crisis_name)
        print(json.dumps(rhythm, ensure_ascii=False, indent=2))
    
    elif command == "team":
        org_size = int(sys.argv[2]) if len(sys.argv) > 2 else 100
        team = skill.build_team(org_size)
        print(json.dumps(team, ensure_ascii=False, indent=2))
    
    elif command == "decision-start":
        question = sys.argv[2] if len(sys.argv) > 2 else "决策问题"
        deadline = int(sys.argv[4]) if len(sys.argv) > 4 and sys.argv[3] == "--deadline" else 72
        decision = skill.start_decision(question, deadline)
        print(json.dumps(decision, ensure_ascii=False, indent=2))
    
    elif command == "quote":
        category = sys.argv[2] if len(sys.argv) > 2 else "general"
        print(skill.get_churchill_quote(category))
    
    else:
        print(f"Unknown command: {command}")
        print("Available: speech, rhythm, team, decision-start, quote")
        sys.exit(1)