import matplotlib.pyplot as plt
import numpy as np

# フォントの設定（日本語対応）
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['MS Gothic', 'Yu Gothic', 'Meiryo', 'sans-serif']

# データの準備
y = np.linspace(0, 10, 100)  # 実質GDP

# 総需要曲線
p_ad1 = 10 - 0.5 * y  # 初期の総需要曲線
p_ad2 = 12 - 0.5 * y  # 総需要増加後の曲線

# 短期総供給曲線
p_sras = 2 + 0.3 * y  # 短期総供給曲線

# 長期総供給曲線（自然産出量水準）
y_lras = 6 * np.ones_like(y)
p_lras_range = np.linspace(0, 10, 100)

# 初期均衡点の計算
y_eq1 = (10 - 2) / (0.5 + 0.3)
p_eq1 = 2 + 0.3 * y_eq1

# 短期的な新均衡点の計算
y_eq2 = (12 - 2) / (0.5 + 0.3)
p_eq2 = 2 + 0.3 * y_eq2

# 長期的な新均衡点の計算
y_eq3 = 6  # 長期的には自然産出量水準に戻る
p_eq3 = 12 - 0.5 * y_eq3  # 新しい総需要曲線上の点

# 図の作成
plt.figure(figsize=(10, 6))

# 曲線のプロット
plt.plot(y, p_ad1, 'b-', label='総需要曲線(AD1)')
plt.plot(y, p_ad2, 'b--', label='総需要曲線(AD2)')
plt.plot(y, p_sras, 'r-', label='短期総供給曲線(SRAS)')
plt.plot(6*np.ones_like(p_lras_range), p_lras_range, 'g-', label='長期総供給曲線(LRAS)')

# 均衡点のプロット
plt.plot(y_eq1, p_eq1, 'ko', markersize=8)
plt.plot(y_eq2, p_eq2, 'ko', markersize=8)
plt.plot(y_eq3, p_eq3, 'ko', markersize=8)

# 均衡点から線を引く
plt.axhline(y=p_eq1, color='gray', linestyle='--', alpha=0.3)
plt.axvline(x=y_eq1, color='gray', linestyle='--', alpha=0.3)
plt.axhline(y=p_eq2, color='gray', linestyle='--', alpha=0.3)
plt.axvline(x=y_eq2, color='gray', linestyle='--', alpha=0.3)
plt.axhline(y=p_eq3, color='gray', linestyle='--', alpha=0.3)
plt.axvline(x=y_eq3, color='gray', linestyle='--', alpha=0.3)

# 注釈
plt.text(y_eq1, p_eq1, '初期均衡', fontsize=12, ha='right')
plt.text(y_eq2, p_eq2, '短期的な新均衡', fontsize=12, ha='left')
plt.text(y_eq3, p_eq3, '長期的な新均衡', fontsize=12, ha='right')

# グラフの設定
plt.title('総需要・総供給モデル（AD-AS）', fontsize=16)
plt.xlabel('実質GDP(Y)', fontsize=14)
plt.ylabel('物価水準(P)', fontsize=14)
plt.legend(loc='best', fontsize=12)
plt.grid(True, alpha=0.3)

# 保存と表示
plt.savefig('images/AD-ASモデル.png', dpi=300, bbox_inches='tight')
plt.close() 