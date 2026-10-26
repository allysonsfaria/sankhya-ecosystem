---
id: "22006698664215"
titulo: "Configurações para Aproveitamento do Crédito de ICMS do Simples Nacional com a Alíquota de ICMS configurada na Partilha/Anexo do Simples Nacional"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/22006698664215-Configura%C3%A7%C3%B5es-para-Aproveitamento-do-Cr%C3%A9dito-de-ICMS-do-Simples-Nacional-com-a-Al%C3%ADquota-de-ICMS-configurada-na-Partilha-Anexo-do-Simples-Nacional"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:49:36Z"
rotulos: ["Configuração", "Simples Nacional", "XML", "Crédito", "ICMS", "Impostos"]
---

# Configurações para Aproveitamento do Crédito de ICMS do Simples Nacional com a Alíquota de ICMS configurada na Partilha/Anexo do Simples Nacional

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/22006761077783)SOLUÇÃO:**

Configurações para Aproveitamento do Crédito de ICMS do Simples Nacional com a Alíquota de ICMS configurada na Partilha/Anexo do Simples Nacional.

Após a configuração feita com o apoio do Artigo [Quais as principais configurações para cálculo de ICMS Simples Nacional](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110154-Quais-as-principais-configura%C3%A7%C3%B5es-para-c%C3%A1lculo-de-ICMS-Simples-Nacional), caso o cálculo do ICMS na TGFDIN ainda não esteja sendo feito, atente-se nas próximas configurações.

Verifique o parâmetro: **"Usar Alíq Efetiva do SN no XML com Crédito de ICMS - USAALQEFETSNXML"**

Caso o mesmo esteja **"Ligado"**, As informações referentes à alíquota efetiva servirão para o preenchimento do Documento de Arrecadação do Simples Nacional (DAS). Sendo assim, aqui serão consideradas as alíquotas efetivas do Simples Nacional para composição das tags <pCredSN> e <vCredICMSSN>.

**Observação:**Sempre que houver alteração da alíquota efetiva na tela Central de Apuração da Receita, aba Apuração do Simples Nacional, campo "Alíquota Efetiva", o sistema irá incluir um novo cadastro nessa tela de Partilha/Anexo do Simples Nacional, considerando as alíquotas efetivas.
Para o cenário onde deve pegar a Alíquota configura na tela de Partilha/Anexo do Simples Nacional, onde não foi feita, ou não é utilizado a Central de Apuração da Receita. O Parâmetro deve se manter desligado.

Após feita as configurações e validado o parâmetro, é preciso validar a Regra de Alíquota de ICMS que está sendo levado ao Item.

É **necessário** ter Alíquota configurada na tela Alíquota de ICMS na aba Geral para "Alimentar" valores de ICMS na TGFITE. O sistema hoje faz a validação da Alíquota cadastrada na aba Geral para "levar valores" na Tabela de Itens, **porém** na TGFDIN (Consultar/Alterar Dados do Item) o sistema irá considerar a Alíquota que estiver configurada na tela Partilha/Anexo do Simples Nacional.

**Exemplo:** Caso tenha a Alíquota configurada na tela Partilha/Anexo do Simples Nacional, porém na Regra da Alíquota de ICMS, aba Geral, deixe o campo Alíquota igual a 0 ou Vazio. O sistema não faz o Cálculo do ICMS, pois por não ter Alíquota na aba Geral, ou estar zerado, entende-se que não existe cálculo de ICMS para o item.

**Alíquota 0,00**

![Imagem 2: Alíquota 0,00](https://ajuda.sankhya.com.br/hc/article_attachments/22063525514135)
 

Tabela de Itens ficam valores zerados:

![Imagem 3: Tabela de Itens ficam valores zerados:](https://ajuda.sankhya.com.br/hc/article_attachments/22063525523735)

TGFDIN (Consultar/Alterar Dados do Item) Ficam zerados, não levando a Alíquota nenhuma.

![Imagem 4: Sendo assim vimos que é preciso ser informado um valor de Alíquota na aba Geral para que o sistema faça o Cálculo do…](https://ajuda.sankhya.com.br/attachments/token/TGkzWAc7rY0jZXf6I7Fm4ud1E/?name=image.png)
 
Sendo assim vimos que é preciso ser informado um valor de Alíquota na aba Geral para que o sistema faça o Cálculo do ICMS na Tabela de Impostos. Levando para o XML nas TAGS corretas e não apresentando valor nos campos próprios do ICMS.
 
**Segue exemplo:**
 
Alíquota de ICMS = 1%

![Imagem 5: Sistema levou o 1% do cálculo para a Tabela de Itens (TGFITE) Na tabela de Impostos (TGFDIN - Consultar/Alterar Dados…](https://ajuda.sankhya.com.br/hc/article_attachments/22063525534487)
 
 Sistema levou o 1% do cálculo para a Tabela de Itens (TGFITE)
 
![Imagem 6: Sistema levou o 1% do cálculo para a Tabela de Itens (TGFITE) Na tabela de Impostos (TGFDIN - Consultar/Alterar Dados…](https://ajuda.sankhya.com.br/hc/article_attachments/22063525544599)
 
Na tabela de Impostos (TGFDIN - Consultar/Alterar Dados do Item) o sistema leva a Alíquota configurada na tela Partilha/Anexo do Simples Nacional, conforme exemplo:

 
![Imagem 7: Sistema levou o 1% do cálculo para a Tabela de Itens (TGFITE) Na tabela de Impostos (TGFDIN - Consultar/Alterar Dados…](https://ajuda.sankhya.com.br/attachments/token/ViptYnRxoY6rdjLCqhf3lgEnE/?name=image.png)

Partilha/Anexo do Simples Nacional

![Imagem 8: No momento em que se confirma a Nota, já podemos perceber o sistema remover os valores que foram colocados do ICMS nos…](https://ajuda.sankhya.com.br/hc/article_attachments/22063509374231)
 

No momento em que se confirma a Nota, já podemos perceber o sistema remover os valores que foram colocados do ICMS nos campos próprios na TGFITE - Tabela de Itens.

![Imagem 9: Vemos que no XML o sistema não leva valores de ICMS em campo próprio, e preenche as devidas tags no XML com os valores…](https://ajuda.sankhya.com.br/hc/article_attachments/22063525561751)
 
Vemos que no XML o sistema não leva valores de ICMS em campo próprio, e preenche as devidas tags no XML com os valores levados na TGFDIN (Consultar/Alterar Dados do Item) com a Alíquota preenchida na Partilha/Anexo do Simples Nacional.

![Imagem 10: Vemos que no XML o sistema não leva valores de ICMS em campo próprio, e preenche as devidas tags no XML com os valores…](https://ajuda.sankhya.com.br/hc/article_attachments/22063509382039)
