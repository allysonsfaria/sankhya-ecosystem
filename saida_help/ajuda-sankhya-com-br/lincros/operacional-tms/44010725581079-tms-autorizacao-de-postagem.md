---
id: "44010725581079"
titulo: "[TMS] - Autorização de Postagem"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010725581079--TMS-Autoriza%C3%A7%C3%A3o-de-Postagem"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T18:44:52Z"
rotulos: ["sync_hc", "lincros", "sync_hash_c1293d39ca03", "lincros_13433304"]
---

# [TMS] - Autorização de Postagem

**Menu:** Operacional > Importação > Correios > Autorização de postagem

**Objetivo**: Como realizar a importação de autorização de postagem (E-ticket) que pode ser via arquivo .xlsx ou via webservice, permitindo assim acompanhar o andamento das autorizações através do sistema

**Considerações**:

- Para importação é obrigatório informar unidade, transportadora e modal;
- As transportadoras buscadas serão apenas aquelas que no cadastro de transportadora estão marcadas como Transportadora Correios;
- O e-mail informado no campo 'E-mails para notificar conclusão' é o que receberá notificação quando a importação for concluída;
- O arquivo para importação é gerado através do SIGEP WEB Correios, e deve ser de extensão .xlsx.

## Como importar uma Autorização de Postagem:

1. Acesse o Menu: Operacional > Importação > Correios > Autorização de postagem;
2. Informe os campos abaixo e clique em "Adicionar" para anexar o arquivo .xlsx gerado através do SIGEP WEB Correios;

   ![Imagem 1: Informe os campos abaixo e clique em "Adicionar" para anexar o arquivo .xlsx gerado através do SIGEP WEB Correios;](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963363025/0261c66207f20def01253f30857a/1B6E20274B6F29F79C577B0BC68E9DFA?expires=1791331200&signature=1ad4c3441887a9c2f714865391e4e1b0739aba86533f22a4dd7b28750336db25&req=dSkhFcp4noFdXPMW3nq%2BgQZIIFtjqGFy3zyNZ%2BFbTcOCmblqpNSgQU4nrgrv%0AHA2rlr0oe78rNEMA8Y5tJ5F7VCc%3D%0A)

Abaixo os campos obrigatórios para importação da Autorização de Postagem:

- Nº Autorização
- Situação
- Status do Objeto
- Data da Postagem
- Remetente
- CNPJ/CPF
- CEP Origem
- Destinatário
- CEP Destino

Caso tenha sido informado um e-mail, será notificado através dele quando for concluído o processamento da planilha.

![Imagem 2: Caso tenha sido informado um e-mail, será notificado através dele quando for concluído o processamento da planilha.](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963363034/dfef86b7550115f92c5e914b01e0/CC56A50913AB0553C113AFB656BC6D5E?expires=1791331200&signature=f945ea2eb1ec5e1f4ea07ad9490899dd234a3090faf2db9d40978c4d61aad994&req=dSkhFcp4noFcXfMW3nq%2BgeoACgqziwkedRoN%2FXuCmghj7tApkwTKEePIoppy%0A7EQD3I1%2Fbd918xvOXSYHXwJNjgw%3D%0A)

Após a importação do arquivo, é possível acessar as autorizações em **Operacional > Documentos de despacho > Correios > Autorização de postagem**

![Imagem 3: Após a importação do arquivo, é possível acessar as autorizações em Operacional > Documentos de despacho > Correios >…](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963363047/060fb719cbd20ab1870429ab7793/5ACE70A28C1C91400CCD801931B02484?expires=1791331200&signature=487064532e0d6dd6201f57137e97d5d219704521a40d77aa8f9fdea3f81cd415&req=dSkhFcp4noFbXvMW3nq%2BgURTBUMIj%2Foo%2FjmkNidO1LA7WG7WvZ6c6rI6jeGp%0AWbXKCboZBhrTs7StFGRdGApc624%3D%0A)

Para cada autorização importada, o sistema criará um pré-conhecimento. Que pode ser acessado através do link na edição de autorização de postagem;

![Imagem 4: Para cada autorização importada, o sistema criará um pré-conhecimento. Que pode ser acessado através do link na edição…](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963363054/ef1263f4098c38ba65c284af5058/504C0FA77059867288F34F44E1089D1F?expires=1791331200&signature=7ce18ddad2df3ca9d49efdb01fac31024ca0e3d16fb8e3925713b9411a628337&req=dSkhFcp4noFaXfMW3nq%2BgVxeCqPxaMqrWRHg39d88ZHvjXOmnYO0GBNS3w2B%0AZk1sd6acUkbgE9zoBy1QoN3FFWw%3D%0A)

O código de rastreio informado na planilha ou JSON, é o que será utilizado posteriormente para importar as ocorrências dos Correios. As ocorrências importadas podem ser visualizadas na tela de Edição de autorização de postagem.

![Imagem 5: O código de rastreio informado na planilha ou JSON, é o que será utilizado posteriormente para importar as ocorrências…](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963363068/87ca7cccf7f65a381d768a417439/8910109B714DFE7847B3973BCC70B461?expires=1791331200&signature=81f47e3fe5e612046a34dccd27fca0b7bda380220eb82d666fa83547c402b5ae&req=dSkhFcp4noFZUfMW3nq%2BgQPm84nWabwSpSCZyWnQ5AQ8CWwUoIwRBz2P91XP%0A0Ocj9GITBS4AEVRqnwhaNZ69lxk%3D%0A)

Nas telas de Acompanhamento de entregas e Rastreamento de mercadorias é possível visualizar as autorizações de postagem.

**Menu**: Entregas e ocorrência > Acompanhamento de entregas

![Imagem 6: Menu : Entregas e ocorrência > Acompanhamento de entregas](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963363078/1a028e7bd74ef07d56723b0437ef/152B4357D9A4F4BAE85C67262254A022?expires=1791331200&signature=f28fe51a6af22e16a279be3487c7604c637411e86d4540a2e07125eccb07ed75&req=dSkhFcp4noFYUfMW3nq%2BgbOmTTP5Xv8%2BUk%2FlDmk3ooMa1fKuT8bHfmihaB5N%0AjzL8IQ4ks3RyXr7Uy%2FEXGPkWhCI%3D%0A)

**Menu**: Entregas e ocorrências > Rastreamento de mercadorias

![Imagem 7: Menu : Entregas e ocorrências > Rastreamento de mercadorias](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963363090/356b925a82861c07bb1659980717/C923E370C4AD133960387FEB233136EE?expires=1791331200&signature=a95e5e70ba661f8a7381ba1a3ad5b1c262cca1c998dec2ebfc38165c9727e031&req=dSkhFcp4noFWWfMW3nq%2Bgec05yYe3GSaX0cmYcUy%2BJDi9T4jbh2jeIXo1ODi%0AyAAaocAqFyls%2Bjap06tqAn5N8aQ%3D%0A)

**Obs.:** Para importação das ocorrências, é necessário possuir [integração com Correios](https://sankhya.zendesk.com/hc/pt-br/articles/44010725581079).

Os campos com \* são campos de preenchimento obrigatório.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
