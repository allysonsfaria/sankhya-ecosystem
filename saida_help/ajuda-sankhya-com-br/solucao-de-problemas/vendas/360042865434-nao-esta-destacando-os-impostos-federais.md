---
id: "360042865434"
titulo: "Não está destacando os impostos federais como PIS / COFINS / CSLL no XML da NFS-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360042865434-N%C3%A3o-est%C3%A1-destacando-os-impostos-federais-como-PIS-COFINS-CSLL-no-XML-da-NFS-e"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:05:49Z"
rotulos: ["#RevisadoJR", "Configuração", "COFINS", "PIS", "CSLL", "XML", "Impostos", "NFS-e", "Defina imposto como \"Retido\"", "Cheque \"Retém no Financeiro\"", "Ative \"DESTIMPNRETIDO\""]
---

# Não está destacando os impostos federais como PIS / COFINS / CSLL no XML da NFS-e

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16114214643351) SOLUÇÃO:**

![Imagem 2: Acesse Configurações » Cadastros » " Impostos "](https://ajuda.sankhya.com.br/hc/article_attachments/16114214646167) Acesse Configurações » Cadastros » **"[Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos)"**

Campo **"Tipo Impostos"**, selecione o Imposto correspondente e configure o Tipo de Imposto como Retido.

![Imagem 3: Campo "Tipo Impostos" , selecione o Imposto correspondente e configure o Tipo de Imposto como Retido.](https://ajuda.sankhya.com.br/hc/article_attachments/12092734646167)

O sistema na geração do XML, busca primeiramente os impostos calculados via outros impostos como retidos (TGFIMN), desde que o Tipo Imposto no cadastro do imposto esteja devidamente configurado com imposto correspondente (TGFIMC.TIPOIMPOSTO), como PIS/COFINS/CSLL.

**(2)** Caso não tenha configuração via Outros Impostos, sistema passa para Etapa 2.

![Imagem 4: Acesse Alíquotas de PIS / COFINS / CSLL](https://ajuda.sankhya.com.br/hc/article_attachments/16114214653847) Acesse Alíquotas de PIS / COFINS / CSLL

**(2)** Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de PIS

**(2)** Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de COFINS

**(2)** Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de CSLL

Campo **"Retém no Financeiro"** marcado.

Na ausência de impostos calculados via outros impostos, o sistema verifica na tabela de impostos, se existem os impostos PIS, COFINS e CSLL, calculados como retidos -  marcação 'Retém no financeiro' do cadastro de alíquotas de PIS, COFINS e CSLL (TGFIFE.RETEMFIN).

**(2)** Caso o cálculo dos impostos federais seja não retido, mas precisa destacar no xml, sistema passa para a Etapa 3.

![Imagem 5: Caso não exista o cálculo dos impostos como retidos, mas os mesmos estejam calculados em um dos pontos mencionados…](https://ajuda.sankhya.com.br/hc/article_attachments/16114214656919) Caso não exista o cálculo dos impostos como **retidos,**mas os mesmos estejam calculados em um dos pontos mencionados acima como inclusos, para destacar os impostos federais no XML, ligue o parâmetro **"DESTIMPNRETIDO - Destacar impostos federais na NFS-e mesmo quando não retidos"**.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16114214663959) CAUSA:**

Ocorre quando em casos que o imposto não seja do tipo retido via outros impostos ou via Alíquotas de Impostos e mesmo assim precisa destacar na nota, porém o parâmetro DESTIMPNRETIDO está desligado.
