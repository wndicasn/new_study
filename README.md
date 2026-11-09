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

## 三、还原

- 本体文件：Steam「验证游戏文件完整性」。
- 工坊 mod：取消订阅再订阅，或删掉该 mod 目录让其重新下载（改过的文件会被覆盖回原版）。

## 四、备注

- 难度是**存档属性**，改完读现有极难档或新开极难局生效。
- 极难块里 `core_creation_cost = -2` 是无效键，`error.log` 里有 `Unknown modifier. Type: "core_creation_cost"` 报错，实际不生效；未改动（有效键是 `core_creation`，改了会让 AI 免费核心化）。
- `Documents\Paradox Interactive\Europa Universalis IV\logs\error.log` 可用于确认新加的键没有报错。
