---
id: "32580700816279"
titulo: "ISS sobre Serviços Tomados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32580700816279-ISS-sobre-Servi%C3%A7os-Tomados"
trilha: "Assistente de Melhores Práticas > Configurações Tributárias"
atualizado_em: "2026-07-22T14:30:58Z"
rotulos: ["ISS", "Configuração", "Alíquota de ISS", "Cidades", "Impostos", "Prefeituras"]
---

# ISS sobre Serviços Tomados

### Descrição

A funcionalidade **ISS sobre Serviços Tomados** permite configurar as alíquotas de ISS (Imposto Sobre Serviços) aplicáveis a serviços tomados, garantindo a correta apuração e recolhimento do imposto conforme os municípios e tipos de serviços prestados.

Ela permite:

- Definir os responsáveis pelas configurações do ISS
- Selecionar os serviços tomados que exigem apuração
- Configurar alíquotas de ISS por cidade
- Definir o comportamento padrão de retenção do ISS
- Aplicar acessos e preferências automaticamente

### Como instalar

1. Selecione os usuários e/ou grupos responsáveis pelas configurações de ISS.
2. Escolha os serviços tomados que terão alíquotas de ISS configuradas.
3. Configure as alíquotas por cidade, informando também deduções e tipo de dedução, se aplicável.
4. Defina se a empresa irá reter ISS sobre os serviços tomados:

4.1 Sim: todos os fornecedores terão o campo de retenção marcado.

4.2 Não: todos os fornecedores terão o campo de retenção desmarcado.

4.3 Usar do Parceiro: não haverá alteração nos cadastros de fornecedores.

5. Revise os dados coletados e clique em **"Instalar"** para concluir a configuração.

### Detalhes da instalação

**Acessos liberados**

- **Parceiros** – Configurações » Cadastros » Parceiros (Consultar, Alterar)
- **Serviço** – Configurações » Cadastros » Produtos » Serviço (Consultar, Alterar)
- **Alíquotas de ISS** – Configurações » Arquivo » Cadastros » Alíquotas » Alíquotas de ISS (Consultar, Incluir, Alterar)

**Tabelas atualizadas**

**TGFEMP – Empresas**

- Campo ISS (CALCISS) = **"Tributado"** para empresas ativas.

**TGFPAR – Parceiros**

- Campo Retém ISS (RETEMISS) atualizado conforme opção escolhida (Sim/Não).

**TGFTOP – Tipos de Operação**

- Campo Tem ISS (TEMISS) = **"Sim"**.
- Campo Cálculo de ICMS, IPI e ISS (CALCICMS) = **"Calcula e Digita"**.

**TGFISS – Alíquotas de ISS**

- Inclusão de registros conforme cidades e serviços definidos.
- Campos atualizados: CODCID, CODPROD, CODEMP, PERCISS, PERCDEDUCAO, TIPODEDUCAO.

![995dfb79-29b4-43bb-afbe-10f31d50936f](https://ajuda.sankhya.com.br/hc/article_attachments/32580696542103) **Vale saber**

Ao configurar as alíquotas por cidade, lembre-se de verificar as legislações municipais específicas para garantir a conformidade fiscal. Essa atenção evita problemas futuros e assegura que sua empresa esteja operando dentro das normas legais!
