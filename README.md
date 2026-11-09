# EU4 修改存档（YG）

游戏：Europa Universalis IV v1.37.5.0 Inca（491d），安装于 `D:\steam\steamapps\common\Europa Universalis IV`。
本仓库按"仓库路径 → 游戏内路径"原样镜像存放，方便直接对拷回去。

## 目录对应

| 仓库路径 | 游戏内路径 |
|---|---|
| `eu4/events/lcs_events.txt` | `Europa Universalis IV\events\lcs_events.txt` |
| `eu4/common/event_modifiers/zz_lcs_event_modifiers.txt` | `Europa Universalis IV\common\event_modifiers\zz_lcs_event_modifiers.txt` |
| `eu4/localisation/lcs_l_english.yml` | `Europa Universalis IV\localisation\lcs_l_english.yml` |
| `eu4/localisation/lcs_l_simp_chinese.yml` | `Europa Universalis IV\localisation\lcs_l_simp_chinese.yml` |
| `eu4/events/lcs_great_powers.txt` | `Europa Universalis IV\events\lcs_great_powers.txt` |
| `eu4/common/event_modifiers/zz_lcs_great_power_modifiers.txt` | `Europa Universalis IV\common\event_modifiers\zz_lcs_great_power_modifiers.txt` |
| `eu4/localisation/lcs_gp_l_english.yml` | `Europa Universalis IV\localisation\lcs_gp_l_english.yml` |
| `eu4/localisation/lcs_gp_l_simp_chinese.yml` | `Europa Universalis IV\localisation\lcs_gp_l_simp_chinese.yml` |
| `tools/gen_great_powers.py` | 生成器，不在游戏目录内 |
| `eu4/common/static_modifiers/00_static_modifiers.txt` | `Europa Universalis IV\common\static_modifiers\00_static_modifiers.txt` |
| `workshop/Very_hard_ai_xorme_ai__3322593885/common/static_modifiers/xorme_static_modifiers.txt` | `steamapps\workshop\content\236850\3322593885\common\static_modifiers\xorme_static_modifiers.txt`（实际生效的那份） |
| `workshop/Xorme_AI__2451296932/common/static_modifiers/xorme_static_modifiers.txt` | `steamapps\workshop\content\236850\2451296932\common\static_modifiers\xorme_static_modifiers.txt`（同名文件被上面那份覆盖，属备用） |

---

## 一、自定义事件（新增）

`lcs_events.txt`，namespace `lcs`：

- `lcs.1`：`major = yes`、`fire_only_once = yes`、`trigger = { ai = no, NOT = { has_country_modifier = lcs_cheat_modifier } }`、`mean_time_to_happen = { days = 1 }` —— 开局几天自动弹。
- `lcs.2`：`is_triggered_only = yes`，同效果，用于控制台补发。

效果（`lcs_cheat_modifier`，`duration = -1` 永久）：

| 修正 | 数值 | 含义 |
|---|---|---|
| `core_creation` | -0.80 | 核心化花费 -80% |
| `development_cost` | -0.70 | 发展成本 -70%（原 -50% 再叠 -20%） |
| `years_of_nationalism` | -20 | 分离主义年数 -20 |
| `global_regiment_recruit_speed` | -0.50 | 募兵时间 -50% |
| `culture_conversion_time` | -0.90 | 文化转变时间 -90% |
| `culture_conversion_cost` | -0.80 | 文化转变花费 -80% |

本地化：`l_english` 与 `l_simp_chinese` 两份镜像（游戏语言是 `l_english`，与中文汉化包同做法），文件为 UTF-8 **带 BOM**。

触发方式：控制台需要 Steam 启动项 `-debug_mode`，进游戏按 `~` 输入 `event lcs.1` 或 `event lcs.2`。
事件与铁人/成就互斥（有 mod 本来也不出成就）。

## 二、极难（Very Hard）难度 AI 修正改写

三份 `difficulty_very_hard_ai` 同步改，保证换 mod 顺序或关 mod 时表现一致。

### 1. 去掉侵略扩张（AE）减免

| 文件 | 原值 | 现 |
|---|---|---|
| 3322593885 | `ae_impact = -1`（-100%） | 删除 |
| 2451296932 | `ae_impact = -0.33` | 删除 |
| 本体 00_static_modifiers.txt | `ae_impact = -0.33` | 删除 |

玩家侧：本体 `difficulty_very_hard_player` 本来就是空块，全部启用 mod 也没有任何一处给玩家加 AE 惩罚；两份 mod 文件里现补了显式空块 `difficulty_very_hard_player = { }`，防止将来被别的定义叠加。

### 2. 只强化陆军质量，海军加成清零

新增（陆军质量）：`land_morale = 0.15`（士气 +15%）、`discipline = 0.10`（训练 +10%）、`infantry_power = 0.10`、`cavalry_power = 0.10`、`artillery_power = 0.10`；3322593885 补 `land_forcelimit_modifier = 0.5`。

删除（海军）：`global_ship_cost`（-33% / -50%）、`naval_forcelimit_modifier`（+50%）。

保留的陆军相关项：`manpower_recovery_speed`、`global_manpower_modifier`、`global_regiment_cost`、`land_forcelimit_modifier`、`global_supply_limit_modifier` 等。

### 3. 仍存在的 AE 减免（未改动）

`xorme_static_modifiers.txt` 的 `luck` 块（幸运国家机制，不分难度）仍有 `ae_impact = -0.25`。要清零就删掉那一行。

## 三、主要国家 · 时代专属修正（新增）

`eu4/events/lcs_great_powers.txt`，namespace `lcs_gp`：12 组国家 / 54 个事件 / 54 个 `duration = -1` 专属修正（数值在 `eu4/common/event_modifiers/zz_lcs_great_power_modifiers.txt`）。

每个事件的触发条件 = 国家标签匹配 + 当前年份落在该时代区间 + 未持有该时代的 flag，`mean_time_to_happen = { days = 5 }`，进入时代后几天内自动弹出，点掉即永久生效；同一时代不会重复弹。国家若在后期才成立（如大清、大不列颠），只拿当前及之后时代的加成。

后期国家会拿到**衰退修正**：明自 1500 起逐级下滑、1600 年「大厦将倾」为大衰退，奥斯曼自 1600 年起停滞、1800 年「西亚病夫」，清 1800 年「嘉道中衰」；数值为负是刻意的历史模拟。满洲（建州/海西/野人女真/满洲）在 1600 年后获得「八旗」超强修正，并对明取得征服宣战理由。

每个修正都作用于**拥有该 tag 的国家本身**，玩家和 AI 一视同仁；只想给自己用，就在对应事件的 `trigger` 里加一行 `ai = no`。

| 国家 | 时代 | 修正 id | 效果 |
|---|---|---|---|
| 法兰西 | 1444–1499 | `lcs_fra_1` | 陆军士气 +10%；人力恢复 +10% |
| 法兰西 | 1500–1599 | `lcs_fra_2` | 步兵战斗力 +10%；陆军上限 +10% |
| 法兰西 | 1600–1699 | `lcs_fra_3` | 训练度 +5%；每年威望 +0.5；行政维护 -5% |
| 法兰西 | 1700–1799 | `lcs_fra_4` | 科技花费 -10%；理念花费 -10% |
| 法兰西 | 1800+ | `lcs_fra_5` | 陆军士气 +15%；训练度 +10%；人力恢复 +10% |
| 不列颠 | 1444–1499 | `lcs_gbr_1` | 海军士气 +10%；船只耐久 +5% |
| 不列颠 | 1500–1599 | `lcs_gbr_2` | 海军上限 +15%；船只耐久 +10%；海军士气 +5% |
| 不列颠 | 1600–1699 | `lcs_gbr_3` | 贷款利息 -1；贸易效率 +10% |
| 不列颠 | 1700–1799 | `lcs_gbr_4` | 生产效率 +10%；科技花费 -5% |
| 不列颠 | 1800+ | `lcs_gbr_5` | 生产效率 +15%；贸易效率 +10%；贸易竞争力 +10% |
| 西班牙 | 1444–1499 | `lcs_spa_1` | 陆军士气 +5%；传教强度 +2% |
| 西班牙 | 1500–1599 | `lcs_spa_2` | 殖民范围 +20%；殖民者 +1 名 |
| 西班牙 | 1600–1699 | `lcs_spa_3` | 贸易效率 +10%；每年威望 +0.5 |
| 西班牙 | 1700–1799 | `lcs_spa_4` | 建筑花费 -10%；发展成本 -5%；税收 +5% |
| 西班牙 | 1800+ | `lcs_spa_5` | 稳定花费 -10%；行政效率 +5% |
| 奥斯曼 | 1444–1499 | `lcs_tur_1` | 陆军士气 +10%；人力恢复 +10% |
| 奥斯曼 | 1500–1599 | `lcs_tur_2` | 训练度 +5%；行政效率 +5% |
| 奥斯曼 | 1600–1699 | `lcs_tur_3` | 陆军士气 -5%；科技花费 +5%；税收 -5% |
| 奥斯曼 | 1700–1799 | `lcs_tur_4` | 陆军士气 -10%；训练度 -5%；科技花费 +10%；税收 -10%；全国动乱 +1 |
| 奥斯曼 | 1800+ | `lcs_tur_5` | 陆军士气 -15%；训练度 -10%；税收 -15%；人力上限 -20%；科技花费 +20%；行政效率 -10%；稳定花费 +20%；全国动乱 +2 |
| 奥地利 | 1444–1499 | `lcs_hab_1` | 外交声望 +1；改善关系 +20% |
| 奥地利 | 1500–1599 | `lcs_hab_2` | 传教强度 +3%；稳定花费 -5% |
| 奥地利 | 1600–1699 | `lcs_hab_3` | 训练度 +5%；人力上限 +10% |
| 奥地利 | 1700–1799 | `lcs_hab_4` | 税收 +10%；行政效率 +5% |
| 奥地利 | 1800+ | `lcs_hab_5` | 外交声望 +2；改善关系 +30% |
| 俄罗斯 | 1444–1499 | `lcs_rus_1` | 人力上限 +15%；人力恢复 +10% |
| 俄罗斯 | 1500–1599 | `lcs_rus_2` | 训练度 +5%；全国动乱 -1 |
| 俄罗斯 | 1600–1699 | `lcs_rus_3` | 治理容量 +10%；税收 +10% |
| 俄罗斯 | 1700–1799 | `lcs_rus_4` | 科技花费 -10%；训练度 +5% |
| 俄罗斯 | 1800+ | `lcs_rus_5` | 人力恢复 +20%；陆军士气 +10%；人力上限 +10% |
| 明 | 1444–1499 | `lcs_mng_1` | 税收 +10%；稳定花费 -10% |
| 明 | 1500–1599 | `lcs_mng_2` | 陆军士气 -10%；训练度 -5%；税收 -5%；全国动乱 +1 |
| 明 | 1600–1699 | `lcs_mng_3` | 陆军士气 -20%；训练度 -10%；税收 -20%；发展成本 +20%；人力上限 -25%；人力恢复 -30%；稳定花费 +25%；全国动乱 +2；科技花费 +15%；行政效率 -10%；陆军上限 -20%；建筑花费 +15% |
| 明 | 1700–1799 | `lcs_mng_4` | 陆军士气 -15%；税收 -20%；全国动乱 +3；行政效率 -15%；人力恢复 -20% |
| 明 | 1800+ | `lcs_mng_5` | 税收 -20%；科技花费 +25%；建筑花费 +15%；全国动乱 +3；陆军士气 -10% |
| 清 | 1600–1699 | `lcs_qng_1` | 陆军士气 +10%；训练度 +10%；行政效率 +5% |
| 清 | 1700–1799 | `lcs_qng_2` | 税收 +15%；发展成本 -15%；建筑花费 -10%；稳定花费 -10% |
| 清 | 1800+ | `lcs_qng_3` | 税收 -15%；科技花费 +20%；全国动乱 +2；建筑花费 +10% |
| 满洲 | 1600+ | `lcs_mch_1` | 陆军士气 +20%；训练度 +15%；步兵战斗力 +20%；骑兵战斗力 +20%；人力上限 +50%；人力恢复 +50%；陆军募兵花费 -40%；陆军上限 +50%；战争疲劳 -0.05 |
| 波兰 | 1444–1499 | `lcs_pol_1` | 骑兵战斗力 +15%；陆军士气 +5% |
| 波兰 | 1500–1599 | `lcs_pol_2` | 骑兵战斗力 +10%；外交声望 +1 |
| 波兰 | 1600–1699 | `lcs_pol_3` | 陆军士气 +10%；人力恢复 +10% |
| 波兰 | 1700–1799 | `lcs_pol_4` | 稳定花费 -10%；行政效率 +5% |
| 波兰 | 1800+ | `lcs_pol_5` | 陆军士气 +10%；步兵战斗力 +10% |
| 瑞典 | 1444–1499 | `lcs_swe_1` | 生产效率 +5%；建筑花费 -5% |
| 瑞典 | 1500–1599 | `lcs_swe_2` | 步兵战斗力 +15%；训练度 +5% |
| 瑞典 | 1600–1699 | `lcs_swe_3` | 人力恢复 +10%；陆军上限 +10% |
| 瑞典 | 1700–1799 | `lcs_swe_4` | 科技花费 -10%；理念花费 -10% |
| 瑞典 | 1800+ | `lcs_swe_5` | 陆军士气 +10%；训练度 +5% |
| 普鲁士 | 1444–1499 | `lcs_pru_1` | 陆军士气 +5%；人力恢复 +10% |
| 普鲁士 | 1500–1599 | `lcs_pru_2` | 训练度 +5%；步兵战斗力 +5% |
| 普鲁士 | 1600–1699 | `lcs_pru_3` | 训练度 +5%；陆军上限 +10% |
| 普鲁士 | 1700–1799 | `lcs_pru_4` | 训练度 +10%；陆军士气 +10% |
| 普鲁士 | 1800+ | `lcs_pru_5` | 训练度 +5%；人力恢复 +20%；行政效率 +5% |

生成器：`tools/gen_great_powers.py`（改数值直接改 `GROUPS`，重跑即可整套重生成）。

## 四、还原

- 本体文件：Steam「验证游戏文件完整性」。
- 工坊 mod：取消订阅再订阅，或删掉该 mod 目录让其重新下载（改过的文件会被覆盖回原版）。

## 五、备注

- 难度是**存档属性**，改完读现有极难档或新开极难局生效。
- 极难块里 `core_creation_cost = -2` 是无效键，`error.log` 里有 `Unknown modifier. Type: "core_creation_cost"` 报错，实际不生效；未改动（有效键是 `core_creation`，改了会让 AI 免费核心化）。
- `Documents\Paradox Interactive\Europa Universalis IV\logs\error.log` 可用于确认新加的键没有报错。
- 本地化 yml 必须 UTF-8 **带 BOM**：被剥掉 BOM 的文件游戏会按单字节读，`error.log` 报 `Error in localization value! Key: "...", Error: "Couldn't find Latin1 character"`，中文不再显示。
