---
id: "360044110654"
titulo: "Campo Obrigatório. 4- TIPO_MOV 'Tipo de Movimentação' - REGISTRO G125"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110654-Campo-Obrigat%C3%B3rio-4-TIPO-MOV-Tipo-de-Movimenta%C3%A7%C3%A3o-REGISTRO-G125"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:53:20Z"
rotulos: ["#revisadojunior", "Configuração", "Fiscal", "TOP", "EFD", "Campo Obrigatório. TIPO_MOV - REGISTRO G125", "Defina 'Tipo de Mov. do Bem' em \"Tipo de Operação - TOP\"", "Registro G125 enviado sem 'Tipo de Movimentação do Bem'", "Registro G125"]
---

# Campo Obrigatório. 4- TIPO_MOV 'Tipo de Movimentação' - REGISTRO G125

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16618813954071) MENSAGEM:**

Campo Obrigatório. 4- TIPO\_MOV 'Tipo de Movimentação' - REGISTRO G125.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16618794456983) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse a tela "Tipo de Operação - TOP" , localize o cód. TOP utilizado no respectivo lançamento.](https://ajuda.sankhya.com.br/hc/article_attachments/16618813962135) Acesse a tela **"Tipo de Operação - TOP"**, localize o cód. TOP utilizado no respectivo lançamento.

**(1)** Aba Livros Fiscais » Campo **'Tipo de Mov. do Bem (SPED)'**: este campo indica o 'Tipo de Movimentação do Bem' para efeito de SPED, será o responsável por compor o campo 04 TIPO\_MOV do registro G125.

![Imagem 4: (1) Aba Livros Fiscais » Campo 'Tipo de Mov. do Bem (SPED)' : este campo indica o 'Tipo de Movimentação do Bem' para…](https://ajuda.sankhya.com.br/hc/article_attachments/14873352131735)

De acordo com orientações da Contabilidade, defina o campo com uma das opções abaixo:

- MC = Imobilização oriunda do Ativo Circulante;
- AT = Alienação ou Transferência;
- PE = Perecimento, Extravio ou Deterioração;
- OT = Outras Saídas do Imobilizado

**![Imagem 5: IMPORTANTE: o ajuste acima é histórico, dessa forma a configuração correta impedirá o erro para os próximos…](https://ajuda.sankhya.com.br/hc/article_attachments/16618813966999) IMPORTANTE:** o ajuste acima é histórico, dessa forma a configuração correta impedirá o erro para os próximos lançamentos. Para os lançamentos já impactados será necessário que os ajustes dessa referência sejam realizados diretamente no PVA.  Caso trate-se de um volume significativo, necessário ajustes via banco junto ao DBA da empresa.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16618794460823)CAUSA:**

Mensagem apresentada quando o registro G125 é enviado sem informações do 'Tipo de Movimentação do Bem'.
