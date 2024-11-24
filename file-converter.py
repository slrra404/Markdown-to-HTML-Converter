import sys
import markdown
import os

def convert_markdown_to_html(input_file, output_file):
    try:
        with open(input_file, 'r', encoding = 'utf-8') as f:
            text = f.read()
            html = markdown.markdown(text, extensions = ['extra', 'toc', 'sane_lists', 'codehilite'])
        
        with open(output_file, 'w', encoding = 'utf-8') as f:
            f.write(html)

        print(f"変換が完了しました。 {output_file}")

    except Exception as e:
            print(f"エラーが発生しました: {e}")
 
def main():
    if len(sys.argv) < 3 or len(sys.argv) > 4 or sys.argv[1] != 'markdown':
        print("使用方法: python3 file_converter.py markdown input_file output_file")
        sys.exit(1)

    input_file = sys.argv[2]
    output_file = sys.argv[3] if len(sys.argv) == 4 else 'index.html'

    if not os.path.exists(input_file):
        print(f"入力ファイルが見つかりません: {input_file}")
        sys.exit(1)

    convert_markdown_to_html(input_file, output_file)

if __name__ == "__main__":
    main()