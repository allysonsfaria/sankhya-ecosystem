---
id: "37099331628439"
titulo: "1076 Rejeição: Total da BC do IBS e da CBS difere da soma dos itens"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37099331628439-1076-Rejei%C3%A7%C3%A3o-Total-da-BC-do-IBS-e-da-CBS-difere-da-soma-dos-itens"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-10-08T14:58:15Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Passos para resolver", "Erro", "Como Resolver", "Reforma Tributária", "Artigo atualizado KCS", "Alíquotas de CBS", "Alíquotas de IBS", "Soma dos itens", "BC do IBS e da CBS", "Valor total da base do cálculo", "Valor total da Base de Cálculo do IBS e da CBS", "Docs Eletrônicos - KCS"]
---

# 1076 Rejeição: Total da BC do IBS e da CBS difere da soma dos itens

**SITUAÇÃO**

Ao transmitir a NF-e/NFC-e, a SEFAZ retorna a rejeição 1076. Isso acontece quando a base de cálculo do IBS e da CBS no total da nota (tag `vBCIBSCBS`) não bate com a soma das bases informadas nos itens. Como o IBS e a CBS usam a mesma base, qualquer diferença nos itens, seja por duplicidade de valores ou por arredondamento, aparece no total.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo de acordo com o seu cenário:

**Cenário 1: Atualizar o sistema (correção definitiva)**
**(1)** Atualize o **Sistema ERP Sankhya** para a versão **4.35b470 ou superior** e o **Módulo de Livros Fiscais** para a versão **5.29.7 ou superior**. Essas versões trazem as correções para a duplicidade em produtos KIT e para as diferenças de centavos.

**(2)** Depois de atualizar, abra a nota rejeitada, exclua os itens e inclua de novo para que os impostos sejam recalculados.

**(3)** Transmita a nota e confira no XML se as tags `vBCIBSCBS`, `vIBSUF`, `vIBSMun`, `vIBS` e `vCBS` estão preenchidas corretamente e sem duplicidade.

**Cenário 2: Recalcular os impostos da nota**
**(1)** Acesse a nota rejeitada pelo **Portal de Vendas** (Comercial >> Consulta >> Portal de Vendas).

**(2)** Exclua o item e inclua de novo para recalcular os impostos. Se o sistema não permitir alterar a nota, exclua a nota e gere outra.

**(3)** Na nota, clique no botão **Outras Opções de Item** e selecione **Consultar/Alterar Dados de Imposto de Item** para conferir os valores de IBS e CBS.

**(4)** Se ainda houver diferença de centavos, ajuste manualmente a base de cálculo de um dos itens e recalcule os totais da nota.

**Cenário 3: Revisar a configuração da TOP e da tributação**
**(1)** Acesse **Tipos de Operação – TOP** (Comercial >> Arquivo >> Cadastros >> Tipos de Operação – TOP) e confira se as opções **Calcula IBS** e **Calcula CBS** estão marcadas. Se precisar ajustar valores manualmente, configure como **Calcula e Digita**.

**(2)** Acesse **Alíquotas de IBS** (Livros Fiscais >> Cadastros >> Alíquotas de IBS) e **Alíquotas de CBS** (Livros Fiscais >> Cadastros >> Alíquotas de CBS). Confira a regra de tributação: Empresa, CST, Classificação Tributária e Alíquota.

**(3)** Revise o cadastro de **Alíquota de PIS/COFINS** e confira se a opção que define se o PIS/COFINS ST soma no total da nota está correta. Essa opção muda o valor deduzido da base de IBS/CBS.

**(4)** Se a diferença continuar, use o **Assistente de Configuração da Tributação Integral da Reforma Tributária** para revisar as configurações automaticamente.

Em notas de **devolução**, confira se a TOP de devolução também calcula IBS/CBS, para que os totais sejam preenchidos no XML.

**(6)** Para conferir os valores direto na tela da nota, acesse o **Configurador de Layout da Nota** (Comercial >> Configuração >> Configurador de Layout da Nota), localize o layout usado e inclua a sub-aba **Reforma Tributária** no rodapé.

**Cenário 4: Gerar log para análise do suporte**
**(1)** Acesse **Preferências** (Configurações >> Avançado >> Preferências) e habilite o parâmetro **LOGDETCALCREF**.

**(2)** Tente confirmar e transmitir a nota de novo para gerar o log.

**(3)** Abra um chamado com o suporte e anexe o log, o XML da nota e o número da nota.

**CAUSA**

As causas mais comuns são:

- **Versão desatualizada:** versões antigas duplicavam os valores de IBS/CBS em produtos do tipo KIT e em transferências. Também podiam gerar diferenças de R$ 0,01 a R$ 0,02 por arredondamento.
- **Nota Técnica 2025.002-RTC:** opção habilitada sem que o ambiente esteja preparado para ela.
- **Configuração:** regras de IBS/CBS, TOP ou cadastro de alíquota de PIS/COFINS (que define se o PIS/COFINS é somado ao total ou deduzido da base de IBS/CBS) configurados de forma incorreta.
- **Preenchimento:** totais de IBS/CBS ausentes ou incompletos, principalmente em notas de devolução.
