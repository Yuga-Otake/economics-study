import matplotlib.pyplot as plt
import numpy as np

# フォントの設定（日本語対応）
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['MS Gothic', 'Yu Gothic', 'Meiryo', 'sans-serif']

# データの準備
x = np.linspace(0, 10, 100)  # 所得水準
y_is = 10 - 0.6 * x          # IS曲線
y_lm = 2 + 0.4 * x           # LM曲線

# 交点の計算
x_eq = (10 - 2) / (0.6 + 0.4)
y_eq = 10 - 0.6 * x_eq

# 図の作成
plt.figure(figsize=(10, 6))
plt.plot(x, y_is, 'b-', label='IS曲線')
plt.plot(x, y_lm, 'r-', label='LM曲線')
plt.plot(x_eq, y_eq, 'ko', markersize=8)  # 均衡点

# 均衡点から線を引く
plt.axhline(y=y_eq, color='gray', linestyle='--', alpha=0.3)
plt.axvline(x=x_eq, color='gray', linestyle='--', alpha=0.3)

# 財政政策の影響（IS曲線のシフト）
y_is_fiscal = 12 - 0.6 * x  # 財政拡大により右にシフト
plt.plot(x, y_is_fiscal, 'b--', label='IS曲線（財政政策後）')

# 新しい均衡点
x_eq_fiscal = (12 - 2) / (0.6 + 0.4)
y_eq_fiscal = 12 - 0.6 * x_eq_fiscal
plt.plot(x_eq_fiscal, y_eq_fiscal, 'ko', markersize=8)

# 金融政策の影響（LM曲線のシフト）
y_lm_monetary = 0 + 0.4 * x  # 金融緩和により右にシフト
plt.plot(x, y_lm_monetary, 'r--', label='LM曲線（金融政策後）')

# 新しい均衡点
x_eq_monetary = (10 - 0) / (0.6 + 0.4)
y_eq_monetary = 10 - 0.6 * x_eq_monetary
plt.plot(x_eq_monetary, y_eq_monetary, 'ko', markersize=8)

# グラフの設定
plt.title('IS-LM分析における財政政策と金融政策の効果', fontsize=16)
plt.xlabel('所得水準(Y)', fontsize=14)
plt.ylabel('利子率(r)', fontsize=14)
plt.legend(loc='best', fontsize=12)
plt.grid(True, alpha=0.3)
plt.text(x_eq, y_eq, '初期均衡', fontsize=12, ha='right')
plt.text(x_eq_fiscal, y_eq_fiscal, '財政政策後の均衡', fontsize=12, ha='left')
plt.text(x_eq_monetary, y_eq_monetary, '金融政策後の均衡', fontsize=12, ha='right')

# 保存と表示
plt.savefig('images/IS-LM曲線.png', dpi=300, bbox_inches='tight')
plt.close() 