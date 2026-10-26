---
id: "360044465693"
titulo: "Configurações necessárias para cálculo do Diferencial de Alíquotas automático na entrada da NF"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044465693-Configura%C3%A7%C3%B5es-necess%C3%A1rias-para-c%C3%A1lculo-do-Diferencial-de-Al%C3%ADquotas-autom%C3%A1tico-na-entrada-da-NF"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-08-25T14:22:52Z"
rotulos: ["Alíquotas", "Configuração", "NF-e", "ICMS", "Impostos", "TOP", "CFOP", "#ValidadoThiagoArantes", "Configuração Automática do Diferencial de Alíquotas na Entrada de NF no SankhyaOm"]
---

# Configurações necessárias para cálculo do Diferencial de Alíquotas automático na entrada da NF

**(1)** Regras para cálculo de diferencial de alíquotas entre UF's:

![Imagem 1: (1) Regras para cálculo de diferencial de alíquotas entre UF's: Em "Tipos de Operação - TOP" (Caminho de acesso:…](https://ajuda.sankhya.com.br/hc/article_attachments/16834561798423) Em **"Tipos de Operação - TOP"** (Caminho de acesso: Comercial » Arquivo » Cadastros), na aba **"Impostos",** marque a opção **"Calcular diferença de ICMS":**

![Imagem 2: (1) Regras para cálculo de diferencial de alíquotas entre UF's: Em "Tipos de Operação - TOP" (Caminho de acesso:…](https://ajuda.sankhya.com.br/hc/article_attachments/14446118851095)

![Imagem 3: No cadastro do CFOP utilizado (Caminho de acesso: Comercial » Arquivo » Cadastros » CFOP) marque a opção "Calcular…](https://ajuda.sankhya.com.br/hc/article_attachments/16834539324951) No cadastro do CFOP utilizado (Caminho de acesso: Comercial » Arquivo » Cadastros » CFOP) marque a opção **"Calcular Diferença de ICMS":**

![Imagem 4: No cadastro do CFOP utilizado (Caminho de acesso: Comercial » Arquivo » Cadastros » CFOP) marque a opção "Calcular…](https://ajuda.sankhya.com.br/hc/article_attachments/14446137852183)

![Imagem 5: Tenha cadastrado nas regras de cálculo de ICMS uma regra interna (Caminho de acesso: Comercial » Arquivo » Cadastros »…](https://ajuda.sankhya.com.br/hc/article_attachments/16834539325975) Tenha cadastrado nas regras de cálculo de ICMS uma regra interna (Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS).

![Imagem 6: Defina na tela "Empresa" (Caminho de acesso: Comercial » Preferências), na aba "Geração de ICMS/IPI", o método a ser…](https://ajuda.sankhya.com.br/hc/article_attachments/16834561802263) Defina na tela **"Empresa"** (Caminho de acesso: Comercial » Preferências), na aba **"Geração de ICMS/IPI",** o método a ser utilizado:

- Por meio do campo **"Método para Calcular Diferencial de Alíquota"**, define-se o embasamento para o cálculo do devido diferencial de alíquota nas entradas, considerando os cálculos de ICMS por dentro e por fora. Tem-se as seguintes opções:

![Imagem 7: Por meio do campo "Método para Calcular Diferencial de Alíquota" , define-se o embasamento para o cálculo do devido…](https://ajuda.sankhya.com.br/hc/article_attachments/14446216245527)

**![Imagem 8: Observação: O valor calculado é apresentado na nota, botão "outras opções" » "consultar/alterar dados dos impostos do…](https://ajuda.sankhya.com.br/hc/article_attachments/16834561804311)Observação:**O valor calculado é apresentado na nota, botão **"outras opções" » "consultar/alterar dados dos impostos do item",** campo **"Valor de Diferencial"** para o imposto ICMS.

(1)** Parâmetros:**

Tela "Preferências": 'Configurações » Avançado'

Chave **"Momento do cálculo do diferencial de alíquota - MOMCALCDIFALIQ"**: defina neste parâmetro o momento do cálculo do diferencial de alíquota, com uma das opções abaixo:

No livro
Na central
Na central e recálculo no livro

**(1)**Sendo que, ao selecionar a opção "No livro", o sistema irá executar o calculo do diferencial de alíquotas apenas na Geração do livro (rotina: Geração ICMS/IPI), registrando o valor no campo Diferença ICMS da aba ICMS/IPI/ST da tela Cadastro Livro ICMS/IPI.

**(1)**Se selecionada a opção "Na central", o sistema irá executar o cálculo do diferencial de alíquotas na nota, registrando o valor no campo "Valor de Diferencial" para o imposto ICMS da tabela de impostos (TGFDIN) e replicará o valor na geração do livro, sem refazer o cálculo.

**(1)**Se selecionado a opção "Na central e recálculo no livro", o cálculo será executado na nota e posteriormente recalculado na geração do livro fiscal, seguindo a regra definida nas preferências da empresa, aba "Geração ICMS/IPI", campo "Método para Calcular Diferencial de Alíquota".

**![Imagem 9: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16834539336343) IMPORTANTE:**

Para o cálculo da diferença de ICMS, o sistema usa as exceções abaixo, conforme definição das prioridades:

- por produto
- por grupo de produtos
- por grupo de ICMS do produto
- por grupo de ICMS do grupo de produto
- por capítulo do NCM
- por posição do NCM
- por NCM
- sem exceção

Já as exceções abaixo **não são analisadas** para o cálculo da diferença de ICMS:

- por perfil principal
- por TOP
- por TARE
- por cidade origem
- por cidade destino
- por grupo de ICMS do parceiro
- CONSUMIDOR
- Consumidor Contribuinte
- Produtor Rural
- por tipo de transporte de importação
- por cód. exceção NCM

**![Imagem 10: Observação: Caso exista duas alíquotas sem exceção cadastradas, o sistema não aplicará o cálculo do Diferencial de…](https://ajuda.sankhya.com.br/hc/article_attachments/16834561804311) Observação:** Caso exista duas alíquotas sem exceção cadastradas, o sistema não aplicará o cálculo do Diferencial de Alíquota.
