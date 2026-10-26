---
id: "28050677988119"
titulo: "Inputs - Analytics Studio"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28050677988119-Inputs-Analytics-Studio"
trilha: "Manual do Produto > Inteligência e Análise > Analytics AI > Componentes"
atualizado_em: "2026-09-23T17:13:58Z"
rotulos: ["Configuração", "Variáveis", "Componentes", "Analytics Studio", "Inputs"]
---

# Inputs - Analytics Studio

Os componentes de Input são utilizados para capturar dados inseridos pelos usuários em diferentes formatos, como texto, números, datas, seleções e anexos. A plataforma oferece 10 tipos de componentes de input:

- Texto;
- Texto Grande;
- Numérico;
- Data;
- Checkbox;
- Radio Button;
- Seletor de Botão;
- Droplist;
- Anexo;
- Input com View (obsoleto e não abordado aqui).

Cada input gera uma variável que pode ser usada tanto em SQL quanto em ações de database, como INSERT, UPDATE e DELETE. Essas variáveis são fundamentais para interações dinâmicas com o banco de dados.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=vO78RxWdGpg)

### Como configurar

#### Variáveis do Input

Ao criar um input, uma variável é automaticamente gerada no formato :INPUT\_ID, onde "ID" corresponde ao identificador único de cada input criado. Essa variável pode ser utilizada tanto em consultas SQL quanto em DMLs (Data Manipulation Language).

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=7VehMDGIrD8)

#### Título do Input, Placeholder e Texto de ajuda

- **Título do Input:** o título do input aparece visualmente na parte superior do componente.
- **Placeholder:** texto que aparece dentro do input para orientar o usuário sobre o que deve ser inserido.
- **Texto de Ajuda:** texto que aparece abaixo ou ao lado do input para fornecer informações adicionais.

#### Formatação

- **Inputs de Texto:** podem ser formatados como e-mail, URL, entre outros.
- **Inputs Numéricos:** podem ser formatados como moeda, porcentagem, telefone, CPF, CNPJ, CEP, entre outros.

#### Obrigatoriedade

Inputs podem ser configurados como obrigatórios. Quando um input é obrigatório, ele deve ser preenchido antes de permitir que uma ação associada seja executada.

Pode-se vincular o botão que exigirá o preenchimento do input obrigatório. Por exemplo, se dois inputs são obrigatórios, o botão de **"Submissão"** só ficará ativo quando todos os inputs forem preenchidos.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=VXyI8OUo1k4)

#### Conteúdo inicial

O conteúdo inicial de um input pode ser definido via SQL. Essa funcionalidade é útil para pré-preencher o input com um valor baseado em dados existentes. Por exemplo, em uma tela que já filtra um executivo, o nome do executivo pode ser recuperado e exibido no input, permitindo que o usuário edite o nome antes de salvar.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=w-b2ZhQm2y0)

### Inputs com Opções (Checkbox, Radio Button, Seletor de botão, Droplist)

Os componentes de **"Checkbox"**, **"Radio Button"**, **"Seletor de Botão"** e **"Droplist"** são um pouco mais complexos, pois exigem a definição de opções:

#### Origem das opções

- **Estático:** o ID e a descrição de cada item são definidos manualmente.
- **Cadastro:** as opções são geradas automaticamente a partir de um cadastro existente.
- **SQL:** as opções são definidas com base em uma query SQL configurada.

#### Comportamento de seleção

- **Checkbox:** permite a seleção de múltiplos itens.
- **Radio Button:** possibilita a seleção de apenas um item.
- **Droplist:** pode ser configurado para permitir a seleção de um ou múltiplos itens.
- **Seletor de Botão:** funciona como um radio button, mas com um design mais moderno e visualmente atrativo. Permite que seja adicionado ícones a cada opção, tornando-o ideal para interfaces que precisam de uma apresentação visual mais sofisticada.

#### Configuração de seletor de botão

Pode-se configurar uma query SQL para retornar o ID, a descrição e o ícone de cada opção. O componente exibirá as opções na horizontal, com os ícones associados, criando um seletor de botão estilizado e funcional.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=j9xhwzCqr5E)

---

![Imagem 1: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/28157051386903) Acesse também:

[Analytics AI](https://ajuda.sankhya.com.br/hc/pt-br/articles/25640296222231-Analytics-AI)

[Analytics Studio](https://ajuda.sankhya.com.br/hc/pt-br/articles/25648251050647-Analytics-Studio)
