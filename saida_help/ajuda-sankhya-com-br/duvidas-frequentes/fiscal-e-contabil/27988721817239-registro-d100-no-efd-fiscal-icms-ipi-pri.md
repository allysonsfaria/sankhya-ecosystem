---
id: "27988721817239"
titulo: "Registro D100 no EFD Fiscal (ICMS/IPI): principais problemas e como solucioná-los"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27988721817239-Registro-D100-no-EFD-Fiscal-ICMS-IPI-principais-problemas-e-como-solucion%C3%A1-los"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-29T15:32:51Z"
rotulos: ["CT-e", "IPI", "ICMS", "Cancelamento", "EFD", "EFD Fiscal - ICMS/IPI - D100 Cancelado", "Artigo atualizado KCS", "Fiscal/Contábil - KCS", "Documentos Eletrônicos"]
---

# Registro D100 no EFD Fiscal (ICMS/IPI): principais problemas e como solucioná-los

O **"Registro D100"** é utilizado no **"SPED Fiscal (EFD ICMS/IPI)"** para escriturar documentos fiscais de serviços de transporte, como **"CT-e (Conhecimento de Transporte Eletrônico)"**. Este registro é fundamental para a correta apuração de impostos e cumprimento das obrigações acessórias.

### Problemas comuns no Registro D100

• CT-e presente no Livro Fiscal, mas **não gerado no SPED.**
• CT-e gerado em **duplicidade**.
• Registro D100 de **documento cancelado** sem preenchimento completo.
• Registros **D101 e D105** com **valores divergentes.**
• **Geração limitada** por configuração de UF.

### Solução para CT-e não gerados no D100

Quando os **"CT-e"** constam no **"Livro Fiscal"** mas não aparecem no arquivo do **"SPED"**, verifique as configurações de UF:

**(1)** Acesse a tela **"EFD - Fiscal ICMS/IPI"** (Livros Fiscais » Conexão)

**(2)** Clique na aba **"Configurações"**

**(3)** Verifique o campo de seleção de **"UF"**.

**(4)** Certifique-se de que todas as UFs necessárias estejam selecionadas.

**(5)** Salve as alterações e gere novamente o arquivo **"EFD"**.

### Solução para lançamentos duplicados no D100

O erro **"Arquivo não gerado por ausência de registros"** ou erros de duplicidade podem ocorrer quando há **"CT-e"** lançados em duplicidade no sistema:

**(1)** Acesse o **"Cadastro do Livro ICMS"** (Livros Fiscais » Arquivos).

**(2)** Filtre os documentos do tipo **"CT-e"** com origem **"Financeira"**.

**(3)** Identifique se há **"CT-e"** com mesmo número e chave lançados mais de uma vez.

**(4)** Valide com o setor responsável qual é o lançamento correto.

**(5)** Exclua o **"CT-e"** incorreto ou duplicado.

**(6)** Gere novamente o **"EFD Fiscal ICMS/IPI"**.

### Geração do Registro D100 para documentos cancelados

Ao realizar o cancelamento de um **"D100"** e gerá-lo no **"EFD"**, o sistema não preenche todos os campos pertinentes. Confira a seguir os campos preenchidos para documentos cancelados:

Campo 01 - **"REG"** = D100
Campo 02 - **"IND\_OPER"** = Campo Entrada ou Saída, da tela **"Cadastro Livro ICMS/IPI"**
Campo 03 - **"IND\_EMIT"** = 0
Campo 05 - **"COD\_MOD"** = Código do modelo do documento presente na tela **"Cadastro Livro ICMS/IPI"**
Campo 06 - **"COD\_SIT"** = 02 (Cancelado)
Campo 07 - **"SER"** = Número de Série, presente na tela **"Cadastro Livro ICMS/IPI"**
Campo 09 - **"NUM\_DOC"** = Número de documento, presente na tela **"Cadastro Livro ICMS/IPI"**
Campo 10 - **"CHV\_CTE"** = Chave CT-e, presente na tela **"Cadastro Livro ICMS/IPI"**

Os demais campos serão deixados vazios. **Observação:** para que o **"CT-e"** cancelado seja gerado no arquivo do **"EFD"**, é necessário que ele esteja no **"Cadastro Livro ICMS/IPI"**. Documentos cancelados nos livros ficam com o seu número único **negativo** na tela.

### Utilização da tela correta para geração

A tela **"EFD - Escrituração Fiscal Digital - ICMS/IPI"** (layout Flex) foi descontinuada. Utilize sempre a tela **"EFD - Fiscal ICMS/IPI"** (layout HTML5). Para habilitar, certifique-se de que o parâmetro **"Habilitar novo layout EFD Fiscal - HABEFISLAYNOVO"** esteja ativo.

### Observações importantes sobre registros D101 e D105

Os registros **"D101"** e **"D105"** são filhos do **"D100"** e contêm informações sobre PIS e COFINS. O sistema gera esses registros com base na **"Natureza Financeira"** configurada.

**Atenção:** Se houver necessidade de aproveitamento parcial de crédito, pode ser necessário ajuste manual ou parametrização específica, pois o sistema considera o valor integral do documento por padrão.
