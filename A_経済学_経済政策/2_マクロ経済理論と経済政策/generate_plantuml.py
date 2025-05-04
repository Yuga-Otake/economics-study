import plantuml
import os

# PlantUMLサーバーのURL
plantuml_server = 'http://www.plantuml.com/plantuml/img/'

def generate_plantuml_image(file_path, output_path):
    """
    PlantUMLファイルからPNG画像を生成する
    """
    # PlantUMLクライアントを初期化
    pl = plantuml.PlantUML(url=plantuml_server)
    
    # ファイルの内容を読み込む
    with open(file_path, 'r', encoding='utf-8') as f:
        puml_content = f.read()
    
    # PNG画像を生成
    response = pl.processes(puml_content)
    
    # 出力先に保存
    with open(output_path, 'wb') as f:
        f.write(response)
    
    print(f"画像を生成しました: {output_path}")

# 現在のディレクトリ
current_dir = os.path.dirname(os.path.abspath(__file__))

# PlantUMLファイルとその出力先
plantuml_files = [
    {
        'file': os.path.join(current_dir, 'マクロ経済モデル関連図.plantuml'),
        'output': os.path.join(current_dir, 'images', 'マクロ経済モデル関連図.png')
    },
]

# 出力ディレクトリが存在することを確認
os.makedirs(os.path.join(current_dir, 'images'), exist_ok=True)

# 各PlantUMLファイルを処理
for item in plantuml_files:
    generate_plantuml_image(item['file'], item['output'])

print("すべての画像生成が完了しました。") 