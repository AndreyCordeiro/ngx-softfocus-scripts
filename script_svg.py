import os

icon_names = r'/home/developer/Documentos/features/CRED-524/first-icons-optimized'
content = ''

def remove_file_extension(file = ''):
    return file.replace('.svg', '')

# Interage com a pasta de um diretório já a ordenando por ordem alfabética
for file_name in sorted(os.listdir(icon_names)):
    svg_content = open(icon_names + '/' + file_name, mode='r').read()

    # Gera um código HTML para formatação desejada para o arquivo README
    content += '<div style="margin-bottom: 10px; display:inline-flex; flex-direction: row; align-items: center;">' + svg_content + '<span style="display: inline-block; margin-left: 8px;">'+ remove_file_extension(file_name) + '</span></div>\n<br>'

# É necessário ter um arquivo para que seja salvo os dados processados
with open("icon_names.txt", mode='w') as file:
    file.write(content)