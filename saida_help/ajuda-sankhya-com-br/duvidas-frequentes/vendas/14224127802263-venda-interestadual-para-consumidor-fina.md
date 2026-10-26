---
id: "14224127802263"
titulo: "Venda interestadual para 'Consumidor Final Contribuinte' ou 'Consumidor Final Não Contribuinte'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14224127802263-Venda-interestadual-para-Consumidor-Final-Contribuinte-ou-Consumidor-Final-N%C3%A3o-Contribuinte"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T14:59:10Z"
rotulos: ["Configuração", "Parceiro", "NF-e", "DIFAL", "ICMS", "Impostos", "Definir data e percentual", "Ativar DIFAL e ICMS", "Habilitar cálculo e configurar regras"]
---

# Venda interestadual para 'Consumidor Final Contribuinte' ou 'Consumidor Final Não Contribuinte'

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16912376132247) **SITUAÇÃO:**

Como parametrizar o sistema para que a regra de alíquota seja puxada corretamente em operações de venda interestaduais onde a classificação ICMS do parceiro é 'Consumidor Final Contribuinte' ou 'Consumidor Final Não Contribuinte'.

![Imagem 2: Acesse a tela " Partilhas DIFAL" (Caminho de acesso: Configurações » Cadastros » Partilhas DIFAL):](https://ajuda.sankhya.com.br/hc/article_attachments/16912392990743) Acesse a tela "**Partilhas DIFAL"** (Caminho de acesso: Configurações » Cadastros » Partilhas DIFAL):

**"Data Início Partilha"**: informe a data início da partilha de acordo com o ano vigente;

**"Percentual de Partilha DIFAL":** informe o percentual necessário de acordo com a orientação da contabilidade da empresa.

![Imagem 3: "Percentual de Partilha DIFAL": informe o percentual necessário de acordo com a orientação da contabilidade da empresa.](https://ajuda.sankhya.com.br/hc/article_attachments/14223240644247)

![Imagem 4: Acesse a tela " Tipos de Operação" (Caminho de acesso: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)](https://ajuda.sankhya.com.br/hc/article_attachments/16912376138007) Acesse a tela **"Tipos de Operação"** (Caminho de acesso: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)

Aba: **"Impostos"**

**"Calcular DIFAL Partilhado":** ativo

**"Tem ICMS"**: ativo

**"Cálculo de ICMS, IPI e ISS":** Calcula e digita ou Calcula e não digita (de acordo com o processo da empresa)

![Imagem 5: "Cálculo de ICMS, IPI e ISS": Calcula e digita ou Calcula e não digita (de acordo com o processo da empresa)](https://ajuda.sankhya.com.br/hc/article_attachments/15136888513175)

![Imagem 6: Acesse a tela " Produtos" (Caminho de acesso: Configurações » Cadastros » Produtos » Produtos), v erifique as marcações…](https://ajuda.sankhya.com.br/hc/article_attachments/16912376139287) Acesse a tela **"Produtos"** (Caminho de acesso: Configurações » Cadastros » Produtos » Produtos), verifique as marcações abaixo, na aba **"Impostos"** ou **"Impostos/Informações por Empresa",** caso a empresa trabalhe com Imposto por Empresa.

**"Calcular ICMS":** ativo

**"Calcular DIFAL?":** ativo

![Imagem 7: "Calcular DIFAL?": ativo](https://ajuda.sankhya.com.br/hc/article_attachments/15136952148375)

![Imagem 8: Acesse a tela " Alíquotas de ICMS" (Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS)](https://ajuda.sankhya.com.br/hc/article_attachments/16912392994583) Acesse a tela **"Alíquotas de ICMS"** (Caminho de acesso: Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ICMS)

Nesse cadastro, parametrize as regras de alíquota para as UF's de origem e destino, com o 'Tipo 1 de exceção', de acordo com a classificação ICMS do parceiro (Consumidor ou Consumidor Contribuinte).

**(1)** **Exceções:** Tipo 1:
**Consumidor:** quando o parceiro for 'Consumidor Final Não Contribuinte';
**Consumidor Contribuinte:** quando o parceiro for 'Consumidor Final Contribuinte'.

- Preencha corretamente a sessão: 'DIFAL / FCP (Não contribuinte)', de acordo com as orientações da contabilidade da empresa.
  - Lembrando que quando o parceiro é 'Consumidor Final Não Contribuinte', preencha o campo **"Alíq. Interna Destino"** para gerar a Tag <ICMSUFDest>.
  - Para mais informações sobre a geração da Tag e fórmulas para o cálculo, acesse o artigo: '[Como é feito o cálculo do DIFAL no sistema?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044296013-Como-%C3%A9-feito-o-c%C3%A1lculo-do-DIFAL-no-sistema-?source=search&auth_token=eyJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjo5NjE4MTY4LCJ1c2VyX2lkIjoxNTAyNTI0MzQ2NjIxLCJ0aWNrZXRfaWQiOjI3NDY1MiwiY2hhbm5lbF9pZCI6NjMsInR5cGUiOiJTRUFSQ0giLCJleHAiOjE2ODUyODE2MzN9.s_pTatalMiW8PYlNN1I1eRfMd012xL3r2rmbUf633lk)'.

![Imagem 9: Para mais informações sobre a geração da Tag e fórmulas para o cálculo, acesse o artigo: ' Como é feito o cálculo do…](https://ajuda.sankhya.com.br/hc/article_attachments/15136948269463)

**![Imagem 10: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16912392996247)OBSERVAÇÃO:**

Todas as configurações relacionadas diretamente ao 'Difal' são necessárias somente caso o parceiro seja 'Consumidor Final Não Contribuinte'.
