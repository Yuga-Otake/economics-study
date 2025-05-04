import os
import subprocess
import sys

def run_script(script_path):
    """
    Pythonスクリプトを実行する
    """
    print(f"実行中: {script_path}")
    try:
        subprocess.run([sys.executable, script_path], check=True)
        print(f"成功: {script_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"エラー: {script_path} の実行中にエラーが発生しました。")
        print(f"詳細: {e}")
        return False

# 現在のディレクトリ
current_dir = os.path.dirname(os.path.abspath(__file__))

# 実行するスクリプトのリスト
scripts = [
    os.path.join(current_dir, 'IS-LM曲線.py'),
    os.path.join(current_dir, 'AD-ASモデル.py'),
    os.path.join(current_dir, 'フィリップス曲線.py'),
    os.path.join(current_dir, 'generate_plantuml.py'),
]

# 出力ディレクトリが存在することを確認
images_dir = os.path.join(current_dir, 'images')
os.makedirs(images_dir, exist_ok=True)

# 各スクリプトを実行
success_count = 0
for script in scripts:
    if os.path.exists(script):
        if run_script(script):
            success_count += 1
    else:
        print(f"警告: スクリプト {script} が見つかりません。")

print(f"\n実行完了: {success_count}/{len(scripts)} のスクリプトが正常に実行されました。")

# 生成された画像ファイルの一覧を表示
print("\n生成された画像ファイル:")
for file in os.listdir(images_dir):
    if file.endswith('.png'):
        file_path = os.path.join(images_dir, file)
        file_size = os.path.getsize(file_path) / 1024  # KB単位
        print(f"- {file} ({file_size:.2f} KB)") 