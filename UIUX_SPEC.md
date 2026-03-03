# Knowledge Graph — UI/UX 設計規格書

> **版本**: v1.0  
> **最後更新**: 2026-03-03  
> **適用對象**: `knowledge_graph.html` / `index.html`  
> **部署平台**: Vercel（doc-2-md.vercel.app）  
> **渲染引擎**: vis.js (vis-network standalone)

---

## 1. 設計理念 (Design Philosophy)

### 1.1 風格定位
- **暗色模式 (Dark Mode)** 為唯一模式，以深色背景降低視覺疲勞
- 整體風格參考 **Apple / OpenAI** 的簡約現代美學
- 視覺靈感來源：**Neo4j Bloom** 互動圖譜介面
- 玻璃擬態 (Glassmorphism)：頂部欄與側面板採用 `backdrop-filter: blur()` 毛玻璃效果

### 1.2 核心原則
| 原則 | 說明 |
|------|------|
| **層級清晰** | 不同節點類型透過顏色、尺寸、邊框粗細產生明確的視覺權重差異 |
| **資訊漸進揭露** | 初始顯示概覽 → 點擊節點展開詳細資訊 → 雙擊聚焦放大 |
| **自然互動** | 拖曳時帶有微弱物理回饋，相連節點會自然跟隨，不死板也不混亂 |
| **可探索性** | 搜尋、篩選、影響分析等多種方式探索圖譜 |

---

## 2. 色彩系統 (Color System)

### 2.1 全域 CSS 變數
```css
:root {
  --bg:      #0a0a12;   /* 最深背景色 */
  --surface: #12121e;   /* 表面元素色（卡片、列表項） */
  --surface2:#1a1a2e;   /* 次級表面色（輸入框、hover 狀態） */
  --border:  #2a2a40;   /* 邊框色 */
  --text:    #e0e0f0;   /* 主文字色 */
  --text2:   #9090b0;   /* 次級文字色 */
  --accent:  #6c63ff;   /* 品牌強調色（紫色） */
}
```

### 2.2 節點色彩配置 (Node Color Palette)

每個產品有獨立的**色相家族**，透過深淺區分層級：深色 = 產品級（高權重），中色 = 模組級，淺色 = 前端頁面級。共用類使用灰色系。

#### Company（頂層）
| 類型 | 代碼 | 背景色 | 邊框色 | 字體色 | 尺寸 | 字號 |
|------|------|--------|--------|--------|------|------|
| Company | `company` | `#F5F5F5` 淺灰白 | `#9E9E9E` | `#212121` | 85 | 14 |

#### 🔵 MAAC — 藍色家族 (Blue Family)
| 層級 | 代碼 | 背景色 | 邊框色 | 字體色 | 尺寸 | 字號 |
|------|------|--------|--------|--------|------|------|
| Product | `maac_product` | `#1565C0` 深藍 | `#0D47A1` | `#FFFFFF` | 65 | 12 |
| Module | `maac_module` | `#42A5F5` 中藍 | `#1E88E5` | `#0D47A1` | 28 | 9 |
| Frontend | `maac_frontend` | `#BBDEFB` 淺藍 | `#64B5F6` | `#0D47A1` | 16 | 7 |

#### 🟢 CAAC — 綠色家族 (Green Family)
| 層級 | 代碼 | 背景色 | 邊框色 | 字體色 | 尺寸 | 字號 |
|------|------|--------|--------|--------|------|------|
| Product | `caac_product` | `#2E7D32` 深綠 | `#1B5E20` | `#FFFFFF` | 65 | 12 |
| Module | `caac_module` | `#66BB6A` 中綠 | `#43A047` | `#1B5E20` | 28 | 9 |
| Frontend | `caac_frontend` | `#C8E6C9` 淺綠 | `#81C784` | `#1B5E20` | 16 | 7 |

#### 🟠 DAAC — 琥珀色家族 (Amber Family)
| 層級 | 代碼 | 背景色 | 邊框色 | 字體色 | 尺寸 | 字號 |
|------|------|--------|--------|--------|------|------|
| Product | `daac_product` | `#E65100` 深橙 | `#BF360C` | `#FFFFFF` | 65 | 12 |
| Module | `daac_module` | `#FFA726` 中橙 | `#FB8C00` | `#4E342E` | 28 | 9 |

#### 🔴 CDH — 玫紅色家族 (Rose Family)
| 層級 | 代碼 | 背景色 | 邊框色 | 字體色 | 尺寸 | 字號 |
|------|------|--------|--------|--------|------|------|
| Product | `cdh_product` | `#C62828` 深紅 | `#B71C1C` | `#FFFFFF` | 65 | 12 |
| Module | `cdh_module` | `#EF5350` 中紅 | `#E53935` | `#FFFFFF` | 28 | 9 |

#### ⚪ 共用 — 灰色系 (Neutral Gray)
| 類型 | 代碼 | 背景色 | 邊框色 | 字體色 | 尺寸 | 字號 |
|------|------|--------|--------|--------|------|------|
| Infrastructure | `infra` | `#78909C` 灰藍 | `#546E7A` | `#FFFFFF` | 22 | 8 |
| Shared Service | `shared_service` | `#B0BEC5` 淺灰 | `#78909C` | `#263238` | 24 | 9 |

> **設計原則**: 同產品內透過深淺自然分層。跨產品透過色相一眼區分。共用類用中性灰色，不搶注意力。

### 2.3 邊線色彩配置 (Edge Color Palette)
| 關係類型 | 顏色 | 線寬 | 虛線樣式 | 說明 |
|----------|------|------|----------|------|
| `hierarchy` | `rgba(255,255,255,0.12)` | 1 | 實線 | 層級歸屬（最淡，不搶焦） |
| `code_dep` | `rgba(79,195,247,0.25)` | 1 | `[4,4]` | 程式碼依賴 |
| `api_call` | `rgba(255,167,38,0.5)` | 1.5 | 實線 | API 呼叫（較亮，較粗） |
| `infra_dep` | `rgba(144,164,174,0.3)` | 1 | `[6,3]` | 基礎設施依賴 |
| `service_dep` | `rgba(179,157,219,0.4)` | 1 | 實線 | 共用服務依賴 |
| `data_sync` | `rgba(102,187,106,0.5)` | 2 | `[8,4]` | 資料同步（最粗） |

> **標籤顯示規則**: `hierarchy` 和 `code_dep` 類型的邊**不顯示**文字標籤，其餘類型顯示。

---

## 3. 排版與字體 (Typography)

### 3.1 字體堆疊
```
'Inter', system-ui, sans-serif
```
- 載入 Google Fonts：`Inter` 字重 300/400/500/600/700
- 節點內文字使用 `multi: true` 支援多行顯示

### 3.2 字體規格
| 元素 | 字體大小 | 字重 | 顏色 |
|------|----------|------|------|
| 頂部欄標題 | 15px | 600 | `--text` |
| 頂部欄標題品牌字 | 15px | 700 | `--accent` |
| 搜尋框 | 13px | 400 | `--text` |
| 統計數字 | 12px | 400/600 | `--text2` / `--text` |
| 篩選 Chip | 11px | 500 | 白色（active）/ 預設 |
| 側面板標題 (h2) | 16px | 600 | `--text` |
| 側面板描述 | 13px | 400 | `--text2` |
| 側面板分區標題 (h3) | 13px | 600 | `--accent` |
| 關係列表項 | 12px | 400 | `--text` |
| 圖例文字 | 11px | 400 | `--text2` |
| 節點內文字 | 見節點表 | - | `#1a1a2e`（深色） |
| 邊線標籤 | 8px | - | `#ccc` |

---

## 4. 佈局結構 (Layout Architecture)

### 4.1 整體結構
```
┌─────────────────────────────────────────────────┐
│  Top Bar (fixed, 56px height, z:100)            │
├─────────────────────────────────────────────────┤
│  Filter Chips (fixed, top:64px, left:24px, z:99)│
├────────────────────────────────────┬────────────┤
│                                    │   Detail   │
│                                    │   Panel    │
│        Graph Canvas (#net)         │  (380px)   │
│        (100vw × 100vh)             │  (z:98)    │
│                                    │  slide-in  │
│                                    │            │
├────────────────────────────────────┴────────────┤
│  Legend (fixed, bottom:16px, left:24px, z:99)   │
└─────────────────────────────────────────────────┘
```

### 4.2 Top Bar（頂部導覽列）
- **高度**: 56px
- **背景**: `rgba(10,10,18,0.85)` + `backdrop-filter: blur(16px)`
- **底部邊框**: 1px solid `--border`
- **固定定位**: `position: fixed; top:0; left:0; right:0`
- **z-index**: 100
- **內容（左→右）**:
  1. 品牌標題：`<span style="color:accent">CL</span> Code Architecture Graph`
  2. 搜尋框：`max-width: 400px`，圓角 8px
  3. 統計資訊：Nodes / Edges / Modules / Pages 數量

### 4.3 Filter Chips（篩選標籤列）
- **位置**: `top: 64px; left: 24px`
- **排列**: `flex-wrap: wrap; gap: 6px`
- **每個 Chip**:
  - 圓角 16px（膠囊形）
  - 預設狀態：`--surface` 背景 + `--border` 邊框
  - Active 狀態：`rgba(108,99,255,0.15)` 背景 + `--accent` 邊框 + 白色文字
  - Hover 時邊框變為 `--accent`

### 4.4 Graph Canvas（圖譜畫布）
- **佔據**: 全螢幕 `100% × 100vh`
- **位置**: `position: relative; z-index: 0`
- **背景色**: 繼承 body 的 `--bg`

### 4.5 Detail Panel（詳細資訊面板）
- **寬度**: 380px
- **高度**: `calc(100vh - 56px)`
- **位置**: 右側滑入 `transform: translateX(100%)` → `.open` 狀態 `translateX(0)`
- **過渡動畫**: `transform 0.3s ease`
- **背景**: `rgba(18,18,30,0.95)` + `backdrop-filter: blur(20px)`
- **左邊框**: 1px solid `--border`
- **內距**: 20px
- **可捲動**: `overflow-y: auto`
- **內容結構**:
  1. 關閉按鈕（右上角 ✕）
  2. 節點名稱 (h2)
  3. 類型徽章（使用節點對應色）
  4. 描述文字
  5. 所屬產品（若有）
  6. 影響分析按鈕（僅 module / product 類型顯示）
  7. 「⬅ Depends on」—— 列出所有**入邊**關係
  8. 「➡ Impacts / Provides」—— 列出所有**出邊**關係

### 4.6 Legend（圖例）
- **位置**: `fixed; bottom: 16px; left: 24px`
- **排列**: `flex; gap: 12px; flex-wrap: wrap`
- 每個項目：12×12 圓點 + 類型名稱

### 4.7 Impact Banner（影響分析橫幅）
- **位置**: `fixed; top: 56px; left: 50%; transform: translateX(-50%)`
- **樣式**: 紅色半透明背景 + 紅色邊框，圓角 8px
- **預設隱藏**: `display: none`，啟動影響分析時顯示

---

## 5. 節點設計 (Node Design)

### 5.1 通用屬性
- **形狀**: 一律 `circle`（圓形），文字顯示在節點內部
- **陰影**: `enabled: true, color: rgba(0,0,0,0.3), size: 6, x: 0, y: 3`
- **Highlight 效果**: 背景變白 `#fff`，邊框保持該類型色

### 5.2 尺寸層級（由大到小）
```
Company (85px) > Product (65px) > Module (28px) > Shared Service (24px) > Infra (22px) > Frontend Page (16px)
```

### 5.3 邊框粗細
| 類型 | `borderWidth` |
|------|---------------|
| Company | 6px |
| Product | 5px |
| 其他所有 | 2px |

### 5.4 標籤處理
- 如果 `label` 包含 `/`，只顯示最後一段（例如 `maac/line` → `line`）
- `title`（Hover Tooltip）顯示完整描述，`\n` 轉為換行

### 5.5 初始座標
- 節點使用預計算的 `x, y` 座標（同心圓佈局）
- 座標乘以 `1.6` 倍放大間距
- 同心圓層級：
  - **圓心**: Crescendo Lab（Company）
  - **第一環 (r=250)**: MAAC, CAAC, DAAC, CDH（Products）
  - **第二環 (r=680)**: 各產品的 Modules
  - **第三環 (r≈550)**: Infrastructure, Shared Services
  - **第四環 (r≈980)**: Frontend Pages

---

## 6. 邊線設計 (Edge Design)

### 6.1 通用屬性
- **方向箭頭**: 預設 `arrows: "to"`
- **平滑曲線**: `smooth: { type: "continuous", roundness: 0.15 }`
- **Highlight 顏色**: `#fff`
- **透明度**: `opacity: 0.8`

### 6.2 標籤樣式
- 字體大小：8px，顏色：`#ccc`
- 背景：`rgba(10,10,18,0.7)`（確保在深色背景上可讀）
- `strokeWidth: 0`（無描邊）
- `align: "middle"`

### 6.3 標籤可見性規則
- `hierarchy` 與 `code_dep` 類型：**不顯示**標籤（避免視覺雜亂）
- `api_call`, `infra_dep`, `service_dep`, `data_sync`：**顯示**標籤

---

## 7. 互動設計 (Interaction Design)

### 7.1 物理引擎 (Physics Engine)
這是 UX 的核心——節點需要有**有機、自然的互動感**，但不能失控。

```javascript
physics: {
  enabled: true,
  solver: "forceAtlas2Based",
  forceAtlas2Based: {
    gravitationalConstant: -30,   // 微弱斥力，防止重疊
    centralGravity: 0.003,        // 極微弱向心力
    springLength: 120,            // 彈簧自然長度
    springConstant: 0.01,         // 柔和彈簧力
    damping: 0.85,                // 高阻尼，快速收斂
    avoidOverlap: 0.8,            // 避免重疊
  },
  stabilization: {
    enabled: true,
    iterations: 80,               // 初始穩定迭代次數
    fit: false,                   // 不自動調整視角
  },
  maxVelocity: 25,                // 限制最大速度
  minVelocity: 0.3,               // 最小速度閾值
  timestep: 0.4,                  // 時間步長
}
```

**關鍵行為**:
- ✅ 物理引擎**常駐開啟**（`enabled: true`）
- ✅ 拖曳一個節點時，相連節點**自然地微微跟隨**
- ✅ 放開後整體**柔和地重新平衡**
- ✅ 高 damping (0.85) 確保快速收斂，不會無限漂移
- ✅ maxVelocity (25) 防止節點飛出畫面
- ❌ **不可**讓整個圖譜因拖曳一個節點而劇烈震動

### 7.2 拖曳行為
```javascript
interaction: {
  hover: true,
  tooltipDelay: 150,     // Hover 150ms 後顯示 Tooltip
  zoomView: true,        // 允許滾輪縮放
  dragView: true,        // 允許拖曳畫布
  dragNodes: true,       // 允許拖曳節點
}
```

### 7.3 點擊行為
| 操作 | 目標 | 行為 |
|------|------|------|
| 單擊節點 | 任意節點 | 開啟右側 Detail Panel |
| 單擊空白 | 畫布 | 關閉 Detail Panel；若在影響分析模式則退出 |
| 雙擊節點 | 任意節點 | 聚焦 + 放大至 `scale: 1.8`，動畫 400ms |
| Hover 節點 | 任意節點 | 顯示 Tooltip（150ms 延遲） |

### 7.4 搜尋行為
- **即時搜尋**（`input` 事件監聽）
- 搜尋範圍：節點 `label` 和 `desc` 欄位（不區分大小寫）
- 匹配邏輯：
  1. 找出所有匹配的節點
  2. **展開一層**：將匹配節點的相鄰節點也顯示
  3. 隱藏所有不在展開範圍內的節點和邊
- 清空搜尋框時恢復全部顯示

### 7.5 篩選行為
- 每種節點類型有一個 Chip 按鈕
- 預設全部**啟用**（active）
- 點擊切換啟用/停用
- 停用時隱藏該類型的所有節點及其相關邊線

### 7.6 影響分析 (Impact Analysis)
- **觸發方式**: 在 Detail Panel 中點擊「🔴 Impact Analysis」按鈕
- **僅限** `module` 和 `product` 類型節點可觸發
- **演算法**: 從選中節點進行 **BFS（廣度優先搜尋）**，最大深度 **3 層**
- **視覺效果**:
  - 受影響節點保持正常透明度 (`opacity: 1`)
  - 不受影響節點降為 `opacity: 0.08`（幾乎隱形）
  - 不相關的邊線隱藏
- **退出方式**: 點擊空白區域

### 7.7 面板內導航
- 關係列表中每個項目可點擊
- 點擊後：
  1. 聚焦到目標節點（`scale: 1.5`，動畫 400ms）
  2. 選中目標節點
  3. 更新 Detail Panel 為目標節點的資訊

---

## 8. 響應式與效能考量

### 8.1 全螢幕設計
- `overflow: hidden` 防止頁面捲動
- `height: 100vh` 填滿視窗

### 8.2 佈局設定
```javascript
layout: { improvedLayout: false }
```
- 使用預計算座標，不依賴 vis.js 自動佈局

### 8.3 效能注意事項
- 當前節點數量 ~137，邊線數量 ~495
- 物理引擎參數已針對此規模最佳化
- 若節點數量大幅增加（>500），可能需要：
  - 降低 `timestep`
  - 增加 `damping`
  - 考慮分群/摺疊機制

---

## 9. 動畫規格 (Animation Specs)

| 動畫 | 持續時間 | 緩動函數 | 觸發條件 |
|------|----------|----------|----------|
| Detail Panel 滑入/出 | 300ms | `ease` | 點擊節點/空白 |
| 聚焦節點 | 400ms | vis.js 預設 | 雙擊節點 |
| 面板內導航聚焦 | 400ms | vis.js 預設 | 點擊關係列表項 |
| Filter Chip 狀態 | 200ms | `ease`（CSS all） | 點擊 Chip |
| 搜尋框 Focus 邊框 | 200ms | `ease`（CSS border-color） | Focus 搜尋框 |
| 關係列表項 Hover | 150ms | `ease`（CSS background） | Hover |

---

## 10. 資料結構規格 (Data Schema)

### 10.1 節點 (Node)
```json
{
  "id": 1,
  "label": "顯示名稱（可含路徑前綴如 maac/line）",
  "type": "company | product | module | infra | shared_service | frontend_page",
  "group": "用於色彩映射的分組（如 maac_module, caac_frontend）",
  "title": "Hover Tooltip 內容（支援 \\n 換行）",
  "product": "所屬產品（MAAC/CAAC/DAAC/CDH/空字串）",
  "desc": "節點描述",
  "x": 0,
  "y": 0
}
```

### 10.2 邊線 (Edge)
```json
{
  "from": 1,
  "to": 2,
  "label": "關係標籤（如 contains, imports, calls API）",
  "type": "hierarchy | code_dep | api_call | infra_dep | service_dep | data_sync",
  "arrows": "to"
}
```

---

## 11. 技術依賴 (Tech Stack)

| 依賴 | 版本/來源 | 用途 |
|------|-----------|------|
| vis-network | CDN (unpkg) standalone | 圖譜渲染引擎 |
| Inter | Google Fonts | 全域字體 |
| 純 HTML/CSS/JS | 無框架 | 零依賴，單檔部署 |

---

## 12. 部署須知

- 整個應用為**單一 HTML 檔案**（含內嵌 JSON 資料）
- `knowledge_graph.html` 為主檔，`index.html` 為 Vercel 部署用的複本
- **更新流程**: 修改 `knowledge_graph.html` → 複製為 `index.html` → 推送 GitHub → Vercel 自動部署
- 外部依賴通過 CDN 載入（vis-network, Google Fonts），需網路連線

---

## 13. 設計決策紀錄 (Design Decision Log)

| 日期 | 決策 | 原因 |
|------|------|------|
| 2026-03 | 節點一律使用圓形 (circle) | 統一視覺，文字在圓內可讀 |
| 2026-03 | 物理引擎常駐開啟 | 讓拖曳體驗自然，相連節點微微跟隨 |
| 2026-03 | 座標乘以 1.6 倍 | 增加節點間距，避免擁擠 |
| 2026-03 | Company/Product 節點加粗邊框 | 增加視覺權重，與模組層級區分 |
| 2026-03 | hierarchy/code_dep 邊不顯示標籤 | 這兩類邊數量最多，顯示標籤會造成視覺噪音 |
| 2026-03 | 影響分析 BFS 深度限制 3 層 | 平衡分析深度與視覺可讀性 |
| 2026-03 | 搜尋結果展開一層鄰居 | 提供搜尋目標的上下文脈絡 |
| 2026-03 | 單一 HTML 檔案架構 | 簡化部署，降低維護成本 |

---

## 14. 未來擴充建議

1. **節點摺疊/展開**: 允許將產品下的所有模組摺疊為一個聚合節點
2. **路徑查詢**: 查詢任意兩個節點間的最短路徑
3. **時間軸模式**: 展示系統隨時間的演進
4. **匯出功能**: 將當前視圖匯出為 PNG/SVG
5. **深色/淺色模式切換**: 支援淺色主題
6. **節點群組框**: 用半透明框將同一產品的模組群組化
7. **即時協作**: 多人同時查看與標記
