---
id: "360044513933"
titulo: "Quais as configurações necessárias para geração do BLOCO K?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044513933-Quais-as-configura%C3%A7%C3%B5es-necess%C3%A1rias-para-gera%C3%A7%C3%A3o-do-BLOCO-K"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:56:07Z"
rotulos: ["#revisadojunior", "Produtos", "Configuração", "SPED", "Fiscal", "EFD", "Estoque", "produção terceirizada", "Configurações: Habilitar Bloco K em \"Preferências\" configurar registros K100 K200 K230 K235 K250 K255 e K280.", "Premissas: Cadastro correto de produtos controle de estoque e formulação de produção.", "Geração: Verificar registros e informações para o controle de produção e estoque no SPED Fiscal."]
---

# Quais as configurações necessárias para geração do BLOCO K?

**(1)** Bloco K é um novo bloco do SPED Fiscal que inclui informações para controle da produção e dos estoques.

#### **(1)** Premissas:

Dentre os diversos pré-requisitos para um bom controle deste processo, destaca-se alguns pontos:

- Cadastro dos produtos codificados corretamente (tipo, NCM, unidades);
- Ter um controle efetivo do estoque, com o lançamento/registro no ERP de todos os documentos
  envolvidos, notas fiscais, ordens de produção e requisições corretamente;
- Definição correta e cadastro das formulas de produção, e previsão de perdas;
- Ter o controle das perdas / quebras dos insumos aplicados no processo de industrialização;
- Ter o controle de estoque e materiais de terceiros.

**![Imagem 1: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17004780789655) OBSERVAÇÃO:**

Todas as premissas acima apenas se aplicam quando for necessária a entrega completa do bloco K, porém com os registros parciais, importante ter o controle da mesma forma para ter o estoque correto para entrega no K200.

**(2)** **Configurações necessárias para geração do Bloco K:**

![Imagem 2: Tela "Empresa" (Caminho de acesso: Comercial » Preferências), aba "EFD - Escrituração Fiscal Digital"](https://ajuda.sankhya.com.br/hc/article_attachments/17004780805527) Tela **"Empresa"** (Caminho de acesso: Comercial » Preferências), aba **"EFD - Escrituração Fiscal Digital"**

- Configure Bloco K -  **"Gerar Bloco":** sim
- Configure Registros do Bloco K - **"Gerar Registro"**: sim

Essa configuração deve ser realizada de acordo com o [Guia Prático](http://sped.rfb.gov.br/estatico/AE/B0DEF8D93F24CB4EEFE8AD1443A14E7E8F4319/GUIA%20PR%C3%81TICO%20EFD%20ICMS%20IPI%20-%20Vers%C3%A3o%203.01.pdf), com apoio e validações do Contador da Empresa. A validação de quais registros deverão ser inseridos será definido junto ao Contador.

#### **(1)** Detalhando os registros do Bloco K gerados no sistema:

**![Imagem 3: Registro K100 - Período de Apuração: informe o período (data inicial e final) a que se refere a escrituração do…](https://ajuda.sankhya.com.br/hc/article_attachments/17004780805527) Registro K100 - Período de Apuração:** informe o período (data inicial e final) a que se refere a escrituração do estoque, será gerada conforme data informada na tela de geração do EFD.

**![Imagem 4: Registro K200:](https://ajuda.sankhya.com.br/hc/article_attachments/17004780814487) Registro K200:**

- Esse registro é denominado como **"Estoque escriturado"**, e apresenta o saldo em estoque de cada produto no último dia do período de apuração do Bloco K, incluindo o código do produto, a quantidade em estoque, o indicador do tipo de estoque, e o código do participante nos tipos de estoque 1 e 2.
- Este registro pode ser gerado após execução da 'Cópia' e 'Contagem' de estoque (Processo de inventario) ou pode considerar o estoque que consta no último dia da geração do SPED da referência em questão.
- Caso opte por gerar através da primeira opção ('Inventário'), habilite o parâmetro **"GERAK200CTE"** (Caminho de acesso: Configurações » Avançado » Preferências). Se **habilitado** o sistema habilita um campo **"Data de contagem p/k200"**, na tela de geração do EFD ICMS/IPI no qual deverá ser informada a data da contagem. Se **desabilitado** será considerado o saldo do estoque do último dia do mês gerado.

**![Imagem 5: Registro K230 - Itens produzidos (produção própria)](https://ajuda.sankhya.com.br/hc/article_attachments/17004809982999) Registro K230 - Itens produzidos (produção própria)**

Este registro tem o objetivo de informar a produção acabada de produto em processo (tipo 03 –campo TIPO\_ITEM do registro 0200) e produto acabado (tipo 04 – campo TIPO\_ITEM do registro 0200). -Definições:

- Serão demonstradas as produções finalizadas (confirmadas) cuja TOP seja do tipo ‘F-Produção’
  dentro do período informado no K100 para os tipos de produtos = 04 – Produto Acabado (USORPOD =‘V’);
- A data da produção será a data de baixa da matéria prima e do produto acabado;
- O nr. da OP será o nunota.

**![Imagem 6: IMPORTANTE: As perdas serão escrituradas conforme as notas fiscais nos registros C100 e filhos, conforme orientação da…](https://ajuda.sankhya.com.br/hc/article_attachments/17004780829079) IMPORTANTE:** As perdas serão escrituradas conforme as notas fiscais nos registros C100 e filhos, conforme orientação da RFB, no seu documento de perguntas e respostas.

**![Imagem 7: Registro K235 - Itens consumidos (produção própria)](https://ajuda.sankhya.com.br/hc/article_attachments/17004780835735) Registro K235 - Itens consumidos (produção própria)**

Este registro tem o objetivo de informar o consumo do insumo (MP) no processo produtivo, vinculado ao produto resultante (PA) informado no campo COD\_ITEM do Registro K230 – Itens Produzidos.

-Definições:

- Serão demonstradas as MP’s consumidas vinculadas a OP gerada no registro pai K230. Sendo assim, serão gerados os itens efetivamente consumidos constantes da Ordem de produção finalizada e estes são determinados pela fórmula de produção cadastradas no sistema diretamente no módulo de Produção.
- **Observação 1:** no momento não geramos o campo 05-COD\_INS\_SUBST, posteriormente será avaliada sua
  necessidade conforme processos envolvidos.
- **Observação 2:** os insumos (MP’s) que que tiverem quantidade consumida = 0 (zero) não serão listados.

**![Imagem 8: Registro K250 - Industrialização efetuada por terceiros - itens produzidos.](https://ajuda.sankhya.com.br/hc/article_attachments/17004810003479) Registro K250 - Industrialização efetuada por terceiros - itens produzidos.**

Este registro tem o objetivo de informar os produtos que foram industrializados por terceiros e sua quantidade. A quantidade produzida deve ser expressa, obrigatoriamente, na unidade de medida de controle de estoque constante no campo 06 do registro 0200: UNID\_INV..

-Definições:

- Serão demonstradas as produções finalizadas (confirmadas), cuja TOP seja do tipo ‘F-Produção’ dentro do período informado no K100 para os tipos de produtos = 04 – Produto Acabado (USORPOD =‘V’) e também que esteja marcado na TOP o novo campo **“Industrialização efetuada por terceiros”** na aba "**Estoque de terceiros"**. Este campo será habilitado apenas para as TOP’s do tipo ‘F-Produção’.
- A data da produção será a data de baixa da matéria prima e do produto acabado e o nr. da OP será o nunota.
- Desta forma, as industrializações efetuadas por terceiros devem ser lançadas normalmente no sistema, utilizando uma TOP de produção com a marcação que é industrialização efetuada por terceiros conforme descrito acima. Assim será possível a geração dos dados corretamente do K250 e K255.

**![Imagem 9: Registro K255 - Industrialização terceiros - itens consumidos.](https://ajuda.sankhya.com.br/hc/article_attachments/17004810011799) Registro K255 - Industrialização  terceiros - itens consumidos.**

Este registro tem o objetivo de informar a quantidade de consumo do insumo que foi remetido para ser industrializado em terceiro, vinculado ao produto resultante informado no campo COD\_ITEM do Registro K250.

-Definições:

- Serão demonstradas as MP’s consumidas, vinculadas a OP gerada no registro pai K230. Sendo assim, serão gerados os itens efetivamente consumidos constantes da Ordem de produção finalizada e estes são determinados pela fórmula de produção cadastradas no sistema diretamente no módulo de Produção.

**![Imagem 10: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17004780789655) OBSERVAÇÃO:**

No momento não geramos o campo 05-COD\_INS\_SUBST, posteriormente será avaliada sua necessidade conforme processos envolvidos.

**![Imagem 11: Registro K280 - Correção de Apontamento - Estoque Escriturado](https://ajuda.sankhya.com.br/hc/article_attachments/17004780853655) Registro K280 - Correção de Apontamento - Estoque Escriturado**

As versões liberadas no [portal do cliente,](http://downloads.sankhya.com.br/) a partir do dia 15/02, já possuem a funcionalidade de gerar K280, lembrando que esse registro tem o objetivo de escriturar correção de apontamento de estoque escriturado de período de apuração anterior, escriturado no Registro K200.
