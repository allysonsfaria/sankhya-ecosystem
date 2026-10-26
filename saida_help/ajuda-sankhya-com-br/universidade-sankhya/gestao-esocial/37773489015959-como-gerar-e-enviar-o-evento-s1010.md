---
id: "37773489015959"
titulo: "Como gerar e enviar o evento S1010"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37773489015959-Como-gerar-e-enviar-o-evento-S1010"
trilha: "Universidade Sankhya > Gestão eSocial"
atualizado_em: "2026-07-22T14:08:41Z"
rotulos: ["Configuração", "Eventos", "XML", "eSocial", "Folha de Pagamento", "Central do eSocial"]
---

# Como gerar e enviar o evento S1010

| Categoria |
| --- |
| [O que é o evento S1010?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773489015959-Como-gerar-e-enviar-o-evento-S1010#h_01KFB214NEEKXQ6DFPNTWT3BSM) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773489015959-Como-gerar-e-enviar-o-evento-S1010#h_01KFB2108JKQ465M6HC78XMPS2) |
| [Conferência dos eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773489015959-Como-gerar-e-enviar-o-evento-S1010#h_01KFB20NQSAMBP17ECN1GE0475) |
| [Geração e envio do evento S1010](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773489015959-Como-gerar-e-enviar-o-evento-S1010#h_01KFB20HBN3PSW63VTRJNX2XY0) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773489015959-Como-gerar-e-enviar-o-evento-S1010#h_01KFB205X9DDAV0BNA28MCGTHG) |

## Evento S1010 - Rúbricas

#### O que é o evento S1010?

O evento S-1010 é responsável por registrar, alterar ou excluir as rubricas utilizadas na folha de pagamento da empresa. Ele funciona como uma tabela de referência que detalha cada tipo de provento, desconto ou informação informativa aplicada ao colaborador, como salário, horas extras, adicionais, faltas, entre outros.

Essas rubricas precisam estar classificadas corretamente de acordo com a Tabela 3 do eSocial, que define a natureza de cada lançamento.

Esse evento é essencial porque serve de base para validar os eventos de remuneração (como o S-1200), garantindo que tudo esteja em conformidade com as regras da legislação trabalhista e previdenciária.

##### Vídeo com demonstração prática no sistema

Geração e envio do evento S1010

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/942352418)

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

Siga as orientações indicadas abaixo para executar o evento S1010 em sua base de testes.

1. ##### Conferência dos eventos

**Acesse**: Pessoal+  » Cadastros »  Eventos

- Com o evento desejado selecionado verifique:
- Marcação do campo “Compõe eSocial” na aba Básico
- Preenchimento dos campos que indicam a natureza da rúbrica e incidências para a previdência, IRRF, FGTS e Contribuição sindical

2. ##### Geração e envio do evento S1010

**Acesse**: Pessoal+  » Rotinas Folha »  Central do eSocial

- Na lateral esquerda da tela, selecione a empresa, a referência e o ambiente de envio, e em seguida clique em '**Carregar**'.
- No menu lateral, acesse a aba “**Geração**” e escolha a opção **Individual**
- Selecione o evento **S-1010** e em seguida clique em “**Iniciar** **Geração**”
- Após a geração, o evento será listado como card na aba '**Eventos Pendentes**'. Para realizar a transmissão ao eSocial, utilize o botão '**Enviar dados**'

Após o envio, o evento ficará na aba '**Eventos na Fila**' até a conclusão do processamento pelo ambiente do eSocial. Finalizado o envio, ele será movido para a aba '**Acompanhamento**', onde é possível visualizar os dados enviados e os XMLs de retorno por meio do botão '**Visualizar dados**'

#### Correção e Repetição

- Revise os registros para confirmar se os passos foram seguidos.
- Caso haja erro no registro verifique atentamente os campos mencionados no erro e consulte o manual do eSocial.
