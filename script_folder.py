import os

folder = r'/home/developer/Documentos/features/CRED-524/first-icons'
new_folder = r'/home/developer/Documentos/features/CRED-524/first-icons-renamed'
optimized_folder = r'/home/developer/Documentos/features/CRED-524/first-icons-optimized'

imported = 0
not_imported = 0

def replace_lower_strip_string(directory = ''):
    return directory.replace(' ', '-').lower().strip()

# Interage em todas as pastas de um diretório
for sub_dir in os.listdir(folder):
    # Entro na subpasta
    source = folder + '/' + sub_dir

    for name_dir in os.listdir(source):
        # Entro na pasta do nome do ícone
        name_dir_source =  source + '/' + name_dir

        for file_name in os.listdir(name_dir_source):
            old_file = name_dir_source + '/' + file_name
            new_file = new_folder + '/' + replace_lower_strip_string(sub_dir) + '-' +  replace_lower_strip_string(name_dir) + '-' + replace_lower_strip_string(file_name)

            # Verifica se o nome do arquivo já existe no diretório alvo
            if os.path.isfile(new_file):
                print('O arquivo ' + old_file.replace(folder, '') + ' já existe! (RENOMEAR ARQUIVO)')
                not_imported += 1
            else:
                # Renomeia e muda o diretório do arquivo
                os.rename(old_file, new_file)
                imported += 1
        
print('Arquivos importados: ' + str(imported) + '\nArquivos não importados: ' + str(not_imported))

# Roda um comando no termnal para otimizar os ícones .svg
print('Executando script para otimização dos arquivos .svg')
try:
    os.system('svgo -f ' + new_folder + ' -o ' + optimized_folder)
    print('Script executado!')
except:
    print('Erro ao executar o comando!')
