---
id: "4414636201111"
titulo: "Configurações para a geração do Evento R-2055 no EFD-Reinf"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4414636201111-Configura%C3%A7%C3%B5es-para-a-gera%C3%A7%C3%A3o-do-Evento-R-2055-no-EFD-Reinf"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-10-20T17:45:29Z"
rotulos: ["Produtos", "Configuração", "Fiscal", "Parceiro", "NF-e", "R-2055", "Marque R-2055 na aba EFD-Reinf para geração.", "Escolha indicativo de aquisição para Pessoa Jurídica ou Física", "Marque \"Comercialização Agrícola?\" e \"Enquadrado no Reintegra/Prev\" se necessário.", "Artigo atualizado KCS", "Fiscal/Contábil - KCS", "EFD-REINF"]
---

# Configurações para a geração do Evento R-2055 no EFD-Reinf

**SITUAÇÃO**

Ao gerar o **"EFD-Reinf"** (Livro Fiscais >> Conexão >> Reinf), as notas fiscais de aquisição de produtor rural ou as notas fiscais de devolução não são apresentadas no **"registro R-2055"**, mesmo com configurações aparentemente corretas. O problema pode ocorrer em cenários como:

- Notas fiscais com **"CFOP"** restritivos;
- Configurações incorretas no cadastro de produtos ou serviços;
- Parâmetros da empresa não configurados adequadamente.

**SOLUÇÃO**

**(1)** Para resolver o problema de geração do registro R-2055, siga os passos abaixo:

Acesse a tela Empresa (''Comercial » Preferências » Empresa''), aba **"EFD-Reinf"** e marque o registro R-2055 para ser gerado.

![Imagem 1: Acesse a tela Empresa (''Comercial » Preferências » Empresa''), aba "EFD-Reinf" e marque o registro R-2055 para ser…](https://ajuda.sankhya.com.br/hc/article_attachments/15745157991447)

Ainda na aba EFD-Reinf, habilite a marcação **"Considerar devoluções para geração do evento R-2055?"** para que as devoluções de NF-e no R-2055 sejam consideradas.

O sistema irá verificar se a nota de saída por devolução está relacionada a nota de aquisição e assim procederá com o abatimento dos valores.

![Imagem 2: O sistema irá verificar se a nota de saída por devolução está relacionada a nota de aquisição e assim procederá com o…](https://ajuda.sankhya.com.br/hc/article_attachments/15745174112791)

**(2)**No cadastro de Parceiros (Caminho de acesso: Configurações » Cadastros » Parceiros):

**(1)** Se o tipo de Parceiro for **Pessoa Jurídica**, marque uma das seguintes opções do campo **"Indicativo da aquisição",** da aba **"Fiscal"**, de acordo com suas preferências:

| - "Aquisição de produção de produtor rural pessoa jurídica por entidade do PAA"; - "Aquisição de produção de produtor rural pessoa jurídica por entidade do PAA - Produção isenta". |
| --- |

**(1)** Caso o Parceiro seja **Pessoa Física**, temos as opções:

| - "Aquisição de produção de produtor rural pessoa física ou segurado especial em geral"; - "Aquisição de produção de produtor rural pessoa física ou segurado especial em geral por entidade do PAA"; - "Aquisição de produção de produtor rural pessoa física ou segurado especial em geral - Produção isenta"; - "Aquisição de produção de produtor rural pessoa física ou segurado especial em geral por entidade do PAA - Produção isenta"; - "Aquisição de produção de produtor rural pessoa física ou segurado especial para fins de exportação". - Cadastro de Produtos |
| --- |

Para o parceiros do tipo Pessoa Jurídica, configure o campo **"CPF Prod. Rural"**.

![Imagem 3: Para o parceiros do tipo Pessoa Jurídica, configure o campo "CPF Prod. Rural" .](https://ajuda.sankhya.com.br/hc/article_attachments/15745185110039)

**(3)** Ainda no cadastro de Parceiros, aba ‘Fiscal’, configurar o campo 'Tributação Contr. Previdenciária (Prod. Rural)' indicando a opção do produtor em relação a forma de tributação da Contribuição Previdenciária:

- Sobre a comercialização da produção

- Sobre a Folha de Pagamento

![Imagem 4: - Sobre a Folha de Pagamento](https://ajuda.sankhya.com.br/hc/article_attachments/15745203757207)

**(4)**  No cadastro de Produtos/Serviços (Configurações » Cadastros » Produtos » Produtos), aba **"Geral",** realize a habilitação da marcação **"Comercialização Agrícola?"**.

![Imagem 5: (4) No cadastro de Produtos/Serviços (Configurações » Cadastros » Produtos » Produtos), aba "Geral", realize a…](https://ajuda.sankhya.com.br/hc/article_attachments/15745206297623)

**(5)** No cadastro da TOP (Comercial >> Arquivo >> Cadastros) usada no Lançamento da Nota Fiscal, o campo ‘**Atualização de livro ICMS**’ deverá estar como ‘**Livro de Entrada**’ e nos casos de notas de devolução de compra,  estar como **‘Livro de Saída’.**

**(6)** Se a nota for de modelo 55 (NF-e), esta deverá ter o campo  ‘Status NF-e’ igual a ‘Aprovada’ ou ser NF-e de Terceiros.

**(7)** No **"Portal de Compras"**, para que o sistema considere a nota de compra no evento R-2055, se faz necessário que o lançamento tenha ao menos um dos impostos (INSS/Funrural, Gilrat e Senar).

- No caso do INSS, este poderá estar calculado via TGFDIN (sendo do tipo Retido) ou via cadastro de 'Outros Impostos'.
- No caso do **Gilrat e Senar**, somente via cadastro de TGFIMN ('Outros Impostos'), o ‘Tipo Imposto’ deverá estar como ‘Retido’.

O Funrural é composto pela soma de três tributos: **Previdência**, **GILRAT** e **SENAR**. O sistema está preparado para tratar essas informações de diferentes formas:

- Quando os tributos são lançados separadamente, vindo da tela de impostos, o sistema identifica cada um deles individualmente e os envia corretamente para o REINF.
- Quando é utilizado apenas o lançamento do **Funrural**, o sistema realiza automaticamente a distribuição do valor total entre Previdência, GILRAT e SENAR, respeitando as proporções previstas para cada tributo.
- Ao inserir o imposto do FUNRURAL 1,63% na TGFIMN ("Outros Impostos") com o imposto retido, ele será distribuído entre os campos de Previdência, Gilrat e Senar dentro do R-2055.

**(8)** A nota precisa estar confirmada na Central de Compras.

O sistema irá verificar se a nota de saída por devolução está relacionada à nota de aquisição e assim procederá com o abatimento dos valores.

- A geração do **evento R-2055 não considera CFOP´s de Devolução** que estiverem nos **grupos abaixo:**
  **1200 -** Devoluções de vendas de produção do estabelecimento, de produtos de terceiros ou anulações de valores
  **1900 -** Outras entradas de mercadorias ou aquisições de serviços
  **2200 -** Devoluções de vendas de produção do estabelecimento ou de terceiros ou anulações de valores
  **2900 -** Outras entradas de mercadorias ou aquisições de serviços

- **As CFOP´s de Devolução consideradas no evento R-2055 são:**
  **5201** - Devolução de compra para industrialização ou produção rural
  **5202** - Devolução de compra para comercialização
  **6201** - Devolução de compra para industrialização ou produção rural
  **6202** - Devolução de compra para comercialização

   Após os ajustes, processe novamente a EFD-Reinf para o período desejado e valide a geração do registro R-2055.
