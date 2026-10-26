---
id: "37773732324375"
titulo: "Como gerar e enviar o evento S2206"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37773732324375-Como-gerar-e-enviar-o-evento-S2206"
trilha: "Universidade Sankhya > Gestão eSocial"
atualizado_em: "2026-07-22T14:08:38Z"
rotulos: ["Eventos", "XML", "Folha", "eSocial", "Configuração Funcionários", "Central do eSocial"]
---

# Como gerar e enviar o evento S2206

| Categoria |
| --- |
| [O que é o evento S2206?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773732324375-Como-gerar-e-enviar-o-evento-S2206#h_01KFB2RPKYS5N9PVTM3K5CTZQ3) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773732324375-Como-gerar-e-enviar-o-evento-S2206#h_01KFB2RGW8704DBMEMGWDK9XB2) |
| [Para alterações de cadastros](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773732324375-Como-gerar-e-enviar-o-evento-S2206#h_01KFB2R58E2DSFJKC6JSQQ2NQZ) |
| [Geração e envio do evento S2206](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773732324375-Como-gerar-e-enviar-o-evento-S2206#h_01KFB2QD198G937KY4ZY0YCFBH) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773732324375-Como-gerar-e-enviar-o-evento-S2206#h_01KFB2Q0MY09J4442SAD02ZNN1) |

## Evento S2206 - Alteração Contratual

#### O que é o evento S2206?

O evento S-2206 é utilizado para registrar no eSocial qualquer alteração contratual que afete a relação de trabalho entre a empresa e o colaborador. Isso inclui mudanças no cargo, salário, jornada, tipo de contrato, local de trabalho, sindicato ou lotação tributária. Diferente do S-2205, que trata exclusivamente de dados cadastrais do trabalhador, o S-2206 modifica informações contratuais, impactando diretamente nos cálculos da folha de pagamento, nos encargos trabalhistas e nas obrigações acessórias da empresa. Esse evento deve ser enviado sempre que houver alterações com efeitos legais, previdenciários ou tributários, garantindo que o vínculo esteja refletido corretamente na base do eSocial e evitando inconsistências nos eventos subsequentes, como remuneração (S-1200) e desligamento (S-2299).

##### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/944171028)

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. ##### Para alterações de cadastros

   **Acesse**: Configurações » Cadastros » Pessoal » Configurações Funcionários

- Após realizar as alterações contratuais no cadastro do usuário é necessário preencher a data de alteração e descrição opcional dos dados modificados.

Alterações relacionadas à remuneração podem ser realizadas através da rotina **Reajuste salarial**

2. ##### Geração e envio do evento S2206

   **Acesse**: Pessoal+  » Rotinas Folha »  Central do eSocial

- Na lateral esquerda da tela, selecione a empresa, a referência e o ambiente de envio, e em seguida clique em '**Carregar**'.
- No menu lateral, acesse a aba “**Geração**” e escolha a opção **Individual**
- Selecione o evento **S-2206** e em seguida clique em “**Iniciar** **Geração**”
- Após a geração, o evento será listado como card na aba '**Eventos Pendentes**'. Para realizar a transmissão ao eSocial, utilize o botão '**Enviar dados**'

Após o envio, o evento ficará na aba '**Eventos na Fila**' até a conclusão do processamento pelo ambiente do eSocial. Finalizado o envio, ele será movido para a aba '**Acompanhamento**', onde é possível visualizar os dados enviados e os XMLs de retorno por meio do botão '**Visualizar dados**'

#### Correção e Repetição

- Revise os registros para confirmar se os passos foram seguidos.
- Caso haja erro no registro verifique atentamente os campos mencionados no erro e consulte o manual do eSocial.
