---
id: "29413236538775"
titulo: "Geração EFD Fiscal - Registros K260 e K265"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/29413236538775-Gera%C3%A7%C3%A3o-EFD-Fiscal-Registros-K260-e-K265"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:37:10Z"
rotulos: ["Produtos", "Configuração", "Fiscal", "EFD", "Registros K260", "Registros K265"]
---

# Geração EFD Fiscal - Registros K260 e K265

![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/29588002749591)**SOLUÇÃO:**

Na tela **Empresa** (Comercial > Preferências > Empresa), na aba EFD  Escrituração Fiscal Digital, posicionado na opção "EFD" no campo Tipo de Escrituração, devemos verificar se na sub-aba Blocos e Registros, temos o bloco K criado e marcado para gerar, e também se os registros K260/K265 estão criados e marcados para gerarem.

![Imagem 2: Na tela Empresa (Comercial > Preferências > Empresa) , na aba EFD Escrituração Fiscal Digital, posicionado na opção…](https://ajuda.sankhya.com.br/hc/article_attachments/29588002753303)

#### Regras para geração K260

O sistema buscará as Notas de Produção oriundas da tela [Ordens de Produção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119313-Ordens-de-Produ%C3%A7%C3%A3o) que se enquadrem nas condições:

- O tipo de movimento da TOP, usado na Central de Produção, deve ser **"Produção"**;
- A Data do campo **"Dt. Movimento"** na Central de Produção, deve estar dentro do período de geração do txt do EFD, pois é neste campo que o sistema filtra a busca;
- O documento na Central de Produção deve estar **"confirmado"**;
- Na tela [Processo Produtivo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058418533-Processo-Produtivo-Nova) o campo **"Reprocessamento/reparo"** deve estar marcado;
- Na tela **"Composição do Produto"**, aba **"Matérias-Primas"**, é possível incluir o **Produto acabado** como matéria-prima de si mesmo quando o parâmetro **"Permitir definir produto como MP de si próprio. - PRODMPPROP"** estiver **habilitado**.
- Na grade de itens, na Central de Produção, o campo **"Quantidade"** deve ser maior que zero;

#### Regras para geração K265

- Na grade de itens, na Central de Produção, o campo **"Quantidade"** deve ser maior que zero;
- Na tela: Configurações > Cadastros > Produtos > Produtos: na aba Formação de Custo/Preço, os campos **"Filtro p/ Cálc.Custo baseado no Financeiro" e "Filtro p/ Cálc.Custo baseado na Requisição"** serão considerados na geração;
- Ainda na tela de Produtos, o campo **"usado como"**, deve estar com uma dessas opções:

Revenda
Matéria prima
Embalagem
Em Processo
Venda (fabricação própria)
Subproduto
Outros insumos
