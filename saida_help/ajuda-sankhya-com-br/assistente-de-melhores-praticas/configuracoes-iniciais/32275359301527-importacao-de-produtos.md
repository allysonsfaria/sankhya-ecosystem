---
id: "32275359301527"
titulo: "Importação de Produtos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32275359301527-Importa%C3%A7%C3%A3o-de-Produtos"
trilha: "Assistente de Melhores Práticas > Configurações Iniciais"
atualizado_em: "2026-07-22T16:17:12Z"
rotulos: ["Produtos", "Configuração", "NF-e", "XML", "Importação", "CFOP"]
---

# Importação de Produtos

### Descrição

Permite importar produtos e grupos de produtos no sistema, validando dados essenciais como grupo, descrição, unidade e NCM. Visa garantir  a integridade das informações, observando as dependências existentes entre elas.

É possível importar produtos de duas maneiras: **Planilha modelo** ou xml das **Notas Fiscais Eletrônicas**.

**1. Planilha modelo**

**1.1 Validação de Colunas Obrigatórias e Tamanho:**

• O sistema valida se as colunas GRUPO\_PAI, DESCR\_PROD, USO\_PROD, UNIDADE, NCM estão preenchidas corretamente.

• O sistema verifica se o tamanho de cada valor nas colunas preenchidas não excede o limite máximo definido (consultar Comentários nas colunas da planilha-modelo).

**1.3 Validação de Dependências entre Colunas:**

• Grupo Neto, se preenchido, depende de Grupo Filho preenchido.

• Grupo Bisneto, se preenchido, depende de Grupo Neto preenchido.

**1.4 Dados de Imobilizado:**

• As informações das colunas IDENTIF\_IMOBILIZADO e UTILIZ\_IMOBILIZADO da planilha importada são salvas nas colunas "Identificação do Imobilizado" (IDENTIMOB) e "Utilização do Imobilizado" (UTILIMOB) no cadastro de produto.

**2. Notas Fiscais Eletrônicas (NF-e):**

**Validação de Colunas Obrigatórias:**

- O sistema valida as informações obrigatórias nos XMLs, assegurando-se de que o pacote contém XMLs íntegros.
- São observados apenas os XMLs emitidos por empresas controladas pelo sistema, ou seja, cujo CNPJ do emitente está registrado no cadastro de empresas. Isso acontece para evitar a importação de produtos em duplicidade, uma vez que o mesmo produto vendido pela empresa pode aparecer com outro código e nomenclatura nas notas de fornecedores.

**Regras para o preenchimento do cadastro:**

- Para o preenchimento do campo ‘Usado Como’ (USOPROD), identificamos quais são as CFOPs utilizadas nas vendas, da seguinte forma:
  - Se CFOP estiver contido em (5101,5103,5105,5109,5111,5116,5118,5122,5151,5155,5401,5402,5408,6101,6103,…,6408) então ‘V’ (Venda - produção própria)
  - Se CFOP estiver contido em (5201,5410,6201,6410), então ‘M’ (Matéria Prima)
  - Se CFOP estiver contido em (5124,5125,6124,6125) ou estiver entre 5250 e 5400 e entre 6250 e 6400, então ‘S’ (Serviço)
  - Se CFOP estiver contido em (5551,5552,5553,5554,6551,6552,6553,6554) então ‘I’ (Imobilizado)
  - Se CFOP estiver contido em (5556,5557,6556,6557) então ‘C’ (Uso e Consumo).
  - Se o produto não aparecer em operações de venda com nenhuma dessas CFOPs, então ficará como ‘R’ (Revenda).

### Como instalar

1. Clique em "**Iniciar**".

2.Clique na opção "**Planilha modelo**" ou "**Notas Fiscais Eletrônicas (NF-e)**"

2.1. Se a escolha for "**Planilha modelo**"

2.1.1 Clique em "**Baixar Modelo**" para fazer o download da planilha modelo que deverá ser preenchida para a importação de produtos.

Você pode adicionar outras colunas, além das disponíveis na planilha, incluindo campos adicionais. Porém, não inclua as colunas já previstas, como REFERENCIA (populada a partir do conteúdo da coluna COD\_BARRAS), para evitar duplicidade de dados.

2.1.2. Faça o upload da planilha preenchida nos formatos .xls ou .xlsx.

2.1.3. Clique em "**Avançar**".

2.1.4. Defina como seguir com os códigos de produtos: "**Definir códigos automaticamente**" ou "**Utilizar códigos atuais**".

Mesmo que escolhida a opção de manter a numeração atual, os produtos serão automaticamente numerados se o código do produto no sistema anterior possuir letras, pois no SankhyaOm o código do produto deve ser um número inteiro.

2.1.5. Clique em "**Avançar**".

2.1.6. Valide a estrutura dos níveis da hierarquia de Grupos de Produtos.

2.1.7. Clique em "**Avançar**".

2.1.8. Verifique o resumo com uma prévia dos produtos que serão instalados.

2.1.9. Clique em "**Instalar**" para finalizar a configuração.

2.2. Se a escolha for "**Notas Fiscais Eletrônicas (NF-e)**"

2.2.1 Adicione o arquivo zipado dos documentos fiscais emitidos, ao longo dos últimos 6 meses, pelo menos

2.2.1.1. Clique em "**Avançar**".

2.2.1.2. Defina como seguir com os códigos de produtos: "**Definir códigos automaticamente**" ou "**Utilizar códigos atuai**s"

2.2.1.3. Verifique o resumo com uma prévia dos produtos que serão instalados.

Para a importação de produtos são consideradas apenas as NF-e emitidas por empresas controladas pelo sistema, a fim de evitar duplicidade nos cadastros. Notas de terceiros eventualmente enviadas **são ignoradas**.

2.2.1.4. Clique em "**Instalar**" para finalizar a configuração.

2.2.2 Utilizar os arquivos que já foram importados

2.2.2.1. Manter as notas já importadas anteriomente.

2.2.2.1.1 Clique em "**Avançar**".

2.2.2.1.2. Verifique o resumo com uma prévia dos produtos que serão instalados.

2.2.2.1.3. Clique em "**Instalar**" para finalizar a configuração.

2.2.2.2. Adicione o arquivo zipado dos documentos fiscais emitidos ao longo dos últimos 6 meses, pelo menos.

3. Clique em "**Avançar**".

4. Verifique o resumo com uma prévia dos produtos que serão instalados.

5. Clique em "**Instalar**" para finalizar a configuração.

### Detalhes da instalação

Com base nos dados inseridos na planilha, o sistema define a máscara de grupo de produto (preferência MASCGRUPOPROD) e realiza a atualização sequencial das seguintes tabelas:

**Cadastro de Grupo de Produtos e Produtos**

- TGFGRU – Cadastro de grupo de produtos
- TGFPRO – Cadastro de produto

### Como simular

Para acessar os cadastros realizados:

**Produtos:**

1. Vá até Configurações > Cadastros > Produtos > Produtos.
2. Clique em **"Mostrar grade"** e, em seguida, em **"Atualizar"**.
3. Consulte todos os produtos já cadastrados no sistema, inclusive os que foram importados pela prática.

**Vale saber**

Planilha bem preenchida garante um cadastro mais completo e com menos erros. Mas se quiser ganhar tempo, pode usar as NF-es — só lembre que só entram produtos de notas emitidas por suas próprias empresas.

Ah, e atenção aos códigos: no SankhyaOm eles precisam ser numéricos!
