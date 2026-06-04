import os

html_dir = r'C:\Users\马怡湘\Desktop\实验报告\数据库\SANFU_LAB\html'

for filename in os.listdir(html_dir):
    if filename.endswith('.html'):
        filepath = os.path.join(html_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if '附近门店' in content:
            content = content.replace('附近门店', '品牌故事')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'已修改: {filename}')

print('所有页面的导航文字已替换完成！')