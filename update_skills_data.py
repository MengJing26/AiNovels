#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将24个新技能包添加到skills_data.js文件中
"""

# 24个新技能包的数据
new_skills = [
    {
        "id": "antoninus-pius-piety-governance",
        "name": "安敦尼·庇护仁爱与系统化治理引擎",
        "nameEn": "Antoninus Pius Piety & Systematic Governance Engine",
        "author": "蒙境AI",
        "authorEn": "Mengjing AI",
        "created": "2026-03-27",
        "version": "1.0.0",
        "tags": ["governance", "leadership", "stability", "roman-history"],
        "rating": 4.7,
        "pricing": {"personal": 149, "professional": 449, "enterprise": 1999, "premium": 6999},
        "file": "skills/antoninus-pius-piety-governance/SKILL.md",
        "sizeKB": 15.9,
        "description": "将安敦尼·庇护23年零重大战争的治理实践系统化，形成仁爱治理+系统化决策+财政审慎+文化融合+法律公正+权力过渡的完整框架",
        "coreFormula": "和平繁荣 = (仁爱治理 × 系统化决策) + (财政审慎 × 文化融合) + (法律公正 × 权力过渡)",
        "scenarios": ["成熟组织稳定期管理", "CEO/高管领导力培养", "政府治理", "企业文化建设", "继任规划", "危机后恢复期"],
        "uniqueValue": "唯一23年零重大战争的历史验证，仁爱治理可量化",
        "commercialPotential": "$10-30M/年"
    },
    {
        "id": "benjamin-franklin-self-improvement-civic-innovation",
        "name": "本杰明·富兰克林自我改进与 Civic Innovation 引擎",
        "nameEn": "Benjamin Franklin Self-Improvement & Civic Innovation Engine",
        "author": "蒙境AI",
        "authorEn": "Mengjing AI",
        "created": "2026-03-27",
        "version": "1.0.0",
        "tags": ["self-improvement", "civic", "innovation", "networking"],
        "rating": 4.7,
        "pricing": {"personal": 149, "professional": 449, "enterprise": 1999, "premium": 6999},
        "file": "skills/benjamin-franklin-self-improvement-civic-innovation/SKILL.md",
        "sizeKB": 19.6,
        "description": "13项美德系统+Junto俱乐部+实用发明+网络构建+自我神话=个人到社会的完整成长路径",
        "coreFormula": "multifold impact = (自律系统 × 持续改进) + (实用发明 × civic institution-building) + (network building × diplomatic influence)",
        "scenarios": ["个人效率提升", "团队文化建设", "社区/NGO组织孵化", "创业者multifold成长路径", "社会企业设计", "知识社区运营"],
        "uniqueValue": "200+年验证的美德追踪系统，个人成长到社会贡献的完整路径",
        "commercialPotential": "$15-30M/年"
    },
    {
        "id": "constantine-the-great-religious-transformation",
        "name": "君士坦丁大帝宗教转型与帝国重构引擎",
        "nameEn": "Constantine the Great Religious Transformation & Empire Reconstruction Engine",
        "author": "蒙境AI",
        "authorEn": "Mengjing AI",
        "created": "2026-03-27",
        "version": "1.0.0",
        "tags": ["transformation", "religious", "empire", "strategy"],
        "rating": 4.6,
        "pricing": {"personal": 149, "professional": 449, "enterprise": 1999, "premium": 6999},
        "file": "skills/constantine-the-great-religious-transformation/SKILL.md",
        "sizeKB": 16.6,
        "description": "军事胜利合法性+宗教政策工具+首都重构+行政改革+货币稳定+王朝规划=帝国转型完整路径",
        "coreFormula": "帝国重生 = (军事胜利合法性 × 宗教政策工具) + (首都重构 × 行政改革) + (货币稳定 × 王朝规划)",
        "scenarios": ["组织危机后合法性重建", "企业/国家品牌重塑", "总部迁移或地理战略重构", "行政体系改革与效率提升", "货币或定价体系稳定化", "家族企业多子女继承规划"],
        "uniqueValue": "唯一整合军事-宗教-首都-行政-货币-继承六维转型系统",
        "commercialPotential": "$10-30M/年"
    },
    {
        "id": "dali-creative-system-cross-border",
        "name": "达利创意系统与跨界变现引擎",
        "nameEn": "Dali Creative System & Cross-Border Monetization Engine",
        "author": "蒙境AI",
        "authorEn": "Mengjing AI",
        "created": "2026-03-27",
        "version": "1.0.0",
        "tags": ["creative", "art", "innovation", "personal-branding"],
        "rating": 4.5,
        "pricing": {"personal": 149, "professional": 449, "enterprise": 1999, "premium": 6999},
        "file": "skills/dali-creative-system-cross-border/SKILL.md",
        "sizeKB": 19.1,
        "description": "偏执狂批判法+潜意识挖掘+跨界融合+自我神话构建+商业变现+争议营销=颠覆性创意全链路",
        "coreFormula": "颠覆性创意 = (偏执狂批判法 × 潜意识挖掘) + (跨界融合 × 自我神话构建) + (商业变现 × 争议营销)",
        "scenarios": ["创意行业", "个人品牌打造", "创意工作流程优化", "跨领域创新", "艺术品商业化", "内容创作"],
        "uniqueValue": "唯一将'偏执'系统化为创意方法，全链路创意变现",
        "commercialPotential": "$10-20M/年"
    },
    {
        "id": "ford-assembly-line",
        "name": "福特流水线生产方法论",
        "nameEn": "Ford Assembly Line Production Methodology",
        "author": "蒙境AI (基于亨利·福特生产体系)",
        "authorEn": "Mengjing AI (Based on Henry Ford Production System)",
        "created": "2026-03-29",
        "version": "1.0.0",
        "tags": ["manufacturing", "efficiency", "standardization", "innovation"],
        "rating": 4.8,
        "pricing": {"personal": 149, "professional": 449, "enterprise": 1999, "premium": 6999},
        "file": "skills/ford-assembly-line/SKILL.md",
        "sizeKB": 20.1,
        "description": "流水线设计器+垂直整合决策引擎+高工资低价格模型+成本压缩循环+学习曲线效应=大规模生产革命框架",
        "coreFormula": "productivity_gain = (传统周期时间 - 流水线周期时间) / 传统周期时间",
        "scenarios": ["制造业", "物流仓储", "软件工程", "服务业", "任何重复性、可分解、产量>10K/年的业务"],
        "uniqueValue": "效率革命的奠基系统，从作坊式到流水线的完整路径",
        "commercialPotential": "$15-30M/年"
    },
    {
        "id": "hadrian-empire-governance-resilience",
        "name": "哈德良帝国治理与韧性构建引擎",
        "nameEn": "Hadrian Empire Governance & Resilience Building Engine",
        "author": "蒙境AI",
        "authorEn": "Mengjing AI",
        "created": "2026-03-27",
        "version": "1.0.0",
        "tags": ["governance", "resilience", "leadership", "empire"],
        "rating": 4.8,
        "pricing": {"personal": 149, "professional": 449, "enterprise": 1999, "premium": 6999},
        "file": "skills/hadrian-empire-governance-resilience/SKILL.md",
        "sizeKB": 16.4,
        "description": "边疆防御ROI+文化统一与地方自治平衡+危机预防巡视系统+养子继承制与领导力过渡=从扩张到治理的转型框架",
        "coreFormula": "韧性 = (边疆防御 × 文化整合) + (危机预防 × 领导力魅力) + (制度传承 × 可持续发展)",
        "scenarios": ["企业帝国多区域/多国家业务整合", "集团管控", "危机管理", "组织韧性", "领导力传承"],
        "uniqueValue": "从'扩张思维'到'韧性思维'的转型框架，量化治理指标",
        "commercialPotential": "$10-30M/年"
    },
    {
        "id": "hanfeizi-legalist-governance",
        "name": "韩非子法家治理引擎",
        "nameEn": "Hanfei Legalist Governance Engine",
        "author": "韩非（思想）+ 蒙境AI（封装）",
        "authorEn": "Hanfei (Philosophy) + Mengjing AI (Packaging)",
        "created": "2026-03-28",
        "version": "1.0.0",
        "tags": ["governance", "compliance", "performance-management", "legalist", "ancient-chinese-philosophy"],
        "rating": 4.6,
        "pricing": {"personal": 99, "professional": 499, "enterprise": 1999, "premium": 5999},
        "file": "skills/hanfeizi-legalist-governance/SKILL.md",
        "sizeKB": 7.4,
        "description": "法(规则引擎)+术(行政技法)+势(权威维护)+五蠹净化+考功黜陟=法家集大成系统",
        "coreFormula": "LawClarity = (规则数量 × 平均条文可读性得分) / (10 × 违规类型数)",
        "scenarios": ["初创公司建立合规与绩效体系", "传统企业转型", "政府部门/事业单位效能诊断与改革", "家族企业治理", "危机中出现效率下滑的组织", "需要快速建立权威的新任领导"],
        "uniqueValue": "法家思想集大成者，可量化治理效率",
        "commercialPotential": "$8-18M/年"
    },
    {
        "id": "herbert-simon-bounded-rationality",
        "name": "赫伯特·西蒙跨学科创新与决策理论引擎",
        "nameEn": "Herbert Simon Cross-Disciplinary Innovation & Decision Theory Engine",
        "author": "蒙境AI",
        "authorEn": "Mengjing AI",
        "created": "2026-03-27",
        "version": "1.0.0",
        "tags": ["decision-making", "bounded-rationality", "innovation", "cognitive-science"],
        "rating": 4.6,
        "pricing": {"personal": 149, "professional": 449, "enterprise": 1999, "premium": 6999},
        "file": "skills/herbert-simon-bounded-rationality/SKILL.md",
        "sizeKB": 14.2,
        "description": "有限理性+satisficing+符号主义AI+认知架构+问题求解启发式+跨领域迁移=诺贝尔+图灵奖跨界思维",
        "coreFormula": "跨学科创新 = (有限理性 × satisficing) + (符号主义 AI + 认知架构) + (问题求解启发式 + 跨领域迁移)",
        "scenarios": ["Decision support systems", "Behavioral economics", "Symbolic AI", "Expert systems", "Cognitive science", "Cross-disciplinary innovation", "Organisational decision processes"],
        "uniqueValue": "有限理性颠覆完全理性假设，更贴近真实决策",
        "commercialPotential": "$10-20M/年"
    },
    {
        "id": "inamori-altruism-amoeba",
        "name": "稻盛和夫利他经营哲学与阿米巴管理系统",
        "nameEn": "Kazuo Inamori Altruism & Amoeba Management System",
        "author": "蒙境AI",
        "authorEn": "Mengjing AI",
        "created": "2026-03-27",
        "version": "1.0.0",
        "tags": ["management", "amoeba", "altruism", "japanese"],
        "rating": 4.7,
        "pricing": {"personal": 149, "professional": 449, "enterprise": 1999, "premium": 6999},
        "file": "skills/inamori-altruism-amoeba/SKILL.md",
        "sizeKB": 15.4,
        "description": "阿米巴管理+利他哲学+全员哲学+现场主义+危机turnaround+持续精进=日式经营哲学完整体系",
        "coreFormula": "日式经营哲学 = (阿米巴管理 × 利他精神) + (全员哲学 + 现场主义) + (危机 turnaround × 持续精进)",
        "scenarios": ["Japanese-style management acquisition/transformation", "Crisis turnaround", "中小企业 engagement 提升", "Corporate culture building", "Cost-cutting + employee morale", "Leadership development"],
        "uniqueValue": "唯一阿米巴+利哲学+现场+turnaround四合一，日航12个月扭亏为盈案例",
        "commercialPotential": "$20-40M/年"
    },
    {
        "id": "justinian-corpus-juris",
        "name": "查士丁尼法典编纂与帝国复兴引擎",
        "nameEn": "Justinian Corpus Juris & Empire Revival Engine",
        "author": "蒙境AI",
        "authorEn": "Mengjing AI",
        "created": "2026-03-29",
        "version": "1.0.0",
        "tags": ["legal", "governance", "empire", "project-management"],
        "rating": 4.7,
        "pricing": {"personal": 149, "professional": 449, "enterprise": 1999, "premium": 6999},
        "file": "skills/justinian-corpus-juris/SKILL.md",
        "sizeKB": 10.7,
        "description": "法典编纂系统+法律工程与合规转换器+大规模项目资本配置引擎+危机与韧性决策系统+标准化与流程管理=帝国复兴三部曲",
        "coreFormula": "帝国复兴 = (法典编纂系统 × 法律工程能力) + (军事再征服 × 资本配置) + (标准化行政 × 大规模项目管理)",
        "scenarios": ["跨国企业合规整合", "地方政府应急管理", "大型基建项目群"],
        "uniqueValue": "唯一整合法典编纂+危机管理+资本配置三位一体的系统",
        "commercialPotential": "$15-30M/年"
    },
    {
        "id": "mozi-utilitarian-governance",
        "name": "墨子兼爱非攻与实用主义治理引擎",
        "nameEn": "Mozi Utilitarian Governance Engine",
        "author": "墨子（思想）+ 蒙境AI（封装）",
        "authorEn": "Mozi (Philosophy) + Mengjing AI (Packaging)",
        "created": "2026-03-28",
        "version": "1.0.0",
        "tags": ["governance", "utilitarianism", "meritocracy", "frugality", "peace", "chinese-philosophy", "decision-making"],
        "rating": 4.7,
        "pricing": {"personal": 99, "professional": 499, "enterprise": 1999, "premium": 5999},
        "file": "skills/mozi-utilitarian-governance/SKILL.md",
        "sizeKB": 9.3,
        "description": "兼爱公平性诊断+非攻冲突避免+尚贤meritocracy系统+节用效率优化+天志alignment=普遍利益为核心的治理系统",
        "coreFormula": "UBS = Σ(wi × Benefiti)",
        "scenarios": ["政府政策制定与影响评估", "企业治理与董事会决策", "人力资源：晋升、招聘、绩效体系设计", "预算分配与成本控制", "企业战略：避免恶性竞争", "ESG/Corporate Social Responsibility 评估"],
        "uniqueValue": "用'利'衡量一切政策，兼爱非攻实现共赢",
        "commercialPotential": "$10-25M/年"
    },
    {
        "id": "qian-xuesen-system-engineering",
        "name": "钱学森系统工程方法论",
        "nameEn": "Qian Xuesen System Engineering Methodology",
        "author": "蒙境AI (基于钱学森系统工程理论)",
        "authorEn": "Mengjing AI (Based on Qian Xuesen System Engineering Theory)",
        "created": "2026-03-29",
        "version": "1.0.0",
        "tags": ["system-engineering", "complex-systems", "project-management", "innovation"],
        "rating": 4.9,
        "pricing": {"personal": 149, "professional": 449, "enterprise": 1999, "premium": 6999},
        "file": "skills/qian-xuesen-system-engineering/SKILL.md",
        "sizeKB": 22.0,
        "description": "系统工程架构设计器+技术科学思想+综合集成法+反馈控制+人机协同+战略前瞻=复杂系统设计与managed evolution框架",
        "coreFormula": "system_quality = (hierarchy_clear×0.3) + (interface_defined×0.3) + (modularity×0.2) + (scalability×0.2)",
        "scenarios": ["大型工程项目", "企业级产品/技术架构", "R&D portfolio management", "国家产业规划", "公共政策设计"],
        "uniqueValue": "两弹一星成功验证的系统工程方法论，复杂系统设计的顶层框架",
        "commercialPotential": "$20-40M/年"
    },
    {
        "id": "ren-zhengfei-huawei",
        "name": "任正非华为管理方法论",
        "nameEn": "Ren Zhengfei Huawei Management Methodology",
        "author": "蒙境AI (基于任正非华为管理实践)",
        "authorEn": "Mengjing AI (Based on Ren Zhengfei Huawei Management Practice)",
        "created": "2026-03-29",
        "version": "1.0.0",
        "tags": ["management", "leadership", "organization", "china-tech"],
        "rating": 4.8,
        "pricing": {"personal": 149, "professional": 449, "enterprise": 1999, "premium": 6999},
        "file": "skills/ren-zhengfei-huawei/SKILL.md",
        "sizeKB": 22.0,
        "description": "灰度理论+奋斗者文化+战略聚焦+压强原则+铁三角协同+流程再造+自我批判+活下去哲学=华为崛起密码",
        "coreFormula": "gray_zone_score = (ambiguity_tolerance×0.4) + (compromise_skill×0.3) + (dynamic_adjustment×0.3)",
        "scenarios": ["高成长科技企业", "全球化公司", "从初创向规模化转型", "面临大公司病", "需要建立技术护城河和长期竞争力"],
        "uniqueValue": "20万人30年验证的中国式管理方法论，灰度+奋斗者+压强+铁三角组合",
        "commercialPotential": "$25-50M/年"
    },
    {
        "id": "rockefeller-monopoly-philanthropy",
        "name": "洛克菲勒垄断构建与慈善商业模式",
        "nameEn": "Rockefeller Monopoly Construction & Philanthropy Business Model",
        "author": "蒙境AI",
        "authorEn": "Mengjing AI",
        "created": "2026-03-27",
        "version": "1.0.0",
        "tags": ["monopoly", "philanthropy", "business", "family-office"],
        "rating": 4.6,
        "pricing": {"personal": 149, "professional": 449, "enterprise": 1999, "premium": 6999},
        "file": "skills/rockefeller-monopoly-philanthropy/SKILL.md",
        "sizeKB": 14.5,
        "description": "垂直整合与成本控制+Acquisition整合+Trust治理结构+慈善商业模式+家族治理=从垄断到慈善的完整路径",
        "coreFormula": "垄断构建 = (垂直整合 × 成本控制) + (acquisition 整合 × trust 治理) + (慈善商业模式 × 家族治理)",
        "scenarios": ["行业整合", "传统行业成本优化", "高净值家族财富传承", "基金会/慈善项目管理", "反垄断合规", "Business model innovation"],
        "uniqueValue": "唯一从垄断到慈善的完整路径，家族5代传承成功案例",
        "commercialPotential": "$10-25M/年"
    },
    {
        "id": "sam-walton-retail-edlc",
        "name": "山姆·沃尔顿零售帝国与 EDLC 引擎",
        "name": "Sam Walton Retail Empire & EDLC Engine",
        "author": "蒙境AI",
        "authorEn": "Mengjing AI",
        "created": "2026-03-27",
        "version": "1.0.0",
        "tags": ["retail", "growth", "cost-leadership", "supply-chain"],
        "rating": 4.6,
        "pricing": {"personal": 149, "professional": 449, "enterprise": 1999, "premium": 6999},
        "file": "skills/sam-walton-retail-edlc/SKILL.md",
        "sizeKB": 13.5,
        "description": "EDLC定价引擎+小城镇扩张决策器+供应链数字化系统+客户痴迷+员工激励+快速铺开=零售帝国操作系统",
        "coreFormula": "零售帝国 = (EDLC × 规模效应) + (小城镇策略 × 客户痴迷) + (供应链科技 × 快速铺开) + (员工持股 × 节俭文化)",
        "scenarios": ["Retail chain expansion", "E-commerce & logistics", "Traditional retail digital transformation", "Supply chain optimization", "Cost leadership strategy", "Rural/underserved market penetration"],
        "uniqueValue": "沃尔玛全球10,000+店的经验，EDLC + 小城镇 + 供应链科技三合一",
        "commercialPotential": "$15-30M/年"
    },
    {
        "id": "septimius-severus-military-centralization",
        "name": "塞普蒂米乌斯·塞维鲁军事集权与帝国转型引擎",
        "nameEn": "Septimius Severus Military Centralization & Empire Transformation Engine",
        "author": "蒙境AI",
        "authorEn": "Mengjing AI",
        "created": "2026-03-27",
        "version": "1.0.0",
        "tags": ["transformation", "centralization", "authority", "crisis"],
        "rating": 4.4,
        "pricing": {"personal": 149, "professional": 449, "enterprise": 1999, "premium": 6999},
        "file": "skills/septimius-severus-military-centralization/SKILL.md",
        "sizeKB": 17.3,
        "description": "军事忠诚度购买计算器+财政集中化可行性评估+法律皇权化升级路径+家族继承与多子制衡系统=从军事到集权的转型框架",
        "coreFormula": "帝国转型 = (军事忠诚基础 × 财政集中化) + (法律工具化 × 家族继承规划)",
        "scenarios": ["危机组织权力重组", "政府/国企行政集权化改革", "企业并购后整合", "家族企业多子女继承规划", "机构改革", "国家紧急状态下的统治转型"],
        "uniqueValue": "唯一系统化军事→财政→法律→继承四步转型框架，军事忠诚度可量化",
        "commercialPotential": "$10-25M/年"
    },
    {
        "id": "solon-constitutional-reform",
        "name": "梭伦宪政改革方法论",
        "nameEn": "Solon Constitutional Reform Methodology",
        "author": "蒙境AI (基于梭伦历史研究)",
        "authorEn": "Mengjing AI (Based on Solon Historical Research)",
        "created": "2026-03-29",
        "version": "1.0.0",
        "tags": ["constitutional", "reform", "governance", "balance"],
        "rating": 4.6,
        "pricing": {"personal": 149, "professional": 449, "enterprise": 1999, "premium": 6999},
        "file": "skills/solon-constitutional-reform/SKILL.md",
        "sizeKB": 20.0,
        "description": "立法平衡度诊断器+权力制衡设计框架(SBAR)+经济-社会和解引擎+渐进式改革路线图+中庸之道计算器=改革平衡系统",
        "coreFormula": "legitimacy_score = (aristocracy_support×0.3) + (commoner_benefit×0.4) + (long_term_stability×0.3)",
        "scenarios": ["国家宪政转型", "多利益集团社会的立法平衡设计", "革命后的权力分配与制度重建", "国际多边谈判与条约设计", "企业/组织治理结构改革"],
        "uniqueValue": "在极端之间寻找让所有人都觉得'虽然不完美但可以接受'的中间道路",
        "commercialPotential": "$20-40M/年"
    },
    {
        "id": "taiichi-ohno-toyota-production-system",
        "name": "大野耐一精益制造与丰田生产系统引擎",
        "nameEn": "Taiichi Ohno Toyota Production System Engine",
        "author": "蒙境AI",
        "authorEn": "Mengjing AI",
        "created": "2026-03-27",
        "version": "1.0.0",
        "tags": ["manufacturing", "lean", "toyota", "kaizen"],
        "rating": 4.8,
        "pricing": {"personal": 149, "professional": 449, "enterprise": 1999, "premium": 6999},
        "file": "skills/taiichi-ohno-toyota-production-system/SKILL.md",
        "sizeKB": 15.9,
        "description": "7大浪费诊断+Just-in-Time效率公式+Jidoka质量内生系统+Kaizen持续改进引擎+看板可视化+5S现场主义=精益制造完整系统",
        "coreFormula": "精益革命 = (Just-in-Time × Jidoka) + (Kaizen × muda 消除) + (安灯系统 × 看板可视化) + (现场主义 + 员工赋能)",
        "scenarios": ["Manufacturing optimization", "Supply chain efficiency", "Operational excellence programs", "Lean transformation consulting", "跨行业应用", "Cost reduction + quality improvement"],
        "uniqueValue": "最系统化的制造操作系统TPS源头，50+年持续成功验证",
        "commercialPotential": "$30-60M/年"
    },
    {
        "id": "taylor-scientific-management",
        "name": "泰勒科学管理方法论",
        "nameEn": "Taylor Scientific Management Methodology",
        "author": "蒙境AI (基于 Frederick Winslow Taylor 科学管理理论)",
        "authorEn": "Mengjing AI (Based on Frederick Winslow Taylor Scientific Management Theory)",
        "created": "2026-03-29",
        "version": "1.0.0",
        "tags": ["management", "scientific", "efficiency", "standardization"],
        "rating": 4.7,
        "pricing": {"personal": 149, "professional": 449, "enterprise": 1999, "premium": 6999},
        "file": "skills/taylor-scientific-management/SKILL.md",
        "sizeKB": 19.4,
        "description": "时间-动作研究+标准化三维体系+差异计件制+职能制+持续改进与知识积累=效率革命框架",
        "coreFormula": "efficiency = (标准时间/实际当前时间) × (标准方法质量评分/采用方法质量评分)",
        "scenarios": ["制造业", "服务业", "知识工作", "医疗流程", "任何可重复、可测量的任务"],
        "uniqueValue": "效率革命的奠基人，时间-动作研究+标准化+计件制三要素",
        "commercialPotential": "$25-60M/年"
    },
    {
        "id": "tesla-innovation-system-ac-revolution",
        "name": "特斯拉创新系统与 AC 革命引擎",
        "nameEn": "Tesla Innovation System & AC Revolution Engine",
        "author": "蒙境AI",
        "authorEn": "Mengjing AI",
        "created": "2026-03-27",
        "version": "1.0.0",
        "tags": ["innovation", "technology", "patents", "showmanship"],
        "rating": 4.6,
        "pricing": {"personal": 149, "professional": 449, "enterprise": 1999, "premium": 6999},
        "file": "skills/tesla-innovation-system-ac-revolution/SKILL.md",
        "sizeKB": 22.7,
        "description": "Mental Prototyping训练系统+关键专利+商业合作引擎+演示营销+神秘主义品牌构建+韧劲培养=技术革命完整路径",
        "coreFormula": "技术革命 = (mental prototyping × 精确记忆) + (关键专利 × 商业合作时机) + (演示营销 × 神秘主义个人品牌) + (失败后 persistence)",
        "scenarios": ["硬科技创业", "工程师创新方法论", "专利策略与授权谈判", "技术产品发布会", "个人品牌打造", "技术扩散策略"],
        "uniqueValue": "唯一mental prototyping系统化，300+专利实战，AC革命完整路径",
        "commercialPotential": "$30-80M/年"
    },
    {
        "id": "theodosius-i-religious-unity-empire-transition",
        "name": "狄奥多西一世宗教统一与帝国转型引擎",
        "nameEn": "Theodosius I Religious Unity & Empire Transition Engine",
        "author": "蒙境AI",
        "authorEn": "Mengjing AI",
        "created": "2026-03-28",
        "version": "1.0.0",
        "tags": ["religion", "unity", "transformation", "governance"],
        "rating": 4.5,
        "pricing": {"personal": 149, "professional": 449, "enterprise": 1999, "premium": 6999},
        "file": "skills/theodosius-i-religious-unity-empire-transition/SKILL.md",
        "sizeKB": 10.7,
        "description": "宗教统一三阶段模型+蛮族融入与军事改革+行政集权与区域重组+王朝危机与过渡管理=转型操作系统",
        "coreFormula": "orthodox_adoption_rate = 信徒比例 × 0.6 + clergy比例 × 0.4",
        "scenarios": ["企业并购后文化整合", "多元化团队管理", "领导力继任规划", "大型组织区域重组", "价值观驱动变革"],
        "uniqueValue": "宗教统一+蛮族融入+分治+继承四维转型系统",
        "commercialPotential": "$10-25M/年"
    },
    {
        "id": "wang-chuanfu-byd-vertical-integration-new-energy",
        "name": "王传福 BYD 垂直整合与新能源革命引擎",
        "nameEn": "Wang Chuanfu BYD Vertical Integration & New Energy Revolution Engine",
        "author": "蒙境AI",
        "authorEn": "Mengjing AI",
        "created": "2026-03-28",
        "version": "1.0.0",
        "tags": ["manufacturing", "ev", "vertical-integration", "china-tech"],
        "rating": 4.4,
        "pricing": {"personal": 149, "professional": 449, "enterprise": 1999, "premium": 6999},
        "file": "skills/wang-chuanfu-byd-vertical-integration-new-energy/SKILL.md",
        "sizeKB": 13.0,
        "description": "垂直整合决策引擎+电池技术演进路线图+全产业链自研系统+政策借力与市场Timing+成本压缩与规模化=新能源革命引擎",
        "coreFormula": "vertical_integration_score = (tech_strategic×0.4) + (cost_sensitivity×0.3) + (supply_chain_risk×0.3)",
        "scenarios": ["硬件创业公司", "传统车企转型电动化", "新能源产业链投资", "制造业成本优化", "政策驱动行业战略"],
        "uniqueValue": "BYD逆袭路径，垂直整合+成本控制+政策借力的三引擎",
        "commercialPotential": "$15-30M/年"
    },
    {
        "id": "welch-ge-transformation-vitality-curve",
        "name": "韦尔奇企业转型与活力曲线引擎",
        "nameEn": "Welch GE Transformation & Vitality Curve Engine",
        "author": "蒙境AI",
        "authorEn": "Mengjing AI",
        "created": "2026-03-27",
        "version": "1.0.0",
        "tags": ["transformation", "performance", "vitality-curve", "leadership"],
        "rating": 4.5,
        "pricing": {"personal": 149, "professional": 449, "enterprise": 1999, "premium": 6999},
        "file": "skills/welch-ge-transformation-vitality-curve/SKILL.md",
        "sizeKB": 15.4,
        "description": "数一数二战略决策器+活力曲线强制分布系统+4E+1P领导力评估系统+全球化-六西格玛-电子商务Triad评估+Candid Feedback文化评估=企业转型完整playbook",
        "coreFormula": "企业转型 = (数一数二战略 × 活力曲线) + (全球化 + 六西格玛) + (领导力评估 × candid feedback)",
        "scenarios": ["Enterprise transformation", "Portfolio optimization", "Performance management overhaul", "Leadership development", "Culture change", "M&A integration"],
        "uniqueValue": "GE 20年27倍增长案例，数一数二+活力曲线+4E领导力三合一",
        "commercialPotential": "$10-20M/年"
    },
    {
        "id": "zhang-yiming-algorithmic-growth-globalization",
        "name": "字节跳动算法增长与全球化引擎",
        "nameEn": "Zhang Yiming Algorithmic Growth & Globalization Engine",
        "author": "张一鸣（思想）+ 蒙境AI（封装）",
        "authorEn": "Zhang Yiming (Philosophy) + Mengjing AI (Packaging)",
        "created": "2026-03-28",
        "version": "1.0.0",
        "tags": ["algorithm", "growth", "recommendation", "globalization", "data-driven"],
        "rating": 4.8,
        "pricing": {"personal": 149, "professional": 449, "enterprise": 1999, "premium": 6999},
        "file": "skills/zhang-yiming-algorithmic-growth-globalization/SKILL.md",
        "sizeKB": 8.5,
        "description": "推荐算法系统+全球化与本地化+产品迭代与A/B实验+数据驱动决策+组织扁平化与人才密度=算法增长操作系统",
        "coreFormula": "RecEff = α·CTR + β·停留时长 + γ·留存率 - δ·流失率",
        "scenarios": ["内容平台增长优化", "电商个性化推荐系统建设", "企业出海本地化与合规", "传统企业数字化转型", "创业公司从0到1打造增长引擎", "中型公司组织扁平化改革"],
        "uniqueValue": "字节跳动从0到1到全球化的增长方法论，算法+数据+组织三角",
        "commercialPotential": "$30-80M/年"
    },
    {
        "id": "zhuge-liang-strategic-management",
        "name": "诸葛亮战略管理体系",
        "nameEn": "Zhuge Liang Strategic Management System",
        "author": "蒙境AI",
        "authorEn": "Mengjing AI",
        "created": "2026-03-29",
        "version": "1.0.0",
        "tags": ["strategy", "governance", "leadership", "chinese-history"],
        "rating": 4.5,
        "pricing": {"personal": 149, "professional": 449, "enterprise": 1999, "premium": 6999},
        "file": "skills/zhuge-liang-strategic-management/SKILL.md",
        "sizeKB": 10.3,
        "description": "隆中对战略规划系统+蜀科法治管理体系+识人七法人才评估系统+木牛流马问题解决引擎+廉洁风险控制系统=诸葛亮战略管理完整系统",
        "coreFormula": "综合成功指数 = (战略清晰度 × 0.3) + (法治有效性 × 0.2) + (人才匹配度 × 0.2) + (技术创新率 × 0.15) + (廉洁控制力 × 0.15)",
        "scenarios": ["创业公司A轮/B轮战略定位", "中小企业3年规划", "项目组合管理", "家族企业转型决策", "核心岗位招聘", "晋升评估"],
        "uniqueValue": "隆中对+蜀科+识人七法+木牛流马+廉洁控制的五维战略系统",
        "commercialPotential": "$15-30M/年"
    }
]

import json

def main():
    # 读取原文件
    with open('D:/openclaw/AiNovelsOK/skills_data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 解析现有数据
    start_marker = '  "skills": ['
    end_marker = '  ],'
    
    start_idx = content.find(start_marker)
    end_idx = content.rfind(end_marker)
    
    if start_idx == -1 or end_idx == -1:
        print("错误：无法找到skills数组")
        return
    
    prefix = content[:start_idx + len(start_marker)]
    existing_skills = content[start_idx + len(start_marker):end_idx]
    suffix = content[end_idx + len(end_marker):]
    
    # 解析现有技能
    try:
        existing_skills_data = json.loads(existing_skills)
    except:
        print("错误：无法解析现有技能数据")
        return
    
    # 合并新旧技能
    all_skills = existing_skills_data + new_skills
    
    # 计算新的总数和平均评分
    new_total = len(all_skills)
    new_average = sum(skill.get("rating", 0) for skill in all_skills) / new_total
    
    # 更新头部信息
    new_prefix = f'''// AI Skills Marketplace Data - UPDATED
// 更新时间: {pd.Timestamp.now().strftime('%Y/%m/%d %H:%M:%S.%f')[:-3]}Z
// 总数: {new_total}个Skill (完整数据)
// 新增: 24个Skill (历史人物技能包)

const skillsData = {{
  "generated": "{pd.Timestamp.now().strftime('%Y-%m-%dT%H:%M:%S.%f')}Z",
  "total": {new_total},
  "averageRating": "{new_average:.2f}",
  "skills": {json.dumps(all_skills, ensure_ascii=False, indent=2)}'''
    
    # 写入新文件
    new_content = prefix[:-2] + '}\n\nexport default skillsData;'
    
    with open('D:/openclaw/AiNovelsOK/skills_data.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ 成功更新 skills_data.js 文件")
    print(f"📊 新总数: {new_total} (原71个 + 新增24个)")
    print(f"⭐ 新平均评分: {new_average:.2f}")
    print(f"📈 新增技能包:")
    for skill in new_skills:
        print(f"   - {skill['name']} ({skill['rating']}/5)")

if __name__ == "__main__":
    main()
