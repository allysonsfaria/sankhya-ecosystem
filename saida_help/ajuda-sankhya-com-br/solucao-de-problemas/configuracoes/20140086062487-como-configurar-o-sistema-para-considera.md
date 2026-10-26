---
id: "20140086062487"
titulo: "Como configurar o sistema para considerar o endereço de entrega do parceiro no cálculo dos impostos em notas de vendas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/20140086062487-Como-configurar-o-sistema-para-considerar-o-endere%C3%A7o-de-entrega-do-parceiro-no-c%C3%A1lculo-dos-impostos-em-notas-de-vendas"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-24T12:43:18Z"
rotulos: ["Configuração", "Fiscal", "Parceiro", "NF-e", "Impostos", "Vendas", "Parâmetro"]
---

# Como configurar o sistema para considerar o endereço de entrega do parceiro no cálculo dos impostos em notas de vendas

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/20314355556759) **SITUAÇÃO:**

Como configurar o sistema para considerar o endereço de entrega do parceiro no cálculo dos impostos em notas de vendas.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/20140086055191)SOLUÇÃO:**

Seguem as duas opções de parametrização para que o endereço de retirada/entrega da mercadoria seja utilizado para cálculo do imposto:
 
**Ativando o parâmetro ENDICMS - Endereço para ICMS:**
A abrangência do parâmetro é global. Se alterado, afetara todos os parceiros que tenham endereço de entrega ou recebimento cadastrado. O sistema utilizará o endereço de acordo com a opção selecionada.
 
• **Endereço de entrega:** Cadastrado na aba 'Endereço de entrega' na tela 'Parceiros'.
• **Endereço recebimento:** Cadastrado na aba 'Recebimento/Trabalho' na tela 'Parceiros'.
• **Endereço Principal:** Cadastrado na aba 'Endereço' na tela 'Parceiros'.
 
**Ativando o parâmetro USENDENTREGA - Usa endereço de entrega dos contatos:**
Utilizando o endereço de contato do parceiro, pode se cadastrar quantos contatos forem necessários  e informar o contato que será utilizado no lançamento da nota.
 
![Imagem 3: Seguem as duas opções de parametrização para que o endereço de retirada/entrega da mercadoria seja utilizado para…](https://ajuda.sankhya.com.br/hc/article_attachments/20314355562775) Acesse a tela **Preferências** (Configurações > Avançado) e pesquise pelo parâmetro **"Usa endereço de entrega dos contatos - USENDENTREGA"**. Certifique-se que o mesmo esteja ligado.
 
![Imagem 4: Seguem as duas opções de parametrização para que o endereço de retirada/entrega da mercadoria seja utilizado para…](https://ajuda.sankhya.com.br/hc/article_attachments/20314355564951) Acesse a tela **Parceiros** (Configurações > Cadastros) e na aba 'Endereço' verifique se a opção **"Utiliza endereço de entrega do contato"** está marcada.

![Imagem 5: Seguem as duas opções de parametrização para que o endereço de retirada/entrega da mercadoria seja utilizado para…](https://ajuda.sankhya.com.br/hc/article_attachments/20314344085271)

![Imagem 6: Acesse a tela Parceiros (Configurações > Cadastros) e cadastre os dados do endereço de entrega na aba 'Contatos'.](https://ajuda.sankhya.com.br/hc/article_attachments/20314355574167) Acesse a tela **Parceiros** (Configurações > Cadastros) e cadastre os dados do endereço de entrega na aba 'Contatos'.

![Imagem 7: Acesse a tela Parceiros (Configurações > Cadastros) e cadastre os dados do endereço de entrega na aba 'Contatos'.](https://ajuda.sankhya.com.br/hc/article_attachments/20314355584919)

![Imagem 8: Adicione os campo 'Contato' e 'Contato de Entrega' no layout da nota. Caso tenha dúvidas de como fazer acesse o manual…](https://ajuda.sankhya.com.br/hc/article_attachments/20314355595799) Adicione os campo 'Contato' e 'Contato de Entrega' no layout da nota. Caso tenha dúvidas de como fazer acesse o manual da tela [Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota).

![Imagem 9: Adicione os campo 'Contato' e 'Contato de Entrega' no layout da nota. Caso tenha dúvidas de como fazer acesse o manual…](https://ajuda.sankhya.com.br/hc/article_attachments/20314355608087)

Com essas configurações, ao lançar um pedido/nota de venda e informar um Parceiro que esteja com o campo 'Utiliza endereço de entrega do contato' marcado, o sistema irá informar um contato com endereço preenchido no cabeçalho do pedido/nota. 
 
**Observações:**

Se o Parceiro possuir um contato cadastrado, mas o mesmo não tiver endereço preenchido, o sistema irá a seguinte mensagem: "Contato não tem endereço preenchido";
Se o campo 'Utiliza endereço de entrega do contato' estiver marcado, mas o Parceiro não possui um contato cadastrado, o sistema não irá salvar o pedido/nota e emitirá a seguinte mensagem: "É obrigatório informar o contato do parceiro para entrega".
 
No XML constará o endereço principal cadastrado e o endereço do contato de entrega.

**Orientação 2:**

**Caso o descrito acima, por algum motivo, não atenda às necessidades da empresa, essa segunda opção pode ser analisada, e caso seja viável, podemos adotá-la.**

Para que seja considerada a alíquota correta no lançamento da nota, a sugestão é que seja criada uma regra de alíquota entre os estados da empresa e do parceiro principal, cuja a primeira exceção seja a classificação fiscal do parceiro (consumidor final não contribuinte) e a segunda exceção seja o CFOP(cfop interno). Assim, o sistema irá aplicar a regra de alíquota com as devidas tributações e alíquota, como se fosse uma operação interna.

![Imagem 10: Para que seja considerada a alíquota correta no lançamento da nota, a sugestão é que seja criada uma regra de alíquota…](https://ajuda.sankhya.com.br/hc/article_attachments/21164843534871)

![Imagem 11: Para que seja considerada a alíquota correta no lançamento da nota, a sugestão é que seja criada uma regra de alíquota…](https://ajuda.sankhya.com.br/hc/article_attachments/21164843548823)

![Imagem 12: Para que seja considerada a alíquota correta no lançamento da nota, a sugestão é que seja criada uma regra de alíquota…](https://ajuda.sankhya.com.br/hc/article_attachments/21164843557655)
