---
id: "37775418920983"
titulo: "Como gerar e enviar o evento S1210"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37775418920983-Como-gerar-e-enviar-o-evento-S1210"
trilha: "Universidade Sankhya > Gestão eSocial"
atualizado_em: "2026-07-22T14:08:26Z"
rotulos: ["Eventos", "XML", "Impostos", "Pagamento", "DIRF", "eSocial", "Central do eSocial"]
---

# Como gerar e enviar o evento S1210

| Categoria |
| --- |
| [O que é o evento S1210?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37775418920983-Como-gerar-e-enviar-o-evento-S1210#h_01KFB81QRTKB0BX385FTHY82S0) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37775418920983-Como-gerar-e-enviar-o-evento-S1210#h_01KFB81K025KJ8S26850E3REK1) |
| [Geração e envio do evento S1210](https://ajuda.sankhya.com.br/hc/pt-br/articles/37775418920983-Como-gerar-e-enviar-o-evento-S1210#h_01KFB814ACKM3AWD0E5C5E1A5T) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37775418920983-Como-gerar-e-enviar-o-evento-S1210#h_01KFB80SB5Q8H4RX72N583ZTK5) |

## Evento S1210 - Pagamento de Rendimentos do Trabalho

#### O que é o evento S1210?

O evento S-1210 é utilizado para informar ao eSocial os valores efetivamente pagos ao trabalhador, com ou sem vínculo empregatício, incluindo salários, férias, 13º, rescisões e Participação nos Lucros ou Resultados (PLR). Ele complementa o evento S-1200 (Remuneração), registrando quando e como os rendimentos foram pagos, além de detalhar as retenções de Imposto de Renda Retido na Fonte (IRRF). Esse evento é essencial para garantir o cruzamento correto com a DIRF e para o cumprimento das obrigações acessórias. O envio do S-1210 é obrigatório sempre que houver pagamento de rendimento, e deve ser realizado até o dia 15 do mês seguinte ao pagamento, respeitando o regime de caixa adotado pela empresa.

##### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/944433258)

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

**Atenção!** Para gerar o evento S-1210, é necessário que o evento S-1200 já tenha sido enviado e recepcionado pelo eSocial. O S-1210 deve ser enviado na referência do pagamento.

**Por exemplo:** se a folha de janeiro foi paga em fevereiro (regime de caixa), o evento S-1200 será enviado com a competência de janeiro, e o S-1210 será enviado com a referência de fevereiro, que é o mês em que o pagamento ocorreu.

1. ##### Geração e envio do evento S1210

**Acesse**: Pessoal+  » Rotinas Folha »  Central do eSocial

- Na lateral esquerda da tela, selecione a empresa, a referência e o ambiente de envio, e em seguida clique em '**Carregar**'.
- No menu lateral, acesse a aba “**Geração**” e escolha a opção **Individual**
- Selecione o evento **S-1210** e em seguida clique em “**Iniciar** **Geração**”
- Após a geração, o evento será listado como card na aba '**Eventos Pendentes**'. Para realizar a transmissão ao eSocial, utilize o botão '**Enviar dados**'

Após o envio, o evento ficará na aba '**Eventos na Fila**' até a conclusão do processamento pelo ambiente do eSocial. Finalizado o envio, ele será movido para a aba '**Acompanhamento**', onde é possível visualizar os dados enviados e os XMLs de retorno por meio do botão '**Visualizar dados**'

#### Correção e Repetição

- Revise os registros para confirmar se os passos foram seguidos.
- Caso haja erro no registro verifique atentamente os campos mencionados no erro e consulte o manual do eSocial.
