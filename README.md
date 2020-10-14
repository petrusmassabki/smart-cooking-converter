# Smart Cooking Converter

Aplicação web para conversão inteligente de gramas para medidas culinárias

![App views](https://github.com/petrusmassabki/smart-cooking-converter/blob/master/screens.png)

## Funcionamento

## Instalação

1. Em uma nova pasta, clone este repositório:
```bash
git clone https://github.com/petrusmassabki/smart-cooking-converter.git .
```
2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/Scripts/activate
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```
4. Crie um arquivo ".env" e insira o conteúdo necessário:
```
SECRET_KEY=secret
DEBUG=True
ALLOWED_HOSTS=.localhost
```
5. Se desejar, gere uma nova SECRET_KEY e atualize o arquivo ".env".
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
6. Realize a primeira migração:
```bash
python manage.py makemigrations
python manage.py migrate
```
7. Inicie o servidor:
```bash
python manage.py runserver
```
8. Para acessar a interface de administração do Django e adicionar ingredientes ao aplicativo, crie um novo usuário:
```bash
python manage.py createsuperuser
```