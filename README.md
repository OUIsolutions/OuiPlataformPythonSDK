# Oui Plataform SDK for easy control of OUI plataform

Esse repositório contém o SDK para realização de ações na plataforma fornecida, como por exemplo, listagem de templates, buscas, criação de templates, etc.

## Instalação

Para instalar o SDK, basta executar o comando abaixo:

```bash
pip install git+https://github.com/OUIsolutions/OuiPlataformPythonSDK
```

## Utilização

Para utilizar o SDK, basta importar o módulo `Session` e instanciar um objeto da classe `Session`, passando como parâmetro a URL, USUARIO e SENHA da plataforma:

```python
from OuiPlataform.Session import Session

session = Session("https://domain.com", 'username', 'password')
```

Com o objeto `session` instanciado, é possível realizar diversas ações na plataforma, como por exemplo, listar templates, listar buscas, dentre outras coisas.

## Entity

As entidades são os objetos que representam um processo. Entity é a classe que representa um processo na plataforma e possui métodos para realizar ações como criar, listar, buscar, etc.

Para criar uma entidade, basta instanciar um objeto da classe `Entity` passando como parâmetro o nome da entidade, porém, caso não saiba o nome da entidade, é possível listar todas as entidades disponíveis na plataforma utilizando o método `list_entities` do objeto `session`, o qual retorna uma lista de objetos `Entity`:

```python
from OuiPlataform.Session import Session

s = Session("https://domain.com", 'username', 'password')

entities = s.list_entities()
for entity in entities:
    print(entity.name)
```

**Saída:**

```bash
entity_name_1
entity_name_2
entity_name_3
...
entity_name_n
```

**Nota:** Note que que o método "__str__" da classe `Entity` retorna o nome da entidade.

Com a lista de entidades em mãos, é possível instanciar um objeto `Entity` passando como parâmetro o nome da entidade:

```python
from OuiPlataform.Session import Session

s = Session("https://domain.com", 'username', 'password')

entity = s.get_entity("entity_name")
```

Agora que temos um objeto `Entity`, é possível realizar diversas ações, como por exemplo, listar, buscar, criar, etc.

### Listar Documentos Estáticos

Para listar os documentos estáticos de uma entidade, basta utilizar o método `list_all_static_documents` do objeto `Entity`. Esse método retorna uma lista de strings, onde cada string representa o nome de um documento estático:

```python
from OuiPlataform.Session import Session

s = Session("https://domain.com", 'username', 'password')

ent = s.get_entity("entity_name")

print(ent.list_all_static_documents())
```

**Saída:**

```bash
['document_name_1', 'document_name_2', 'document_name_3', ..., 'document_name_n']
```

### Listar Documentos Dinâmicos

Para listar os documentos dinâmicos de uma entidade, basta utilizar o método `list_all_dynamic_documents` do objeto `Entity`. Esse método retorna uma lista de strings, onde cada string representa o nome de um documento dinâmico:

```python
from OuiPlataform.Session import Session

s = Session("https://domain.com", 'username', 'password')

ent = s.get_entity("entity_name")

print(ent.list_all_dynamic_documents())
```
**Saída:**

```bash
['document_name_1', 'document_name_2', 'document_name_3', ..., 'document_name_n']
```

### Listar Jsons

Para listar os jsons de uma entidade, basta utilizar o método `list_all_jsons` do objeto `Entity`. Esse método retorna uma lista de strings, onde cada string representa o nome de um json:

```python
from OuiPlataform.Session import Session

s = Session("https://domain.com", 'username', 'password')

ent = s.get_entity("entity_name")

print(ent.list_jsons())
```

**Saída:**

```bash
['json_name_1', 'json_name_2', 'json_name_3', ..., 'json_name_n']
```

### Pegar Conteúdo de um Json

É possível pegar o conteúdo de um json de uma entidade utilizando o método `get_json` do objeto `Entity`. Esse método recebe como parâmetro o nome do json e retorna o conteúdo do json:

```python
from OuiPlataform.Session import Session

s = Session("https://domain.com", 'username', 'password')

ent = s.get_entity("entity_name")

print(ent.get_json("dados_capa"))
```

**Saída:**

```bash
{
    "nome": "João",
    "sobrenome": "Silva",
    "idade": 30
}
```

**Nota:** Note que o método `get_json` pode receber o nome do json com ou sem a extensão `.json`.


### Definindo/Criando um Json

É possível definir/criar um json de uma entidade utilizando o método `set_json` do objeto `Entity`. Esse método recebe como parâmetro o nome do json e o conteúdo do json. Caso o json já exista, o conteúdo do json será atualizado, caso contrário, um novo json será criado:

```python
from OuiPlataform.Session import Session

s = Session("https://domain.com", 'username', 'password')

ent = s.get_entity("entity_name")

ent.set_json("dados_capa", {
    "nome": "João",
    "sobrenome": "Silva",
    "idade": 30
})
```

### Enviando Documentos Estáticos

É possível enviar documentos estáticos para uma entidade utilizando o método `upload_static_document_from_file` do objeto `Entity`. Esse método recebe como parâmetro o nome do documento estático e o caminho do arquivo que será enviado:

```python
from OuiPlataform.Session import Session

s = Session("https://domain.com", 'username', 'password')

ent = s.get_entity("entity_name")

ent.upload_static_document_from_file("document_name", "path/to/file")
```

### Pega Documentos Estáticos

### Pegar Documentos Dinâmicos

## Search

Com os objetos `Search` é possível gerar, excluir e pegar buscas de uma entidade. Para criar um objeto `Search`, basta instanciar um objeto da classe `Search` passando como parâmetro o nome da busca, porém, caso não saiba o nome da busca, é possível listar todas as buscas disponíveis na plataforma utilizando o método `list_searches` do objeto `session`, o qual retorna uma lista de objetos `Search`:

```python
from OuiPlataform.Session import Session

s = Session("https://domain.com", 'username', 'password')

searches = s.list_searches()
search = searches[0]

search = s.get_search("search_name")
```

Agora que temos um objeto `Search`, é possível realizar diversas ações, assim como definir e recuperar props, definir e recuperar codigos, etc.

### Definindo Propriedades

É possível definir propriedades de uma busca utilizando o método `set_prop` do objeto `Search`. Esse método recebe como parâmetro uma lista de propriedades no formato de dicionário, exemplo:

```python
from OuiPlataform.Session import Session

props = [{'name': 'tempo_maximo', 'required': True, 'question': 'Informe o tempo m�ximo em minutos', 'type': 'number'}, {'name': 'tempo_minimo', 'required': True, 'question': 'Informe o tempo m�nimo em minutos', 'type': 'number'}]

s = Session("https://domain.com", 'username', 'password')

search = s.get_search("search_name")

search.set_search_props(props)
```

### Pegando Propriedades

É possível pegar as propriedades de uma busca utilizando o método `get_search_props` do objeto `Search`. Esse método retorna uma lista de propriedades no formato de dicionário:

```python
from OuiPlataform.Session import Session

s = Session("https://domain.com", 'username', 'password')

search = s.get_search("search_name")

print(search.get_search_props())
```

### Definindo Códigos

É possível definir códigos de uma busca utilizando o método `set_codes` do objeto `Search`. Esse método recebe como parâmetro uma string que será o código lua da busca:

```python
from OuiPlataform.Session import Session

s = Session("https://domain.com", 'username', 'password')

search = s.get_search("search_name")

search.set_search_code(
"""function filter(props)
 return true
end
""")

```

### Pegando Códigos

É possível pegar o código de uma busca utilizando o método `get_search_code` do objeto `Search`. Esse método retorna uma string que é o código lua da busca:

```python
from OuiPlataform.Session import Session

s = Session("https://domain.com", 'username', 'password')

search = s.get_search("search_name")

print(search.get_search_code())
```

### Removendo Busca

Através do método `remove` do objeto `Search` é possível remover uma busca de uma entidade. Quando esse método é chamado, a busca é removida da plataforma:

```python
from OuiPlataform.Session import Session

s = Session("https://domain.com", 'username', 'password')

search = s.get_search("search_name")

search.remove()
```

**Nota:** Note que o método `remove` não retorna nada e caso a busca não exista, uma exceção será lançada.

## Mapper

### get_mapper_function

### set_mapper_function


## Documentos Dinâmicos

Objetos dinâmicos são aqueles gerados automaticamente pela plataforma a partir de informações e configurações previamente definidas. A classe `DynamicDoc` é responsável por representar um documento dinâmico e possui métodos para realizar ações como listar, buscar, criar, etc.

### get_generator_code

### get_validator_code

### set_validator_code

### set_generator_code
