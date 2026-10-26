---
id: "37775482726423"
titulo: "Como gerar a exclusão dos eventos S1200/S1210"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37775482726423-Como-gerar-a-exclus%C3%A3o-dos-eventos-S1200-S1210"
trilha: "Universidade Sankhya > Gestão eSocial"
atualizado_em: "2026-07-22T14:08:25Z"
rotulos: ["Eventos", "Folha", "S1200", "eSocial", "Gerenciador de Folhas", "Central do eSocial", "S1210"]
---

# Como gerar a exclusão dos eventos S1200/S1210

| Categoria |
| --- |
| [Exclusão](https://ajuda.sankhya.com.br/hc/pt-br/articles/37775482726423-Como-gerar-a-exclus%C3%A3o-dos-eventos-S1200-S1210#h_01KFB88XQ6SSAKBCKA9VBPSYPH) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37775482726423-Como-gerar-a-exclus%C3%A3o-dos-eventos-S1200-S1210#h_01KFB88S9DWTBWVHP76MFHV2M7) |
| [Para excluir a folha](https://ajuda.sankhya.com.br/hc/pt-br/articles/37775482726423-Como-gerar-a-exclus%C3%A3o-dos-eventos-S1200-S1210#h_01KFB888B5G83W8W4ABNE0R4F4) |
| [Exclusão do evento S1210](https://ajuda.sankhya.com.br/hc/pt-br/articles/37775482726423-Como-gerar-a-exclus%C3%A3o-dos-eventos-S1200-S1210#h_01KFB881HNA6986FJ01K8N2J22) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37775482726423-Como-gerar-a-exclus%C3%A3o-dos-eventos-S1200-S1210#h_01KFB87KQHR7RMDBD19EXT62JZ) |

## Evento S1200 - Remuneração do Trabalhador / Evento S1210 - Pagamento de Rendimentos do Trabalho

#### Exclusão

##### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/944433315)

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. ##### Para excluir a folha

**Acesse**: Pessoal+ » Rotinas Folha » Gerenciador de Folhas

- Na lateral direita da tela, clique no botão Liberação para eSocial
- Informe o tipo de folha que deseja excluir
- Informe a referência do cálculo
- Defina o tipo de ação “Bloquear dados”
- Selecione a empresa no resultado dos filtros
- Na aba Funcionários selecione os funcionários que terão os dados da folha bloqueados para o esocial
- Clique no botão “Bloquear liberação”

1. ##### Exclusão do evento S1210

**Acesse**: Pessoal+  » Rotinas Folha »  Central do eSocial

- Na lateral esquerda da tela, selecione a empresa, a referência e o ambiente de envio, e em seguida clique em '**Carregar**'.
- No menu lateral, acesse a aba “**Geração**” e escolha a opção **Individual**
- Selecione o evento **S-1210** e em seguida clique em “**Iniciar** **Geração**”
- Após a geração, o evento será listado como card na aba '**Eventos Pendentes**'. Para realizar a transmissão ao eSocial, utilize o botão '**Enviar dados**'

Após o envio, o evento ficará na aba '**Eventos na Fila**' até a conclusão do processamento pelo ambiente do eSocial. Finalizado o envio, ele será movido para a aba '**Acompanhamento**', onde é possível visualizar os dados enviados e os XMLs de retorno por meio do botão '**Visualizar dados**'

- Repita o procedimento para a exclusão do evento S-1200.

Após finalizar todas as exclusões, você poderá reprocessar os dados da folha e realizar novamente o envio das informações ao eSocial.

**Importante:**

Neste exemplo, a exclusão foi feita para todas as folhas do cálculo, por isso o sistema gerou automaticamente a exclusão do evento S-1210 também. 

No entanto, se o bloqueio for realizado apenas para retificação de parte dos funcionários, o sistema não excluirá o S-1210 por completo — ele irá gerar uma retificação apenas para os colaboradores com alterações após o bloqueio.

#### Correção e Repetição

- Revise os registros para confirmar se os passos foram seguidos.
- Caso haja erro no registro verifique atentamente os campos mencionados no erro e consulte o manual do eSocial.
