import shutil
import sys

# Pega o argumento da linha de comando (local ou neon)
if len(sys.argv) != 2:
    print("Uso: python setenv.py [local|neon]")
    sys.exit(1)

env_type = sys.argv[1]

# Define o arquivo de origem com base no argumento
if env_type == "local":
    source = ".env.local"
elif env_type == "neon":
    source = ".env.neon"
else:
    print("Erro: escolha 'local' ou 'neon'")
    sys.exit(1)

# Copia o arquivo correspondente para .env
shutil.copyfile(source, ".env")
print(f".env configurado para ambiente: {env_type}")
