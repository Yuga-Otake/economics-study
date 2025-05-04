import matplotlib.pyplot as plt
import numpy as np

# フォントの設定（日本語対応）
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['MS Gothic', 'Yu Gothic', 'Meiryo', 'sans-serif']

# データの準備
u = np.linspace(2, 10, 100)  # 失業率の範囲

# 自然失業率
u_star = 5.0

# 短期フィリップス曲線（インフレ期待が異なる3つの曲線）
pi_exp1 = 2  # 期待インフレ率1
pi_exp2 = 4  # 期待インフレ率2
pi_exp3 = 6  # 期待インフレ率3

# 短期フィリップス曲線（各期待インフレ率に対応）
srpc1 = pi_exp1 - 1.5 * (u - u_star)
srpc2 = pi_exp2 - 1.5 * (u - u_star)
srpc3 = pi_exp3 - 1.5 * (u - u_star)

# 図の作成
plt.figure(figsize=(10, 6))

# 曲線のプロット
plt.plot(u, srpc1, 'b-', label='短期フィリップス曲線（期待インフレ率=2%）')
plt.plot(u, srpc2, 'b--', label='短期フィリップス曲線（期待インフレ率=4%）')
plt.plot(u, srpc3, 'b:', label='短期フィリップス曲線（期待インフレ率=6%）')

# 長期フィリップス曲線（自然失業率で垂直な線）
plt.axvline(x=u_star, color='r', linestyle='-', label='長期フィリップス曲線')

# 均衡点
plt.plot(u_star, pi_exp1, 'ko', markersize=8)
plt.plot(u_star, pi_exp2, 'ko', markersize=8)
plt.plot(u_star, pi_exp3, 'ko', markersize=8)

# フィリップス曲線上の移動を示す矢印
plt.annotate('', xy=(4, 3.5), xytext=(5, 2),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8))
plt.annotate('', xy=(5, 4), xytext=(4, 3.5),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8))
plt.annotate('', xy=(4, 5.5), xytext=(5, 4),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8))

# 注釈
plt.text(u_star, pi_exp1, '  (u*, π₁)', fontsize=12)
plt.text(u_star, pi_exp2, '  (u*, π₂)', fontsize=12)
plt.text(u_star, pi_exp3, '  (u*, π₃)', fontsize=12)
plt.text(u_star+0.5, 1, '自然失業率', fontsize=12, rotation=90)

# グラフの設定
plt.title('フィリップス曲線の長期・短期関係', fontsize=16)
plt.xlabel('失業率 (u)', fontsize=14)
plt.ylabel('インフレ率 (π)', fontsize=14)
plt.legend(loc='best', fontsize=10)
plt.grid(True, alpha=0.3)
plt.xlim(3, 8)
plt.ylim(0, 8)

# 保存と表示
plt.savefig('images/フィリップス曲線.png', dpi=300, bbox_inches='tight')
plt.close() 