#!/usr/bin/env python3
"""
Churchill Team Architect
危机团队构建与授权 - Churchill 如何组建战时内阁并授权将领
"""

from typing import Dict, List
import json


class ChurchillTeamArchitect:
    """ Churchill 式团队构建器"""
    
    # Churchill 战时内阁历史构成
    CHURCHILL_WAR_CABINET = {
        "1940-05": {
            "members": [
                "Winston Churchill (首相 + 战时内阁主席)",
                "Clement Attlee (工党领袖，副首相)",
                "Lord Halifax (外交大臣)",
                "Sir Archibald Sinclair (空军大臣)",
                "Anthony Eden (外交次官，后任外交大臣)"
            ],
            "size": 5,
            "characteristics": [
                "跨党派（包含工党）",
                "核心决策者仅5人（ Hitler 的战争会议有17人， Churchill 坚持精简）",
                "海军、空军、外交全覆盖"
            ]
        },
        "1942-07": {
            "members": [
                "Churchill (首相)",
                "Attlee (副首相)",
                "Cripps (战时内阁成员)",
                "Beaverbrook (战时内阁成员，战时生产大臣)",
                " Eden (外交大臣)",
                "Alanbrooke (帝国总参谋长)",
                "Portal (空军参谋长)"
            ],
            "size": 7,
            "characteristics": [
                "加入战时生产主管",
                "增加军事参谋长",
                " Churchill 仍然保持核心决策层≤7人"
            ]
        }
    }
    
    # Churchill 授权将领的格言
    DELEGATION_QUOTES = [
        "You are responsible for the conduct of the battle. I trust you completely.",
        "Do not tell me how to do it. Tell me what you need, and I'll get it for you.",
        "No one can do your job better than you. Just keep me informed.",
        "Go ahead. If you fail, I'll take the responsibility. Just make sure you've thought it through."
    ]
    
    def __init__(self):
        self.team_patterns = self._load_team_patterns()
    
    def _load_team_patterns(self) -> Dict:
        """加载不同规模的团队模式"""
        return {
            "small": {
                "size": "≤50人",
                "core_team": {
                    "决策者": {"人数": 1, " Churchill 角色": "首相本人", "授权": "最终决策"},
                    "战略家": {"人数": 1, "授权": "制定战略框架 + 战略总监", " Churchill 角色": "参谋长"},
                    "执行者": {"人数": 2, "授权": "跨职能执行", " Churchill 角色": "各领域主管"},
                    "情报官": {"人数": 1, "授权": "情报收集与预警", " Churchill 角色": "情报首脑"}
                },
                "total_core": 5,
                " Churchill 比例": "核心团队占10%（ Churchill 战时内阁比例）"
            },
            "medium": {
                "size": "50-500人",
                "core_team": {
                    "决策者": {"人数": 1, " Churchill 角色": "首相", "授权": "最终决策"},
                    "战略总监": {"人数": 1, " Churchill 角色": "参谋长委员会主席", "授权": "战略规划"},
                    "执行总监A": {"人数": 1, " Churchill 角色": "A领域参谋长", "授权": "A领域执行"},
                    "执行总监B": {"人数": 1, " Churchill 角色": "B领域参谋长", "授权": "B领域执行"},
                    "情报总监": {"人数": 1, " Churchill 角色": "情报部门负责人", "授权": "情报+风险预警"},
                    "沟通总监": {"人数": 1, " Churchill 角色": "宣传大臣", "授权": "内外沟通"}
                },
                "total_core": 6,
                " Churchill 比例": "核心团队占1.2%（ Churchill 战时内阁比例）"
            },
            "large": {
                "size": "500+人",
                "core_team": {
                    "决策委员会": {"人数": 3, " Churchill 角色": "战时内阁", "授权": "集体决策 + 最终拍板"},
                    "战略委员会": {"人数": 3, " Churchill 角色": "参谋长委员会", "授权": "中长期战略"},
                    "执行副总裁": {"人数": 5, " Churchill 角色": "各军种参谋长", "授权": "跨部门执行"},
                    "情报副总裁": {"人数": 2, " Churchill 角色": "联合情报委员会", "授权": "情报+数据分析"},
                    "沟通副总裁": {"人数": 2, " Churchill 角色": "宣传部门+对外联络", "授权": "媒体+利益相关者沟通"},
                    "跨职能协调官": {"人数": 1, " Churchill 角色": "内阁秘书", "授权": "打破部门墙 + 流程优化"}
                },
                "total_core": 16,
                " Churchill 比例": "核心团队占≤0.5%（ Churchill 式分散式核心）"
            }
        }
    
    def build_team(self, org_size: int, crisis_type: str = "general") -> Dict:
        """构建危机团队
        
        Args:
            org_size: 组织规模
            crisis_type: 危机类型（general/product/financial/pr）
            
        Returns:
            Dict: 团队构建方案
        """
        if org_size < 50:
            pattern = self.team_patterns["small"]
        elif org_size < 500:
            pattern = self.team_patterns["medium"]
        else:
            pattern = self.team_patterns["large"]
        
        # 根据危机类型微调
        role_adjustments = self._get_crisis_specific_roles(crisis_type)
        
        # Churchill 团队构建核心原则
        churchill_principles = [
            " Churchill 战时内阁仅5-7人（核心决策层≤6人）",
            "打破党派/部门壁垒（ Churchill 纳入工党Attlee）",
            "必须包含情报官（ Churchill 每日听Bletchley Park简报）",
            "必须有专门的沟通负责人（ Churchill 的宣传大臣）",
            "决策者必须保持最终拍板权（ Churchill 亲自起草关键命令）"
        ]
        
        return {
            "危机类型": crisis_type,
            "组织规模": org_size,
            " Churchill 参考": "1940-1945年战时内阁",
            "核心团队规模": pattern["total_core"],
            "核心团队比例": pattern[" Churchill 比例"],
            "角色定义": pattern["core_team"],
            "危机特殊调整": role_adjustments,
            " Churchill 原则": churchill_principles,
            "沟通机制": {
                "daily": "核心团队每日Starding（ Churchill 每日战时内阁）",
                "weekly": "全员战略会议（ Churchill 每周议会报告）",
                "ad_hoc": "情报官直接向决策者汇报（ Churchill 每日单独听情报）",
                "1on1": "决策者每周与每个核心成员1次1对1"
            },
            "授权协议": self.generate_delegation_agreement()
        }
    
    def _get_crisis_specific_roles(self, crisis_type: str) -> Dict:
        """危机类型特定的角色调整"""
        adjustments = {
            "product": {
                "新增角色": "产品总监（ Churchill 角色：战时生产大臣Beaverbrook）",
                "调整": "情报官角色增强为'市场+竞争情报'",
                "重点": "快速迭代 + 用户反馈循环"
            },
            "financial": {
                "新增角色": "CFO + 现金流管控官",
                "调整": "沟通总监需增加'投资者关系'",
                "重点": "资金安全 + 成本控制 + 融资策略"
            },
            "pr": {
                "新增角色": "PR危机经理 + 社交媒体官",
                "调整": "沟通总监为主要发言人",
                "重点": "透明沟通 + 快速响应 + 情感共鸣"
            },
            "operational": {
                "新增角色": "COO + 供应链总监",
                "调整": "执行者增加现场指挥官",
                "重点": "运营延续 + 供应链安全"
            }
        }
        return adjustments.get(crisis_type, {"通用": "按标准模式构建"})
    
    def generate_delegation_agreement(self) -> str:
        """生成 Churchill 式授权协议模板"""
        return """
## Churchill 式授权协议

**授权原则**:
1. 告诉我要做什么，但不要告诉我怎么做
2. 你有完全的作战自主权，但必须每日向我汇报进展
3. 允许失败，但不允许隐瞒信息
4. 公开场合我永远支持你，私下我会直接反馈

**授权语句（ Churchill 风格）**:
> "你全权负责这方面的工作。我相信你的判断。给我想要的结果，而不是过程报告。如果遇到无法解决的问题，直接来找我。但如果只是困难，我希望你自己解决。"

**定期检查**:
- 每日：核心团队会议（ Churchill 每日战时内阁）
- 每周：1对1深度沟通（ Churchill 每周与将领单独谈）
- 每月：绩效评估 + 授权调整

**终止授权条件**:
- 隐瞒关键信息（ Churchill 零容忍）
- 未经沟通的重大决策
- 团队士气严重下滑
        """
    
    def get_team_health_checklist(self) -> List[Dict]:
        """团队健康度检查清单"""
        return [
            {
                "检查项": "核心团队规模",
                " Churchill 标准": "≤6人",
                "健康标准": "6-9人",
                "警告": ">10人（ Churchill : '太多人开会只是浪费时间'）",
                " Churchill 格言": "少即是多"
            },
            {
                "检查项": "每日核心会议",
                " Churchill 标准": "每天1次，风雨无阻",
                "健康标准": "每周5次",
                "警告": "每周<3次",
                " Churchill 格言": "Never Less than Daily"
            },
            {
                "检查项": "情报官汇报线",
                " Churchill 标准": "直接向决策者汇报",
                "健康标准": "2层内",
                "警告": ">3层或经过过滤",
                " Churchill 格言": "信息不能经过'层层过滤器'"
            },
            {
                "检查项": "跨部门合作",
                " Churchill 标准": "核心团队来自不同部门",
                "健康标准": "至少3个不同部门",
                "警告": "单一部门主导",
                " Churchill 格言": "打破部门墙是危机管理的首要任务"
            },
            {
                "检查项": "决策速度",
                " Churchill 标准": "重大决策≤72小时",
                "健康标准": "≤5天",
                "警告": ">7天",
                " Churchill 格言": "Better to decide and be wrong than continue uncertainty"
            },
            {
                "检查项": "胜利庆祝",
                " Churchill 标准": "每周至少1次",
                "健康标准": "每周1次",
                "警告": "每月<1次",
                " Churchill 格言": "Small wins matter. Celebrate them."
            }
        ]
    
    def calculate_team_health_score(self, responses: Dict) -> Dict:
        """计算团队健康度评分"""
        weights = {
            "core_team_size": 15,
            "daily_meeting": 20,
            "intelligence_line": 15,
            "cross_dept": 15,
            "decision_speed": 20,
            "celebration": 15
        }
        
        # 简化的评分逻辑
        scores = {
            "core_team_size": 5 if responses.get("core_team_size", 10) <= 6 else 3 if responses.get("core_team_size", 10) <= 9 else 1,
            "daily_meeting": 5 if responses.get("daily_meeting_freq", 5) >= 5 else 4 if responses.get("daily_meeting_freq", 5) >= 3 else 1,
            "intelligence_line": 5 if responses.get("intel_direct", False) else 2,
            "cross_dept": 5 if responses.get("cross_dept_count", 0) >= 3 else 3 if responses.get("cross_dept_count", 0) >= 2 else 1,
            "decision_speed": 5 if responses.get("decision_hours", 120) <= 72 else 4 if responses.get("decision_hours", 120) <= 120 else 1,
            "celebration": 5 if responses.get("weekly_celebration", False) else 1
        }
        
        weighted_score = sum(scores[k] * weights[k] / 5 for k in scores)
        max_score = sum(weights.values())
        
        return {
            "健康度评分": f"{round(weighted_score, 1)}/{max_score}",
            " Churchill 团队成熟度": self._interpret_team_score(weighted_score / max_score * 100),
            "各维度得分": scores,
            "改进建议": self._get_improvements(scores)
        }
    
    def _interpret_team_score(self, score_percent: float) -> str:
        """解释团队健康度"""
        if score_percent >= 80:
            return "⭐⭐⭐⭐⭐  Churchill 式精英团队"
        elif score_percent >= 60:
            return "⭐⭐⭐⭐   Churchill 风格明显"
        elif score_percent >= 40:
            return "⭐⭐⭐    Churchill 化进行中"
        elif score_percent >= 20:
            return "⭐⭐    需要 Churchill 式改革"
        else:
            return "⭐      传统团队，急需变革"
    
    def _get_improvements(self, scores: Dict) -> List[str]:
        """基于得分提供改进建议"""
        improvements = []
        if scores.get("core_team_size", 5) < 5:
            improvements.append("🔧 核心团队过大，需精简至 Churchill 标准（6人内）")
        if scores.get("daily_meeting", 5) < 4:
            improvements.append("🔧 建立每日核心团队会议（ Churchill 每日战时内阁风雨无阻）")
        if not scores.get("intelligence_direct", 0):
            improvements.append("🔧 确保情报官直接向决策者汇报（ Churchill 每日单独听情报）")
        if scores.get("cross_dept", 0) < 4:
            improvements.append("🔧 增强团队跨部门性（ Churchill 打破党派壁垒）")
        if scores.get("decision_speed", 5) < 4:
            improvements.append("🔧 加快决策节奏（ Churchill 标准：≤72小时）")
        if scores.get("celebration", 5) < 3:
            improvements.append("🔧 建立每周胜利庆祝机制（ Churchill : '即使小胜也要庆祝'）")
        
        return improvements if improvements else ["✅ 各项指标符合 Churchill 标准，继续保持"]
    
    def generate_team_handbook(self, team_config: Dict) -> str:
        """生成团队手册"""
        handbook = f"""
# 🦞 {team_config['危机类型']}危机团队手册

##  Churchill 式团队核心

### 团队构成
- 核心团队规模: {team_config['核心团队规模']}人（ Churchill 标准）
-  Churchill 参考: {team_config[' Churchill 参考']}

### 角色与授权

{chr(10).join([f"- **{role}**: {info[' Churchill 角色']}" for role, info in team_config['角色定义'].items()])}

###  Churchill 团队运作原则

1. **每日战时内阁**（ Churchill 战时内阁每日开会，风雨无阻）
2. **情报直接通道**（ Churchill 每日单独听情报简报）
3. **跨部门打破壁垒**（ Churchill 纳入工党领袖）
4. **结果导向授权**（ Churchill : "告诉我做什么，别告诉我怎么做"）
5. **每周胜利庆祝**（ Churchill 每次战役胜利立即庆祝）

### 沟通机制

- **每日**: {team_config['沟通机制']['daily']}
- **每周**: {team_config['沟通机制']['weekly']}
- **临时**: {team_config['沟通机制']['ad_hoc']}
- **1对1**: {team_config['沟通机制']['1on1']}

###  Churchill 授权金句

{chr(10).join([f'> "{quote}"' for quote in self.DELEGATION_QUOTES[:3]])}

---

* Churchill 说："The price of greatness is responsibility."*
* 本手册基于 Churchill 1940-1945年战时内阁实践
"""
        return handbook.strip()


# 快速测试
if __name__ == "__main__":
    architect = ChurchillTeamArchitect()
    
    # 构建一个200人企业的危机团队
    team = architect.build_team(200, "pr")
    
    print("=== Churchill 式危机团队构建方案 ===")
    print(f"组织规模: {team['组织规模']}人")
    print(f"核心团队: {team['核心团队规模']}人")
    print(f" Churchill 参考: {team[' Churchill 参考']}")
    
    print("\n角色定义:")
    for role, info in team['角色定义'].items():
        print(f"  {role}: {info[' Churchill 角色']} - {info['授权']}")
    
    print("\n Churchill 核心原则:")
    for principle in team[' Churchill 原则']:
        print(f"  • {principle}")
    
    print("\n沟通机制:")
    for k, v in team['沟通机制'].items():
        print(f"  {k}: {v}")
    
    print("\n危机特殊调整:")
    for k, v in team['危机特殊调整'].items():
        print(f"  {k}: {v}")
    
    print("\n" + "="*50)
    print("团队健康度检查:")
    checklist = architect.get_team_health_checklist()
    for item in checklist:
        print(f"\n{item['检查项']}")
        print(f"   Churchill 标准: {item[' Churchill 标准']}")
        print(f"   格言: {item[' Churchill 格言']}")
    
    print("\n" + "="*50)
    print("团队手册预览:")
    print(architect.generate_team_handbook(team)[:800] + "...")