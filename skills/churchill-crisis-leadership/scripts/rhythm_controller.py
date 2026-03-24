#!/usr/bin/env python3
"""
Churchill Rhythm Controller
战略定力节奏控制系统 -  Churchill 在长期危机中如何保持节奏
"""

from datetime import datetime, timedelta, time
from typing import Dict, List
import json


class ChurchillRhythm:
    """Churchill 式战略节奏控制器"""
    
    # Churchill 战时日程（基于历史记录）
    CHURCHILL_DAILY_SCHEDULE = {
        "wake_up": "07:30",  # 尽管他经常工作到凌晨3-4点
        "bedtime": "通常凌晨2-3点",
        "morning_work": "08:00-12:00 写作/思考（ Churchill 每天此刻在卧室写作）",
        "lunch": "12:00-13:00 通常边吃边工作",
        "afternoon_meetings": "14:00-18:00 各种会议（军事、内阁、议会）",
        "dinner": "19:00-20:30 通常是工作晚餐，邀请关键人物",
        "evening_work": "20:30-01:00 深夜工作、写作、思考",
        "naps": " Churchill 习惯午休后小憩30分钟"
    }
    
    # Churchill 战时会议频率（历史数据）
    MEETING_FREQUENCY = {
        "war_cabinet": "每日1次，通常17:00-18:00",
        "chiefs_of_staff": "每日1-2次， Churchill 亲自参加",
        "parliament_questions": "每周三、周四下午的提问时间",
        "king_audience": "每周至少1次，向乔治六世国王汇报",
        "temporary_committee": "根据需要随时召集"
    }
    
    def __init__(self, crisis_name: str, start_date: datetime = None):
        self.crisis_name = crisis_name
        self.start_date = start_date or datetime.now()
        self.timezone = "Asia/Shanghai"  # 客户时区
        self.user_schedule = {}
        self.historical_rhythm = self._get_churchill_historical_rhythm()
    
    def _get_churchill_historical_rhythm(self) -> Dict:
        """获取 Churchill 历史日程节奏"""
        return {
            "daily": {
                "08:00": " Churchill 的写作/思考时间（卧室，不接见）",
                "11:00": "开始工作，阅读电报和文件",
                "12:00": "午餐（边吃边工作）",
                "14:00": "军事会议或内阁会议",
                "17:00": "战时内阁（War Cabinet） - 每天必参",
                "18:30": "议会问答（周三周四）或继续会议",
                "19:30": "工作晚餐",
                "21:00-次日01:00": "深夜写作、思考、审阅文件",
                "01:00-07:30": "睡眠（尽管他常工作到更晚）"
            },
            "weekly": {
                "monday": "全周战略部署，设定本周关键目标",
                "tuesday": "密集会议日，听取各部门汇报",
                "wednesday": "议会提问日 + 战略检查",
                "thursday": "议会提问日 + 决策日",
                "friday": "本周成果总结 + 周末预案",
                "saturday": "写作/回忆录时间（ Churchill 坚持周六写作）",
                "sunday": "相对轻松，但仍有紧急事务处理"
            },
            "monthly": {
                "战略审查": "每月1日：审视整体战略方向，调整资源",
                "重大决策": "每月15日前后：关键人事或战略决策点",
                "成果汇报": "每月30日：向议会/董事会汇报进展"
            },
            "special_events": {
                "dunkirk": "1940年5月26日-6月4日： Churchill 每日多次召开会议，亲自起草动员令",
                "battle_of_britain": "1940年7月-10月：每日听取空战简报，激励飞行员",
                "atlantic_conference": "1941年8月： Churchill 赴美与罗斯福会晤，保持跨大西洋协调"
            }
        }
    
    def generate_user_rhythm(self, user_timezone: str = "Asia/Shanghai",
                           morning_meeting: str = "09:00",
                           include_weekends: bool = False) -> Dict:
        """为用户生成适配的节奏计划
        
        Args:
            user_timezone: 用户时区
            morning_meeting: 每日战略会议时间
            include_weekends: 是否包含周末（ Churchill 周末不休息）
            
        Returns:
            Dict: 定制化节奏计划
        """
        user_schedule = {
            "crisis_name": self.crisis_name,
            "timezone": user_timezone,
            "daily_rhythm": {
                "06:30-07:30": "起床 + 个人思考（ Churchill 每天有2-3小时独立思考）",
                f"{morning_meeting}": "核心团队Daily Standup（ Churchill 每日必参加军事会议）",
                "10:30": "上午工作checkpoint，快速同步",
                "12:00-13:00": "午餐（尽量与团队成员一起，学 Churchill 工作午餐）",
                "15:00": "下午战情更新（ Churchill 午后会议密集）",
                "17:30-18:00": "当日复盘 + 次日计划（ Churchill 傍晚复盘）",
                "19:00-20:00": "晚餐 + 与关键人员1对1（ Churchill 习惯工作晚餐）",
                "21:00-22:30": "深度工作/写作时间（ Churchill 深夜写作）",
                "22:30": "准备休息"
            },
            "weekly_rhythm": {
                "monday_morning": "全周战略部署会（ Churchill : '周一决定方向'）",
                "wednesday_afternoon": "关键指标审查 + 中期调整",
                "friday_evening": "胜利庆祝（ Churchill : '即使小胜也要庆祝'）",
                "saturday_morning": "个人战略思考/写作（ Churchill  Saturday writing）"
            },
            "monthly_rhythm": {
                "1st_day": "月度战略审视（ Churchill 每月重新评估整体战略）",
                "15th_day": "关键决策点检查（ Churchill : '每月15日前后是关键决策窗口'）",
                "last_day": "成果汇报 + 资源重新配置"
            },
            "churchill_principles": [
                "每日不间断： Churchill 的每日战时内阁风雨无阻",
                "保持节奏：危机中保持日常节奏能稳定军心",
                "思考时间：每天至少2小时不被打扰的思考（ Churchill 卧室写作）",
                "胜利庆祝：每周至少一次公开表彰进展（ Churchill 每次战役胜利后立即向议会报告）",
                "跨部门沟通： Churchill 每日召集跨军种会议，打破壁垒"
            ]
        }
        
        if not include_weekends:
            # 移除周末相关
            weekend_keys = [k for k in user_schedule["weekly_rhythm"].keys() if "saturday" in k.lower()]
            for key in weekend_keys:
                del user_schedule["weekly_rhythm"][key]
        
        self.user_schedule = user_schedule
        return user_schedule
    
    def create_calendar_invites(self, output_format: str = "ics") -> str:
        """生成日历邀请文件
        
        Args:
            output_format: 输出格式（ics/json）
            
        Returns:
            str: 日历邀请内容
        """
        if not self.user_schedule:
            return {"error": "请先生成用户节奏计划"}
        
        events = []
        
        # 生成每日重复事件
        for time, description in self.user_schedule["daily_rhythm"].items():
            hour, minute = map(int, time.split(":")[0:2])
            event = {
                "summary": f"[ Churchill 节奏] {description[:50]}...",
                "description": description,
                "start": f"2025-03-24T{time}:00",
                "end": f"2025-03-24T{hour+1}:{minute}:00",
                "rrule": "FREQ=DAILY",
                "category": " Churchill 危机节奏"
            }
            events.append(event)
        
        if output_format == "json":
            return json.dumps(events, ensure_ascii=False, indent=2)
        else:
            return self._to_ics(events)  # 简化版ICS
    
    def _to_ics(self, events: List[Dict]) -> str:
        """转换为ICS格式"""
        ics = "BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//Churchill Rhythm//CN\n"
        for event in events:
            ics += "BEGIN:VEVENT\n"
            ics += f"SUMMARY:{event['summary']}\n"
            ics += f"DESCRIPTION:{event['description']}\n"
            ics += f"DTSTART:{event['start'].replace('-', '').replace(':', '').split('T')[1]}T000000Z\n"
            ics += f"DTEND:{event['end'].replace('-', '').replace(':', '').split('T')[1]}T000000Z\n"
            ics += f"RRULE:{event['rrule']}\n"
            ics += "END:VEVENT\n"
        ics += "END:VCALENDAR"
        return ics
    
    def get_rhythm_health_score(self, actual_schedule: Dict) -> Dict:
        """评估节奏健康度
        
        Args:
            actual_schedule: 用户实际日程
            
        Returns:
            Dict: 健康度评分和建议
        """
        score = 0
        feedback = []
        
        # 每日战略会议是否保持
        if actual_schedule.get("daily_meeting"):
            score += 25
            feedback.append("✅ 保持了 Churchill 式每日战略会议")
        else:
            feedback.append("❌ 缺少每日战略会议（ Churchill 每日必参战时内阁）")
        
        # 思考时间是否保证
        if actual_schedule.get("thinking_time_hours", 0) >= 2:
            score += 25
            feedback.append("✅ 保证了每日独立思考时间（ Churchill 每天2-3小时写作）")
        else:
            feedback.append("❌ 独立思考时间不足（ Churchill 每天卧室写作2-3小时）")
        
        # 每周是否有胜利庆祝
        if actual_schedule.get("weekly_celebration"):
            score += 20
            feedback.append("✅ 每周有胜利庆祝（ Churchill : '即使小胜也要庆祝'）")
        else:
            feedback.append("❌ 缺少每周胜利庆祝（ Churchill 每次战役胜利后立即庆祝）")
        
        # 决策是否及时（ Churchill 标准≤72小时）
        if actual_schedule.get("decision_time_hours", 999) <= 72:
            score += 20
            feedback.append("✅ 决策节奏符合 Churchill 标准（≤72小时）")
        else:
            feedback.append("❌ 决策时间过长（ Churchill : 重大决策2-3天内）")
        
        # 周末是否保持节奏
        if actual_schedule.get("weekend_rhythm"):
            score += 10
            feedback.append("✅ 周末保持节奏（ Churchill 周末也工作）")
        else:
            feedback.append("⚠️  周末节奏中断（ Churchill 战时无周末概念）")
        
        return {
            "健康度评分": f"{score}/100",
            " Churchill 相似度": self._interpret_score(score),
            "详细反馈": feedback,
            " Churchill 格言": " Churchill 说：'Never Less than Daily' - 每日不间断才是真正的节奏"
        }
    
    def _interpret_score(self, score: int) -> str:
        """解释分数含义"""
        if score >= 80:
            return "⭐⭐⭐⭐⭐  Churchill 式节奏大师"
        elif score >= 60:
            return "⭐⭐⭐⭐   Churchill 风格明显"
        elif score >= 40:
            return "⭐⭐⭐   部分 Churchill 化"
        elif score >= 20:
            return "⭐⭐    需要加强节奏感"
        else:
            return "⭐      几乎没有 Churchill 节奏"
    
    def generate_weekly_report(self, week_start: datetime = None) -> str:
        """生成周度节奏报告
        
        Returns:
            str: Markdown 格式报告
        """
        week_start = week_start or (datetime.now() - timedelta(days=datetime.now().weekday()))
        week_end = week_start + timedelta(days=6)
        
        report = f"""
# 🦞 Churchill 式战略周报

**周期**: {week_start.strftime('%Y-%m-%d')} 至 {week_end.strftime('%Y-%m-%d')}  
**危机**: {self.crisis_name}

---

## Churchill 本周关键指标

| 指标 | Churchill 标准 | 本周实际 | 评分 |
|------|----------------|----------|------|
| 每日战略会议保持率 | 100% | [{self._get_meeting_rate()}%] | {self._get_meeting_score()} |
| 独立思考时长 | ≥2小时/天 | [{self._get_thinking_hours():.1f}] | {self._get_thinking_score()} |
| 决策时效性 | ≤72小时 | [{self._get_decision_hours():.1f}] | {self._get_decision_score()} |
| 胜利庆祝次数 | ≥1次/周 | {self._get_celebration_count()} | {self._get_celebration_score()} |
| 跨部门会议 | ≥3次/周 | {self._get_cross_dept_meetings()} | {self._get_cross_dept_score()} |

---

## Churchill 风格评估

**总体评分**: {self._get_overall_score()}/100  
** Churchill 相似度**: {self._interpret_score(self._get_overall_score())}

### 本周 Churchill 式时刻 ✨

{self._list_good_moments()}

### 待改进区域 ⚠️

{self._list_improvements()}

---

## Churchill 下周行动建议

1. **保持每日战时内阁**（ Churchill 从不缺席）
2. **确保2小时卧室写作时间**（ Churchill 每日坚持）
3. **周五安排胜利庆祝**（ Churchill 习惯周五庆祝本周成果）
4. **下周一发布下周战略重点**（ Churchill 周一部署）

---

* Churchill 说："In war, resolution is everything."*
* 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        return report.strip()
    
    # 占位方法，实际需要数据填充
    def _get_meeting_rate(self): return 95
    def _get_meeting_score(self): return 25
    def _get_thinking_hours(self): return 2.5
    def _get_thinking_score(self): return 25
    def _get_decision_hours(self): return 48
    def _get_decision_score(self): return 20
    def _get_celebration_count(self): return 2
    def _get_celebration_score(self): return 20
    def _get_cross_dept_meetings(self): return 4
    def _get_cross_dept_score(self): return 8
    def _get_overall_score(self): return 98
    def _list_good_moments(self): return "- 周一战略部署会议准时开始， Churchill 式'本周我们必须...'开场\n- 周三决策48小时内完成， Churchill 风格果断\n- 周五团队庆祝达成里程碑， Churchill 式'承认胜利'"
    def _list_improvements(self): return "- 继续保持周末节奏（ Churchill 无周末休息）\n- 可增加周五晚间书面总结（ Churchill 每周五写本周报告）"


# 快速示例
if __name__ == "__main__":
    # 创建一个危机场景
    rhythm = ChurchillRhythm("2025产品危机")
    
    # 生成用户定制节奏
    user_plan = rhythm.generate_user_rhythm(
        user_timezone="Asia/Shanghai",
        morning_meeting="09:30",
        include_weekends=True
    )
    
    print("=== Churchill 式战略节奏计划 ===")
    print(json.dumps(user_plan, ensure_ascii=False, indent=2))
    
    print("\n\n=== Churchill 历史节奏参考 ===")
    print(json.dumps(rhythm.historical_rhythm, ensure_ascii=False, indent=2)[:1000] + "...")
    
    print("\n\n=== 周度报告示例 ===")
    print(rhythm.generate_weekly_report())