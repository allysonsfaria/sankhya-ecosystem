---
id: "37775292726807"
titulo: "Como gerar e enviar o evento S1200"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37775292726807-Como-gerar-e-enviar-o-evento-S1200"
trilha: "Universidade Sankhya > Gestão eSocial"
atualizado_em: "2026-07-22T14:08:27Z"
rotulos: ["Eventos", "eSocial", "Folha de Pagamento", "Central do eSocial", "Geração de Arquivos", "Remuneração"]
---

# Como gerar e enviar o evento S1200

| Categoria |
| --- |
| [O que é o evento S1200?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37775292726807-Como-gerar-e-enviar-o-evento-S1200#h_01KFB7P9P9VC7NPXEWKSVN6SRW) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37775292726807-Como-gerar-e-enviar-o-evento-S1200#h_01KFB7P4N5HVV3496X3B0Z7M42) |
| [Para calcular a folha](https://ajuda.sankhya.com.br/hc/pt-br/articles/37775292726807-Como-gerar-e-enviar-o-evento-S1200#h_01KFB7NJPZ9TN3M4MX0VS3R1G0) |
| [Geração e envio do evento S1200](https://ajuda.sankhya.com.br/hc/pt-br/articles/37775292726807-Como-gerar-e-enviar-o-evento-S1200#h_01KFB7NF0793166CB1MTERK1RN) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37775292726807-Como-gerar-e-enviar-o-evento-S1200#h_01KFB7N43VS32TNK4YDDRJKQ92) |

## Evento S1200 - Remuneração do Trabalhador

#### O que é o evento S1200?

O evento S-1200 é utilizado para informar ao eSocial os valores de remuneração devidos ao trabalhador em uma determinada competência, abrangendo salários, adicionais, horas extras, descontos, retenções e demais proventos previstos na folha de pagamento. Ele deve ser enviado para todos os trabalhadores vinculados ao Regime Geral de Previdência Social, incluindo estagiários e bolsistas, mesmo que o pagamento ainda não tenha sido efetivado no período. Faz parte do grupo de eventos periódicos e é obrigatório mensalmente. Os dados informados nesse evento são utilizados para apuração de encargos sociais e geração de tributos via DCTFWeb, além de refletirem diretamente nos cálculos de INSS, FGTS e IRRF. Para garantir a conformidade, o S-1200 deve estar alinhado aos eventos anteriores, como cadastro de vínculos (S-2200), rubricas (S-1010) e lotações tributárias (S-1020) — sendo um dos registros mais críticos para validar a integridade da folha junto ao governo.

##### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/944191363)

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. ##### Para calcular a folha

**Acesse**: Pessoal+ » Rotinas Folha » Gerenciador de Folhas

- Na lateral direita da tela, clique no botão Liberação para eSocial
- Informe o tipo de folha que deseja liberar
- Informe a referência do cálculo
- Defina o tipo de ação “Liberar dados”
- Selecione a empresa no resultado dos filtros
- Na aba Funcionários selecione os funcionários que terão os dados da folha liberados para o esocial
- Clique no botão “Liberar dados para esocial”

2. ##### Geração e envio do evento S1200

**Acesse**: Pessoal+  » Rotinas Folha »  Central do eSocial

- Na lateral esquerda da tela, selecione a empresa, a referência e o ambiente de envio, e em seguida clique em '**Carregar**'.
- No menu lateral, acesse a aba “**Geração**” e escolha a opção **Individual**
- Selecione o evento **S-1200** e em seguida clique em “**Iniciar** **Geração**”
- Após a geração, o evento será listado como card na aba '**Eventos Pendentes**'. Para realizar a transmissão ao eSocial, utilize o botão '**Enviar dados**'

Após o envio, o evento ficará na aba '**Eventos na Fila**' até a conclusão do processamento pelo ambiente do eSocial. Finalizado o envio, ele será movido para a aba '**Acompanhamento**', onde é possível visualizar os dados enviados e os XMLs de retorno por meio do botão '**Visualizar dados**'

#### Correção e Repetição

- Revise os registros para confirmar se os passos foram seguidos.
- Caso haja erro no registro verifique atentamente os campos mencionados no erro e consulte o manual do eSocial.
