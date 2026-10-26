---
id: "28129797729559"
titulo: "Sankhya Tax - Auditoria de Documentos Fiscais (Integração de Notas Fiscais com a Plataforma ASIS no Sankhya)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28129797729559-Sankhya-Tax-Auditoria-de-Documentos-Fiscais-Integra%C3%A7%C3%A3o-de-Notas-Fiscais-com-a-Plataforma-ASIS-no-Sankhya"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Sankhya TAX"
atualizado_em: "2026-10-07T17:47:22Z"
rotulos: ["NF-e", "Integração", "EFD Contribuições", "asis", "integração de notas", "análise tributária", "IAQTDPLIMP", "portal de integração - asis", "IALOGDETINT", "Portal Kolossus da ASIS", "SPED Fiscal", "Sankhya Tax", "br.com.sankhya.mm.integracao.asis", "Documentos Fiscais"]
---

# Sankhya Tax - Auditoria de Documentos Fiscais (Integração de Notas Fiscais com a Plataforma ASIS no Sankhya)

**Módulo:** Configurações › Rotinas

**Caminho de acesso:** Menu Principal › Configurações › Rotinas › Sankhya Tax - Auditoria de documentos e Speds

---

## O que é e para que serve

A tela Sankhya Tax - Auditoria de documentos e Speds é um painel para habilitar e acompanhar o status das integrações dos documentos fiscais eletrônicos do Sankhya Om com o Sankhya Tax, para análise tributária. Os arquivos XML e os arquivos das demais obrigações recebem uma avaliação detalhada, com o cenário tributário completo — o que reduz a complexidade da gestão fiscal e ajuda a manter a conformidade.

Os resultados da análise ficam na tela Sankhya Tax, Captura e Auditoria de XML, no menu Auditorias, separados por tipo de documento (NF-e, NFC-e e SAT). É possível filtrar por período, CNPJ, nível de auditoria e diagnóstico, e conferir quantos documentos caíram em cada auditoria.

Esta rotina não executa a auditoria: ela prepara e envia os documentos, acompanha o retorno e permite reenviar os que apresentarem falha.

## Antes de começar

A rotina está disponível a partir da versão 4.35.

Configure a Chave de Integração, representada pela **Account Key**, que é a chave de acesso de 64 caracteres fornecida pela ASIS.

Depois de salvar as chaves de acesso, o Sankhya Om envia uma solicitação à ASIS para validar a autenticação, e a tela apresenta todas as empresas ou CNPJs vinculados a essa credencial.

A cor do status indica a situação da empresa: **verde** para integrada ou apta para integração e **vermelha** para não integrada ou não apta.

![Status da empresa](https://ajuda.sankhya.com.br/hc/article_attachments/28129797726999)

## Como integrar documentos

Com a Account Key configurada, você integra os documentos de duas formas:

- **Integração manual:** para documentos ou obrigações com data anterior a 30/01/2025. Clique em **Integrar** e preencha os dados da empresa, as informações de envio e as obrigações acessórias.
- **Integração automática:** para documentos incluídos no Sankhya Om a partir de 30/01/2025. Use a opção **Integrar Automático**, configurada por empresa em **Empresas Credenciadas › Editar Empresa** (onde também se define a **Data para Integração** e a **Qtde Dias Integração**).

Na integração automática, são enviadas apenas as notas autorizadas ou canceladas que seguem o padrão de XML estabelecido pelo [Portal de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354-Portal-de-importa%C3%A7%C3%A3o-de-XML). Para notas de entrada, a análise só acontece se o XML estiver disponível, ou seja, o documento precisa ser importado previamente por esse portal.

Além da NF-e, da NFC-e e das EFDs, o CT-e também é enviado na integração automática. A EFD - REINF possui job de integração automática próprio, que faz a busca automática dos eventos.

Você pode configurar a integração para os seguintes documentos:

- **Documentos Eletrônicos:** NF-e, NFC-e e CT-e.
- **Obrigações Acessórias:** EFD - Fiscal ICMS/IPI (SPED Fiscal), EFD - Contribuições PIS/COFINS, ECD, ECF e EFD - REINF.

Os dois grupos são buscados de formas diferentes: os Documentos Eletrônicos por período e as Obrigações Acessórias por **Referência**, que é a competência.

Para atender às obrigações acessórias, você pode gerar mais de um arquivo de conferência no mesmo mês. Se precisar, exclua os arquivos e gere novamente.

### Documentos Eletrônicos

![Imagem 2: Documentos Eletrônicos](https://ajuda.sankhya.com.br/hc/article_attachments/43906526314775)

Nesta aba, os documentos são exibidos conforme a sua seleção. Os tipos disponíveis são NF-e, NFC-e e CT-e.

A busca é feita por período, nos campos **Data Inicial** e **Data Final**, limitada a 30 dias por processamento. Ao informar um período maior, o Sankhya Om exibe a mensagem "O processamento de Documentos Eletrônicos é restrito a um período máximo de 30 dias para garantir a estabilidade da infraestrutura e evitar possíveis travamentos no banco de dados."

Ajuste a visualização da grade com os filtros **Empresa**, **Data Inicial** e **Data Final**.

O CT-e abrange os documentos emitidos, de saída, e os recebidos, de entrada. Para o CT-e de entrada vale a mesma regra das notas de entrada: o XML precisa estar importado e disponível no Portal de Importação de XML.

Se um documento contiver erro, reenvie-o. Se a reintegração for bem-sucedida, o status muda para **Enviado**; se não for, continua como **Erro**. O botão **Reenviar** pode ser usado apenas uma vez a cada 5 minutos — antes disso, o Sankhya Om exibe "Não foi possível obter o retorno do documento. Verifique o motivo na tela de acompanhamento e tente novamente dentro de alguns minutos."

**ℹ️ Nota**

O CT-e não é auditado atualmente na ASIS. Ele é utilizado nos Cruzamentos realizados pelo Sankhya Tax (ASIS).

### Obrigações Acessórias

![Imagem 3: Obrigações Acessórias](https://ajuda.sankhya.com.br/hc/article_attachments/43997079078679)

Esta aba funciona da mesma forma que a aba Documentos Eletrônicos, apresentando os documentos integrados conforme a sua seleção. Os tipos disponíveis são EFD - Fiscal ICMS/IPI, EFD - Contribuições PIS/COFINS, ECD, ECF e EFD - REINF.

A busca é feita por **Referência**, que é a competência, e não por período.

Antes de integrar, confira os pré-requisitos:

- A Referência informada precisa já ter arquivos gerados em **Livros Fiscais › Conexões**. A referência é a mesma para todos os SPEDs.
- **ECD:** informe a referência do exercício, que é o ano. O arquivo ZIP precisa existir em `Contabilidade/ecd`.
- **ECF:** informe a referência do exercício, que é o ano. O arquivo TXT precisa existir em `Contabilidade/ecf`.

Se houver erro no envio, use a opção **Consultar ASIS** para atualizar o status do documento. Assim como o Reenviar, o intervalo mínimo entre as tentativas é de 5 minutos.

## Consulta e reenvio de documentos

Após a integração, cada linha exibe um **Status Sefaz** por documento:

- **Aprovada:** documento aprovado na Sefaz.
- **Cancelada:** documento cancelado na Sefaz.

A coluna **Auditado** segue a mesma lógica:

- **Não:** documentos ainda sem retorno da API da ASIS.
- **Sim:** documentos integrados e com retorno com sucesso.
- **Erro:** documentos que falharam na integração.

Se a autenticação falhar, o Sankhya Om exibe "Problema: Não foi possível realizar a autenticação. Verifique os dados de integração informados no portal Kolossus, tente novamente ou entre em contato com a ASIS."

Quando houver erro na integração, você pode reenviar o documento para uma nova tentativa de processamento ou consultar a ASIS para atualizar o status. Os relatórios detalhados ficam na tela **Sankhya Tax**, no menu **Auditorias**, onde você visualiza a auditoria de cada documento. Para ajustar as credenciais de uma empresa, edite a Account Key nas configurações.

**ℹ️ Nota**

O reenvio e a consulta têm intervalo mínimo de 5 minutos entre as tentativas.

Na barra de ferramentas da grade, você também encontra:

- **Ver Documento:** direciona para a Central de Compras.
- **Detalhes:** mostra o resultado da auditoria do documento, se houver. O detalhamento completo fica na tela Sankhya Tax.

### Configuração da grade

A **engrenagem**, na barra de ferramentas da grade, abre o popup **Configuração da Grade**, com a instrução "Arraste os itens para definir a ordem e visibilidade das colunas da sua grade".

![Imagem 4: A engrenagem , na barra de ferramentas da grade, abre o popup Configuração da Grade , com a instrução "Arraste os itens…](https://ajuda.sankhya.com.br/hc/article_attachments/43997077765399)

- **Colunas disponíveis**, no painel esquerdo: colunas existentes que ainda não são exibidas.
- **Colunas selecionadas**, no painel direito: colunas que aparecem na grade.

Use os botões centrais para mover colunas entre os painéis: **»** move todas, **›** move a selecionada, **‹** remove a selecionada e **«** remove todas. As setas à direita, para cima e para baixo, reordenam as colunas selecionadas. Cada painel tem o campo **Buscar item**.

A seção **Ordenação de dados**, expansível, define a ordenação dos dados da grade.

Clique em **Concluir** para salvar. O Sankhya Om exibe "As configurações foram salvas com sucesso!" e a grade passa a mostrar as colunas escolhidas. A rotina disponibiliza 18 colunas, entre elas Data de Negociação, Cód. Usuário, Empresa, Nome Fantasia (Empresa), Tipo de Movimento, Número Único, Número Nota, Modelo e Série.

**⚠️ Atenção**

Se o painel Colunas selecionadas ficar vazio, com 0 itens, a grade não exibe nenhuma coluna. Mova ao menos uma coluna para esse painel antes de concluir.

## Diagnosticar

![Imagem 5: Diagnosticar](https://ajuda.sankhya.com.br/hc/article_attachments/43906526318487)

O botão **Diagnosticar** abre o popup **Diagnosticar Nota**, usado para descobrir por que um documento não foi integrado ou enviado, comparando a situação do XML da Central com o da Importação e os status de aceite e envio.

![Imagem 6: O botão Diagnosticar abre o popup Diagnosticar Nota , usado para descobrir por que um documento não foi integrado ou…](https://ajuda.sankhya.com.br/hc/article_attachments/43906526321175)

- **Buscar:** informe a **Chave da nota** e a **Referência** e clique em **Buscar**. A **Referência** é um campo de data e vem preenchida com a data atual. Se o documento não for localizado, o Sankhya Om exibe "Nota não encontrada".

![Imagem 7: Buscar: informe a Chave da nota e a Referência e clique em Buscar . A Referência é um campo de data e vem preenchida…](https://ajuda.sankhya.com.br/hc/article_attachments/43906563120663)

- **Informações:** exibe o diagnóstico do documento, com Chave da nota, Data de Negociação, Empresa, Nunota, Num Nota, Origem, Modelo de Documento, Série, Status Aceito, Status Envio, Em Integração, Xml da Central, Xml da Importação, Tipo de Movimento Aceito e Protocolo. O botão **Voltar** retorna à busca.

## Parâmetros que influenciam esta rotina

- **Registro de log detalhado da integração –** `IALOGDETINT`**:** habilite para rastrear todas as etapas da integração com a ASIS. Isso permite que o suporte identifique e resolva falhas rapidamente.
- **Período de armazenamento de dados –** `IAQTDPLIMP`**:** define por quantos dias o Sankhya Om mantém os arquivos armazenados no portal. O padrão é 30 dias e pode ser ajustado conforme a necessidade.
