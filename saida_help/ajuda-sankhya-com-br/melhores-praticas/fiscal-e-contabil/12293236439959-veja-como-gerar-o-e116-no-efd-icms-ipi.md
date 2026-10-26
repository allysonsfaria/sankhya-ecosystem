---
id: "12293236439959"
titulo: "Veja como gerar o E116 no EFD ICMS/IPI"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/12293236439959-Veja-como-gerar-o-E116-no-EFD-ICMS-IPI"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-10-01T12:20:13Z"
rotulos: ["Configuração", "SEFAZ", "ICMS", "EFD", "Lançamento de Obrigações: Registre o ICMS a recolher em \"Obrigações do ICMS e ICMS ST a Recolher\".", "Configuração do Registro: Acesse \"Empresa\" e marque a opção para gerar o E116.", "Apuração e Geração: Preencha e salve o \"Registro de Apuração do ICMS\" depois gere e valide o arquivo EFD.", "Erro", "Artigo atualizado KCS", "Fiscal/Contábil - KCS", "Documentos Eletrônicos"]
---

# Veja como gerar o E116 no EFD ICMS/IPI

O somatório dos campos **"Valor da obrigação a recolher"** dos registros E116 não é igual à soma dos campos **"Valor total de ICMS a recolher"** e **"Valores recolhidos ou a recolher, extrapuração"** do registro E110. Este registro tem o objetivo de discriminar os pagamentos realizados ou a realizar, referentes à apuração do ICMS. Pode acontecer de gerar erro no validador que indicará a necessidade da geração do E116.

### SITUAÇÃO

O erro ocorre durante a validação do arquivo SPED no PVA, indicando divergência entre os valores de apuração de ICMS e os valores informados para recolhimento nos registros E116.

### CAUSA

A divergência é causada pela ausência ou incorreção das obrigações a recolher cadastradas no sistema, que não coincidem com os valores apurados no Registro de Apuração do ICMS.

### SOLUÇÃO

Siga os passos abaixo para realizar o ajuste das informações:

### 1. Verificar as preferências da empresa

Acesse a tela **"Empresa"** (Comercial >> Preferências >> Empresa) e confira as configurações:

- Selecione a empresa e acesse a aba **"EFD-Escrituração Fiscal Digital"**.
- No campo **"Tipo de Escrituração"**, selecione a opção EFD.
- No painel **"Blocos e Registros"**, selecione o Bloco 'E'.
- No painel **"Registros"**, verifique se para o registro E116 está marcada a opção **"Gerar Registro"**.
- Na aba **"EFD"**, garanta que o registro **"C170"** esteja marcado.

![Imagem 1: Na aba "EFD" , garanta que o registro "C170" esteja marcado.](https://ajuda.sankhya.com.br/hc/article_attachments/42156856337431)

### 2. Cadastrar as obrigações de ICMS e ICMS ST

Acesse a tela **"Obrigações do ICMS e ICMS ST a Recolher"** (Livros Fiscais >> Avançado >> Escrituração Fiscal Digital >> Obrigações do ICMS e ICMS ST a Recolher):

- Clique em **"Incluir"** e preencha os dados de recolhimento.
- Defina o campo **"Tipo Apuração"** como **"ICMS"**
- Informe o campo **"Valor da Obrigação a Recolher"** líquido, já descontados os créditos.
- Salve os registros com o aval do contador.

![Imagem 2: Salve os registros com o aval do contador.](https://ajuda.sankhya.com.br/hc/article_attachments/14626610053015)

### 3. Gerar a apuração de ICMS

Acesse a tela **"Registro de Apuração do ICMS"** (Livros Fiscais >> Relatórios >> Registro de Apuração do ICMS):

- Preencha a empresa e o período.
- Clique em **"Abrir"** para processar os lançamentos e confira os valores na guia **"Demonstrativos"**.
- Após a validação, clique em **"Salvar"**.
- Lembrando que, a cada alteração feita na tela de Obrigações do ICMS e ICMS ST a Recolher, sempre é necessário acessar a tela de Registro de Apuração do ICMS, clicar em abrir e salvar, antes de gerar o arquivo EFD-Fiscal..

![Imagem 3: Lembrando que, a cada alteração feita na tela de Obrigações do ICMS e ICMS ST a Recolher , sempre é necessário acessar…](https://ajuda.sankhya.com.br/hc/article_attachments/14626608086039)

### 4. Ajustes de apuração e geração do SPED

Se necessário, verifique a tela **"Ajuste de Apuração ICMS e ICMS ST"** (Livros Fiscais » Arquivos), garantindo que o **"Tipo Imposto".**
Por fim, acesse **"EFD - Escrituração Fiscal Digital - ICMS/IPI"** (INSERIR CAMINHO DA TELA), gere novamente o arquivo e valide no PVA.
