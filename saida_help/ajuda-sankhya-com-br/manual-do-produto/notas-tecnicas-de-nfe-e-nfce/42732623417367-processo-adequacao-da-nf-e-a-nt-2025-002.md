---
id: "42732623417367"
titulo: "Processo Adequação da NF-e à NT 2025.002 v1.10 RTC (IBS/CBS/IS)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42732623417367-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2025-002-v1-10-RTC-IBS-CBS-IS"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Notas Técnicas  > Notas Técnicas de NFe e NFCe"
atualizado_em: "2026-10-15T13:57:59Z"
rotulos: ["gCompraGov", "gTransfCred", "gTribRegular", "gAjusteCompet", "gEstornoCred", "indDoacao"]
---

# Processo Adequação da NF-e à NT 2025.002 v1.10 RTC (IBS/CBS/IS)

**Módulo:** Fiscal e Contábil › Documentos Eletrônicos
**Caminho de acesso:** Menu Principal › Preferências › Empresa › aba NF-e/NFC-e › sub-aba Nota Técnica NF-e

**Você encontra neste artigo:**

| [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/42732623417367-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2025-002-v1-10-RTC-IBS-CBS-IS#h_01M00YNFV4XJ8PEFS0GVB71MCZ)  [Compras Governamentais (gCompraGov)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42732623417367-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2025-002-v1-10-RTC-IBS-CBS-IS#h_01M00YNFV74ZGZZCTS4VRTQ37Z)  [Tributação Regular (gTribRegular)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42732623417367-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2025-002-v1-10-RTC-IBS-CBS-IS#h_01M00YNFVBVYKZF31740YFJZZJ)  [Transferência de Créditos (gTransfCred)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42732623417367-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2025-002-v1-10-RTC-IBS-CBS-IS#h_01M00YNFVEAWY0GMW6MRN804Z8) | [Ajuste de Competência (gAjusteCompet)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42732623417367-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2025-002-v1-10-RTC-IBS-CBS-IS#h_01M00YNFVJTCR59NDNTNK39PKH)  [Estorno de Crédito (gEstornoCred)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42732623417367-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2025-002-v1-10-RTC-IBS-CBS-IS#h_01M00YNFVPXHWASTK7QHA56CDJ)  [Referenciamento em devoluções](https://ajuda.sankhya.com.br/hc/pt-br/articles/42732623417367-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2025-002-v1-10-RTC-IBS-CBS-IS#h_01M00YNFVTPM6K4KA04BKZTWYZ)  [Doações (indDoacao)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42732623417367-Processo-Adequa%C3%A7%C3%A3o-da-NF-e-%C3%A0-NT-2025-002-v1-10-RTC-IBS-CBS-IS#h_01M00YNFW1W3BMRF3J1YR5ZYV3) |
| --- | --- |

## O que é e para que serve

A **Nota Técnica 2025.002-RTC v1.10** adequa a NF-e e a NFC-e ao novo layout da SEFAZ para suportar os tributos IBS, CBS e IS da Reforma Tributária, incluindo os grupos usados para diferenciar compras governamentais, tributação regular, transferência de créditos, ajuste de competência e estorno de crédito. Esta versão não cobre as mudanças dos grupos B, BB, BC, C e UB nem o grupo de alíquota zero em ZFM/ALC — essas fazem parte da NT 2025.002 v1.40, com artigo próprio. Você não precisa montar os blocos manualmente: o sistema identifica a situação e gera os grupos corretos automaticamente.

Com a NT ativa, o sistema passa a gerar tags para **Finalidade da NF-e** (finNFe) com os valores 5 – Nota de Crédito e 6 – Nota de Débito, configurados a partir do Tipo de Operação (TOP). Os tributos IBS, CBS e IS são gerados conforme os valores calculados no motor de cálculo, e totalizados no Grupo W03 (Total da NF-e - IBS / CBS / IS) do XML.

## Compras Governamentais (gCompraGov)

No caso de vendas para órgãos públicos, o sistema gera os grupos **gCompraGov** e **gTribCompraGov**.

O que são esses grupos?

- **gCompraGov** → Indica que a nota fiscal é destinada a um ente governamental.
- **gTribCompraGov** → Mostra os tributos **IBS e CBS** já calculados com a aplicação da **redução de alíquota (pRedutor)** quando houver.

**Quando eles aparecem?**

A inclusão automática desses blocos no XML ocorre quando:

1. O [Cadastro de Parceiro](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros) estiver cadastrado como **Órgão Público** e com o campo **Tipo de ente governamental** preenchido;
2. A [**TOP**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) usada na emissão tiver o campo **Tipo de operação com ente governamental** configurado (Fornecimento ou Recebimento de pagamento);
3. A alíquota de IBS/CBS aplicada ao item possuir valor no campo **% Redução Alíquota (Gov.)**, quando aplicável.

**Regras de Redistribuição (Art. 473 da LC 214/2025)**

Para notas emitidas a partir de 01/01/2027, o sistema realiza automaticamente a redistribuição dos tributos no grupo <gIBSCBS>, considerando o **Tipo de Ente Governamental** e o ano de vigência:

- **União (Tipo 1):**
  - 2027 a 2032 e ≥ 2033: IBS da UF e IBS do Município são zerados. A CBS absorve os valores (IBS UF + IBS Mun + CBS) aplicando o redutor.
- **Estado (Tipo 2):**
  - 2027 a 2032: IBS do Município é zerado. O IBS da UF absorve os valores (IBS UF + IBS Mun) aplicando o redutor.
  - ≥ 2033: IBS do Município e CBS são zerados. O IBS da UF absorve todos os valores aplicando o redutor.
- **Distrito Federal (Tipo 3):**
  - Seguem-se as mesmas regras aplicadas para **Estado**.
- **Município (Tipo 4):**
  - 2027 a 2032: IBS da UF é zerado. O IBS do Município absorve os valores (IBS UF + IBS Mun) aplicando o redutor.
  - ≥ 2033: IBS da UF e CBS são zerados. O IBS do Município absorve todos os valores aplicando o redutor.

**O que eles mostram?**

- Tipo de ente governamental e operação;
- **No grupo gTribCompraGov:** As alíquotas e valores originais de IBS e CBS;
- **No grupo gIBSCBS:** Os valores finais redistribuídos (ex: CBS absorvendo IBS em compras da União), garantindo que não haja rejeição pela Regra 1008.

**Exemplo ilustrativo**

Base de cálculo: **R$ 1.000,00**

- Alíquota IBS UF: **5%** com redutor de **40% → R$ 30,00**
- Alíquota CBS: **3%** com redutor de **20% → R$ 24,00**

**O que isso significa para você?**

A inclusão automática dos grupos de **Compra Governamental** garante:

- **Tributação correta**: os impostos IBS e CBS são destacados com as reduções aplicáveis;
- **Segurança fiscal**: conformidade com as regras da NT 2025.002;
- **Menos esforço manual**: basta configurar o parceiro e a TOP corretamente, que o sistema gera os blocos sozinho.

## Tributação Regular (gTribRegular)

Ele representa a **tributação integral** do IBS (UF e Município) e da CBS, sem reduções especiais, e deve constar no XML da NF-e e NFC-e quando aplicável.

**Quando ele aparece?**

A geração do grupo **gTribRegular** no XML ocorre em três etapas:

1. **No Cadastro de Alíquotas**
   - Ao definir um **Código de Situação Tributária (CST)** ou **Classificação Tributária** que exige tributação regular, o sistema identifica a obrigatoriedade.
2. **Na tela de Cadastro de Alíquotas**

- O sistema habilita a seção **Tributação Regular**, liberando campos específicos para preenchimento.

![Imagem 1: O sistema habilita a seção Tributação Regular , liberando campos específicos para preenchimento.](https://ajuda.sankhya.com.br/hc/article_attachments/42733824411799)

3. **No cálculo da nota**

- - Assim que os dados são preenchidos, o sistema calcula os valores correspondentes e envia o grupo para o XML.

**O que ele mostra?**

O grupo **gTribRegular** traz as informações principais da tributação regular:

- Valor do **IBS da UF**;
- Valor do **IBS do Município**;
- Valor da **CBS**;
- As **alíquotas aplicadas**;
- Os **códigos de CST e Classificação Tributária** exigidos pela Receita.

**Exemplo**

- **Base de cálculo**: R$ 1.000,00
- **Alíquota IBS UF**: 5%
- **Alíquota IBS Município**: 2%
- **Alíquota CBS**: 3%

Dessa forma, o **gTribRegular** garante que as operações sejam registradas com os valores integrais de IBS e CBS, atendendo à legislação da Reforma Tributária.

Com a implementação da Reforma Tributária, os tributos **IBS, CBS e IS** passaram a ser obrigatórios na totalização dos documentos fiscais eletrônicos. O sistema deve considerar estes valores ao calcular os totais de cada item e do documento, garantindo que os XMLs gerados estejam conforme as NTs aplicáveis. (Durante o ano de 2026, esses valores ainda não serão somados)

**(1)** Para mais informações acesse a categoria da [Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/categories/34702076010775-Reforma-tribut%C3%A1ria) ou o [Guia da Reforma](https://www.sankhya.com.br/gestao-de-negocios/guia-completo-da-reforma-tributaria/#introducao).

## Transferência de Créditos (gTransfCred)

Para operações que envolvem transferência de créditos de IBS e CBS, o sistema gera automaticamente o grupo <gTransfCred> dentro do bloco <IBSCBS> do XML.

**Quando ele aparece?** A geração desse grupo ocorre somente quando todas as condições abaixo são atendidas:

- **Finalidade da Nota:** A TOP deve estar configurada como **Nota de Débito** (finNFe = 6).
- **Tipo de Débito:** O campo "Tipo de Nota Fiscal de Débito" deve ser preenchido com uma das opções válidas para transferência:
  - **01** – Transferência de créditos para Cooperativas;
  - **05** – Transferência de crédito de sucessão.
- **CST:** O grupo deve ser gerado apenas quando o CST possuir o indicador <ind\_gAjusteCompet> = 1.
- **Valores:** Pelo menos um dos valores de IBS (vIBS) ou CBS (vCBS) deve ser maior que zero.

**Validações do Sistema** Para garantir a conformidade com a NT 2025.002, o sistema realiza as seguintes validações no momento da emissão:

- **Validação de Tipo:** Se a nota for de Débito, mas o tipo escolhido não for 01 ou 05, o sistema impedirá a emissão com a mensagem: "Tipo de NF-Débito inválido para Transferência de Crédito."
- **Validação de Valores:** Se ambos os valores (IBS e CBS) forem zerados, a emissão será bloqueada com o aviso: "Ao menos um dos valores vIBS ou vCBS deve ser maior que zero."

**Visualização:** no XML gerado, o grupo será apresentado da seguinte forma:

```
<gTransfCred>
    <vIBS>Valor do IBS</vIBS>
    <vCBS>Valor da CBS</vCBS>
</gTransfCred>
```

## Ajuste de Competência (gAjusteCompet)

O sistema gera automaticamente o grupo <gAjusteCompet> dentro do Grupo UB (Informações de IBS/CBS/IS) para registrar ajustes ou estornos em notas de débito, garantindo conformidade com a NT 2025.002-RTC.

**Quando ele aparece?** Este grupo é gerado no XML somente quando **todos** os critérios abaixo são atendidos:

- **Finalidade da Nota:** A TOP deve estar configurada como **Nota de Débito** (finNFe = 6).
- **Tipo de Débito:** O campo "Tipo de Nota Fiscal de Débito" deve ser preenchido com uma das opções:
  - **02** – Anulação de Crédito por Saídas Imunes/Isentas;
  - **03** – Débitos de notas fiscais não processadas na apuração.
- **CST:** O grupo deve ser gerado apenas quando o CST possuir o indicador <ind\_gAjusteCompet> = 1.
- **Valores:** Pelo menos um dos valores de IBS (vIBS) ou CBS (vCBS) deve ser maior que zero.

**Estrutura e Validações**

- **Competência (competApur):** O sistema preenche este campo automaticamente no formato AAAA-MM, utilizando a **data de movimento** do documento (ou a data de negociação, caso a de movimento esteja vazia).
- **Bloqueio:** O sistema impedirá a emissão se ambos os valores (IBS e CBS) forem iguais a zero, exibindo a mensagem: "Obrigatório informar valor positivo de IBS ou CBS no grupo de Ajuste de Competência."

**Visualização no XML**

XML

```
<gAjusteCompet>
    <competApur>2026-02</competApur>
    <vIBS>150.00</vIBS>
    <vCBS>20.00</vCBS>
</gAjusteCompet>
```

## Estorno de Crédito (gEstornoCred)

O sistema gera automaticamente o grupo <gEstornoCred> para representar estornos de crédito de IBS e CBS. Esta geração ocorre tanto no detalhamento de cada item (Grupo UB) quanto na totalização da nota (Grupo W03).

**Quando ele aparece?** A tag é gerada quando uma das seguintes condições é atendida:

- **Pelo CST:** O grupo deve ser gerado apenas quando o CST possuir o indicador <ind\_gEstornoCred> = 1, ou quando;
- **Pelo Tipo de Débito:** A TOP é de Nota de Débito e o campo "Tipo de Nota Fiscal de Débito" é **07 – Perda em estoque**.

**Regras de Validação**

- **Valores:** Como regra geral, pelo menos um dos valores (vIBS ou vCBS) deve ser **maior que zero**.
- **Exceção (Perda em Estoque):** Se o Tipo de Nota de Débito for **07**, o sistema permite que ambos os valores sejam zerados. Caso contrário, se os valores forem zero, o sistema bloqueará a emissão com a mensagem: "Obrigatório informar valor positivo de IBS ou CBS no grupo de Estorno de Crédito, exceto para tpNFDebito = 07."

**Totalização (Grupo W03)** O sistema soma automaticamente os valores de estorno de todos os itens e preenche o grupo de totais <gEstornoCred> (id: W59e) no final do XML.

**Visualização no XML**

XML

```
<gEstornoCred>
    <vIBS>...</vIBS>
    <vCBS>...</vCBS>
</gEstornoCred>
```

## Referenciamento em devoluções e notas de crédito/débito

Com a reforma tributária, ao emitir uma NF-e de devolução, o sistema pode gerar no XML o grupo <DFeReferenciado>, que traz a chave de acesso e o número do item da nota original.

Para que a inclusão do grupo aconteça, todas as condições abaixo precisam ser atendidas:

- A finalidade da nota é Devolução (finNFe = 4)
- O item devolvido está vinculado a uma NF-e (modelo 55)
- A TOP utilizada na operação tem a opção "Buscar NF de origem para referenciar na NFe" marcada
- Não há NFref informada na capa da nota

Você garante a conformidade com a NT 2025.002-RTC ao deixá-la ativa nas [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#sub-abaNotaT%C3%A9cnicaNF-e) e ao configurar cada item da nota de devolução corretamente. Com tudo certo, o sistema passa a incluir automaticamente em cada item a chave de acesso e o número do item da nota fiscal de origem.

Para mais informações, acesse a categoria da [Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/categories/34702076010775-Reforma-tribut%C3%A1ria) ou o [Guia da Reforma](https://www.sankhya.com.br/guia-reforma-tributaria/#introducao).

**Regras de Referenciamento de Documentos (NT 2025.002 v1.30)**

Para garantir a integridade do vínculo entre notas e itens, o sistema adequou a geração das tags <NFref> (referência na nota) e <DFeReferenciado> (referência no item) conforme a finalidade da operação.

**1. Prioridade em Devoluções (finNFe=4)**

- O sistema **prioriza** a geração do grupo <DFeReferenciado> (vínculo item a item) sempre que possível.
- A tag <NFref> (vínculo geral) só será gerada se não for possível estabelecer o vínculo por item.
- **Exceção:** Para os CFOPs **1.201, 1.202, 1.410, 1.411, 5.921 e 6.921**, o sistema pode manter o comportamento de referenciamento geral.

**2. Notas Complementares e de Crédito**

- **Quando gera** **<NFref>:**
  - Notas Complementares (finNFe=2);
  - Notas de Crédito (finNFe=5) dos tipos: **01** (Multa/Juros), **03** (Retorno) e **04** (Redução de Valores).
- **Restrição:** Nestes casos, é permitida apenas **uma** nota referenciada por documento.

**3. Operações com Órgãos Públicos**

- Quando a operação com ente governamental for **"2 – Recebimento do pagamento"** (tpOperGov=2), o preenchimento da tag <NFref> torna-se **obrigatório**.

**4. Notas de Débito (finNFe=6)** As regras variam conforme o Tipo de Débito:

- **Tipo 03 (Débitos não processados):** Exige <DFeReferenciado>, mas **proíbe** a informação do número do item (nItem).
- **Tipo 04 (Multa e Juros):** Exige <DFeReferenciado> e **obriga** a informação do número do item (nItem).

**5. Bloqueios Importantes**

O sistema impedirá a emissão nos seguintes casos:

- Tentar referenciar mais de uma nota em operações de Crédito/Complemento;
- Informar <NFref> quando o item já possui <DFeReferenciado>;
- Duplicidade de chave de acesso e item no mesmo documento;
- Uso de <DFeReferenciado> em NFC-e ou Notas de Crédito (exceto exceções).

**Regras Automáticas e Reforma Tributária (IBS e CBS)**

O sistema automatiza processos complexos para garantir que sua NF-e não seja rejeitada pela SEFAZ:

- **Identificação de Doações:** Para operações de doação, o sistema identifica automaticamente o cenário quando o item utiliza o **CST 410** combinado com os códigos de classificação **410003** ou **410026**.
- **Tag indDoacao:** Nestas condições, a tag <indDoacao> é gerada automaticamente no grupo UB12 do XML, seguindo a Nota Técnica 2025.002-RTC v1.30.
- **Trava de Segurança:** O motor de cálculo valida se a operação é uma doação antes da transmissão. Se o enquadramento fiscal estiver correto, mas a tag não for gerada, o sistema impedirá a emissão.

## Doações (indDoacao)

Para operações de doação, o sistema identifica automaticamente o cenário quando o item usa o CST 410 combinado com os códigos de classificação 410003 ou 410026, gerando a tag <indDoacao> no grupo UB12 do XML, conforme a NT 2025.002-RTC v1.30. O motor de cálculo valida se a operação é uma doação antes da transmissão — se o enquadramento fiscal estiver correto mas a tag não for gerada, o sistema impede a emissão.
