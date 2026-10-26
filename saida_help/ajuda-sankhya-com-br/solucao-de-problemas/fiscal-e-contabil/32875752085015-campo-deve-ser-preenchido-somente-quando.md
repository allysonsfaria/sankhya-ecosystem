---
id: "32875752085015"
titulo: "Campo deve ser preenchido somente quando Forma de Tributação do Lucro abranger o Lucro Presumido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32875752085015-Campo-deve-ser-preenchido-somente-quando-Forma-de-Tributa%C3%A7%C3%A3o-do-Lucro-abranger-o-Lucro-Presumido"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-25T16:29:17Z"
rotulos: ["Configuração", "ECF", "Impostos", "Financeiro", "TIP_ESC_PRE", "0010", "forma_trib", "ECF- Escrituração Contábil Fiscal", "Lucro Presumido"]
---

# Campo deve ser preenchido somente quando Forma de Tributação do Lucro abranger o Lucro Presumido

**MENSAGEM**

Campo deve ser preenchido somente quando Forma de Tributação do Lucro abranger o Lucro Presumido. Ou seja, o campo forma\_trib deve ser igual a 3, 4, 5 ou 7

![Imagem 1: Campo deve ser preenchido somente quando Forma de Tributação do Lucro abranger o Lucro Presumido. Ou seja, o campo…](https://ajuda.sankhya.com.br/hc/article_attachments/33183390239511)

**SITUAÇÃO**

O campo ''**TIP\_ESC\_PRE''** só deve ser preenchido se a empresa estiver **tributando pelo Lucro Presumido**. Os valores válidos para **forma\_trib** são:

- **3** – Lucro Presumido
- **4** – Lucro Presumido – Imunes
- **5** – Lucro Presumido – Isentas
- **7** – Lucro Presumido – SCP

**SOLUÇÃO**

No Sankhya, acesse a tela ''**Empresa'' '**(Contabilidade'' > ''Preferências), aba **''ECF- Escrituração Contábil Fiscal**'' e sub-aba ''**Parâmetros de tributação**'':

- Quando o campo **''Forma de Tributação''** está Lucro Real, o Campo **''Escrituração''** não deve ter configuração.

![Imagem 2: Quando o campo ''Forma de Tributação'' está Lucro Real, o Campo ''Escrituração'' não deve ter configuração.](https://ajuda.sankhya.com.br/hc/article_attachments/33153322826775)

**AMBIENTE E CAUSA DO ERRO:** 

Se o campo ''**forma\_trib''** estiver com um valor diferente, como, por exemplo, **1 –** Lucro Real**,** e ainda assim o campo ''**TIP\_ESC\_PRE'',** for preenchido, isso resultará no erro exibido.

**Registro:** 0010 – Parâmetros de Tributação

**Campo com erro:** TIP\_ESC\_PRE (Tipo de Escrituração do Lucro Presumido)
