# Smart Cooking Converter

Aplicação web desenvolvida em Django para conversão inteligente de gramas em medidas culinárias. Uma versão de teste pode ser conferida [aqui](http://petrusmassabki.pythonanywhere.com/).

![App views](https://github.com/petrusmassabki/smart-cooking-converter/blob/master/screens.png)

## Funcionamento

Esta aplicação substitui a medida de um ingrediente (em gramas) pela melhor combinação dos utensílios de cozinha desejados.

Conversores de medidas culinárias normalmente realizam cálculos exatos de equivalência, o que frequentemente resulta em medidas quebradas, pouco úteis na cozinha do dia a dia. Este aplicativo oferece uma alternativa e apresenta os resultados em frações de no mínimo 1/4, priorizando a praticidade e flexibilizando a exatidão.

Em muitos casos, combinações simples de utensílios - ou de suas frações - geram medidas de equivalência mais facilmente manejáveis do que um único utensílio. Pensando nisso, o cálculo de equivalência não é realizado para cada recipiente, individualmente, mas sobre o conjunto de recipientes escolhidos pelo usuário. Desse modo, é possível definir a melhor *combinação* que satisfaz a medida desejada, seguindo alguns critérios:

- A margem de erro da medida de equivalência deve ser de no máximo 5% ou 10 gramas;
- A melhor combinação é a composta pelo menor número possível de recipientes;
- Se a margem de erro for satisfeita, a melhor combinação é escolhida, ainda que outra produza um resultado mais exato.

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
